from src.models import setup_db, FormMessage, db_drop_and_create_all
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
setup_db(app)  
CORS(app)
db_drop_and_create_all(app)


if __name__ == '__main__':
    app.run(debug=True)

