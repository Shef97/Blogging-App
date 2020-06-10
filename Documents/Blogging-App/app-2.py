from flask import Flask, render_template


app=Flask(__name__)


all_post=[
    {
        'title': 'Post1',
        'content': 'this is content allalala',
        'author':'abc'
    },
    {
        'title': 'Post2',
        'content': 'this is content allalala',
        'author':'abc'
    }
    
]
@app.route("/home")
def index():
    return render_template('index.html')

@app.route("/posts")
def posts():
    return render_template('posts.html', posts=all_post)
@app.route("/home/<string:name>")
def home(name):
    return "Hello! "+name+" Welcome to Home Page"

@app.route("/onlyget",methods=['POST'])
def get_req():
    return "This allows only get request, 1"
if __name__=="__main__":
    app.run(debug=True)