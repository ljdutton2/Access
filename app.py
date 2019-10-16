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
    "departure": "611 Jones street, 94102 San Francisco",
    "arrival": "555 Post street, 94102 San Francisco"
}

@app.route('/', methods=["POST"])
def home():
    return render_template('locations_index.html',locations=locations.find())
    

@app.route('/add',methods=['POST'])
def location_new(): 
        location_data = {
            'departure' : request.form.get('departure'),
            'arrival' : request.form.get('arrival')
        }
        items = locations.find()
        location_id = locations.insert_one(location_data).location_id
        #map = folium.Map(location=(10.3000, -84.8167),zoom_start=13)
        #map.save('map_index.html')
        print(location_id)
        return redirect(url_for('location_save',location_id=location_id))

@app.route('/save', methods=["POST"])
def location_save():
    return render_template('map_index.html')
map = folium.Map(location=(10.3000, -84.8167),zoom_start=13)
map.save('map_index.html')

if __name__ == '__main__':
    app.run(debug=True)