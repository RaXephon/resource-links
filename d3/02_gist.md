
[Let's Make a Block](https://bost.ocks.org/mike/block/#develop)  

**Open terminal window & navigate to folder**  
```
$ dvrs
$ pwd
/Users/reshamashaikh/_ds/metis/metisgh/dataviz_rs
```
**Open files using sublime editor**  
```
$ sublime .
```
Back in the terminal, fire up the web server so that you can preview your code in a web browser:  
```
$ http-server &
```
With http-server running, visit [localhost:8080](http://localhost:8080/) in your browser and refresh whenever you make changes. Iterate as many times as you like to develop your example, bouncing between your text editor and web browser. 

---

##Create a Gist

All my gists:  
https://gist.github.com/reshama

To upload all files in the current directory to your new gist:

```bash
gistup
```

If you just want to create a gist from a single file, try this instead:

```bash
gistup index.html
```

If you specify any options, such as a private gist, you must separate files from options with a double-dash (--) like this:

```bash
gistup --private -- index.html
```

If you want to update your gist later, just use git:

```bash
edit index.html
git commit -m 'Made some awesome changes.'
git push
```
---
**Step 1:**  
https://gist.github.com/reshama

**Step 2:  Choose gist**  
reshama / barley.csv  

**Step 3:  Generate block (at upper right, click on button:  bl.ocks (with arrow pointing to upper right)**:  
Gist will be viewable

--- 

Opens browser with this gist:  
https://gist.github.com/reshama/ee81823a8096de111624b5f089d3dd4a  
It becomes:  
http://bl.ocks.org/reshama/ee81823a8096de111624b5f089d3dd4a  

Now that you’ve made a gist, you can view it on bl.ocks.org! Simply copy the gist number and replace the URL. For example,

https://gist.github.com/mbostock/4060606

becomes

http://bl.ocks.org/mbostock/4060606

You can also install the bl.ocks.org browser extension, which inserts a convenient button on the GitHub Gist page to take you to the corresponding block. 

---

Gistup works with binary files, too!

Arguments:

* --description, -m - provide an optional description
* --interactive, -i - request confirmation of every file before adding
* --exclude, -x - skip files matching pattern; may use wildcards
* --private, --no-public - make a secret gist
* --open [url] - specify the URL to open after creating the gist
* --no-open - don’t open the created gist in your web browser when done
* --remote - specify the name of the git remote
* --help - show some help
* --version - print the current version of gistup

Gistup comes bundled with two helper programs: `gistup-rename` and `gistup-open`. Use `gistup-rename "description of gist"` to update the description of the gist in the current directory and `gistup-open` to open it for viewing in your default browser.

Source:  
https://github.com/mbostock/gistup

