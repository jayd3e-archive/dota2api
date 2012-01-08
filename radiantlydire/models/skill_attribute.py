from radiantlydire.models.base import Base
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class SkillAttributeModel(Base):
    __tablename__ = 'skill_attributes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    string = Column(String(100))
    integer = Column(Integer)
    float = Column(Float)
    percentage = Column(Integer)
    formula = Column(String(100))
    skill_level_id = Column(Integer, ForeignKey('skill_levels.id'))
    
    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<SkillAttribute('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id,
                                                                                     self.name,
                                                                                     self.string,
                                                                                     self.integer,
                                                                                     self.float,
                                                                                     self.percentage,
                                                                                     self.formula,
                                                                                     self.skill_level_id)