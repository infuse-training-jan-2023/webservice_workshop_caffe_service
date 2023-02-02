from flask import Flask, Response 
# import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to CAFFE SERVICE'

@app.route('/menu/all')
def display_all_menu_items():
    return 'menu 1'

@app.route('/cart/<string:cust_name>')
def display_all_cart_items(cust_name):
    return cust_name

@app.route('/cart/add_item')
def add_cart_items():
    return "Add to cart"

if __name__ == '__main__':
    app.run(debug=True,port = 5001,host = "0.0.0.0")