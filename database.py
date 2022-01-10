import sqlalchemy
from sqlalchemy import create_engine

def load_data():
  print('Loading data...')

def start_engine():
  print('Starting engine...')
  engine = create_engine('sqlite:///:memory:')
  return engine

if __name__ == "__main__":
  print("Welcome to the database.")
  print("sqlalchemy v:", sqlalchemy.__version__)
  load_data()
  engine = start_engine()
  print(engine)

