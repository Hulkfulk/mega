from flask import Flask,render_template
from flask_caching import Cache
config={
    "DEBUG":True,
    "CACHE_TYPE":"SimpleCache",
    "CACHE_DEFAULT_TIMEOUT":300
}

app=Flask(__name__)

app.config.from_mapping(config)
cache=Cache(app)


@app.route('/')
@cache.cached(timeout=330)
def home():
    return render_template("home.html")

@app.route('/course')
@cache.cached(timeout=300)
def course():
    return render_template("courses.html")

@app.route('/price')
@cache.cached(timeout=300)
def price():
    return render_template("price.html")

@app.route('/about')
@cache.cached(timeout=300)
def about():
    return render_template("about.html")    

if __name__=='__main__':
    app.run(debug=True)    