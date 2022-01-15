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

class Database:
  def __init__(self):
    print('initializing database')
    self.engine = create_engine('sqlite:///:memory:')
    self.Session = sessionmaker(bind=self.engine)
    self.session = self.Session()

  def say_hello(self):
    print('Hello from inside the Database class')

  def add_cookie(self, cookie):
    self.session.add(cookie)
    self.session.commit()

  def select_cookie(self, cookie_id):
    return self.session.query(Cookie).filter_by(cookie_id=cookie_id).one()

  def get_cookie(self, cookie_id):
    return self.session.query(Cookie).filter_by(cookie_id=cookie_id).one_or_none()

  def get_cookies(self):
    return self.session.query(Cookie).all()

# def load_data():
#   print('Loading data...')

# def start_engine():
#   print('Starting engine...')
#   engine = create_engine('sqlite:///:memory:')
#   Session = sessionmaker(bind=engine)
#   session = Session()

def get_cookie():
  print('Adding cookie...')
  return Cookie(
    cookie_id='12345',
    cookie_name='chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
    cookie_sku='CC01',
    quantity=12, unit_cost=0.50)


if __name__ == "__main__":
  print("Welcome to the database.")
  print("sqlalchemy v:", sqlalchemy.__version__)

  my_db = Database()
  my_db.say_hello()

  my_cookie = get_cookie()
  my_db.add_cookie(my_cookie)
  is_my_cookie = my_db.select_cookie(my_cookie.cookie_id)

  print(is_my_cookie)

  # load_data()
  # engine = start_engine()
  # print(engine)

