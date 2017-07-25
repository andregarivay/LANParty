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

class Rooms(ndb.Model):
    User1 = User
    #User2 = user.id:
    comments = ndb.StringProperty()

class MainPage(webapp2.RequestHandler):
    def get(self):
        log_url = ''
        template = jinja_env.get_template('main.html')
        self.response.out.write(template.render())

class RoomHandler(webapp2.RequestHandler):
    def get(self):
        for room in Rooms:
            i=1

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
        cur_user = users.get_current_user()
        if cur_user:
            self.redirect('/profile')
        else:
            log_url = users.create_login_url('/signup')
            self.redirect(log_url)


class Signup(webapp2.RequestHandler):
    def get(self):
        cur_user = users.get_current_user()
        email = cur_user.email()
        if email:
            key = ndb.Key('User', email)
            user_email = key.get()
            if not user_email:
                template = jinja_environment.get_template('signup.html')
                self.response.out.write(template.render())
            else:
                self.redirect('/profile')

class Profile(webapp2.RequestHandler):
    def post(self):
        user = User()
        user.first_name = self.request.get('first_name')
        user.last_name = self.request.get('last_name')
        user.job = self.request.get('job')
        user.city = self.request.get('city')
        user.state = self.request.get('state')
        user.bio = self.request.get('bio')
        user.put()
        log_url = users.create_logout_url('/')
        variables = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'job': user.job,
            'city': user.city,
            'state': user.state,
            'bio': user.bio,
            'log_url': log_url
        }
        template = jinja_environment.get_template('profile.html')
        self.response.out.write(template.render(variables))

    def get(self):
        user = User()
        first_name = user.first_name
        last_name = user.last_name
        job = user.job
        city = user.city
        state = user.state
        bio = user.bio
        log_url = users.create_logout_url('/')
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



class ChatHandler(webapp2.RequestHandler):
    def get(self):
        if cur_user:
            unique_user_id = random.randint(0, 1000000)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', Signup),
    ('/login', Login),
    ('/profile', Profile)
], debug= True)
