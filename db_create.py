from application import db
from application.models import Fighter, Fight

db.create_all()

print("DB created.")
