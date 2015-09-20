
###### print working directory

`$ pwd`

**list all packages**
```
$ pip freeze
```

**delete directory**
```
$ rmdir ds3     # only removes empty directories
rmdir: ds3: Directory not empty

$ rm -rf ds3    # rf = recursive function ; removes non-empty directories
```


```
# get number of lines in file:  wc -l filename.txt
wc -l tweets.json

# get line numbers of all files in directory
wc -l *

# prints vertically, specifies which are directories
ls -alF   			

# remove first line of file
tail -n +2 mailing100k.csv > mail100k.csv

# take lines, after row 20,000 and put in new file
tail -n +20001 mail100k.csv > mail80k.csv

# take lines 1 to 20,000 and put in new file
tail -n +1 mail100k.csv | head -n 20000 > mail20k.csv

# pull data from url
curl https://archive.ics.uci.edu/ml/machine-learning-databases/voting-records/house-votes-84.data > house_votes_84.csv


# look for text within a directory and sub-dirs
grep -R "_django1" ./*   
```
