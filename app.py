''' 
Notes : 

1. To activate debug mode on mac/linux in the terminal type :

                export FLASK_APP=myapp
                export FLASK_ENV=development

                now run the code using : flask run


2. Flask by default reads .html files from the `templates` folder

3. to render html templates , import the render_template function .

4. To dynamically manipulate html content 'Jinja2' is used as a built in language.

5. Jinja 2 Variable Format : {{variable here}}.

6. Jinja2 Block Format :  {% block your_block_name %} Content {% endblock %}

7. Jinja2 Loops Format :  {% for ___ in ____ %} Content {% endfor %}

8. Jinja2 Conditional Statement Format : {% if ______ %} Content {% else %} Content {% endif %}
'''




#### IMPORTS ####
from flask import Flask, render_template, request, redirect
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


@app.route('/posts', methods=['GET', 'POST'])
def posts():


    # Check if method is POST
    if (request.method == 'POST'):

        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        # Create new BlogPost instance
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        # Add to current Session
        db.session.add(new_post)
        # Commit to DATABASE
        db.session.commit()

        return redirect('/posts')

    else :

        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)


@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():

    if request.method == 'POST':

        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        
        return redirect('/posts')

    else:

        return render_template('new_post.html')

@app.route('/posts/delete/<int:id>')
def delete_post(id):

    # Get the Post to delete from Datbase
    post_to_delete = BlogPost.query.get_or_404(id)
    # Delete and commit
    db.session.delete(post_to_delete)
    db.session.commit()

    return redirect('/posts')


@app.route('/posts/edit/<int:id>',methods=['GET', 'POST'])
def edit_post(id):

    post_to_edit = BlogPost.query.get_or_404(id)

    if (request.method == 'POST'):

        
        post_to_edit.title = request.form['title']
        post_to_edit.author = request.form['author']
        post_to_edit.content = request.form['content']
        db.session.commit()

        return redirect('/posts')

    else :

        return render_template('edit_post.html', post= post_to_edit)


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
  