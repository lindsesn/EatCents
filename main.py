import requests
import json
from collections import namedtuple
from map import making_map
from dash import Dash, dcc, html, no_update
import dash
from dash.dependencies import Output, Input, State


# global variables
API_url = ''
headers = {
    "Authorization": "Bearer SU2UrP6AOSyh1kzid0InZsT_QrnCw71FYgT9O1goVd1481qOD5sCkRKkwpUMB6ZlyzLnw--TJCiII7w0ywF6HKsaTsS046M8TZvZwAlFY75MHSBBoyPxMuI2exVSZnYx",
    "accept": "application/json"}


# creating hmtl
def main():
    app = Dash()
    image_path = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaW9udzZycXJ6amEzZXJkNm9vNjh0aGx2bnhtdHA4ZTQ5cHczcWJ2eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ukpwkOzk6kafXwfwbH/giphy.gif"
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, prevent_initial_callbacks = True,
                    external_stylesheets = external_stylesheets)

    app.layout = html.Div([
        html.Img(src = image_path, style = {'margin': "0 auto"}),
        html.H1(". ݁₊ ⊹ Welcome to EatCents  . ݁˖ . ݁", style = {"font-weight": "bold"}),
        html.H4("Find the most affordable restaurants in your area: ",
                style = {'textAlign': 'center'}),
        html.Div(
            [
                "Enter City Name (in $ currency only): ",
                html.Br(),
                dcc.Input(id = 'my-input', value = '', type = 'text')
            ],
        ),
        html.Br(),
        html.Button(id = 'submit-button', type = 'submit', children = 'Submit',
                    style = {'background-color': 'white'}),
        html.Br(),
        html.Br(),
        html.Div(id = 'my-output')
    ],
        style = {
            'font-family': 'georgia',
            'textAlign': 'center',
            'backgroundColor': "#3B3B3B",
            'boxShadow': '0 0 1px #ccc',
            'color': "#C2E2F0",
            'padding': '50px'
        }, )

    @app.callback(
        [Output('my-output', 'children')],
        [Input('submit-button', 'n_clicks')],
        [State('my-input', 'value')],
    )
    def update_output(clicks, input_value):
        if clicks is not None:
            valid, result = generate_map(input_value)
            if valid:
                return [dcc.Graph(id = "mappy", figure = result)]
            else:
                return [result]
        else:
            return no_update

    app.run_server(debug = True, use_reloader = False)


# clean data + generate map
def generate_map(location):
    API_url = f'https://api.yelp.com/v3/businesses/search?location={location}'
    parameter = {'limit': 50}
    main_set = []
    Restuarant = namedtuple('Restaurant', ['name', 'price', 'coordinates', 'rating'])

    try:
        response = requests.get(url = API_url, headers = headers, params = parameter)

        if response.ok:
            data = response.json()
            # print(data)
            # print("================")

        # sorted_restaurant = {}
        # sorted_restaurant_loc_dict = {}
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

        # print(main_set)

        # latitude and longitude lists
        for rest_name in main_set:
            name_list.append(rest_name.name)
            latitude_list.append(rest_name.coordinates['latitude'])
            longitude_list.append(rest_name.coordinates['longitude'])
            price_list.append(rest_name.price)
            rating_list.append(rest_name.rating)
        # print(latitude_list)
        # print(longitude_list)
        # print(rating_list)

        return True, making_map(name_list, latitude_list, longitude_list, price_list, rating_list)

    except:
        app = Dash()
        image_path1 = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExb25yYXZxM3lpNjNhZG9naXh3dmw2ZWJhanYzN3d5eHNwcHQzb3NqYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/12Bpme5pTzGmg8/giphy.webp"
        app.layout = html.Div([
            html.Img(src = image_path1, style = {'margin': "0 auto"}),
            html.H4("Incorrect Input ☆⌒(｡•́︿•̀｡) Please reload page !!",
                    style = {"font-weight": "bold"})],
            style = {
                'textAlign': 'center',
                'backgroundColor': "#C1C0C0",
                'boxShadow': '0 0 1px #ccc',
                'color': "#325D8A",
                'padding': '50px'
            })
        # print('400 Bad Request')
        return False, app.layout


if __name__ == "__main__":
    print("Welcome to Eatcents !! ")
    main()