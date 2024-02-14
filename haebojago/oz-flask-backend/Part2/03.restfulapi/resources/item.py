from flask import request
from flask_restful import Resource


 # DB의 대체 역할(간단한 DB 역할)
items = []


class Item(Resource):
    def get(self, name):
        for item in items:
            if item["name"] == name:
                return item
            
        return {"MSG" : "Item not found"}, 404

    def post(self, name):
        for item in items:
            if item["name"] == name:
                return {"MSG" : "Item already exists"}, 400
            
        data = request.get_json()

        new_item = {"name": name, "price": data["price"]}
        items.append(new_item)

        return new_item
    
    def put(self, name):
        data = request.get_json()
        for item in items:
            if item["name"] == name:
                item["price"] = data["price"]
                return item
            
        # 만약 업데이트하고자 하는 아이템 데이터가 없다면 -> 추가한다.
        new_item = {"name": name, "price" : data["price"]}
        items.append(new_item)
        
        return new_item
            

    def delete(self, name):
        global items
        items = [item for item in items if item["name"] != name]

        return {"MSG" : "Item deleted"} 
    
class ItemList(Resource):
    def get(self):
        pass