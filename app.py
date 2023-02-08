# import packages
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
# get environment variable
import os 
from dotenv import load_dotenv
load_dotenv()

# instantiate flask and establish PostgreSQL database connection
app = Flask(__name__)
if os.getenv('DATABASE_URL'):
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://", 1)
#app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{username}:{password}@localhost:{port}/{dbname}"
db = SQLAlchemy(app)

# create restaurant review table
class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reviewer = db.Column(db.String(100), nullable=False)
    restaurant = db.Column(db.String(100), nullable=False)
    cuisine = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer)
    review = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    # debugging purposes
    def __repr__(self):
        return f'<Reviewer {self.reviewer}>'
# create table
with app.app_context():
    db.create_all()

# home page
@app.route('/')
def index():
    reviews = Reviews.query.all()
    return render_template('index.html', reviews=reviews)

# submit new reviews
@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        reviewer = request.form['fname']
        restaurant = request.form['fresturant']
        cuisine = request.form['fcuisine']
        rating = int(request.form['frating'])
        review_content = request.form['freview']
        
        review = Reviews(reviewer=reviewer,
                         restaurant=restaurant,
                         cuisine=cuisine,
                         rating=rating,
                          review=review_content)
        db.session.add(review)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('create.html')

# check individual review
@app.route('/<int:review_id>/')
def individual_review(review_id):
    individual_review = Reviews.query.get_or_404(review_id)
    return render_template('review.html', review=individual_review)

# edit reviews
@app.route('/<int:review_id>/edit/', methods=('GET', 'POST'))
def edit(review_id):
    individual_review = Reviews.query.get_or_404(review_id)

    if request.method == 'POST':
        reviewer = request.form['fname']
        restaurant = request.form['fresturant']
        cuisine = request.form['fcuisine']
        rating = int(request.form['frating'])
        review_content = request.form['freview']

        individual_review.reviewer = reviewer
        individual_review.restaurant = restaurant
        individual_review.cuisine = cuisine
        individual_review.rating = rating
        individual_review.review = review_content

        db.session.add(individual_review)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', review=individual_review)

# delete review
@app.post('/<int:review_id>/delete/')
def delete(review_id):
    individual_review = Reviews.query.get_or_404(review_id)
    db.session.delete(individual_review)
    db.session.commit()
    return redirect(url_for('index'))

# about page
@app.route('/about')
def about():
    return render_template('about.html')