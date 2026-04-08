import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from order_service import create_order
from models import Base, Order 

class FakeUserRepository:
    def get_user_email(self, user_id):
        return f"user{user_id}@fake.local"

class DummyLogger:
    def log(self, msg):
        pass

class NullNotifier:
    def send(self, to, message):
        pass


@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:") 
    Base.metadata.create_all(engine)              
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


def test_create_order_integration_with_fake(db):
    order = create_order(3, 60, NullNotifier(), DummyLogger(), db, FakeUserRepository())
    assert order.status == "CREATED"
    assert order.user_email == "user3@fake.local"