from app import app
from flask import render_template
from app.graphs import createGraph

@app.route('/')
@app.route('/index')
def index():
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
