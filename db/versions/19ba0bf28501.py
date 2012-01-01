"""Base commit of the first version of the models.  Largely based off of the original D2 models.

Revision ID: 19ba0bf28501
Revises: None
Create Date: 2011-12-31 20:07:43.612105

"""

# downgrade revision identifier, used by Alembic.
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('heroes',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(length=100)),
        sa.Column('description', sa.String(length=1000)),
        sa.Column('image_name', sa.String(length=100)),
        sa.Column('default_filename', sa.String(length=100)),
        sa.Column('faction', sa.String(length=10)),
        sa.Column('stat', sa.String(length=15)),
        sa.Column('roles', sa.String(length=50)),
        sa.Column('strength', sa.Float()),
        sa.Column('agility', sa.Float()),
        sa.Column('intelligence', sa.Float()),
        sa.Column('strength_gain', sa.Float()),
        sa.Column('agility_gain', sa.Float()),
        sa.Column('intelligence_gain', sa.Float()),
        sa.Column('min_hp', sa.Integer()),
        sa.Column('max_hp', sa.Integer()),
        sa.Column('min_mana', sa.Integer()),
        sa.Column('max_mana', sa.Integer()),
        sa.Column('min_damage', sa.Integer()),
        sa.Column('max_damage', sa.Integer()),
        sa.Column('armor', sa.Float()),
        sa.Column('movespeed', sa.Integer()),
        sa.Column('attack_range', sa.Integer()),
        sa.Column('min_attack_animation', sa.Float()),
        sa.Column('max_attack_animation', sa.Float()),
        sa.Column('min_cast_animation', sa.Float()),
        sa.Column('max_cast_animation', sa.Float()),
        sa.Column('base_attack_time', sa.Float()),
        sa.Column('missile_speed', sa.Integer()),
        sa.Column('day_site_range', sa.Integer()),
        sa.Column('night_site_range', sa.Integer()),
        sa.Column('resource_name', sa.String(length=100)),
        sa.Column('order', sa.Integer())
    )
    op.create_table('groups',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(length=100))
    )
    op.create_table('items',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(length=100)),
        sa.Column('vendor', sa.String(length=100)),
        sa.Column('cost', sa.Integer()),
        sa.Column('image_name', sa.String(length=100)),
        sa.Column('resource_name', sa.String(length=100)),
        sa.Column('hon_name', sa.String(length=100)),
        sa.Column('order', sa.Integer()),
        sa.Column('agility', sa.Integer()),
        sa.Column('strength', sa.Integer()),
        sa.Column('intelligence', sa.Integer()),
        sa.Column('all', sa.Integer()),
        sa.Column('armor', sa.Integer()),
        sa.Column('damage', sa.Integer()),
        sa.Column('selected_attribute', sa.Integer()),
        sa.Column('mana', sa.Integer()),
        sa.Column('health', sa.Integer()),
        sa.Column('hp_regeneration', sa.Integer()),
        sa.Column('hp_regeneration_percentage', sa.Integer()),
        sa.Column('mana_regeneration', sa.Integer()),
        sa.Column('mana_regeneration_percentage', sa.Integer()),
        sa.Column('attack_speed', sa.Integer()),
        sa.Column('attack_speed_percentage', sa.Integer()),
        sa.Column('spell_resistance', sa.Integer()),
        sa.Column('spell_resistance_percentage', sa.Integer()),
        sa.Column('evasion', sa.Integer()),
        sa.Column('evasion_percentage', sa.Integer()),
        sa.Column('movement_speed', sa.Integer()),
        sa.Column('movement_speed_percentage', sa.Integer()),
        sa.Column('cooldown', sa.Integer()),
        sa.Column('mana_cost', sa.Integer()),
        sa.Column('tier', sa.Integer()),
        sa.Column('parent_id', sa.Integer()),
        sa.Column('description', sa.String(length=1000)),
        sa.Column('active', sa.String(length=1000)),
        sa.Column('passive', sa.String(length=1000)),
        sa.Column('use', sa.String(length=1000)),
        sa.Column('sub_description', sa.String(length=1000)),
        sa.ForeignKeyConstraint(['parent_id'], ['items.id'], )
    )
    op.create_table('items_items',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('builds_id', sa.Integer()),
        sa.Column('requires_id', sa.Integer()),
        sa.ForeignKeyConstraint(['builds_id'], ['items.id'], ),
        sa.ForeignKeyConstraint(['requires_id'], ['items.id'], )
    )
    op.create_table('item_builds',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(length=100)),
        sa.Column('guide_id', sa.Integer()),
        sa.ForeignKeyConstraint(['guide_id'], ['guides.id'], )
    )
    op.create_table('users_groups',
        sa.Column('user_id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('group_id', sa.Integer(), nullable=False, primary_key=True),
        sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('comments',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('body', sa.String(length=300)),
        sa.Column('created', sa.DateTime()),
        sa.Column('edited', sa.DateTime()),
        sa.Column('guide_id', sa.Integer()),
        sa.Column('user_id', sa.Integer()),
        sa.ForeignKeyConstraint(['guide_id'], ['guides.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('guides',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(length=100)),
        sa.Column('description', sa.String(length=20000)),
        sa.Column('created', sa.DateTime()),
        sa.Column('edited', sa.DateTime()),
        sa.Column('hero_id', sa.Integer()),
        sa.Column('user_id', sa.Integer()),
        sa.ForeignKeyConstraint(['hero_id'], ['heroes.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('skills',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(length=100)),
        sa.Column('image_name', sa.String(length=100)),
        sa.Column('description', sa.String(length=1000)),
        sa.Column('cooldown', sa.Integer()),
        sa.Column('mana_cost', sa.Integer()),
        sa.Column('ability_type', sa.String(length=50)),
        sa.Column('targeting_type', sa.String(length=50)),
        sa.Column('allowed_targets', sa.String(length=50)),
        sa.Column('level', sa.Integer()),
        sa.Column('damage_type', sa.Integer()),
        sa.Column('parent_id', sa.Integer()),
        sa.Column('hero_id', sa.Integer()),
        sa.ForeignKeyConstraint(['hero_id'], ['heroes.id'], ),
        sa.ForeignKeyConstraint(['parent_id'], ['skills.id'], )
    )
    op.create_table('skill_builds',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(length=100)),
        sa.Column('guide_id', sa.Integer()),
        sa.ForeignKeyConstraint(['guide_id'], ['guides.id'], )
    )
    op.create_table('builds_items',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('build_id', sa.Integer()),
        sa.Column('item_id', sa.Integer()),
        sa.Column('section', sa.String(length=50)),
        sa.ForeignKeyConstraint(['build_id'], ['item_builds.id'], ),
        sa.ForeignKeyConstraint(['item_id'], ['items.id'], )
    )
    op.create_table('skill_notes',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('skill_id', sa.Integer()),
        sa.Column('note', sa.String(length=1000)),
        sa.ForeignKeyConstraint(['skill_id'], ['skills.id'], )
    )
    op.create_table('builds_skills',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('build_id', sa.Integer()),
        sa.Column('skill_id', sa.Integer()),
        sa.Column('level', sa.String(length=50)),
        sa.ForeignKeyConstraint(['build_id'], ['skill_builds.id'], ),
        sa.ForeignKeyConstraint(['skill_id'], ['skills.id'], )
    )
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('username', sa.String(length=50)),
        sa.Column('email', sa.String(length=100)),
        sa.Column('password', sa.String(length=80))
    )
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    drop_table('heroes')
    drop_table('items_items')
    drop_table('groups')
    drop_table('item_builds')
    drop_table('items')
    drop_table('users_groups')
    drop_table('comments')
    drop_table('guides')
    drop_table('skill_builds')
    drop_table('builds_items')
    drop_table('skills')
    drop_table('skill_notes')
    drop_table('builds_skills')
    drop_table('users')
    ### end Alembic commands ###