from dota2api.models.base import Base
from dota2api.models.skill_note import SkillNoteModel
from dota2api.models.skill_level import SkillLevelModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class SkillModel(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    image_name = Column(String(100))
    description = Column(String(1000))
    ability_type = Column(String(50))
    targeting_type = Column(String(50))
    allowed_targets = Column(String(50))
    damage_type = Column(String(50))
    hero_id = Column(Integer, ForeignKey('heroes.id'))

    skill_notes = relationship(SkillNoteModel, backref="skill")
    skill_levels = relationship(SkillLevelModel, backref="skill")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Skill('%s', '%s', '%s', '%s', '%s')>" % (self.id,
                                                          self.name,
                                                          self.image_name,
                                                          self.description,
                                                          self.hero_id)
