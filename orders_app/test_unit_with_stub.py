from order_service import create_order
from database import SessionLocal
from models import Order

class StubUserRepository:
    def get_user_email(self, user_id):
        # TODO: retornar siempre el mismo email ficticio
        return "gaby@prueba.com"

class DummyLogger:
    def log(self, msg):
        pass

class NullNotifier:
    def send(self, to, message):
        pass

def test_create_order_with_stub():
    db = SessionLocal()
    order = create_order(10, 200, NullNotifier(), DummyLogger(), db, StubUserRepository())
    # TODO: Comparar con las respuestas esperadas
    assert order.status == 'CREATED'
    assert order.user_email == "gaby@prueba.com"
    
    db.query(Order).delete()
    db.commit()
    db.close()
