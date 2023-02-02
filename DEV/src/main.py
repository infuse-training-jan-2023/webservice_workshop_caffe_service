from flask import Flask, Response ,request
from item_actions import ItemActions
import json
import requests

app = Flask(__name__)
item_actions = ItemActions()

@app.route('/')
def home():
    return 'Welcome to CAFFE SERVICE'

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


if __name__ == '__main__':
    app.run(debug=True,port = 5001,host = "0.0.0.0")