from flask import Flask


app=Flask(__name__)

@app.route("/download")
def default():
    return "welcome from download"

@app.route("/movie")
def read():
    return "welcome from movie"


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)