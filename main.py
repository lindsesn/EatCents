import requests
import json

API_url = 'https://api.yelp.com/v3/businesses/search?location=Irvine'
headers = {"Authorization": "Bearer SU2UrP6AOSyh1kzid0InZsT_QrnCw71FYgT9O1goVd1481qOD5sCkRKkwpUMB6ZlyzLnw--TJCiII7w0ywF6HKsaTsS046M8TZvZwAlFY75MHSBBoyPxMuI2exVSZnYx", "accept": "application/json"}

def main():

    print('Welcome to EatCents!')
    parameter = {'limit': 50}
    response = requests.get(url=API_url, headers=headers, params=parameter)

    try:
        if response.ok:
            data = response.json()
            print(data)

        for business in data['businesses']:
            try:
                if business['price'] == '$':
                    print(f"{business['name']}: {business['price']}")
            except KeyError: # KeyError triggers if business does not have a price level shown
                pass
                # print(f"{business['name']}: no price is shown")
    except:
        print('400 Bad Request')


if __name__ == "__main__":
    main()