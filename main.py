import binascii
import jinja2
import random
import logging
import os
import json
import random
import webapp2
import urllib
import urllib2
from google.appengine.api import users
from google.appengine.ext import ndb

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
message = ['Hey there Alex, how can I help?']

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
    is_logged_in = ndb.BooleanProperty()

class MainPage(webapp2.RequestHandler):
    def get(self):
        log_url = ''
        template = jinja_env.get_template('main.html')
        self.response.out.write(template.render())

class Changes(webapp2.RequestHandler):
    def get(self):
        cur_user = users.get_current_user()
        identity = cur_user.user_id()
        user_key = ndb.Key('User', identity)
        user = user_key.get()
        holder = cur_user.user_id()
        url = urllib.quote(holder)
        unique_url = ('/chat?id=' + url)
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
        user.put()
        template = jinja_env.get_template('profilechanges.html')
        self.response.out.write(template.render(variables))

class Send(webapp2.RequestHandler):
    def get(self):
        query = User.query()
        online_users = query.fetch()
        for user in online_users:
            if user.is_logged_in:
                url = user.unique_url
                user.is_logged_in = False
                user.put()
                self.redirect(url)
                break
        template = jinja_env.get_template('sorry.html')
        self.response.out.write(template.render())



class RoomHandler(webapp2.RequestHandler):
    def get(self):
        for room in Rooms:
            i=1

class Logout(webapp2.RequestHandler):
    def get(self):
        log_url = users.create_logout_url('/')
        cur_user = users.get_current_user()
        identity = cur_user.user_id()
        user_key = ndb.Key('User', identity)
        user = user_key.get()
        user.is_logged_in = False
        user.put()
        self.redirect(log_url)

class Login(webapp2.RequestHandler):
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
        holder = cur_user.user_id()
        url = urllib.quote(holder)
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
            unique_url = '/chat?id=' + url,
            is_logged_in = True
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
            'unique_url': user.unique_url
        }
        template = jinja_env.get_template('profile.html')
        self.response.out.write(template.render(variables))

    def get(self):
        cur_user = users.get_current_user()
        if cur_user:
            identity = cur_user.user_id()
            user_key = ndb.Key('User', identity)
            user = user_key.get()
            holder = cur_user.user_id()
            url = urllib.quote(holder)
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
                user.is_logged_in = True
                user.put()
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
        user = User.query()
        query = user.fetch()
        cur_user = users.get_current_user()
        logging.warning(message)
        logging.critical(message)
        if not cur_user:
            ident = self.request.get('id')
            unique_url = '/chat?id=' + ident
            query = User.query()
            host_users = query.fetch()
            host_user = None
            for user in host_users:
                if user.unique_url == unique_url:
                    host_user = user
            picture = "data:image;base64," + binascii.b2a_base64(host_user.picture)
            host_user.is_logged_in = False
            variables = {
                'first_name': host_user.first_name,
                'last_name': host_user.last_name,
                'job': host_user.job,
                'city': host_user.city,
                'state': host_user.state,
                'bio': host_user.bio,
                'picture': picture,
                'message': message
            }
            template= jinja_env.get_template('chatroom.html')
            self.response.out.write(template.render(variables))
        else:
            holder = cur_user.user_id()
            url = urllib.quote(holder)
            unique_url = ('/chat?id=' + url)
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
                    'user1': Rooms.user1,
                    'User' : User,
                    'message': message
                    }
            template= jinja_env.get_template('chatroom.html')
            self.response.out.write(template.render(variables))

    def post(self):
        user = User.query()
        query = user.fetch()
        cur_user = users.get_current_user()
        messaged = self.request.get('message')
        logging.warning(messaged)
        message.append(messaged)
        logging.critical(message)
        if not cur_user:
            variables = {
                'messages': message
            }
            template= jinja_env.get_template('chatroom.html')
            self.response.out.write(template.render(variables))
        else:
            holder = cur_user.user_id()
            url = urllib.quote(holder)
            unique_url = ('/chat?id=' + url)
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
                    'user1': Rooms.user1,
                    'User' : User,
                    'messages': message
                }
            template= jinja_env.get_template('chatroom.html')
            self.response.out.write(template.render(variables))
            self.response.out.write('message')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', Signup),
    ('/login', Login),
    ('/profile', Profile),
    ('/chat', ChatHandler),
    ('/send', Send),
    ('/logout', Logout),
    ('/changes', Changes)
], debug= True)
