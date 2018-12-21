import pygal
import os



def world_map():
    chart = pygal.maps.world.World()
    chart.title = 'Some Countries'
    chart.add('US Runners', {
        'us': 5,
        'ru': 10
    })

    path = os. path.abspath(os.path.dirname(__file__)) + '/static/graph_images/'

    chart_name = 'world_map.svg'

    url = path + chart_name

    chart.render_to_file(url)
