from google.appengine.ext import ndb

class NewUser(ndb.Model):
    type = ndb.StringProperty(required=True, default="NewUser")
    Username = ndb.StringProperty(required=True)
    Password = ndb.StringProperty(required=True)
    Body = ndb.StringProperty(required=True)
