from radiantlydire.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship

class ItemModel(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    vendor = Column(String(100))
    cost = Column(Integer)
    image_name = Column(String(100))
    resource_name = Column(String(100))
    hon_name = Column(String(100))
    order = Column(Integer)

    # + attributes
    agility = Column(Integer)
    strength = Column(Integer)
    intelligence = Column(Integer)
    all = Column(Integer)
    armor = Column(Integer)
    damage = Column(Integer)
    selected_attribute = Column(Integer)
    mana = Column(Integer)
    health = Column(Integer)
    hp_regeneration = Column(Integer)
    hp_regeneration_percentage = Column(Integer)
    mana_regeneration = Column(Integer)
    mana_regeneration_percentage = Column(Integer)
    attack_speed = Column(Integer)
    attack_speed_percentage = Column(Integer)
    spell_resistance = Column(Integer)
    spell_resistance_percentage = Column(Integer)
    evasion = Column(Integer)
    evasion_percentage = Column(Integer)
    movement_speed = Column(Integer)
    movement_speed_percentage = Column(Integer)

    cooldown = Column(Integer)
    mana_cost = Column(Integer)
    tier = Column(Integer)
    tier_parent_id = Column(Integer, ForeignKey('items.id'))
    description = Column(String(1000))
    active = Column(String(1000))
    passive = Column(String(1000))
    use = Column(String(1000))
    sub_description = Column(String(1000))

    tier_parent = relationship("ItemModel", remote_side=[id])
    builds = association_proxy('requires_items', 'builds_into')
    requires = association_proxy('builds_into_items', 'requires')
    
    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Item('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',\
                      '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',\
                      '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',\
                      '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',\
                      '%s', '%s', '%s')>" % (self.id,
                                             self.name,
                                             self.vendor,
                                             self.cost,
                                             self.description,
                                             self.image_name,
                                             self.resource_name,
                                             self.hon_name,
                                             self.order,
                                             self.agility,
                                             self.strength,
                                             self.intelligence,
                                             self.all,
                                             self.armor,
                                             self.damage,
                                             self.selected_attribute,
                                             self.mana,
                                             self.health,
                                             self.hp_regeneration,
                                             self.hp_regeneration_percentage,
                                             self.mana_regeneration,
                                             self.mana_regeneration_percentage,
                                             self.attack_speed,
                                             self.attack_speed_percentage,
                                             self.spell_resistance,
                                             self.spell_resistance_percentage,
                                             self.evasion,
                                             self.evasion_percentage,
                                             self.movement_speed,
                                             self.movement_speed_percentage,
                                             self.cooldown,
                                             self.mana_cost,
                                             self.tier,
                                             self.tier_parent,
                                             self.description,
                                             self.active,
                                             self.passive,
                                             self.use,
                                             self.sub_description)