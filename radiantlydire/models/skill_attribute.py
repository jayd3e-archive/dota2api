from radiantlydire.models.base import Base
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class SkillAttributeModel(Base):
    __tablename__ = 'skill_attributes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    value = Column(String(100))
    skill_id = Column(Integer, ForeignKey('skills.id'))
    
    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<SkillAttribute('%s', '%s', '%s', '%s')>" % (self.id,
                                                             self.name,
                                                             self.value,
                                                             self.skill_id)