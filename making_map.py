#adding map
import pandas as pd
import plotly.graph_objects as go


token = 'pk.eyJ1IjoibmF0aGFsaWVjaGl1dSIsImEiOiJjbHdtamZmcXUxdWpwMml0Z2pxc3Znc3A2In0.YudR05400cNQ08lFk67_Jw'
def making_map(name, lat, lon):
    mapbox_access_token = token
    fig = go.Figure(go.Scattermapbox(
        lat = lat,
        lon = lon,
        mode = 'markers',
        marker = go.scattermapbox.Marker(
            size = 10
        ),
        text = name
    ))

    fig.update_layout(
        autosize = True,
        hovermode = 'closest',
        mapbox=dict(
            accesstoken= mapbox_access_token,
            bearing=0,
            center=dict(
                lat= lat[0],
                lon= lon[0],
            ),
            pitch=0,
            zoom=10,
        ),
    )
    fig.show()