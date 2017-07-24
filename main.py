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

class User(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    job = ndb.StringProperty()
    city = ndb.StringProperty()
    state = ndb.StringProperty()
    bio = ndb.StringProperty()
    email = ndb.StringProperty(indexed = True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        log_url = ''
        template = jinja_env.get_template('templates/main.html')
        self.response.out.write(template.render())

class Help(webapp2.RequestHandler):
    def get(self):
        cur_user = users.get_current_user()
        email = cur_user.email()
        if email:
            key = ndb.Key('User', email)
            user_email = key.get()
            if not user_email:
                self.redirect('/signup')
        log_url = users.create_logout_url('/')
        variables = {
            'log_url': log_url
        }
        template = jinja_env.get_template('templates/profile.html')
        self.response.out.write(template.render(variables))

class Signup(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/signup.html')
        self.response.out.write(template.render())

class Login(webapp2.RequestHandler):
    def get(self):
        log_url = users.create_login_url('/')
        self.redirect(log_url)

class Profile(webapp2.RequestHandler):
    def post(self):
        template = jinja_env.get_template('templates/profile.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/start', Help),
    ('/signup', Signup),
    ('/login', Login),
    ('/profile', Profile)
], debug= True)
