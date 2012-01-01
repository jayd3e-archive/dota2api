from radiantlydire.models.base import Base
from radiantlydire.models.skill_note import SkillNoteModel
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class SkillModel(Base):
    __tablename__ = 'skills'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    image_name = Column(String(100))
    description = Column(String(1000))
    cooldown = Column(Integer)
    mana_cost = Column(Integer)
    ability_type = Column(String(50))
    targeting_type = Column(String(50))
    allowed_targets = Column(String(50))
    level = Column(Integer)
    damage_type = Column(Integer)
    skill_parent_id = Column(Integer, ForeignKey('skills.id'))
    hero_id = Column(Integer, ForeignKey('heroes.id'))

    skill_parent = relationship("SkillModel", remote_side=[id])
    skill_notes = relationship(SkillNoteModel, backref="skill")
    
    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Skill('%s', '%s', '%s', '%s', '%s')>" % (self.id,
                                                          self.name,
                                                          self.image_name,
                                                          self.description,
                                                          self.hero_id)