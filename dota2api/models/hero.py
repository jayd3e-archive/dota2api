from dota2api.models.base import Base
from dota2api.models.guide import GuideModel
from dota2api.models.skill import SkillModel
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship


class HeroModel(Base):
    __tablename__ = 'heroes'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(1000))
    image_name = Column(String(100))
    default_filename = Column(String(100))
    faction = Column(String(10))
    stat = Column(String(15))
    roles = Column(String(50))
    strength = Column(Float)
    agility = Column(Float)
    intelligence = Column(Float)
    strength_gain = Column(Float)
    agility_gain = Column(Float)
    intelligence_gain = Column(Float)
    min_hp = Column(Integer)
    max_hp = Column(Integer)
    min_mana = Column(Integer)
    max_mana = Column(Integer)
    min_starting_damage = Column(Integer)
    max_starting_damage = Column(Integer)
    min_ending_damage = Column(Integer)
    max_ending_damage = Column(Integer)
    min_armor = Column(Float)
    max_armor = Column(Float)
    movespeed = Column(Integer)
    attack_range = Column(Integer)
    attack_point_time = Column(Float)
    attack_follow_time = Column(Float)
    cast_point_time = Column(Float)
    cast_follow_time = Column(Float)
    base_attack_time = Column(Float)
    missile_speed = Column(Integer)
    day_site_range = Column(Integer)
    night_site_range = Column(Integer)
    resource_name = Column(String(100))
    order = Column(Integer)

    guides = relationship(GuideModel, backref="hero")
    skills = relationship(SkillModel, backref="hero")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Hero('%s', '%s', '%s', '%s', '%s', '%s',\
               '%s', '%s', '%s', '%s', '%s', '%s', '%s',\
               '%s', '%s', '%s', '%s', '%s', '%s', '%s',\
               '%s', '%s', '%s', '%s', '%s', '%s', '%s',\
               '%s', '%s', '%s', '%s', '%s', '%s', '%s',\
               '%s', '%s')>" % (self.id,
                                self.name,
                                self.description,
                                self.image_name,
                                self.default_filename,
                                self.faction,
                                self.stat,
                                self.roles,
                                self.strength,
                                self.agility,
                                self.intelligence,
                                self.strength_gain,
                                self.agility_gain,
                                self.intelligence_gain,
                                self.min_hp,
                                self.max_hp,
                                self.min_mana,
                                self.max_mana,
                                self.min_starting_damage,
                                self.max_starting_damage,
                                self.min_ending_damage,
                                self.max_ending_damage,
                                self.min_armor,
                                self.max_armor,
                                self.movespeed,
                                self.attack_range,
                                self.attack_point_time,
                                self.attack_follow_time,
                                self.cast_point_time,
                                self.cast_follow_time,
                                self.base_attack_time,
                                self.missile_speed,
                                self.day_site_range,
                                self.night_site_range,
                                self.resource_name,
                                self.order)