#!/usr/bin/env python3
"""Tests for portfolio sorting and feed metadata enrichment."""

import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src import generate_feed  # noqa: E402
from src import portfolio_sorting as sorting  # noqa: E402


def entry(name, url, **extra):
    data = {"name": name, "url": url}
    data.update(extra)
    return data


class TestSortPortfolios(unittest.TestCase):
    def test_name_sort_is_case_insensitive(self):
        portfolios = [entry("bob", "https://b.example"), entry("Alice", "https://a.example")]
        result = sorting.sort_portfolios(portfolios, "name")
        self.assertEqual([p["name"] for p in result], ["Alice", "bob"])

    def test_sort_does_not_mutate_input(self):
        portfolios = [
            entry("Zoe", "https://z.example", views=1),
            entry("Amy", "https://a.example", views=9),
        ]
        original = [dict(p) for p in portfolios]
        sorting.sort_portfolios(portfolios, "views")
        self.assertEqual(portfolios, original)

    def test_newest_sorts_by_date_descending(self):
        portfolios = [
            entry("Old", "https://old.example", date_added="2023-01-05"),
            entry("New", "https://new.example", date_added="2026-09-01"),
            entry("Mid", "https://mid.example", date_added="2024-06-30"),
        ]
        result = sorting.sort_portfolios(portfolios, "newest")
        self.assertEqual([p["name"] for p in result], ["New", "Mid", "Old"])

    def test_newest_puts_missing_dates_last(self):
        portfolios = [
            entry("Unknown", "https://unknown.example"),
            entry("Dated", "https://dated.example", date_added="2020-02-02"),
            entry("Bad", "https://bad.example", date_added="not-a-date"),
        ]
        result = sorting.sort_portfolios(portfolios, "newest")
        self.assertEqual(result[0]["name"], "Dated")
        self.assertEqual({result[1]["name"], result[2]["name"]}, {"Bad", "Unknown"})

    def test_popular_uses_explicit_popularity_override(self):
        portfolios = [
            entry("Many views", "https://many.example", views=1000, clicks=100),
            entry("Curated", "https://curated.example", views=1, clicks=1, popularity=9999),
        ]
        result = sorting.sort_portfolios(portfolios, "popular")
        self.assertEqual(result[0]["name"], "Curated")

    def test_popular_falls_back_to_views_plus_clicks(self):
        portfolios = [
            entry("Low", "https://low.example", views=10, clicks=1),
            entry("High", "https://high.example", views=40, clicks=25),
            entry("Mid", "https://mid.example", views=50, clicks=0),
        ]
        result = sorting.sort_portfolios(portfolios, "popular")
        self.assertEqual([p["name"] for p in result], ["High", "Mid", "Low"])

    def test_views_sorts_by_views_then_clicks(self):
        portfolios = [
            entry("Fewer views", "https://fewer.example", views=5, clicks=100),
            entry("Most views", "https://most.example", views=50, clicks=1),
            entry("Tie more clicks", "https://tie.example", views=50, clicks=9),
        ]
        result = sorting.sort_portfolios(portfolios, "views")
        self.assertEqual(
            [p["name"] for p in result],
            ["Tie more clicks", "Most views", "Fewer views"],
        )

    def test_unknown_sort_option_raises(self):
        with self.assertRaises(ValueError):
            sorting.sort_portfolios([], "sideways")

    def test_sort_aliases(self):
        portfolios = [
            entry("A", "https://a.example", date_added="2024-01-01"),
            entry("B", "https://b.example", date_added="2025-01-01"),
        ]
        for alias in ("recent", "most_recent", "NEWEST"):
            result = sorting.sort_portfolios(portfolios, alias)
            self.assertEqual(result[0]["name"], "B", alias)
        self.assertEqual(sorting.normalize_sort_option("a-z"), "name")
        self.assertEqual(sorting.normalize_sort_option("most-viewed"), "views")

    def test_ties_break_alphabetically(self):
        portfolios = [
            entry("Zed", "https://z.example", views=10),
            entry("Ann", "https://a.example", views=10),
        ]
        result = sorting.sort_portfolios(portfolios, "views")
        self.assertEqual([p["name"] for p in result], ["Ann", "Zed"])


