from src import app
from src import db



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=3000)

