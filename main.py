import requests
import json
from collections import namedtuple
from map import making_map
from dash import Dash, dcc, html, no_update
from dash.dependencies import Output, Input, State


# global variables
API_url = ''
headers = {
    "Authorization": "Bearer SU2UrP6AOSyh1kzid0InZsT_QrnCw71FYgT9O1goVd1481qOD5sCkRKkwpUMB6ZlyzLnw--TJCiII7w0ywF6HKsaTsS046M8TZvZwAlFY75MHSBBoyPxMuI2exVSZnYx",
    "accept": "application/json"}


# creating html
def main():
    app = Dash()
    app.layout = html.Div([
        html.H1("Welcome to EatCents !!"),
        html.H3("Find the most affordable restaurants (in $ currency) in your area"),
        html.Div(
            [
                "City Name: ",
                dcc.Input(id = 'my-input', value = '', type = 'text')
            ],
        ),
        html.Button(id = 'submit-button', type = 'submit', children = 'Submit'),
        html.Br(),
        html.Div(id = 'my-output')

    ])

    @app.callback(
        [Output('my-output', 'children')],
        [Input('submit-button', 'n_clicks')],
        [State('my-input', 'value')],
    )
    def update_output(clicks, input_value):
        if clicks is not None:
            map = generate_map(input_value)
            return [dcc.Graph(id = "mappy", figure = map)]
        else:
            return no_update

    app.run_server(debug = True, use_reloader = False)


# functions
def generate_map(location):
    API_url = f'https://api.yelp.com/v3/businesses/search?location={location}'
    parameter = {'limit': 50}
    main_set = []
    Restuarant = namedtuple('Restaurant', ['name', 'price', 'coordinates', 'rating'])

    try:
        response = requests.get(url = API_url, headers = headers, params = parameter)

        if response.ok:
            data = response.json()


        latitude_list = []
        longitude_list = []
        price_list = []
        name_list = []
        rating_list = []

        for business in data['businesses']:
            c_name = ''
            c_price = ''
            c_coord = {}
            c_rate = ''

            try:
                if business['price'] == '$':
                    c_name = business['name']
                    c_price = business['price']
                    c_coord = business['coordinates']
                    c_rate = business['rating']
                    r_tuple = Restuarant(c_name, c_price, c_coord, c_rate)
                    main_set.append(r_tuple)


                elif business['price'] == '$$':
                    c_name = business['name']
                    c_price = business['price']
                    c_coord = business['coordinates']
                    c_rate = business['rating']
                    r_tuple = Restuarant(c_name, c_price, c_coord, c_rate)
                    main_set.append(r_tuple)

            except KeyError:
                pass


        # latitude and longitude lists
        for rest_name in main_set:
            name_list.append(rest_name.name)
            latitude_list.append(rest_name.coordinates['latitude'])
            longitude_list.append(rest_name.coordinates['longitude'])
            price_list.append(rest_name.price)
            rating_list.append(rest_name.rating)


        return making_map(name_list, latitude_list, longitude_list, price_list, rating_list)

    except:
        print('400 Bad Request')


if __name__ == "__main__":
    print("Welcome to Eatcents !! ")
    main()