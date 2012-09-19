from dota2api.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, DateTime


class CommentModel(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    body = Column(String(300))
    created = Column(DateTime)
    edited = Column(DateTime)
    guide_id = Column(Integer, ForeignKey('guides.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Comment('%s', '%s', '%s', '%s', '%s')>" % (self.id,
                                                            self.body,
                                                            self.created,
                                                            self.edited,
                                                            self.user_id)
