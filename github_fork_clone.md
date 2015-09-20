## Fork a repo; Clone a repo

#### Step 1:  Go to repo
In my personal account on GitHub, go to repo to be cloned.

In this example, it is:  https://github.com/thisismetis/ds5

#### Step 2:  Fork repo
Upper right of github page:  "Fork" the repo

Go to my forked repo: https://github.com/reshama/ds5
 
#### Step 3:  Clone repo
Clone that forked repo (which is now under my name)

In right column, find the link to **HTTPS clone URL** and copy that URL to be cloned.

In terminal: 
* go to directory where repo will be cloned
* clone repo
* cd into clone repo
```
$ metisgh
$ pwd
/Users/reshamashaikh/_ds/metis/metisgh

$ cd metisgh/
$ ls

$ git clone https://github.com/reshama/ds5.git
$ cd ds5
```
--
## Set upstream

If there are changes to the original repo, how do you get them?  You need to tell your local repo that it can also get updates from the original.

Origin:  reshama/ds5

**Note:  Need to be in that directory on Unix to update repo**
```
$ git remote -v
origin	https://github.com/reshama/ds5.git (fetch)
origin	https://github.com/reshama/ds5.git (push)
```

Want to add reference to metis repo (which is master repo)
Note:  can call it “upstream” or “root” or any other name
```
$ git remote add upstream https://github.com/thisismetis/ds5.git
```

Now we see we have two remotes: 
* origin
* upstream
```
$ git remote -v
origin	https://github.com/reshama/ds5.git (fetch)
origin	https://github.com/reshama/ds5.git (push)
upstream	https://github.com/thisismetis/ds5.git (fetch)
upstream	https://github.com/thisismetis/ds5.git (push)
```
--
## Sync repos
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
```
`$ git status`

git push or git push origin master
change from metis (master) down to local (my computer) and up to origin (me/ds3)
`$ git push`











