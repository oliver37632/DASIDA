from sqlalchemy.orm import relationship
from sqlalchemy import Column, VARCHAR, Integer, DATETIME, text, ForeignKey

from model import Base

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(VARCHAR(255), nullable=False)
    title = Column(VARCHAR(20), nullable=False)
    created_at = Column(DATETIME, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    user_id = Column(VARCHAR(10), ForeignKey('user.id'))

    comment = relationship("Comment", cascade="all,delete", backref="post")