from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def Home():
    return "111"


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0',port=80)
   
