from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json


'''
with open('config.json', 'r') as c:
    params = json.load(c)["params"]
'''


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
    prep_time = db.Column(db.String(50), nullable=False)
    cook_time = db.Column(db.String(50), nullable=False)
    serv = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(120000000), nullable=False)
    ingre = db.Column(db.String(50), nullable=False)
    tip = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(12), nullable=True)


class proce(db.Model):
    slug = db.Column(db.String(50), nullable=False)
    step = db.Column(db.Integer, primary_key=True)
    proc = db.Column(db.String(1000), nullable=False)


class Ingredients(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(50), nullable=False)
    ingredient = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.String(50), nullable=False)


@app.route("/")
def hello():
    return render_template('index.html')


'''
@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    ''''''if ('user' in session and session['user'] == params['admin_user']):
        ###posts = Posts.query.all()
        return render_template('dashboard.html', params=params)''''''

    if request.method == 'POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username == params['admin_user'] and userpass == params['admin_password']):
            # set the session variable
            session['user'] = username
            ###posts = Posts.query.all()
            return render_template('rohan2 profile page/index.html', params=params)

    return render_template('rohan1 login page/index.html', params=params)
'''


@app.route("/post-recipes", methods=['GET', 'POST'])
def post_recipes():
    if request.method == 'POST':
        box_title = request.form.get('title')
        description = request.form.get('description')
        slug = box_title.replace(' ', '-')
        prep_time = request.form.get('prep-time')
        cook_time = request.form.get('cook-time')
        serv = request.form.get('serv')
        content = request.form.get('content')
        ingre = request.form.get('ingre')
        tip = request.form.get('tip')
        date = datetime.now()
        recipe = Recipes(title=box_title, slug=slug, prep_time=prep_time, cook_time=cook_time,
                         serv=serv, ingre=ingre, tip=tip, content=content, description=description, date=date)
        db.session.add(recipe)
        db.session.commit()
    return render_template('post-recipes.html')


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Recipes.query.filter_by(slug=post_slug).first()
    return render_template('post.html', post=post)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/recipes")
def recipes():
    return render_template('recipes.html')


@app.route("/tags")
def tags():
    return render_template('tags.html')


@app.route("/ingri")
def ingri():
    return render_template('ingri.html')


@app.route("/find-nutritional-value")
def nutritional():
    return render_template('find-nutritional-value.html')


app.run(debug=True)
