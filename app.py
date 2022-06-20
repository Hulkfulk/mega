from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/course')
def course():
    return render_template("courses.html")

@app.route('/price')
def price():
    return render_template("price.html")

if __name__=='__main__':
    app.run(debug=True)    