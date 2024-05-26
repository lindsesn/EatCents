import requests
import json
from collections import namedtuple
from map import making_map
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# global variables
API_url = ''
headers = {
    "Authorization": "Bearer SU2UrP6AOSyh1kzid0InZsT_QrnCw71FYgT9O1goVd1481qOD5sCkRKkwpUMB6ZlyzLnw--TJCiII7w0ywF6HKsaTsS046M8TZvZwAlFY75MHSBBoyPxMuI2exVSZnYx",
    "accept": "application/json"}


# functions
@app.route("/")
def main():
    location = request.json_data()
    API_url = f'https://api.yelp.com/v3/businesses/search?location={location}'
    parameter = {'limit': 50}
    main_set = []
    Restuarant = namedtuple('Restaurant', ['name', 'price', 'coordinates'])

    try:
        response = requests.get(url = API_url, headers = headers, params = parameter)

        if response.ok:
            data = response.json()
            # print(data)
            print("================")

        # sorted_restaurant = {}
        # sorted_restaurant_loc_dict = {}
        latitude_list = []
        longitude_list = []
        price_list = []
        name_list = []

        for business in data['businesses']:
            c_name = ''
            c_price = ''
            c_coord = {}

            try:
                if business['price'] == '$':
                    c_name = business['name']
                    c_price = business['price']
                    c_coord = business['coordinates']
                    # c_rating = business['rating']
                    r_tuple = Restuarant(c_name, c_price, c_coord)
                    main_set.append(r_tuple)


                elif business['price'] == '$$':
                    c_name = business['name']
                    c_price = business['price']
                    c_coord = business['coordinates']
                    # c_rating = business['rating']
                    r_tuple = Restuarant(c_name, c_price, c_coord)
                    main_set.append(r_tuple)

            except KeyError:
                pass

        print(main_set)

        # latitude and longitude lists
        for rest_name in main_set:
            name_list.append(rest_name.name)
            latitude_list.append(rest_name.coordinates['latitude'])
            longitude_list.append(rest_name.coordinates['longitude'])
            price_list.append(rest_name.price)
        # print(latitude_list)
        # print(longitude_list)

        making_map(name_list, latitude_list, longitude_list, price_list)

    except:
        print('400 Bad Request')


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 3000)
    print("Welcome to Eatcents !! ")
    city = input('What city would you like to search?: ')
    main(city)