from flask import Flask, Response, request
from item_actions import ItemActions
import json

app = Flask(__name__)
item_actions = ItemActions()

@app.route('/')
def home():
    return 'Welcome to CAFFE SERVICE'

@app.route('/menu/all', methods=['GET'])
@app.route('/menu/all',methods=['GET'])
def display_all_menu_items():
    items = item_actions.display_all_menu_items()
    print (items)
    return Response(json.dumps(items),mimetype='application/json',status=200)

@app.route('/menu/get/<string:item_id>',methods=['GET'])
def display_one_menu_item(item_id):
    items = item_actions.display_one_menu_item(item_id)
    print(items)
    return Response(json.dumps(items),mimetype='application/json',status=200)

@app.route('/menu/add_item', methods=['POST'])
def add_menu_item():
    request_data = request.get_json()
    menu_item_id = request_data['menu_item_id']
    menu_item_name = request_data['menu_item_name']
    menu_item_description = request_data['menu_item_description']
    menu_item_price = request_data['menu_item_price']
    added_item = item_actions.add_menu_item(menu_item_id, menu_item_name, menu_item_description, menu_item_price)
    if added_item == {}:
        return Response("{'error': 'Error addding the item'}",mimetype='application.json',status=500)
    return Response(json.dumps(added_item),mimetype='application/json',status=201)

@app.route('/menu/del/<string:item_id>',methods=['POST'])
def delete_a_menu_item(item_id):
    items = item_actions.delete_a_menu_item(item_id)
    print(items)
    return Response(json.dumps(items),mimetype='application/json',status=200)

@app.route('/cart/get/<string:cust_name>', methods=['GET'])
def display_all_cart_items(cust_name):
  items = item_actions.get_all_cart_items(cust_name)
  print(items)
  return Response(json.dumps(items), mimetype='application/json', status=200)

@app.route('/cart/add_item', methods=['POST'])
def add_cart_items():
  request_data = request.get_json()
  menu_item_id = request_data['menu_item_id']
  order_quantity = request_data['order_quantity']
  customer_name = request_data['customer_name']

  added_item = item_actions.add_cart_item(menu_item_id, order_quantity, customer_name)
  if added_item == {}:
    return Response("{'error': 'Erro addding the item'}", mimetype='application/json', status=500)
  return Response(json.dumps(added_item), mimetype='application/json', status=201)

@app.route('/cart/set/<int:cart_id>', methods=['POST'])
def update_order_quantity(cart_id):
  request_data = request.get_json()
  order_quantity = request_data['order_quantity']

  added_item = item_actions.update_order_quantity(cart_id, order_quantity)
  if added_item == {}:
    return Response("{'error': 'Error updating the item'}", mimetype='application/json', status=500)
  return Response(json.dumps(added_item), mimetype='application/json', status=201)

@app.route('/cart/del/<string:cart_id>',methods=['POST'])
def delete_cart_item(cart_id):
    items = item_actions.delete_cart_item(cart_id)
    print(items)
    return Response(json.dumps(items),mimetype='application/json',status=200)

if __name__ == '__main__':
    app.run(debug=True,port = 5001,host = "0.0.0.0")