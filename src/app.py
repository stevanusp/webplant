# Import
# TODO: Clean imports
from flask import *
# GLOBALS
host = '0.0.0.0'  # == localhost
port = 3000
app = Flask(__name__)

# Routes


@app.route("/")
def index():
    return render_template('index.html')


# Main
if __name__ == '__main__':
    app.run(host, port)
