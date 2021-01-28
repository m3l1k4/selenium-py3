## selenium-py3 <br/>
# How to get selenium working on mac


### Steps :

1) Install chromedriver matching chrome version from https://sites.google.com/a/chromium.org/chromedriver/downloads
* Don't download file with m1 in name, 32bit exe wont work on mac 

2) Place the file chromedriver in /usr/local/bin
3) Open terminal in directory and execute xattr -d com.apple.quarantine chromedriver 
* This allows to bypass the cannot open error

tbc
