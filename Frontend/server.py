from flask import Flask, redirect
app = Flask(__name__)


@app.route('/')
def hello():
    return redirect('/static/dashboard.html', code=302)

if __name__ == "__main__":
    app.run()
