import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import text
database_url = os.getenv('DATABASE_URL')
engine = create_engine(database_url)
db = scoped_session(sessionmaker(bind=engine))

def main():
	flights = db.execute(text('SELECT origin, destination, duration FROM flights')).fetchall()
	for flight in flights:
		print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
	main()

