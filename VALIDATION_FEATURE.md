# Section Validation Feature

## Problem
The alphabetization script was sorting entries within each section (A, B, C, etc.) but wasn't validating that entries were in the correct section. This led to cases where entries could end up in the wrong alphabetical section - for example, entries starting with 'D', 'M', 'P', 'R', or 'Z' were found at the end of section A.

## Solution
Added a new `validate_section_placement()` function to the `alphabetical.py` script that:

1. **Parses the README structure** - Identifies section headers (## A, ## B, etc.) and their entries
2. **Validates each entry** - Extracts the name from each markdown link and checks if it belongs in the current section
3. **Moves misplaced entries** - Automatically moves entries to their correct alphabetical section
4. **Creates missing sections** - If an entry needs to go to a section that doesn't exist, it creates that section in the correct alphabetical position
5. **Handles accented characters** - Properly normalizes accented characters (e.g., 'É' → 'E', 'Ö' → 'O') using Unicode normalization
6. **Preserves formatting** - Maintains proper blank line spacing between sections

## How It Works

The validation runs automatically as part of the main alphabetization script, before the sorting step:

```python
# In main() function:
reorganized_lines, moved_count = validate_section_placement(deduped_lines)
if moved_count:
    print(f"Moved {moved_count} misplaced entr{'y' if moved_count == 1 else 'ies'} to correct alphabetical section(s).")
```

## Test Coverage

Added 5 comprehensive test cases in `tests/test_alphabetical.py`:

1. **test_validate_section_placement_single_misplaced** - Tests moving a single entry from wrong section
2. **test_validate_section_placement_multiple_misplaced** - Tests moving multiple misplaced entries
3. **test_validate_section_placement_accented_characters** - Tests handling of accented characters (É, Ö, etc.)
4. **test_validate_section_placement_no_misplaced** - Tests that correctly placed entries aren't moved
5. **test_validate_section_placement_creates_new_section** - Tests creation of new sections when needed

All tests pass successfully.

## Example

**Before validation:**
```markdown
## A

- [Alice](https://alice.com)
- [Andrew](https://andrew.com)
- [Zack](https://zack.com)  ← Wrong section!

## B
```

**After validation:**
```markdown
## A

- [Alice](https://alice.com)
- [Andrew](https://andrew.com)

## B

- [Bob](https://bob.com)

...

## Z

- [Zack](https://zack.com)  ← Moved to correct section!
- [Zoe](https://zoe.com)
```

## Impact

This feature prevents future alphabetization anomalies by automatically detecting and correcting misplaced entries during each run of the alphabetization script. Contributors no longer need to manually verify that entries are in the correct section - the script handles this automatically.

## Files Modified

1. **src/alphabetical.py** - Added `validate_section_placement()` function and integrated it into the main workflow
2. **tests/test_alphabetical.py** - Added 5 new test cases for validation functionality
3. **README.md** - Fixed existing misplaced entries (Debpriyo Ghosal, Muhammad Aamir Malik, Parth Sharma, Raphaël Giraud, Redoyanul Haque, Zuned Aalim)

