import matplotlib.pyplot as plt
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    out = (
            f'All working good.<br>'
            )
    return out

if __name__ == "__main__":

    app.run(host='0.0.0.0')
