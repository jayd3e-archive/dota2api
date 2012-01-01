from radiantlydire.models.base import Base
from radiantlydire.models.skill_build import SkillBuildModel
from radiantlydire.models.skill import SkillModel
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class BuildSkillModel(Base):
    __tablename__ = 'builds_skills'
    
    id = Column(Integer, primary_key=True)
    build_id = Column(Integer, ForeignKey('skill_builds.id'))
    skill_id = Column(Integer, ForeignKey('skills.id'))
    level = Column(String(50))
    
    build = relationship(SkillBuildModel,
                         backref="build_skills")
    skill = relationship(SkillModel,
                         backref="build_skills")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<BuildSkill('%s', '%s', '%s')>" % (self.build_id,
                                                   self.skill_id,
                                                   self.level)    