class TestMetadataHelpers(unittest.TestCase):
    def test_normalize_url(self):
        self.assertEqual(
            sorting.normalize_url("HTTPS://Example.com/"),
            "https://example.com",
        )
        self.assertEqual(
            sorting.normalize_url("https://example.com/path/?a=1#section"),
            "https://example.com/path?a=1",
        )
        self.assertEqual(sorting.normalize_url(None), "")

    def test_parse_added_date(self):
        self.assertEqual(str(sorting.parse_added_date("2024-03-15")), "2024-03-15")
        self.assertEqual(
            str(sorting.parse_added_date("2024-03-15T10:00:00Z")), "2024-03-15"
        )
        self.assertIsNone(sorting.parse_added_date(""))
        self.assertIsNone(sorting.parse_added_date("yesterday"))
        self.assertEqual(
            str(sorting.parse_added_date(1704067200)),  # 2024-01-01 UTC
            "2024-01-01",
        )

    def test_merge_metadata_applies_only_present_fields(self):
        portfolios = [
            entry("One", "https://one.example", date_added="2020-01-01"),
            entry("Two", "https://two.example"),
        ]
        metadata = {"https://two.example": {"views": 12, "clicks": 3}}
        merged = sorting.merge_metadata(portfolios, metadata)
        self.assertEqual(merged[0]["date_added"], "2020-01-01")
        self.assertNotIn("views", merged[0])
        self.assertEqual(merged[1]["views"], 12)
        self.assertEqual(merged[1]["clicks"], 3)

    def test_merge_metadata_matches_trailing_slash_variants(self):
        portfolios = [entry("One", "https://one.example/")]
        merged = sorting.merge_metadata(portfolios, {"https://one.example": {"views": 7}})
        self.assertEqual(merged[0]["views"], 7)

    def test_preserve_metadata(self):
        previous = [entry("One", "https://one.example", views=5, clicks=2)]
        fresh = [entry("One", "https://one.example"), entry("Two", "https://two.example")]
        preserved = sorting.preserve_metadata(fresh, previous)
        self.assertEqual(preserved[0]["views"], 5)
        self.assertEqual(preserved[0]["clicks"], 2)
        self.assertNotIn("views", preserved[1])

    def test_order_entry_fields(self):
        ordered = sorting.order_entry_fields(
            {"views": 1, "name": "A", "url": "https://a.example", "extra": True}
        )
        self.assertEqual(list(ordered), ["name", "url", "views", "extra"])

    def test_load_metrics_supports_mapping_and_list(self):
        with tempfile.TemporaryDirectory() as tmp:
            mapping_path = os.path.join(tmp, "mapping.json")
            with open(mapping_path, "w", encoding="utf-8") as handle:
                json.dump({"https://one.example/": {"views": 4}}, handle)
            self.assertEqual(sorting.load_metrics(mapping_path)["https://one.example"], {"views": 4})

            list_path = os.path.join(tmp, "list.json")
            with open(list_path, "w", encoding="utf-8") as handle:
                json.dump([{"url": "https://two.example", "clicks": 2}], handle)
            self.assertEqual(sorting.load_metrics(list_path)["https://two.example"], {"clicks": 2})

    def test_load_metrics_missing_file_is_empty(self):
        self.assertEqual(sorting.load_metrics("does-not-exist.json"), {})


class TestGitHistoryParsing(unittest.TestCase):
    LOG = (
        "@@@1600000000\n"
        "+++ b/README.md\n"
        "+- [First Person](https://first.example)\n"
        "@@@1700000000\n"
        "+++ b/README.md\n"
        "+- [First Person](https://first.example)\n"
        "+- [Second Person](https://second.example/) [Engineer]\n"
    )

    def test_parse_added_dates_keeps_earliest(self):
        by_url, by_name = sorting.parse_added_dates(self.LOG)
        self.assertEqual(by_url["https://first.example"], 1600000000)
        self.assertEqual(by_url["https://second.example"], 1700000000)
        self.assertEqual(by_name["first person"], 1600000000)

    def test_enrich_with_git_dates_uses_url_then_name(self):
        by_url = {"https://one.example": 1704067200}  # 2024-01-01 UTC
        by_name = {"two person": 1698796800}  # 2023-11-01 UTC
        portfolios = [
            entry("One", "https://one.example"),
            entry("Two Person", "https://renamed.example"),
            entry("Three", "https://three.example"),
        ]
        with mock.patch.object(sorting, "get_added_dates", return_value=(by_url, by_name)):
            enriched = sorting.enrich_with_git_dates(portfolios)
        self.assertEqual(enriched[0]["date_added"], "2024-01-01")
        self.assertEqual(enriched[1]["date_added"], "2023-11-01")
        self.assertNotIn("date_added", enriched[2])

    def test_enrich_keeps_existing_dates_unless_refreshed(self):
        portfolios = [entry("One", "https://one.example", date_added="2020-05-05")]
        with mock.patch.object(
            sorting, "get_added_dates", return_value=({"https://one.example": 1704067200}, {})
        ):
            kept = sorting.enrich_with_git_dates(portfolios)
            refreshed = sorting.enrich_with_git_dates(portfolios, refresh=True)
        self.assertEqual(kept[0]["date_added"], "2020-05-05")
        self.assertEqual(refreshed[0]["date_added"], "2024-01-01")


