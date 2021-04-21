from flask import Flask
from flask.wrappers import Response

app=Flask(__name__)

@app.route('/')
def site_index():
    return Response("TEST")


if __name__=='main':
    app.run()