from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def _():
    pass

if __name__ == '__main__':
    app.run()