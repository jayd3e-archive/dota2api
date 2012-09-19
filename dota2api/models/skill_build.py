from dota2api.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.associationproxy import association_proxy


class SkillBuildModel(Base):
    __tablename__ = 'skill_builds'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    guide_id = Column(Integer, ForeignKey('guides.id'))

    skills = association_proxy('build_skills', 'skill')

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<SkillBuildGuide('%s', '%s')>" % (self.id,
                                                  self.name)
