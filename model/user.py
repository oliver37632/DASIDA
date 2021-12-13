from sqlalchemy import Column, VARCHAR, text
from sqlalchemy.orm import relationship

from model import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(VARCHAR(10), primary_key=True, autoincrement=True, server_default=text("CURRENT_TIMESTAMP"))
    password = Column(VARCHAR(255), nullable=True)
    name = Column(VARCHAR(5), nullable=True)

    post = relationship("Post", cascade="all,delete", backref="user")
    comment = relationship("Comment", cascade="all,delete", backref="user")