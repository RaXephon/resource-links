### Git Branch
```
$ metisgh
$ ls
$ cd dsp
$ pwd
/Users/reshamashaikh/_ds/metis/metisgh/dsp

$ clear

reshama$ git branch          # list the branches in repo
  master
* update_v4


$ git checkout master        # switch to a different branch

reshama$ git branch          # switched to “master” branch
* master
  update_v4
reshama$


reshama$ git branch test     # create “test” branch
reshama$ git branch
* master
  test
  update_v4
reshama$

reshama$ git branch -D test          # delete a branch
Deleted branch test (was d58491d).
reshama$ git branch
* master
  update_v4
reshama$

reshama$ git checkout -b test          # create a branch
```

```
reshama$ git branch
* master
  update_v4
reshama$ git checkout update_v4
Switched to branch 'update_v4'
reshama$ git pull upstream master
From https://github.com/thisismetis/dsp
 * branch            master     -> FETCH_HEAD
Updating a7e3ca7..abea30f
Fast-forward
 05b-python_advanced.md |  2 +-
 06-statistics.md       | 49 +++++++++++++++++++++++++------------------------
 2 files changed, 26 insertions(+), 25 deletions(-)
reshama$ git push origin update_v4
Counting objects: 9, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (9/9), done.
Writing objects: 100% (9/9), 1.14 KiB | 0 bytes/s, done.
Total 9 (delta 5), reused 0 (delta 0)
To https://github.com/reshama/dsp.git
   a7e3ca7..abea30f  update_v4 -> update_v4
reshama$
```
