import gpxpy
import pandas as pd
import plotly.graph_objects as go

# Step 1: Parse GPX file
with open("Night_Walk.gpx", 'r') as gpx_file:
    gpx = gpxpy.parse(gpx_file)

data = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            data.append({
                'time': point.time,
                'lat': point.latitude,
                'lon': point.longitude,
                'elevation': point.elevation
            })

df = pd.DataFrame(data)

# Step 2: Plot 3D path
fig = go.Figure(data=[go.Scatter3d(
    x=df['lon'],
    y=df['lat'],
    z=df['elevation'],
    mode='lines',
    line=dict(
        color=df['elevation'],
        colorscale='Viridis',
        width=4
    )
)])

fig.update_layout(
    scene=dict(
        xaxis_title='Longitude',
        yaxis_title='Latitude',
        zaxis_title='Elevation (m)'
    ),
    title='3D Path from Strava GPX',
)

fig.show()
