from radiantlydire.models.base import Base
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class SkillModel(Base):
    __tablename__ = 'skills'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    image_name = Column(String(100))
    description = Column(String(1000))
    hero_id = Column(Integer, ForeignKey('heroes.id'))
    
    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Skill('%s', '%s', '%s', '%s', '%s')>" % (self.id,
                                                          self.name,
                                                          self.image_name,
                                                          self.description,
                                                          self.hero_id)