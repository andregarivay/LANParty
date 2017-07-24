import jinja2
import random
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
        cur_user = users.get_current_user()
        log_url = ''
        if not cur_user:
            template = jinja_env.get_template('main.html')
            self.response.out.write(template.render())
        else:
            log_url = users.create_logout_url('/')
            variables = {
                'log_url': log_url
            }
            template = jinja_env.get_template('profile.html')
            self.response.out.write(template.render(variables))

class Signup(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('signup.html')
        self.response.out.write(template.render())

class Login(webapp2.RequestHandler):
    def get(self):
        log_url = users.create_login_url('/')
        self.redirect(log_url)

class ChatHandler(webapp2.RequestHandler):
    def get(self):
        if cur_user:
            unique_user_id = random.randint(0, 1000000)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', Signup),
    ('/login', Login),
], debug= True)
