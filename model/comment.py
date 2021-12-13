from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, DATETIME
from model import Base


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(VARCHAR(255), nullable=True)
    created_at = Column(DATETIME, nullable=True, )
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(VARCHAR(10), ForeignKey('user.id'))
