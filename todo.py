from flask import Flask,jsonify,request


app=Flask(__name__)

items=[
    {"id":1,"name":"item 1","description":"this is item 1"},
    {"id":2,"name":"item 2","description":"this is item 2"},
    {"id":3,"name":"item 3","description":"this is item 3"}
]
@app.route("/")
def home():
    return "<html><h1>welcome to the TO DO LIST App</h1></html>"

@app.route("/items",methods=["GET"])
def items():
    return jsonify(items)

@app.route("/items/<int:item_id>",methods="GET")
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error:item not found"})
    else:
        return jsonify(item)

if __name__=="__main__":
    app.run(port=9999,debug=True)