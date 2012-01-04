from radiantlydire.models.base import Base
from radiantlydire.models.skill_build import SkillBuildModel
from radiantlydire.models.skill_level import SkillLevelModel
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class BuildSkillModel(Base):
    __tablename__ = 'builds_skills'
    
    id = Column(Integer, primary_key=True)
    build_id = Column(Integer, ForeignKey('skill_builds.id'))
    skill_level_id = Column(Integer, ForeignKey('skill_levels.id'))
    level = Column(String(50))
    
    build = relationship(SkillBuildModel,
                         backref="build_skills")
    skill = relationship(SkillLevelModel,
                         backref="build_skills")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<BuildSkill('%s', '%s', '%s')>" % (self.build_id,
                                                   self.skill_level_id,
                                                   self.level)    