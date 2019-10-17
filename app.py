 
from flask import Flask, render_template, request, redirect, url_for
import requests
from bson.objectid import ObjectId
from pymongo import MongoClient
import os
from pprint import pprint
from datetime import datetime
import folium
import pandas as pd

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

@app.route('/',methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('locations_index.html',locations=locations.find())
    
    

@app.route('/add',methods=['POST'])
def location_new(): 
        location_data = {
            'departure' : request.form.get('departure'),
            'arrival' : request.form.get('arrival')
        }
        items = locations.find()
        location_id = locations.insert_one(location_data).location_id
       
        print(location_id)
        return redirect(url_for('location_save',location_id=location_id))

@app.route('/save', methods=["POST"])
def location_save():
    if request.method == 'POST':
        # creates the map
        map = folium.Map(location=(10.3000, -84.8167),zoom_start=13)
        departure_lat = request.form['departure_lat']
        departure_long = request.form['departure_long']
        arrival_lat = request.form['arrival_lat']
        arrival_long = request.form['arrival_long']
        # grab coordinates from user data
        departure_coords = [departure_lat,departure_long]
        arrival_coords = [arrival_lat,arrival_long]
        items = locations.find()
        for coordinates in items:
             folium.Marker([departure_lat,departure_long], popup='Departure').add_to(map)
             folium.Marker([arrival_lat,arrival_long], popup='Arrival').add_to(map)
          
            
        # mark corrdinates
       
        # saves the map
        
    

        # TODO: create the map
        # TODO: grab user input from form
        # TODO: store user input into database
        # TODO: use collection.find() method to recieve all resources from collection
        # TODO: loop over all rsources and grab arrival and deprature (coordinates)
        # TODO: append all coordindates to marker
        # TODO: save new map
        # TODO: render the new map
        
       
        map.save('templates/map_index.html')
        return render_template('map_index.html')
if __name__ == '__main__':
    app.run(debug=True)

