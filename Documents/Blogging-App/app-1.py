from flask import Flask
app=Flask(__name__)
@app.route("/home")
def index():
    return "Home Page"

@app.route("/home/<string:name>")
def home(name):
    return "Hello! "+name+" Welcome to Home Page"

@app.route("/onlyget",methods=['POST'])
def get_req():
    return "This allows only get request, 1"
if __name__=="__main__":
    app.run(debug=True)