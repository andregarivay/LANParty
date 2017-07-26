import binascii
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
    email = ndb.StringProperty()
    identity = ndb.StringProperty()
    picture = ndb.BlobProperty()
    unique_url = ndb.StringProperty()

class MainPage(webapp2.RequestHandler):
    def get(self):
        log_url = ''
        template = jinja_env.get_template('main.html')
        self.response.out.write(template.render())

class RoomHandler(webapp2.RequestHandler):
    def get(self):
        for room in Rooms:
            i=1

class Login(webapp2.RequestHandler):
    def get(self):
        cur_user = users.get_current_user()
        logging.info(dir(cur_user))
        if cur_user:
            identity = cur_user.user_id()
            logging.warning(identity)
            user_key = ndb.Key('User', identity)
            logging.warning(user_key)
            user = user_key.get()
            logging.warning(user)
            if user:
                user.key = user_key
                user.put()
                logging.warning(user)
                self.redirect('/profile')
            else:
                self.redirect('/signup')
        else:
            log_url = users.create_login_url('/login')
            self.redirect(log_url)


class Signup(webapp2.RequestHandler):
    def get(self):
        cur_user = users.get_current_user()
        if cur_user:
            identity = cur_user.user_id()
            user_key = ndb.Key('User', identity)
            user = user_key.get()
            if user:
                user.key = user_key
                user.put()
                self.redirect('/profile')
            else:
                template = jinja_env.get_template('signup.html')
                self.response.out.write(template.render())
        else:
            self.redirect('/login')

class Profile(webapp2.RequestHandler):
    def post(self):
        cur_user = users.get_current_user()
        user_key = ndb.Key('User', users.get_current_user().user_id())
        user = user_key.get()
        holder = {'id': Rooms.user1}
        url = urllib.urlencode(holder)
        user = User(
            first_name = self.request.get('first_name'),
            last_name = self.request.get('last_name'),
            job = self.request.get('job'),
            city = self.request.get('city'),
            state = self.request.get('state'),
            bio = self.request.get('bio'),
            email = self.request.get('email'),
            identity = cur_user.user_id(),
            picture = self.request.get('picture'),
            unique_url = '/chat?id=' + url
        )
        user.key = user_key
        user.put()
        log_url = users.create_logout_url('/')
        picture = "data:image;base64," + binascii.b2a_base64(user.picture)
        variables = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'job': user.job,
            'city': user.city,
            'state': user.state,
            'bio': user.bio,
            'log_url': log_url,
            'picture': picture,
            'unique_url': unique_url
        }
        template = jinja_env.get_template('profile.html')
        self.response.out.write(template.render(variables))

    def get(self):
        cur_user = users.get_current_user()
        if cur_user:
            identity = cur_user.user_id()
            user_key = ndb.Key('User', identity)
            user = user_key.get()
            holder = {'id': Rooms.user1}
            url = urllib.urlencode(holder)
            unique_url = ('/chat?id=' + url)
            if user:
                user.key = user_key
                user.put()
                log_url = users.create_logout_url('/')
                if user.picture:
                    picture = "data:image;base64," + binascii.b2a_base64(user.picture)
                else:
                    picture = "https://thumb1.shutterstock.com/display_pic_with_logo/615538/568463788/stock-vector-avatar-icon-vector-illustration-style-is-flat-iconic-symbol-black-color-transparent-background-568463788.jpg"
                variables = {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'job': user.job,
                    'city': user.city,
                    'state': user.state,
                    'bio': user.bio,
                    'log_url': log_url,
                    'picture': picture,
                    'unique_url': unique_url
                }
                template = jinja_env.get_template('profile.html')
                self.response.out.write(template.render(variables))
            else:
                self.redirect('/signup')


class Rooms(ndb.Model):
    user1 = User.key
    #User2 = user.key
    comments = ndb.StringProperty()

class Room(Rooms):
    count = ndb.IntegerProperty()


class ChatHandler(webapp2.RequestHandler):
    def get(self):
<<<<<<< HEAD
        i = 0
=======
        i = 100
>>>>>>> daa59b07d13c66e0691c40c472793a0c690406ad
        user = User.query()
        query = user.fetch()
        cur_user = users.get_current_user()
        if not cur_user:
<<<<<<< HEAD
            for u in query:
                i = 1 + i
=======
>>>>>>> daa59b07d13c66e0691c40c472793a0c690406ad
            variables = {
                'i': i
            }
            template= jinja_env.get_template('chatroom.html')
            self.response.out.write(template.render(variables))
        else:
<<<<<<< HEAD
            i = 1
            variables = {

            }
            template= jinja_env.get_template('chatroom.html')
            self.response.out.write(template.render(variables))
=======
            holder = {'id': Rooms.user1}
            url = urllib.urlencode(holder)
            unique_url = ('/chat?id=' + url)
        #for key in User.iter(keys_only=True):
        #    i = i + 1
            cur_user = users.get_current_user()
            identity = cur_user.user_id()
            user_key = ndb.Key('User', identity)
            user = user_key.get()
            picture = "data:image;base64," + binascii.b2a_base64(user.picture)
            variables = {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'job': user.job,
                    'city': user.city,
                    'state': user.state,
                    'bio': user.bio,
                    'picture': picture,
                    'i': i,
                    'user1': Rooms.user1,
                    'User' : User
                }
            template= jinja_env.get_template('chatroom.html')
            self.response.out.write(template.render(variables))

    def post(self):
        i = 100
        user = User.query()
        query = user.fetch()
        cur_user = users.get_current_user()
        message = self.request.get('message')
        if not cur_user:
            variables = {
                'i': i,
                'message': message
            }
            template= jinja_env.get_template('chatroom.html')
            self.response.out.write(template.render(variables))
        else:
            holder = {'id': Rooms.user1}
            url = urllib.urlencode(holder)
            unique_url = ('/chat?id=' + url)
        #for key in User.iter(keys_only=True):
        #    i = i + 1
            cur_user = users.get_current_user()
            identity = cur_user.user_id()
            user_key = ndb.Key('User', identity)
            user = user_key.get()
            picture = "data:image;base64," + binascii.b2a_base64(user.picture)
            variables = {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'job': user.job,
                    'city': user.city,
                    'state': user.state,
                    'bio': user.bio,
                    'picture': picture,
                    'i': i,
                    'user1': Rooms.user1,
                    'User' : User,
                    'message': message
                }
            template= jinja_env.get_template('chatroom.html')
            self.response.out.write(template.render(variables))
>>>>>>> daa59b07d13c66e0691c40c472793a0c690406ad

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', Signup),
    ('/login', Login),
    ('/profile', Profile),
    ('/chat', ChatHandler)
], debug= True)
