# TLTR: Create a Pull Request
1. Fork this repository.
2. Clone your new repository to your system.
3. Create a new branch (i.e. `add/your-name`).
4. Add your new site. Remember to add **alphabetically to the list.**
5. Commit changes and push the new branch.
6. Open and submit a PR.

If you have never opened a PR and need direction, read more below.

# Contributor's Guide
Feedback, bug reports, and pull requests are welcome. Feel free to ask for [help](https://github.com/emmawedekind/developer-portfolios/issues).

Working on your first Pull Request? You can learn how from this _free_ series [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github)

This guide has been modified from [freeCodeCamp's Contributors Guide](https://github.com/freeCodeCamp/freeCodeCamp/blob/master/CONTRIBUTING.md)

## Forking the Project

### Setting Up Your System

1.  Install [Git](https://git-scm.com/) or your favorite Git client.
2.  (Optional) [Setup an SSH Key](https://help.github.com/articles/generating-an-ssh-key/) for GitHub.

### Forking Developer Portfolios

1.  Go to the top-level page of this [repository](https://github.com/emmawedekind/developer-portfolios)
2.  Click the "Fork" button in the upper right-hand corner of the interface ([More Details Here](https://help.github.com/articles/fork-a-repo/))
3.  After the repository (repo) has been forked, you will be taken to your copy of the Developer Portfolios repo at <https://github.com/yourUsername/developer-portfolios>

### Cloning Your Fork

1.  Open a Terminal / Command Line / Bash Shell in your project's directory (_i.e.: `/yourprojectdirectory/`_)
2.  Clone your fork of `Developer Portfolios`

```shell
$ git clone https://github.com/yourUsername/developer-portfolios.git
```

**(make sure to replace `yourUsername` with your GitHub username)**

This will download the entire `Developer Portfolios` repo to your project's directory.

### Setup Your Upstream

1.  Change directory to the new directory (`cd ./developer-portfolios`)
2.  Add a remote to the original `Developer Portfolios` repo:

```shell
$ git remote add upstream https://github.com/emmawedekind/developer-portfolios.git
```

Congratulations, you now have a local copy of the `Developer Portfolios` repo!

### Maintaining Your Fork

Now that you have a copy of your fork, there is work you will need to do to keep it current.

#### Rebasing from Upstream

Do this prior to every time you create a branch for a PR:

1.  Make sure you are on the `master` branch

```shell
$ git status
On branch master
Your branch is up to date with 'origin/master'.
```

If you aren't on `master`, resolve outstanding files/commits and checkout the `master` branch

```shell
$ git checkout master
```

2.  Do a pull with rebase against `master`

```shell
$ git pull --rebase upstream master
```

This will pull down all of the changes to the official master branch, without making additional commits in your local repo.

3.  Merge remote changes to your local master fork:

```shell
$ git merge upstream/master
```

### Create a Branch

Before you start working, you will need to create a separate branch specific to the issue/feature you're working on. You will push your work to this branch.

#### Naming Your Branch

There are several strategies for naming branches.

You could name the branch something like `fix/xxx` or `feature/xxx` where `xxx` is a short description of the changes or feature you are attempting to add. For example `fix/email-login` would be a branch where you fix something specific to email login.

We'd recommend naming it something that is relevant to your new site (i.e. `add/your-name`

#### Adding Your Branch

To create a branch on your local machine (and switch to this branch):

```shell
$ git checkout -b [add/your-name]
```

and to push to GitHub:

```shell
$ git push origin [add/your-name]
```

**If you need more help with branching, take a look at [this](https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches).**

### Creating a Pull Request

#### What is a Pull Request?

A pull request (PR) is a method of submitting your new site to the `Developer Portfolios` (or any repo, for that matter). You will make changes to copies of the files in a personal fork, then apply to have them accepted by the original repo.

#### Need Help?

Feel free to ask for [help](https://github.com/emmawedekind/developer-portfolios/issues), we are here to help.

#### Important: ALWAYS EDIT ON A BRANCH

Take away only one thing from this document: Never, **EVER** make edits to the `staging` branch. ALWAYS make a new branch BEFORE you edit files. This is critical, because if your PR is not accepted, your copy of staging will be forever sullied and the only way to fix it is to delete your fork and re-fork.

#### Methods

There are two methods of creating a pull request for 'Developer Portfolios':

* Editing files on a local clone (recommended)
* Editing files via the GitHub Interface

##### Method 1: Editing via your Local Fork _(Recommended)_

This is the recommended method. Read about [How to Setup and Maintain a Local Instance](#maintaining-your-fork).

1.  Perform the maintenance step of rebasing `master`.
2.  Ensure you are on the `master` branch using `git status`:

        $ git status
        On branch master
        Your branch is up-to-date with 'origin/master'.

        nothing to commit, working directory clean

3.  If you are not on `master` or your working directory is not clean, resolve any outstanding files/commits and checkout `git checkout master`

4.  Create a branch off of `develop` with git: `git checkout -b add/your-name`

5.  Edit your file(s) locally with the editor of your choice.

6.  Check your `git status` to see unstaged files.

7.  Add your edited files: `git add path/to/filename.ext` You can also do: `git add .` to add all unstaged files. Take care, though, because you can accidentally add files you don't want to be added. Review your `git status` first.

8.  Make sure your new site is added **alphabetically** to the existing list.

9.  Commit your edits. `git commit -m "your-commit-message"`

Please make sure to write a commit message that summarizes the changes. If you find yourself in the need to use `and` it might be better to do two separate commits.

See [Useful Tips for writing better Git commit messages](https://code.likeagirl.io/useful-tips-for-writing-better-git-commit-messages-808770609503) for inspiration.

As a note, use the present tense for your commit messages (i.e. `Add` instead of `Added`).

10. If you would want to add/remove changes to the previous commit, add the files as in Step 5 earlier, and use `git commit --amend` or `git commit --amend --no-edit` (for keeping the same commit message).

11. Push your commits to your GitHub Fork: `git push origin add/your-name`

12. Once the edits have been committed, you will be prompted to create a pull request on your fork's GitHub Page.

13. By default, all pull requests should be against the `Developer Portfolios` main repo, `master` branch.
    **Make sure that your Base Fork is set to developer-portfolios/master when raising a Pull Request.**

14. Submit a pull request from your branch to the `Developer Portfolios` `master` branch.

15. The title (also called the subject) of your PR should be descriptive of your changes and succinctly indicate what is being fixed.

    * **Do not add the issue number in the PR title or commit message.**

    * Examples: `Add site NAME`

### Next Steps

#### If your PR is accepted

Once your PR is accepted, you may delete the branch you created to submit it. This keeps your working fork clean.

You can do this with a press of a button on the GitHub PR interface. You can delete the local copy of the branch with: `git branch -D branch/to-delete-name`

#### If your PR comes back

Don't despair! You are probably being asked to make a formatting change. If you have a local copy of the repo, you can make the requested changes, commit them and push them to your fork.
