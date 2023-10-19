#backend goes here (Dynamic)
from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder='static') #tells flask about the location of the file

@app.route('/')     #program registers pathways
@app.route('/WishList')
def WishList():
    return render_template('WishList.html', title='WishList')


#Add other routings like above to give the user access to pages - Nav bar

#FrontPage
#View detailed information about an item
#Shopping basket
#Checkout                                               which are going to be accessible
#Managing stock
#Purchase Statistics s 
