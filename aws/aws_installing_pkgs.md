##Setting up AWS Machine
###Installing Packages

```
ubuntu@ip-172-31-59-73:/home$ history
    1  clear
    2  pwd
    3  #check if python is installed
    4  python --version
    5  #get into interactive python
    6  python
    7  pwd
    8  cd ..
    9  pwd
   10  ls
   11  #this shows users
   12  ls
   13  #update packages
   14  sudo apt-get upgrade
   15  #install python with anaconda
   16  sudo pip install conda
   17  #install pip
   18  apt-get install pip
   19  #need to be sudo (root)
   20  sudo apt-get install pip
   21  #before you 'apt-search', update our libraries by typing 'sudo apt-get update'
   22  sudo apt-get update
   23  history
   24  apt search pip
   25  sudo apt-get install python-pip
   26  sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy
   27  sudo apt-get install git emacs
   28  #create user acct for yourself
   29  sudo adduser reshama
   30  ls
   31  sudo visudo
   32  history
ubuntu@ip-172-31-59-73:/home$ 

```

###AWS:  adduser reshama
```
reshama$ pwd
/Users/reshamashaikh/.ssh
reshama$ ls *ds7*
-r--------@ 1   1692 Apr 10 17:14 awskeyds7.pem
reshama$ #copy this public key to aws .ssh/authorized_keys
reshama$ ls
total 112
-r--------@ 1   1692 Apr 10 17:14 awskeyds7.pem
reshama$ emacs *ds7*

[1]+  Stopped                 emacs *ds7*
reshama$ 
```
