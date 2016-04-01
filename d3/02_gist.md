
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

##Create a Gist**  
## Usage

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

Opens browser with this gist:  
https://gist.github.com/reshama/ee81823a8096de111624b5f089d3dd4a

