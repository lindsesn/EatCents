import requests
import json

API_url = ''
headers = {"Authorization": "Bearer SU2UrP6AOSyh1kzid0InZsT_QrnCw71FYgT9O1goVd1481qOD5sCkRKkwpUMB6ZlyzLnw--TJCiII7w0ywF6HKsaTsS046M8TZvZwAlFY75MHSBBoyPxMuI2exVSZnYx", "accept": "application/json"}

def main(location):

    API_url = f'https://api.yelp.com/v3/businesses/search?location={location}'
    parameter = {'limit': 50}

    try:
        response = requests.get(url = API_url, headers = headers, params = parameter)

        if response.ok:
            data = response.json()
            print(data)
            print("================")

        sorted_restaurant = {}
        sorted_restaurant_loc_dict = {}
        latitude_list = []
        longitude_list = []


        for business in data['businesses']:
            try:
                if business['price'] == '$':
                    sorted_restaurant[business['name']] = business['price']
                    sorted_restaurant_loc_dict[business['name']] = business['coordinates']
                    #print(sorted_restaurant_loc_dict[business['name']])
                if business['price'] == '$$':
                    sorted_restaurant[business['name']] = business['price']
                    sorted_restaurant_loc_dict[business['name']] = business['coordinates']
                    # print(sorted_restaurant_loc_dict[business['name']])
                    #print(f"{business['name']}: {business['price']}")

            except KeyError: # KeyError triggers if business does not have a price level shown
                pass

        print(f"Restaurants sorted from $ to $$ in {location}: \n\n{sorted_restaurant}")
        # print(sorted_restaurant_loc_dict)

        for rest_name in sorted_restaurant_loc_dict:
            latitude_list.append(rest_name['latitude'])
            longitude_list.append(rest_name['longitude'])
        print(latitude_list)
        print(longitude_list)


        #making_map(name=name, lat=sorted_restaurant_loc_dict, lon=sorted_restaurant_loc_dict)


    except:
        print('400 Bad Request')


if __name__ == "__main__":
    print("Welcome to Eatcents !! ")
    city = input('What city would you like to search?: ')
    main(city)