# DarkmaskAPI

<p class="views" align="right"><img src="https://komarev.com/ghpvc/?username=darkmash-org-darkmask.api&label=Project%20views&color=0e75b6&style=flat" alt="darkmash-org" /></p>


## About :

An API for masking Urls..

## Url :
    
  https://Darkmask.darkmash.repl.co

## Using :

To use the service [GET - method] ,
  ```
  https://Darkmask.darkmash.repl.co/from
  ```
 
 - give the url as url in headers
    
 - returns a masked url

## To use with python :

    import requests as r
    url = "https://darkmash-org.github.io/"
    print(r.get("https://Darkmask.darkmash.repl.co/from", headers = {"url":url}).text)

### On visiting (main page):

![Alt text](https://cdn.discordapp.com/attachments/951417646191083551/1075808861216325694/image.png?raw=true "main-page")
