from flask import Flask, render_template
from flask_cors import CORS
from flask_bootstrap import Bootstrap

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    bootstrap = Bootstrap(app)
