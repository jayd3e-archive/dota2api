from dota2api.models.base import Base
from sqlalchemy import Column, Integer, String


class GroupModel(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Group('%s', '%s')>" % (self.id,
                                        self.name)
