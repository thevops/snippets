from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    for i in request.form:
    	print("%s = %s" % (i, request.form[i]))

    return "ok", 200

if __name__ == '__main__':
    app.run('127.0.0.1', debug=True)



