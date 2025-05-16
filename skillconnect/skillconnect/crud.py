import models

def create_user(db, user):
    db_user = models.User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_service(db, service):
    db_service = models.Service(
        title=service.title,
        description=service.description,
        provider_id=service.provider_id,
    )
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

def get_services(db):
    return db.query(models.Service).all()