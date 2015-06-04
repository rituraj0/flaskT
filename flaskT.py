import hashlib;
import pycps
from pycps.query import *
import xml.etree.ElementTree as ET
import uuid
from random import randint
import os
from time import sleep
from flask import Flask, jsonify
from bs4 import BeautifulSoup
from operator import itemgetter
from time import strptime,strftime,mktime,gmtime,localtime
import json
from urllib2 import urlopen
import threading
# import the flask extension
from flask.ext.cache import Cache   

app = Flask(__name__)

# define the cache config keys, remember that it can be done in a settings file
app.config['CACHE_TYPE'] = 'simple'

# register the cache instance and binds it on to your app 
app.cache = Cache(app)  

@app.route('/')
@app.cache.cached(timeout=10000) # cache for 1 hour
def index():   
    return "Wecome to tutorial";

def start_server():
    port = int(os.environ.get('PORT',5432 ))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
	start_server();