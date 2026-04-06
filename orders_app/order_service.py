from models import Order

def create_order(user_id, amount, notifier, logger, db, user_repository):
    # TODO: obtener el email desde el repositorio
    email = user_repository.get_user_email(user_id)
    logger.log(f'Creating order for {email}')
   
   # TODO: validar que amount sea positivo, de lo contrario lanzar el error "Invalid amount"
    if (amount <= 0):
        raise ValueError ("Invalid Amount")

    order = Order(user_email=email, amount=amount, status='CREATED')
    
    # TODO: persistir la orden
    db.add(order)
    db.commit()
    
    notifier.send(email, 'Order created')
    return order
