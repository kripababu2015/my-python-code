from flask import Flask


app=Flask(__name__)

@app.route("/")
def index():
    return "hello.."
@app.route("/home")
def home():
    return "<h1> welcome to my home page.....</h1>"
@app.route("/contact")
def contact():
    return "welcome to contact page...."

@app.route("/about")
def about():
    return "welcome to about page....."
if(__name__=="__main__"):
  app.run(debug=True)