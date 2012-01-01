from radiantlydire.models.base import Base
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class ItemAttributeModel(Base):
    __tablename__ = 'item_attributes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    value = Column(String(100))
    item_id = Column(Integer, ForeignKey('items.id'))
    
    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<ItemAttribute('%s', '%s', '%s', '%s')>" % (self.id,
                                                            self.name,
                                                            self.value,
                                                            self.item_id)