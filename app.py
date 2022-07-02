from colorama import Cursor
from flask import Flask,render_template, request
from flask_caching import Cache
from flask_wtf import Form
from wtforms import StringField,IntegerField,EmailField,SubmitField,TextAreaField,PasswordField,validators
from flask_mysqldb import MySQL
config={
    "DEBUG":True,
    "CACHE_TYPE":"SimpleCache",
    "CACHE_DEFAULT_TIMEOUT":300
}

class SignupForm(Form):
    # name=StringField('Name',[validators.DataRequired(),validators.length(min=3,max=100)])
    phone=IntegerField('phone',[validators.DataRequired(),validators.length(min=10,max=10)])
    # email=EmailField('Email',[validators.DataRequired(),validators.length(min=5,max=200)])
    submit=SubmitField('Submit')
    # text=TextAreaField('text',[validators.DataRequired(),validators.length(min=50)])

    
    

app=Flask(__name__)
mysql=MySQL(app)

app.config['MYSQL_HOST']='ec2-23-23-151-191.compute-1.amazonaws.com'
app.config['MYSQL_USER']='ekwynoamveeeuz'
app.config['MYSQL_PASSWORD']='3f73008637275a9ba59ba45515ca0e5d2582f1e435adcabedc9964d0ebb74e9b'
app.config['MYSQL_DB']='d45kg41hlircjd'

@app.route('/signup',methods=['GET','POST'])
def signupp():
    form=SignupForm(request.form)
    if  request.method=='POST':
        # name1=form.name.data
        # email1=form.email.data
        phone1=form.phone.data
        Cursor=mysql.connection.cursor()
        Cursor.execute('''INSERT INTO person(id)VALUES(%s)''',(phone1))
        Cursor.connection.commit()
        Cursor.close()
        return "<h1>Thanku for signup we will contact you soon</h1>"


app.config.from_mapping(config)
cache=Cache(app)


@app.route('/signupform')
def signupform():
    form=SignupForm()
    return render_template("signup.html",form=form)


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

@app.route('/mail')
def mail():
    form=SignupForm()
    return render_template("mail.html",form=form)   

if __name__=='__main__':
    app.run(debug=True)    