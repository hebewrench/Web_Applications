from flask import render_template, url_for
from website import app
from website.models import User, Post

@app.route("/")
@app.route("/home")
def home():
  products=products.query.all()
  return render_template('home.html',title='Home', products=products)

@app.route('/')     #program registers pathways
@app.route('/WishList')
def WishList():
    return render_template('WishList.html', title='WishList')

@app.route('/')
@app.route('/Product')
def ProductPage():
    return render_template('product.html', title='Product')
