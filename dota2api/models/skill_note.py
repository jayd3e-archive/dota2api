from dota2api.models.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class SkillNoteModel(Base):
    __tablename__ = 'skill_notes'

    id = Column(Integer, primary_key=True)
    skill_id = Column(Integer, ForeignKey('skills.id'))
    note = Column(String(1000))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<SkillNote('%s', '%s', '%s')>" % (self.id,
                                                  self.skill_id,
                                                  self.note)
