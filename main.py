import webapp2
import jinja2
import os
import datetime

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
    def post(self):
        template1 = the_jinja_env.get_template('Templates/fitnessp1.html')
        bodyType = self.request.get('user-BodyType')
        Body = {
        "body_type": bodyType
        }
        self.response.write(template1.render(Body))

class SecondFitnessHandler(webapp2.RequestHandler):
    def get(self):
        template2 = the_jinja_env.get_template('Templates/fitnessp2.html')
        self.response.write(template2.render())
    def post(self):
        template2 = the_jinja_env.get_template('Templates/fitnessp2.html')
        Goals=self.request.get('user_goal')
        Exercise ={
        "user_Goals": Goals
        }
        self.response.write(template2.render(Exercise))
class MealOneHandler(webapp2.RequestHandler):
    def get(self):
        template2 = the_jinja_env.get_template('Templates/mealp1.html')
        self.response.write(template2.render())
    def post(self):
        template2 = the_jinja_env.get_template('Templates/mealp1.html')
        today= datetime.datetime.now()
        if today.month==1:
            month="January"
        elif today.month==2:
            month="February"
        elif today.month==3:
            month="March"
        elif today.month==4:
            month="April"
        elif today.month==5:
            month="May"
        elif today.month==6:
            month="June"
        elif today.month==7:
            month="July"
        elif today.month==8:
            month="August"
        elif today.month==9:
            month="September"
        elif today.month==10:
            month="October"
        elif today.month==11:
            month="November"
        elif today.month==12:
            month="December"
        Date ={
        "blank": month
        }
        self.response.write(template2.render(Date))
app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/welcome.html', RegisterHandler),
    ('/signin.html', SignInHandler),
    ('/fitnessp2.html', SecondFitnessHandler),
    ('/mealp1.html', MealOneHandler),
], debug=True)
