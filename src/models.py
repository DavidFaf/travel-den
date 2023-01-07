from src import db

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



