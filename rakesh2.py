from flask import Flask
app=Flask(__name__)

@app.route("/rk")
def rakesh2():
    return "Hello Rakesh and jeet welcome to emicon"


@app.route("/")
def rakesh1():
    return "Hello Rakesh and jeet welcome to emicon"
    
    
if __name__=='__main__':
    app.run(debug=True)