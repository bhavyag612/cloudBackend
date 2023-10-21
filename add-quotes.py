from app import app, db
from models import Quote
# Add quotes to the database
quotes=["Believe in yourself and all that you are.",
"Success is not the key to happiness. Happiness is the key to success.",
"The only limit to our realization of tomorrow will be our doubts of today.",
"You are never too old to set another goal or to dream a new dream.",
"Don't watch the clock; do what it does. Keep going.",
"The best way to predict the future is to create it.",
"It does not matter how slowly you go as long as you do not stop.",
"The only way to do great work is to love what you do.",
"Opportunities don't happen. You create them.",
"Your time is limited, don't waste it living someone else's life."]

with app.app_context():
    for quote in quotes:
        obj = Quote(text=quote)
        db.session.add(obj)
    print()
    db.session.commit()



