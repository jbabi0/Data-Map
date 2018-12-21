from app import app
from flask import render_template
from app.graphs import createGraph
from app.parse import getData
from app.tables import hittingData
from app.map import world_map

@app.route('/')
@app.route('/index')
def index():
    world_map()
    return render_template('index.html')



@app.route('/graphs')
def graphs():
    x = [1, 2, 3, 4,]
    y = [2.2, 3.4, 2.6, 4.8]
    xlabel = 'Years'
    ylabel = 'Population'
    title = 'Flask Integraded Graph'
    file = createGraph(x, y, xlabel, ylabel, title)
    #TODO: import and call the graph
    return render_template('graph.html', file=file)

@app.route('/parse')
def parse():
    url = 'http://www.arthurleej.com/e-love.html'
    data = getData(url)
    return render_template('parse.html', data=data)

@app.route('/tables')
def tables():
    table = hittingData()
    return render_template('table.html', table=table)
