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


class History(ndb.Model):
    username= ndb.StringProperty(indexed=True)
    count = ndb.IntegerProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    update_at = ndb.DateTimeProperty(auto_now=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        cur_user = users.get_current_user()
        log_url = ''
        if cur_user:
            log_url = users.create_logout_url('/')
        else:
            log_url = users.create_login_url('/')
        if cur_user:
            query = History.query(ancestor=ndb.Key('User', cur_user.email())).order(-History.created_at)
            results = query.fetch()
        template = jinja_env.get_template('main.html')
        variables = {
        'data': data,
        'gif_urls': gif_urls,
        'q': search_terms,
        'user': cur_user,
        'log_url': log_url,
        'history': results
        }
        self.response.out.write(template.render(variables))

app = webapp2.WSGIApplication([
    ('/',MainPage)
], debug= True)
