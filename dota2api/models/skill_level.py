from dota2api.models.base import Base
from dota2api.models.skill_attribute import SkillAttributeModel
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship


class SkillLevelModel(Base):
    __tablename__ = 'skill_levels'

    id = Column(Integer, primary_key=True)
    level = Column(Integer)
    cooldown = Column(Integer)
    cooldown_float = Column(Float)
    mana_cost = Column(Integer)
    mana_cost_per_second = Column(Integer)
    mana_cost_formula = Column(String)
    parent_id = Column(Integer, ForeignKey('skill_levels.id'))
    skill_id = Column(Integer, ForeignKey('skills.id'))

    skill_parent = relationship("SkillLevelModel", remote_side=[id])
    skill_attributes = relationship(SkillAttributeModel, backref="skill")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<SkillLevel('%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id,
                                                                     self.level,
                                                                     self.cooldown,
                                                                     self.mana_cost,
                                                                     self.parent_id,
                                                                     self.skill_id)
