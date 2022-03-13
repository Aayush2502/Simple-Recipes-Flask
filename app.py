from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json


with open('config.json', 'r') as c:
    params = json.load(c)["params"]


app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/simple-recipes'
db = SQLAlchemy(app)


'''sno,title,slug,user,description,content'''


class Recipes(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    slug = db.Column(db.String(50), nullable=False)
    user = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(2000), nullable=False)
    content = db.Column(db.String(120000000), nullable=False)
    date = db.Column(db.String(12), nullable=True)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    '''if ('user' in session and session['user'] == params['admin_user']):
        ###posts = Posts.query.all()
        return render_template('dashboard.html', params=params)'''

    if request.method == 'POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username == params['admin_user'] and userpass == params['admin_password']):
            # set the session variable
            session['user'] = username
            ###posts = Posts.query.all()
            return render_template('dashboard.html', params=params)

    return render_template('login.html', params=params)


@app.route("/post-recipes", methods=['GET', 'POST'])
def post_recipes():
    if request.method == 'POST':
        box_title = request.form.get('title')
        description = request.form.get('description')
        slug = request.form.get('slug')
        content = request.form.get('content')
        date = datetime.now()
        recipe = Recipes(title=box_title, slug=slug,
                         content=content, description=description, date=date)
        db.session.add(recipe)
        db.session.commit()
    return render_template('post-recipes.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/recipes")
def recipes():
    return render_template('recipes.html')


@app.route("/tags")
def tags():
    return render_template('tags.html')


app.run(debug=True)
