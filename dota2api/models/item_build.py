from dota2api.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.associationproxy import association_proxy


class ItemBuildModel(Base):
    __tablename__ = 'item_builds'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    guide_id = Column(Integer, ForeignKey('guides.id'))

    items = association_proxy('build_items', 'item')

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<ItemBuild('%s', '%s')>" % (self.id,
                                            self.name)
