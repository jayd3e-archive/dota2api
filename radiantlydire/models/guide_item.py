from d2.models.base import Base
from d2.models.guide import GuideModel
from d2.models.item import ItemModel
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class GuideItemModel(Base):
    __tablename__ = 'guides_items'
    
    id = Column(Integer, primary_key=True)
    guide_id = Column(Integer, ForeignKey('guides.id'))
    item_id = Column(Integer, ForeignKey('items.id'))
    section = Column(String(50))
    
    guide = relationship(GuideModel,
                          backref="guide_item")
    item = relationship(ItemModel,
                         backref="guide_item")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<GuideItem('%s', '%s', '%s')>" % (self.guide_id,
                                                  self.item_id,
                                                  self.section)    