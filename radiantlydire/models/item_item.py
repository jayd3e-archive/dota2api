from d2.models.base import Base
from d2.models.item import ItemModel
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class ItemItemModel(Base):
    __tablename__ = 'items_items'
    
    id = Column(Integer, primary_key=True)
    build_id = Column(Integer, ForeignKey('items.id'))
    require_id = Column(Integer, ForeignKey('items.id'))
    
    build = relationship(ItemModel,
                         backref="build_items",
                         primaryjoin=ItemModel.id==build_id)
    require = relationship(ItemModel,
                           backref="require_items",
                           primaryjoin=ItemModel.id==require_id)

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<ItemItem('%s', '%s')>" % (self.build_id,
                                           self.require_id)    