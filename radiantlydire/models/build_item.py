from radiantlydire.models.base import Base
from radiantlydire.models.item_build import ItemBuildModel
from radiantlydire.models.item import ItemModel
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class BuildItemModel(Base):
    __tablename__ = 'builds_items'
    
    id = Column(Integer, primary_key=True)
    build_id = Column(Integer, ForeignKey('item_builds.id'))
    item_id = Column(Integer, ForeignKey('items.id'))
    section = Column(String(50))
    
    build = relationship(ItemBuildModel,
                         backref="build_items")
    item = relationship(ItemModel,
                        backref="build_items")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<BuildItem('%s', '%s', '%s')>" % (self.build_id,
                                                  self.item_id,
                                                  self.section)    