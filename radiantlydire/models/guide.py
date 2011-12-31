from radiantlydire.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.ext.associationproxy import association_proxy

class GuideModel(Base):
    __tablename__ = 'guides'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(20000))
    created = Column(DateTime)
    edited = Column(DateTime)
    hero_id = Column(Integer, ForeignKey('heroes.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    items = association_proxy('guide_item', 'item')

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Guide('%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id, 
                                                                self.name, 
                                                                self.created, 
                                                                self.edited,
                                                                self.hero_id,
                                                                self.user_id)
