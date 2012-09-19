from dota2api.models.base import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey


class ItemAttributeModel(Base):
    __tablename__ = 'item_attributes'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    string = Column(String(100))
    integer = Column(Integer)
    float = Column(Float)
    percentage = Column(Integer)
    formula = Column(String(100))
    item_id = Column(Integer, ForeignKey('items.id'))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<ItemAttribute('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id,
                                                                                    self.name,
                                                                                    self.string,
                                                                                    self.integer,
                                                                                    self.float,
                                                                                    self.percentage,
                                                                                    self.formula,
                                                                                    self.item_id)
