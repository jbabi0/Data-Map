import matplotlib
# this next line is mandatory for wed use
matplotlib.use('agg')

import matplotlib.pyplot as plt
import os

def createGraph(x, y, xlabel, ylabel, title):
    fig = plt.figure(figsize=(20, 10))
    plt.plot(x, y, 'bo-')
    plt.title('{}'.format(title), fontsize=36)
    plt.xlabel('{}'.format(xlabel), fontsize=24)
    plt.ylabel('{}'.format(ylabel), fontsize=24)

    # make sure a graph_images folder is created in static
    # grab absolute path to the graph_images floder so we can save the file to it
    path = os.path.abspath(os.path.dirname(__file__)) + '/static/graph_images/'

    name = 'graph.png'

    # create a url variable of path + name
    url = path + name

    # save the figure using matplotlibs method
    fig.savefig(url)
    # return the name of the file to be referenced on the front end
    return name
