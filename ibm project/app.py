from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=["GET","POST"])
def login():
    return render_template("login.html")           

@app.route('/product')
def product():
    return render_template("product.html")

if __name__ == '_main_':
    app.run(debug=True)
# print(__name__)