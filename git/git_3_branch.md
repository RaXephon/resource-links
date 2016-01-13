### Git Branch
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
