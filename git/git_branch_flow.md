## Git Branch  
[Helpful Tutorial:  Using Branches on Git](https://www.atlassian.com/git/tutorials/using-branches)  

Why use branches?
 * independent line of development
 * think of them as a way to request a brand new working directory, staging area, and project history
 * in Git, branches are a part of your everyday development process. 
    * when you want to add a new feature or fix a bug—no matter how big or how small,  spawn a new branch to encapsulate your changes
    * this makes sure that unstable code is never committed to the main code base
    * it gives you the chance to clean up your feature’s history before merging it into the main branch

---

###Branch Commands
 * **List branches**  
    `$git branch`
 * **Create a new branch**  
    `$git branch reshama_wip`
 * **Navigate between branches**  
    `$git checkout -b branchname`

 * **Delete a branch** (safe delete; won't delete if there are unmerged changes)  
    `$git branch -d reshama_wip`
 * **Delete a branch** (force delete; will delete even if branch has unmerged changes)  
    `$git branch -D reshama_wip`


 * **Rename a branch** (whichever is the current one, be careful)  
    `$git branch -m newone_wip`
 * **Rename a branch** (can specify oldname and newname)
    `$git branch -m <oldname> <newname>`


 * **Back to main branch**  
    `$git checkout master`
 * **Merge branches** (will merge specified <branchname> into current branch)  
    `$git merge <branchname>`
  
--- 

###An Example

```
reshama$ pwd
/Users/reshamashaikh/_ds/metis/metisgh/dsp

reshama$ git branch          # list the branches in repo
  master
* update_v4

reshama$ git checkout master      # switch to a different branch

reshama$ git branch          # switched to “master” branch
* master
  update_v4

reshama$ git branch test     # create “test” branch

reshama$ git branch
* master
  test
  update_v4

reshama$ git branch -D test          # delete a branch
Deleted branch test (was d58491d).

reshama$ git branch
* master
  update_v4

reshama$ git checkout -b test          # create a branch
```

```
reshama$ git branch
* master
  update_v4
```
```
reshama$ git checkout update_v4
Switched to branch 'update_v4'
```

```
reshama$ git pull upstream master
```
```
From https://github.com/thisismetis/dsp
 * branch            master     -> FETCH_HEAD
Updating a7e3ca7..abea30f
Fast-forward
 05b-python_advanced.md |  2 +-
 06-statistics.md       | 49 +++++++++++++++++++++++++------------------------
 2 files changed, 26 insertions(+), 25 deletions(-)
```

```
reshama$ git push origin update_v4
```
```
Counting objects: 9, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (9/9), done.
Writing objects: 100% (9/9), 1.14 KiB | 0 bytes/s, done.
Total 9 (delta 5), reused 0 (delta 0)
To https://github.com/reshama/dsp.git
   a7e3ca7..abea30f  update_v4 -> update_v4
```

#### Committing by Qualifying Remote Name and Branch Name
```
$ git commit remotename branchname -m "message"
$ git commit origin pwupdate -m "updating prework branch" 
```

--

 * Create a branch and switch to it:

```
git checkout -b experiment
```

 * Check your branch situation:

```
git branch
```

 * Change branches:

```
git checkout master
git checkout experiment
```

 * Work on your branch as usual, and then push to your `origin`.

```
git push origin experiment
```

 * Make a pull request on GitHub.

 * When you sync up, sync up `master`!

```
git checkout master
git pull upstream master
```

It's possible to do pull requests from your `master` branch, but this puts you in an awkward position where you're waiting for the pull request to get merged before it's safe for you to sync up again. Topic branches are highly recommended.
