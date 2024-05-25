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

        for business in data['businesses']:
            try:
                if business['price'] == '$' or business['price'] == '$$':
                    print(f"{business['name']}: {business['price']}")
            except KeyError: # KeyError triggers if business does not have a price level shown
                pass

    except:
        print('400 Bad Request')


if __name__ == "__main__":
    print("Welcome to Eatcents !! ")
    city = input('What city would you like to search?: ')
    main(city)