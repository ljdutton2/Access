from flask import Flask, render_template, request, redirect, url_for
import requests
from bson.objectid import ObjectId
from pymongo import MongoClient
import os
from pprint import pprint
from datetime import datetime
from folium import folium


app = Flask(__name__)
FLASK_APP = app

host = os.environ.get('MONGODB_URI','mongodb://127.0.0.1:27017/Access')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
locations = db.locations

location_data = {
    "departure": "611 Geary street, 94102 San Francisco",
    "arrival": "555 Post street, 94102 San Francisco"
}
result = locations.insert_one(location_data)
print('Route: {0}'.format(result.inserted_id))

map = folium.Map(location=(10.3000, -84.8167),zoom_start=10)
map.save('map_index.html')

@app.route('/',methods=['GET'])
def home():
    if request.method == 'GET':
        location_data = {
        "departure": "611 Geary street, 94102 San Francisco",
        "arrival": "555 Post street, 94102 San Francisco"
    }
   
    result = locations.insert_one(location_data)
    print('Route: {0}'.format(result.inserted_id))
    return render_template('index.html')






 











if __name__ == "main":
    app.run()