from flask import Flask, request
import json

app = Flask(__name__)


# @app.route("/register")
# def register():

@app.route('/')
def home():
    print 'It\'s Alive!'

@app.route('/identify', methods=['POST'])
def identify():
    json = request.get_json()

    user = json.user
    data = json.data

    print 'Authenticating {0}'.format(user)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",
            port=int("80")
            )
