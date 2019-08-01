import webapp2
import jinja2
import os
import datetime
from models import NewUser
from google.appengine.ext import ndb
from webapp2_extras import sessions
# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def get_body_type_options(self, body_choice):
    if body_choice == 'Ectomorph':
        url = "../Static/images/typeA.png"
        self.response.write("Characteristics Summary: Often considered the leaner body type, it is very difficult for Ectopmorphs to gain weight and muscle, and very easy for them to lose fat. This is due to their fast metabolism, and means they must have high calorie diets with short and intense workout sessions in order to gain muscle or maintain build. Types of Training Recommended: Strength training, light cardio exercise. Meal Recommendations: Diet is the most important aspect of their routine in order to manipulate their weight. Ectopmorphs tolerate carbs very well, and thus should eat more carbs than anything else thoughout the day, especially during or after working out. Fruit and vegetables are important carbs for every meal, whilst grain carbs every other. Healthy fats and protein are good, as well as protein shakes for weight gain.")
    elif body_choice == 'Mesomorph':
        url = '../Static/images/typeB.png'
        self.response.write("Characteristics Summary: Typically an athletic body build, Mesomorphs can easily gain muscle and maintain a lower body fat. Type of Training Recommended: Strength (Weight specifically) training, Cardio exercise. Meal Recommendations: A well balanced diet is best, with slightly more carbs than proteins and fat (40/30/30) Lowfat proteins, complex carbs, and high fiber foods are best. Try avoiding high starches or surgary carbs unless it's in the morning or after exercise. Focus on light carbs and lean proteins,fruits, vegetables, and seeds. ")
    else:
        url = '../Static/images/typeC.png'
        self.response.write("Characteristics Summary: Often more soft than the other builds, Endomorphs pack extra body mass and find it difficult to lose it. However, they have high functioning muscles and are often successful at sports like football. They store energy well, but have low carb tolerance. This body type must maintain an exercise routine and healthy diet in order to keep fit. Types of Training Recommended: Heavier Cardio exercise, light to moderate focused Weight training. Meal Recommendations: Light carbs and heavier fats and protein work best. Avoid any carbs that are not eaten during or after working out.")
    return url

def get_regimen_options(self,fit_reg):
    if fit_reg == 'Reduce fat':
        return ['Aerobic exercise: This consists of activities that cause you to breathe , faster. Some examples include walking or running on a treadmill, dancing, swimming or water aerobic exercises, playing tennis, bicycle riding (stationary or not),', 'Strength training: This includes lifting weights, using resistance bands, using stairs, walking or running up hills, cycling (stationar or not), dancing, push ups, sit ups, or squats.']
    elif fit_reg == 'Build muscle':
        return ['Strength training: This includes lifting weights, using resistance bands, using stairs, walking or running up hills, cycling (stationar or not), dancing, push ups, sit ups, or squats.',"Resistance training: This type of exercise is like weight training, but you don't need the weights. Examples include bicep curls, shoulder press, bench press, barbell squats, push ups, chin ups, sit ups, and body squats."]
    elif fit_reg == 'Increase strength':
        return ['Strength training: This includes lifting weights, using resistance bands, using stairs, walking or running up hills, cycling (stationar or not), dancing, push ups, sit ups, or squats.', 'Balance exercise: This type of exercise strengthens the muscles we use to stay upright. Examples include tai chi, yoga, pilates, using a balance board, walking heel to toe.']
    else:
        return ['Aerobic exercise: This consists of activities that cause you to breathe , faster. Some examples include walking or running on a treadmill, dancing, swimming or water aerobic exercises, playing tennis, bicycle riding (stationary or not).', "Resistance training: This type of exercise is like weight training, but you don't need the weights. Examples include bicep curls, shoulder press, bench press, barbell squats, push ups, chin ups, sit ups, and body squats."]

def get_meal_options(self, mplan):
    if mplan == 'Option One':
        return []
    elif mplan == 'Option Two':
        return []
    elif mplan == 'Option Three':
        return []

# the handler section
class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        firstwelcome = the_jinja_env.get_template('Templates/FIRSTWELCOME.html')
        self.response.write(firstwelcome.render())
    def post(self):
        self.response.write("A post request to the EnterInfoHandler")
class BaseHandler(webapp2.RequestHandler):              # taken from the webapp2 extrta session example
    def dispatch(self):                                 # override dispatch
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)       # dispatch the main handler
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

class SignInHandler(BaseHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('Templates/signin.html')
        self.response.write(welcome_template.render())
    def post(self):
        Name = self.request.get('user-name')
        Word = self.request.get('pass-word')
        self.session['name']=Name
        self.session['word']=Word
        DataStore = NewUser.query().fetch()
        for user in DataStore:
            if user.Username == Name and user.Password == Word:
                temp = the_jinja_env.get_template('Templates/afterSignIN.html')
                self.response.write(temp.render())
                break

class FirstFitnessHandler(BaseHandler):
    def get(self):
        template1= the_jinja_env.get_template('Templates/fitnessp1.html')
        self.response.write(template1.render())
    def post(self):
        template1= the_jinja_env.get_template('Templates/fitnessp1.html')
        template2= the_jinja_env.get_template('Templates/signin.html')
        name=self.session.get('name')
        BodyType = NewUser.query().filter(NewUser.Username==name).get().Body
        BodyDict = {
        "body_type": BodyType,
        }
        self.response.write(template1.render(BodyDict))
class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('Templates/welcome.html')
        self.response.write(welcome_template.render())
    def post(self):
        template1 = the_jinja_env.get_template('Templates/fitnessp1.html')
        bodyType = self.request.get('user-BodyType')
        Password = self.request.get('password')
        Username = self.request.get('username')
        body_choice = self.request.get('user-BodyType')
        User = NewUser(Username=Username, Password=Password, Body=bodyType)
        User.put()
        bchoice = get_body_type_options(self, body_choice)
        BodyDict = {
        "body_type": bodyType,
        "information_body_type": bchoice
        }
        self.response.write(template1.render(BodyDict))

class SecondFitnessHandler(webapp2.RequestHandler):
    def get(self):
        template2 = the_jinja_env.get_template('Templates/fitnessp2.html')
        self.response.write(template2.render())
    def post(self):
        template2 = the_jinja_env.get_template('Templates/fitnessp2.html')
        Goals=self.request.get('user_goal')
        exercise_options=get_regimen_options(self, Goals)
        Exercise ={
        "user_Goals": Goals,
        "examp": exercise_options[0],
        "examp2": exercise_options[1]
        }
        self.response.write(template2.render(Exercise))
class SummaryHandler(webapp2.RequestHandler):
    def get(self):
        template3 = the_jinja_env.get_template('Templates/summary.html')
        self.response.write(template3.render())
    def post(self):
        template3 = the_jinja_env.get_template('Templates/summary.html')
        self.response.write(template3.render())

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
        #meals=self.request.get()

        self.response.write(template2.render(Date))
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}
app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/welcome.html', RegisterHandler),
    ('/signin.html', SignInHandler),
    ('/fitnessp1.html', FirstFitnessHandler),
    ('/fitnessp2.html', SecondFitnessHandler),
    ('/mealp1.html', MealOneHandler),
    ('/summary.html',SummaryHandler)
], config=config, debug=True)
