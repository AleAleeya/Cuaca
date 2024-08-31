from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/disasters')
def disasters():
    return render_template('disasters.html')

@app.route('/map')
def map():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)
