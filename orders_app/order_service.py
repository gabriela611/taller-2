from models import Order

def create_order(user_id, amount, notifier, logger, db, user_repository):
    # TODO: obtener el email desde el repositorio
    email = ________________________________
    logger.log(f'Creating order for {email}')
   
   # TODO: validar que amount sea positivo, de lo contrario lanzar el error "Invalid amount"
    ______________________
    ______________________
    
    order = Order(user_email=email, amount=amount, status='CREATED')
    
    # TODO: persistir la orden
    ________________________________
    db.commit()
    
    notifier.send(email, 'Order created')
    return order
