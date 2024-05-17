# pylint: skip-file
from flask import Flask
from flask_cors import CORS
from routes.model_routes import lab_bp
import sys
sys.dont_write_bytecode = True

app = Flask(__name__)
CORS(app, resources={r"/lab/*": {"origins": "http://localhost:5173"}})
app.register_blueprint(lab_bp, url_prefix='/lab')

if __name__ == '__main__':
    app.run(debug=True)
