from flask import Flask
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    description = db.Column(db.String(200), unique=False, nullable=True)
    directions = db.Column(db.String(200), unique=False, nullable=True)

    def __repr__(self):
        return '<Recipe %r>' % self.title


@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def print_recipes_from_db():
	output = ""
	for recipe in Recipe.query.all():
		output += recipe.title + "<br>"
		output += recipe.description + "<br>"
		output += recipe.directions + "<br> <br><br>"
	return output


@app.route('/recipe')
def recipes():
    recipe_title = 'pizza'
    return render_template('recipe.html', title=recipe_title)


@app.route('/recipe_args', methods=['GET'])
def recipes_arg_example():
    return request.args.get('title')
    # this returns 'pizza' if the url is
    # http://127.0.0.1:5000/recipe?title=pizza