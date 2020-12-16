from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

if __name__ == "__main__":
    # Create two D6
    die_1 = Die()
    die_2 = Die()

    # Make some rolls
    results = []
    for i in range(1000):
        results.append(die_1.roll() * die_2.roll())
    
    frequencies = []
    for value in range(1, die_1.num_sides * die_2.num_sides + 1):
        frequencies.append(results.count(value))
    
    # Visualize the results
    x_values = list(range(1, die_1.num_sides * die_2.num_sides + 1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result', 'dtick': 1}
    y_axis_config = {'title': 'Frequency of Result'}

    my_layout = Layout(title='Results of rolling two D8 1000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)

    offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')
