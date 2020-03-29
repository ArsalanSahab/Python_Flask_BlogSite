''' 
Notes : 

1. To activate debug mode on mac/linux in the terminal type :

                export FLASK_APP=myapp
                export FLASK_ENV=development

                now run the code using : flask run


2. Flask by default reads .html files from the `templates` folder

3. to render html templates , import the render_template function .

4. To dynamically manipulate html content 'Jinja2' is used as a built in language.

'''




#### IMPORTS ####
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



# CREATE INSTANCE OF FLASK 
app = Flask(__name__) # __name__ , makes it point to the current file


# DATABASE CONFIGURATION

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db' # /// : Relative Path | //// : Abs Path
db = SQLAlchemy(app)


# DATABASE DESIGNING

# Each Table is a Class Instance in the DATABASE
class BlogPost(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default= 'N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self):

        return ('Blog Post {id}'.format(id=self.id))


#### Routing #####

@app.route('/') # '/' indicates the root route (lets say homepage)
# @app.route('/home') , uncomment line to redirect both root and /home to index().
def index():

    return (render_template('index.html'))


@app.route('/posts')
def posts():

    return render_template('posts.html', posts=all_posts)




'''
# Route to any string user inputs in the URL
@app.route('/<string:name>')
def greet(name): # function will get the name argument from the .route and render greet message

    return ("Greetings {user_name}".format(user_name=name))

# Age teller
@app.route('/<int:num>')
def age_teller(num):

    return ("Your age is : {age}".format(age=num))



# Limiting Visitor to Specific HTTP Request Methods
@app.route('/get', methods=['GET'])
def get(methods):
    
    if (methods == 'GET'):

        return 'Horray GET request successful'
    return 'You canonly get this page sorry'

@app.route('/post', methods=['POST'])
def post(methods):

    return 


@app.route('/get-post', methods=['GET', 'POST'])
def get_and_post(methods):

    if (methods == 'GET' or methods == 'POST'):

        return 'GET or POST Sucessful'

    return 'Sorry only GET and POST Allowed'

'''



# Debugging
if __name__ == "__main__":

    # Allow Debug to See Errors
    app.run(debug=True)
  