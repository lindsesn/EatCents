#adding map
import plotly.graph_objects as go

def making_map(name, lat, lon):
    mapbox_access_token = open(".mapbox_token").read()
    fig = go.Figure(go.Scattermapbox(
        lat = [lat[name]['latitude']],
        lon = [lon[name]['longitude']],
        mode = 'markers',
        marker = go.scattermapbox.Marker(
            size = 10
        ),
        text = [name]
    ))

    fig.update_layout(
        autosize = True,
        hovermode = 'closest',
        mapbox=dict(
            accesstoken= mapbox_access_token,
            bearing=0,
            center=dict(
                lat= lat[name]['latitude'],
                lon= [lon[name]['longitude']],
            ),
            pitch=0,
            zoom=10,
        ),
    )
    fig.show()