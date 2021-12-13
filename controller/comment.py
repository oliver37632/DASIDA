from model import session_scope
from model.user import User
from model.comment import Comment
from datetime import datetime


# comment?post_id=1
def comment_post(post_id, content, user_id):
    with session_scope() as session:

        new_comment = Comment(
            post_id=post_id,
            content=content,
            user_id=user_id,
            created_at=datetime.now()
        )

        session.add(new_comment)
        session.commit()

        return {
                   'message': 'success'
               }, 200


def comment_get(post_id):
    with session_scope() as session:

        comment_join = session.query(
            Comment.content,
            User.name
        ).join(User, User.id == Comment.user_id) \
            .filter(Comment.post_id == post_id)

        return {
                   "comment_join": [{
                       "name": name,
                       "content": content
                   } for content, name in comment_join]
               }, 200