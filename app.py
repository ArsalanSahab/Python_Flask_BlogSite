''' 
Notes : 

1. To activate debug mode on mac/linux in the terminal type :

                export FLASK_APP=myapp
                export FLASK_ENV=development

                now run the code using : flask run
'''




#### IMPORTS ####
from flask import Flask


# CREATE INSTANCE OF FLASK 
app = Flask(__name__) # __name__ , makes it point to the current file

#### Routing #####

@app.route('/') # '/' indicates the root route (lets say homepage)
# @app.route('/home') , uncomment line to redirect both root and /home to index().
def index():

    return ('<h1>Home Page</h1>')




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
  