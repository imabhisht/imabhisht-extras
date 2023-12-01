from flask import Flask, request
app = Flask(__name__)

@app.route("/.well-known/discord")
def hello():
    return "dh=b640205682c94bdc24335a0122f2d192053d6d6a"

if __name__ == "__main__":
    app.run()