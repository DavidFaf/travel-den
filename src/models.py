from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setup_db(app, database_path='postgresql://user:bzKa43ROJx5PSW9VxeBNLYinG9L1y8i0@dpg-cestavpa6gdggmlhbi90-a/travel_den_database'):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

def db_drop_and_create_all(app):
    with app.app_context():
        db.drop_all()
        db.create_all() 

class FormMessage(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    fullname = db.Column(db.String(length=30), nullable=False)
    email = db.Column(db.String(length=30), nullable=False)
    countries = db.Column(db.String(length=30), nullable=False)
    


    def __repr__(self):
        return f'FormMessage {self.fullname}'

# def init_db():
#     db.create_all()

#     # Create a test user
#     new_user = FormMessage('a@a.com', 'aaaaaaaa@gmail.com', 'nairobi')
#     db.session.add(new_user)
#     db.session.commit()



# if __name__ == '__main__':
#     init_db()



