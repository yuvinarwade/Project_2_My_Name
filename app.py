from flask import Flask

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return "Hello this is Yuvraj Kishor Narwade"


if __name__=="__main__":
    app.run(debug=True)