class TestGenerateFeed(unittest.TestCase):
    def _write_readme(self, directory):
        path = os.path.join(directory, "README.md")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(
                "## A\n\n"
                "- [Alice](https://alice.example) [Engineer]\n"
                "- [Aman](https://aman.example)\n"
            )
        return path

    def test_create_feed_json_merges_metrics(self):
        with tempfile.TemporaryDirectory() as tmp:
            readme = self._write_readme(tmp)
            metrics_path = os.path.join(tmp, "metrics.json")
            with open(metrics_path, "w", encoding="utf-8") as handle:
                json.dump({"https://alice.example": {"views": 10, "clicks": 2}}, handle)
            output = os.path.join(tmp, "feed.json")

            count = generate_feed.create_feed_json(
                readme_path=readme,
                output_path=output,
                metrics_path=metrics_path,
                with_git_dates=False,
            )

            self.assertEqual(count, 2)
            with open(output, "r", encoding="utf-8") as handle:
                feed = json.load(handle)
            self.assertEqual(feed[0]["views"], 10)
            self.assertEqual(feed[0]["clicks"], 2)
            self.assertEqual(feed[0]["tagline"], "Engineer")
            self.assertNotIn("views", feed[1])

    def test_create_feed_json_preserves_existing_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            readme = self._write_readme(tmp)
            output = os.path.join(tmp, "feed.json")
            with open(output, "w", encoding="utf-8") as handle:
                json.dump(
                    [{"name": "Alice", "url": "https://alice.example", "date_added": "2021-01-01"}],
                    handle,
                )

            generate_feed.create_feed_json(
                readme_path=readme,
                output_path=output,
                with_git_dates=False,
            )

            with open(output, "r", encoding="utf-8") as handle:
                feed = json.load(handle)
            self.assertEqual(feed[0]["date_added"], "2021-01-01")

    def test_alphabetical_regeneration_preserves_metadata(self):
        from src import alphabetical

        with tempfile.TemporaryDirectory() as tmp:
            readme = self._write_readme(tmp)
            output = os.path.join(tmp, "feed.json")
            with open(output, "w", encoding="utf-8") as handle:
                json.dump(
                    [{"name": "Alice", "url": "https://alice.example", "views": 42}],
                    handle,
                )

            alphabetical.create_feed_json(readme_path=readme, output_path=output)

            with open(output, "r", encoding="utf-8") as handle:
                feed = json.load(handle)
            self.assertEqual(feed[0]["views"], 42)


class TestSortCli(unittest.TestCase):
    def test_cli_outputs_sorted_markdown(self):
        with tempfile.TemporaryDirectory() as tmp:
            feed_path = os.path.join(tmp, "feed.json")
            with open(feed_path, "w", encoding="utf-8") as handle:
                json.dump(
                    [
                        entry("Old", "https://old.example", date_added="2020-01-01"),
                        entry("New", "https://new.example", date_added="2026-01-01"),
                    ],
                    handle,
                )

            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                exit_code = sorting.main(["--feed", feed_path, "--by", "newest", "--limit", "1"])

            self.assertEqual(exit_code, 0)
            self.assertEqual(buffer.getvalue().strip(), "- [New](https://new.example)")

    def test_cli_rejects_unknown_sort(self):
        buffer = io.StringIO()
        with contextlib.redirect_stderr(buffer):
            with self.assertRaises(SystemExit):
                sorting.main(["--by", "sideways"])
        self.assertIn("Unknown sort option", buffer.getvalue())

    def test_cli_lists_options(self):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            sorting.main(["--list-options"])
        output = buffer.getvalue()
        for option in ("name", "newest", "popular", "views"):
            self.assertIn(option, output)


if __name__ == "__main__":
    unittest.main()
