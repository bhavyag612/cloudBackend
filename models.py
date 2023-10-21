from database import db


# Define the Quote model
class Quote(db.Model):
    text = db.Column(db.String, primary_key=True)

    def __str__(self):
        return self.text
    def to_dict(self):
        return {'quote': self.text}

