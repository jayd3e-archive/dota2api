from dota2api.models.base import Base
from dota2api.models.item import ItemModel
from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class ItemItemModel(Base):
    __tablename__ = 'items_items'

    id = Column(Integer, primary_key=True)
    builds_id = Column(Integer, ForeignKey('items.id'))
    requires_id = Column(Integer, ForeignKey('items.id'))

    builds_into = relationship(ItemModel,
                               backref="builds_into_items",
                               primaryjoin=ItemModel.id == builds_id)
    requires = relationship(ItemModel,
                            backref="requires_items",
                            primaryjoin=ItemModel.id == requires_id)

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<ItemItem('%s', '%s')>" % (self.builds_id,
                                           self.requires_id)
