import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cookie(Base):
    __tablename__ = 'cookies'

    cookie_id = sqlalchemy.Column(sqlalchemy.String(20), primary_key=True)
    cookie_name = sqlalchemy.Column(sqlalchemy.String(20), nullable=False)
    cookie_recipe_url = sqlalchemy.Column(sqlalchemy.String(255))
    cookie_sku = sqlalchemy.Column(sqlalchemy.String(20))
    quantity = sqlalchemy.Column(sqlalchemy.Integer)
    unit_cost = sqlalchemy.Column(sqlalchemy.Numeric(12, 2))

def load_data():
  print('Loading data...')

def start_engine():
  print('Starting engine...')
  engine = create_engine('sqlite:///:memory:')
  Session = sessionmaker(bind=engine)
  session = Session()

def add_cookie():
  print('Adding cookie...')
  cc_cookie = Cookie(
    cookie_id='12345',
    cookie_name='chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
    cookie_sku='CC01',
    quantity=12, unit_cost=0.50)

if __name__ == "__main__":
  print("Welcome to the database.")
  print("sqlalchemy v:", sqlalchemy.__version__)
  load_data()
  engine = start_engine()
  print(engine)

