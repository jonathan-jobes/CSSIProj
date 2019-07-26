import webapp2
import jinja2
import os

# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        firstwelcome = the_jinja_env.get_template('Templates/FIRSTWELCOME.html')
        self.response.write(firstwelcome.render())
    def post(self):
        self.response.write("A post request to the EnterInfoHandler")

class SignInHandler(webapp2.RequestHandler):
    def get(self): 
        welcome_template = the_jinja_env.get_template('Templates/signin.html')
        self.response.write(welcome_template.render())
class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('Templates/welcome.html')
        self.response.write(welcome_template.render())
app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/welcome.html', RegisterHandler),
    ('/signin.html', SignInHandler),
], debug=True)
