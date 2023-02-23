"""
Darkmask API
By ~ Darkmash
"""

from flask import Flask, request
from flask_cors import CORS
import logging
import random
import string
import json


app = Flask(__name__)
CORS(app)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def read():
  db = open("db.json", "r")
  URLS =json.loads(db.read())
  db.close()  
  return URLS

def write(new):
  db = open("db.json", "w")
  db.write(json.dumps(new))
  db.close()  

def set(a,b):
  db = read()
  print(db)
  db[a] = b
  write(db)

def encode_url(url):
  print(f"ENCODE : URL : {url}")
  while True:
    result = ''.join((random.choice(string.ascii_lowercase) for x in range(8)))
    try:
      read()[result]
    except:
      break 
  set(result, url)
  return result

def decode_url(url):
  url_ = read()
  if url_[url] == None:
    return False
  print(f"DECODE : URL : {url_[url]}")
  return url_[url]

@app.route('/')
def main_func_():
  print("PING__UPTIME")
  return """
   <meta
      property="og:image"
      content="https://cdn.discordapp.com/attachments/1023460179087470663/1062001193733337158/image.png"
    />
    <meta
      name="description"
      content="An API for generating masked urls."
    />
    <meta name="keywords" content="mask , url , darkmask ,darkmash , tools , startup , coders" />
    <link
      rel="icon"
      type="image/png"
      href="https://cdn.discordapp.com/attachments/1023460179087470663/1062001193733337158/image.png"
    />
        <title>Darkmask API ~ Darkmash</title>
  ######## DARKMASH ~ DARKMASK API ~ V.1.0.0 ###################<br>
  To use the service [GET - method] ,<br>
       &nbsp /from <br>
      &nbsp &nbsp give the url as url in headers <br>       
      &nbsp &nbsp returns a masked url <br>
##############################################################
  """


@app.route('/from', methods=['GET'])
def get():
  url = request.headers.get("url")
  return "https://Darkmask.darkmash.repl.co/" + encode_url(url)


@app.route('/<url>')
def random_(url):
  try:
    url = decode_url(url)
    if url == False:
      return f"""
      ERROR : Site Not Found
      """
    if "https://" in url :
      return f"""
  <script>
location.href = '{url}';
</script>
      """
    else:
      return f"""
  <script>
location.href = 'https://{url}';
</script>
  """
  except:
    return "Invalid Url.."

app.run(host="0.0.0.0", port=8080)
