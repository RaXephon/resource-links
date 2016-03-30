
###Step 1:  Create Repo
**In your browser:**  sign in to your GitHub account.  
**To create repo:** Click on the "+" next to your profile photo.  
**Select:**  'New Repository'  
**Repository Name:**  *project1_mta*  
**Description (optional):**  *use MTA turnstile data to estimate the volume of people on the street*  

**Public or Private:**  *select 'Private'*  
**Select (check):**  *Initialize this repository with a README*  

###Step 2:  Clone Repo  
Copy your HTTPS link:  https://github.com/reshama/project1_mta.git

In Unix, in your 'metisgh' folder, clone the repo:  
```
$ git clone https://github.com/reshama/project1_mta.git
```

**Example:**    
```
reshama$ pwd
/Users/reshamashaikh/_ds/metis/metisgh

reshama$ git clone https://github.com/reshama/project1_mta.git

Cloning into 'project1_mta'...
warning: You appear to have cloned an empty repository.
Checking connectivity... done.

reshama$ 
```

###Step 3:  Start Working in Your Repo  
```
reshama$ cd project1_mta/

reshama$ ls

reshama$ 
```
**Create a README.md file - add some lines**  
```
reshama$ emacs README.md

reshama$ more README.md

###My Documentation for Project 1
reshama$ 
```

###Step 4: Copy work over to GitHub repo (on browser)  
```
reshama$ git status

reshama$ git add README.md

reshama$ git commit -m "adding my readme file for project 1"

reshama$ git remote -v
origin	https://github.com/reshama/project1_mta.git (fetch)
origin	https://github.com/reshama/project1_mta.git (push)

reshama$ git push origin master

Counting objects: 3, done.
Writing objects: 100% (3/3), 260 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/reshama/project1_mta.git
 * [new branch]      master -> master
 
reshama$ 
````

**Note:  check your github account and you'll see the README.md file now appears!**  
https://github.com/reshama/project1_mta






