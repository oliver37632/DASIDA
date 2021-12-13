from model import session_scope
from flask import abort
from model.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token


def sigup(id, name, password):
    with session_scope() as session:

        new_sigup = User(
            id=id,
            name=name,
            password=generate_password_hash(password)
        )
        session.add(new_sigup)
        session.commit()

        return {
                   "message": "success"
               }, 201


def auth(id):
    with session_scope() as session:
        auth = session.query(User).filter(User.name == id)

        if auth.scalar():
            return {
                       "message": "overlap"
                   }, 400
        else:
            return {"message": "usable"}, 200


def login(id, password):
    with session_scope() as session:
        user = session.query(User).filter(User.id == id)

        if not user.scalar():
            abort(409, 'user id code does not match')

        user = user.first()
        check_user_pw = check_password_hash(user.password, password)

        if not check_user_pw:
            abort(409, 'user password code does not match')

        access_expires_delta = timedelta(minutes=60)
        refresh_expires_delta = timedelta(weeks=1)

        access_token = create_access_token(expires_delta=access_expires_delta,
                                           identity=id
                                           )
        refresh_token = create_refresh_token(expires_delta=refresh_expires_delta,
                                             identity=id
                                             )
        return {
                   'access_token': access_token,
                   'refresh_token': refresh_token
               }, 201
