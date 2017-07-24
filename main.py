import jinja2
import logging
import os
import json
import webapp2
import urllib
import urllib2
from google.appengine.api import users
from google.appengine.ext import ndb

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('main.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug= True)
