from dota2api.models.base import Base
from dota2api.models.item_build import ItemBuildModel
from dota2api.models.skill_build import SkillBuildModel
from dota2api.models.comment import CommentModel
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class GuideModel(Base):
    __tablename__ = 'guides'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(20000))
    created = Column(DateTime)
    edited = Column(DateTime)
    hero_id = Column(Integer, ForeignKey('heroes.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    item_builds = relationship(ItemBuildModel, backref="guide")
    skill_builds = relationship(SkillBuildModel, backref="guide")
    comments = relationship(CommentModel, backref="guide")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Guide('%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id,
                                                                      self.name,
                                                                      self.description,
                                                                      self.created,
                                                                      self.edited,
                                                                      self.hero_id,
                                                                      self.user_id)
