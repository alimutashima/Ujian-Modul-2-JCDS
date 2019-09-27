from flask import Flask,render_template
from plots import dist1,dist2
from data import data_clean
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data')
def data():
    data = data_clean().head()
    return render_template('table_data.html' , data=data)

@app.route('/stats')
def stats():
    data = data_clean()
    return render_template('stats.html' , data=data)

@app.route('/plots')
def plots():
    plot1 = dist1()
    plot2 = dist2()
    return render_template('plots.html' , data=[dist1,dist2])

if __name__ == '__main__':
    app.run(debug=True, port=6000)