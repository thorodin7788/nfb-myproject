'''
Created on 13 March 2018

@author: nestor
'''
import os
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from index import *

def main():
  http_server = HTTPServer(WSGIContainer(server))
  port = int(os.environ.get("PORT", 5000))
  http_server.listen(port)
  IOLoop.instance().start()
  
if __name__ == "__main__":
  main()
