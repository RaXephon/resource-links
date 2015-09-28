## Git:  Add, Commit a File & Pull Request

--

## Sync repos

**Always "git pull" before sending up any changes**
```
$ pwd
/Users/reshamashaikh/_ds/metis/metisgh/ds5

$ git pull  (by default, it pulls from origin)

$ git pull upstream master (we want to pull from master)

```
$ git pull upstream master
remote: Counting objects: 55, done.
remote: Compressing objects: 100% (31/31), done.
remote: Total 55 (delta 9), reused 0 (delta 0), pack-reused 24
Unpacking objects: 100% (55/55), done.
From https://github.com/thisismetis/ds5
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> upstream/master
Updating 73c9b7f..e2fa70b
Fast-forward
...


## Practice - let's add a file
```
$ cd ds5/challenges/00-practice
$ mkdir reshama
$ cd reshama
```

Make a small file
Redirect standard output to a file called “text.txt”
```
$ echo "Hello! Nice to meet you!" > test.txt
echo "Hello! Nice to meet you" > test.txt

$ cat test.txt 
Hello! Nice to meet you

$ git status
```

### Adding, committing a file
```
$ git add test.txt 
$ git status
$ git commit -m "add a simple file"
$ git push
```

#### Sync repo
```
$ git pull upstream master
$ git push
```

## Pull Request

Go to your forked version
https://github.com/reshama/ds5

Right column, go to "New pull request"

Click on green "Create pull request"

Fill in info at "Leave a comment"

Click on green "Create pull request" at bottom of page.

Look in this repo and see that file has been updated.

--

## Git Commands

```
$ git remote
origin
upstream

$ git remote -v
origin	https://github.com/reshama/ds5.git (fetch)
origin	https://github.com/reshama/ds5.git (push)
upstream	https://github.com/thisismetis/ds5.git (fetch)
upstream	https://github.com/thisismetis/ds5.git (push)

$ git log               # gives log of commits

```
`$ git remote origin master`

>**remote**  origin

>**branch**  master


**Note:**  
GitHub:  commit every day, green dots show up on user home page; looks good for potential employers.







