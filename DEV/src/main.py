from flask import Flask, Response 
from item_actions import ItemActions
import json
import requests

app = Flask(__name__)
item_actions = ItemActions()

@app.route('/')
def home():
    return 'Welcome to CAFFE SERVICE'

@app.route('/menu/all')
def display_all_menu_items():
    items = item_actions.display_all_menu_items()
    print (items)
    return Response(json.dumps(items),mimetype='application/json',status=200)

@app.route('/menu/add_item')
def add_menu_item():
    return 'menu all'

# @app.route('/menu/<string:item_id>')
# def display_one_menu_item():
#     return 'menu 1'

# @app.route('/cart/<string:cust_name>')
# def display_all_cart_items(cust_name):
#     return cust_name

# @app.route('/cart/add_item')
# def add_cart_items():
#     return "Add to cart"

if __name__ == '__main__':
    app.run(debug=True,port = 5001,host = "0.0.0.0")