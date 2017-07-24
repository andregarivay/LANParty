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

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

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
        template = jinja_environment.get_template('main.html')
        self.response.out.write(template.render())

class Login(webapp2.RequestHandler):
    def get(self):
        cur_user = users.get_current_user()
        email = cur_user.user_email()
        if email:
            key = ndb.Key('User', email)
            user_email = key.get()
            if not user_email:
                self.redirect('/signup')
            else:
                self.redirect('/profile')

class Signup(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('signup.html')
        self.response.out.write(template.render())

class Profile(webapp2.RequestHandler):
    def post(self):
        first_name = self.response.get(first_name)
        variables = {
            'first_name': first_name
        }
        template = jinja_environment.get_template('profile.html')
        self.response.out.write(template.render(variables))


class ChatHandler(webapp2.RequestHandler):
    def get(self):
        if cur_user:
            unique_user_id = random.randint(0, 1000000)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/login', Login),
    ('/signup', Signup),
    ('/profile', Profile),
], debug= True)
