import requests
import json
import plotly.graph_objects as go


# global variables
API_url = ''
headers = {
    "Authorization": "Bearer SU2UrP6AOSyh1kzid0InZsT_QrnCw71FYgT9O1goVd1481qOD5sCkRKkwpUMB6ZlyzLnw--TJCiII7w0ywF6HKsaTsS046M8TZvZwAlFY75MHSBBoyPxMuI2exVSZnYx",
    "accept": "application/json"}


# functions
def main(location):
    API_url = f'https://api.yelp.com/v3/businesses/search?location={location}'
    parameter = {'limit': 50}
    main_set = []
    Restaurant = namedtuple('Restaurant', ['name', 'price', 'coordinates'])

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
            latitude_list.append(rest_name.coordinates['latitude'])
            longitude_list.append(rest_name.coordinates['longitude'])
        # print(latitude_list)
        # print(longitude_list)


    except:
        print('400 Bad Request')


if __name__ == "__main__":
    print("Welcome to Eatcents !! ")
    city = input('What city would you like to search?: ')
    main(city)