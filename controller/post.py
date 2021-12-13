from model import session_scope
from flask import abort
from model.user import User
from model.post import Post
from datetime import datetime
from flask_jwt_extended import jwt_required


def post(title, content, user_id):
    with session_scope() as session:

        new_post = Post(
            user_id=user_id,
            title=title,
            content=content,
            created_at=datetime.now()
        )

        session.add(new_post)
        session.commit()

        return {
                   "message": "success"
               }, 201


def post_get():
    with session_scope() as session:
        posts = session.query(
            Post.id,
            Post.title,
            Post.content,
            Post.created_at,
            User.name
        ).join(User, User.id == Post.user_id)

        if posts:
            return {
                       "posts": [{
                           "name": name,
                           "id_pk": id,
                           "title": title,
                           "content": content,
                           "created_at": created_at
                       } for id, title, content, created_at, name in posts]
                   }, 200

        else:
            return abort(404, 'There is not any post')


def post_delete(id, token_Usr):
    with session_scope() as session:
        post_del = session.query(Post).filter(Post.user_id == token_Usr, Post.id == id).first()

        if post_del:
            session.delete(post_del)
            session.commit()
            return {
                       "message": "success"
                   }, 200
        return {
                   "massage": "NotFound"
               }, 404


def post_update(id, title, content, token_Usr):
    with session_scope() as session:
        post = session.query(Post).filter(Post.id == id, Post.user_id == token_Usr).first()

        if post:
            post.title = title
            post.content = content

            return 200

        return {
            'message': 'Error'
        }


