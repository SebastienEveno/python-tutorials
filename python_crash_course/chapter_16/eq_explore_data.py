import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

if __name__ == "__main__":
    
    # Explore the structure of the data.
    filename = 'data/eq_data_1_day_m1.json'
    filename = 'data/eq_data_30_day_m1.json'

    with open(filename) as f:
        all_eq_data = json.load(f)
    
    readable_file = 'data/readable_eq_data.json'
    with open(readable_file, 'w') as f:
        json.dump(all_eq_data, f, indent=4)
    
    all_eq_dicts = all_eq_data['features']
    mags = []
    longs = []
    lats = []
    hover_texts = []

    for eq_dict in all_eq_dicts:
        mags.append(eq_dict['properties']['mag'])
        longs.append(eq_dict['geometry']['coordinates'][0])
        lats.append(eq_dict['geometry']['coordinates'][1])
        hover_texts.append(eq_dict['properties']['title'])
    data = [{
        'type': 'scattergeo',
        'lon': longs,
        'lat': lats,
        'text': hover_texts,
        'marker': {
            'size': [5*mag for mag in mags],
            'color': mags,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Magnitude'}
        },
    }]
    my_layout = Layout(title=all_eq_data['metadata']['title'])

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='global_earthquakes.html')
    