from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '207bb843773ab5c8f14c446c51043b87e37a791af0267138'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c1922896:PASSWORD@csmysql.cs.cf.ac.uk:3306/c1922896_products'

db = SQLAlchemy(app)

from website import routes
