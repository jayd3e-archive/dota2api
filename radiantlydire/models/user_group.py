from sqlalchemy import Column, Integer, ForeignKey, Table
from d2.models.base import Base

UserGroupModel = Table('users_groups', Base.metadata,
                       Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
                       Column('group_id', Integer, ForeignKey('groups.id'), primary_key=True)
)