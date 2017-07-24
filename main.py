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
        template = jinja_env.get_template('main.html')
        self.response.out.write(template.render())

class Signup(webapp2.RequestHandler):
    def get(self):
        cur_user = users.get_current_user()
        email = cur_user.email()
        key = ndb.Key('User', email)
        user_email = key.get()
        if not email:
            template = jinja_env.get_template('signup.html')
            self.response.out.write(template.render())
        else:
            self.redirect('/profile')


class Login(webapp2.RequestHandler):
    def get(self):
        log_url = users.create_login_url('/')
        self.redirect('/profile')


class ChatHandler(webapp2.RequestHandler):
    def get(self):
        if cur_user:
        



class Profile(webapp2.RequestHandler):
    def post(self):
        log_url = users.create_logout_url('/')
        first_name = self.request.get('first_name')
        last_name = self.request.get('last_name')
        job = self.request.get('job')
        city = self.request.get('city')
        state = self.request.get('state')
        bio = self.request.get('bio')
        variables = {
            'first_name': first_name,
            'last_name': last_name,
            'job': job,
            'city': city,
            'state': state,
            'bio': bio,
            'log_url': log_url
        }
        template = jinja_env.get_template('profile.html')
        self.response.out.write(template.render(variables))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', Signup),
    ('/login', Login),
    ('/profile', Profile)
], debug= True)
