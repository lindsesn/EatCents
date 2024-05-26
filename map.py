#adding map

import plotly.graph_objects as go
token = 'pk.eyJ1IjoibmF0aGFsaWVjaGl1dSIsImEiOiJjbHdtamZmcXUxdWpwMml0Z2pxc3Znc3A2In0.YudR05400cNQ08lFk67_Jw'

def set_color(price):
    color_list = []
    for p in price:
        if p == '$':
            color_list.append("skyblue")
        elif p == '$$':
            color_list.append("pink")
    return color_list


def making_map(name, lat, lon, price):

    mapbox_access_token = token

    fig = go.Figure(go.Scattermapbox(
        lat = lat,
        lon = lon,
        mode = 'markers',
        marker = go.scattermapbox.Marker(
            size = 10,
            color = set_color(price),
            opacity = 0.75
        ),
        text = name,
        customdata = price,
        hovertemplate = 'Restaurant: %{text}'+'<br>Coordinate: (%{lat},%{lon})'+'<br>Price: %{customdata}'
    ))

    #hovertemplate = 'Price: %{price}'+'<br>Coordinate: %{lat}%{lon}'

    fig.update_layout(
        autosize = True,
        hovermode = 'closest',
        mapbox=dict(
            accesstoken= mapbox_access_token,
            style = 'dark',
            bearing=0,
            center=dict(
                lat= lat[0],
                lon= lon[0],
            ),
            pitch=0,
            zoom=11,
        ),
    )

    fig.show()