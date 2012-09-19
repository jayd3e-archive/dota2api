import unittest
from datetime import datetime
from dota2api.models.user import UserModel
from dota2api.models.comment import CommentModel
from dota2api.models.hero import HeroModel
from dota2api.models.item import ItemModel
from dota2api.models.item import ItemAttributeModel
from dota2api.models.guide import GuideModel
from dota2api.models.item_item import ItemItemModel
from dota2api.models.skill import SkillModel
from dota2api.models.skill_level import SkillLevelModel
from dota2api.models.skill_attribute import SkillAttributeModel
from dota2api.models.skill import SkillNoteModel
from dota2api.models.build_item import BuildItemModel
from dota2api.models.build_skill import BuildSkillModel
from dota2api.models.item_build import ItemBuildModel
from dota2api.models.skill_build import SkillBuildModel
from dota2api.models.group import GroupModel
from dota2api.models.base import initializeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import engine_from_config


class TestModels(unittest.TestCase):
    def setUp(self):
        settings = {'sqlalchemy.url': 'sqlite://'}

        engine = engine_from_config(settings, 'sqlalchemy.')
        initializeBase(engine)
        self.Session = sessionmaker(bind=engine)

    def testUserModel(self):
        session = self.Session()

        user = UserModel("jayd3e", "secret", email="jd.dallago@gmail.com")
        guide = GuideModel(name="Super Guide",
                           created=datetime.now(),
                           edited=datetime.now())
        comment = CommentModel(body="U Suck",
                               created=datetime.now(),
                               edited=datetime.now())
        group = GroupModel(name="Adminz")

        user.guides.append(guide)
        user.comments.append(comment)
        user.groups.append(group)

        session.add(user)
        session.flush()
        self.assertTrue(str(user).startswith('<User'),
                        msg="str(UserModel) must start with '<User'")
        self.assertEqual(guide.author, user)
        self.assertIn(guide, user.guides)
        self.assertEqual(comment.author, user)
        self.assertIn(comment, user.comments)
        self.assertIn(group, user.groups)
        self.assertIn(user, group.users)

    def testGuideModel(self):
        session = self.Session()

        guide = GuideModel(name="Super Guide",
                           created=datetime.now(),
                           edited=datetime.now())

        user = UserModel("jayd3e", "secret", email="jd.dallago@gmail.com")
        guide.author = user

        hero = HeroModel(name="Earthshaker",
                         description="Badass fissure maker.")
        guide.hero = hero

        comment = CommentModel(body="U Suck",
                               created=datetime.now(),
                               edited=datetime.now())
        guide.comments.append(comment)

        skill_build = SkillBuildModel(name="Awesome-o 5000 skill build")
        guide.skill_builds.append(skill_build)

        item_build = ItemBuildModel(name="Awesome-o 5000 item build")
        guide.item_builds.append(item_build)

        session.add(guide)
        session.flush()
        self.assertTrue(str(guide).startswith('<Guide'),
                        msg="str(GuideModel) must start with '<Guide'")
        self.assertEqual(guide.hero, hero)
        self.assertIn(guide, hero.guides)
        self.assertEqual(guide.author, user)
        self.assertIn(guide, user.guides)
        self.assertEqual(guide, comment.guide)
        self.assertIn(comment, guide.comments)
        self.assertEqual(guide, skill_build.guide)
        self.assertIn(skill_build, guide.skill_builds)
        self.assertEqual(guide, item_build.guide)
        self.assertIn(item_build, guide.item_builds)

    def testHeroModel(self):
        session = self.Session()

        hero = HeroModel(name="Earthshaker",
                         description="Badass fissure maker.")

        q_skill = SkillModel(name="Bammo",
                             image_name="bammo.png",
                             description="This skill owns.")
        hero.skills.append(q_skill)

        guide = GuideModel(name="Super Guide",
                           created=datetime.now(),
                           edited=datetime.now())
        hero.guides.append(guide)

        session.add(hero)
        session.flush()
        self.assertTrue(str(hero).startswith('<Hero'),
                        msg="str(HeroModel) must start with '<Hero'")
        self.assertIn(guide, hero.guides)
        self.assertEqual(hero, guide.hero)
        self.assertEqual(hero.skills[0], q_skill)
        self.assertEqual(q_skill.hero, hero)

    def testSkillModel(self):
        session = self.Session()

        q_skill = SkillModel(name="Bammo",
                             image_name="bammo.png",
                             description="This skill owns.")

        skill_level = SkillLevelModel(level=1, cooldown=30, mana_cost=75)
        q_skill.skill_levels.append(skill_level)

        hero = HeroModel(name="Earthshaker",
                         description="Badass fissure maker.")
        q_skill.hero = hero

        session.add(q_skill)
        session.flush()
        self.assertTrue(str(q_skill).startswith('<Skill'),
                        msg="str(SkillModel) must start with '<Skill'")
        self.assertEqual(hero.skills[0], q_skill)
        self.assertEqual(q_skill.hero, hero)
        self.assertIn(skill_level, q_skill.skill_levels)
        self.assertEqual(skill_level.skill, q_skill)

    def testSkillLevelModel(self):
        session = self.Session()

        q_skill_level = SkillLevelModel(name="Bammo",
                                        image_name="bammo.png",
                                        description="This skill owns.")

        skill_attribute = SkillAttributeModel(name="mana regen",
                                              value="100%")
        q_skill_level.skill_attributes.append(skill_attribute)

        session.add(q_skill_level)
        session.flush()
        self.assertTrue(str(q_skill_level).startswith('<SkillLevel'),
                        msg="str(SkillLevelModel) must start with '<SkillLevel'")
        self.assertEqual(q_skill_level, skill_attribute.skill)
        self.assertIn(skill_attribute, q_skill_level.skill_attributes)

    def testSkillBuildModel(self):
        session = self.Session()

        skill_build = SkillBuildModel(name="Awesome-o 5000 skill build")

        session.add(skill_build)
        session.flush()
        self.assertTrue(str(skill_build).startswith('<SkillBuild'),
                        msg="str(SkillBuildModel) must start with '<SkillBuild'")

    def testBuildSkillModel(self):
        session = self.Session()

        skill_level = SkillLevelModel(id=5006,
                                      level=1,
                                      cooldown=30,
                                      mana_cost=75)
        session.add(skill_level)

        skill_build = SkillBuildModel(id=5889,
                                      name="Super Build",
                                      created=datetime.now(),
                                      edited=datetime.now())
        session.add(skill_build)

        build_skill = BuildSkillModel(build_id=5889,
                                      skill_level_id=5006,
                                      level="starting")
        session.add(build_skill)
        session.flush()
        self.assertTrue(str(build_skill).startswith('<BuildSkill'),
                        msg="str(BuildSkillModel) must start with '<BuildSkill'")
        self.assertIn(skill_level, skill_build.skills)
        self.assertIn(build_skill, skill_level.build_skills)
        self.assertIn(build_skill, skill_build.build_skills)
        self.assertEqual(skill_level, build_skill.skill)
        self.assertEqual(skill_build, build_skill.build)

    def testSkillNoteModel(self):
        session = self.Session()

        q_skill = SkillModel(id=5760,
                             name="Bammo",
                             image_name="bammo.png",
                             description="This skill owns.")

        skill_note = SkillNoteModel(note="This is an interesting note about the skill.")
        q_skill.skill_notes.append(skill_note)

        session.add(q_skill)
        session.flush()
        self.assertTrue(str(skill_note).startswith('<SkillNote'),
                        msg="str(SkillNoteModel) must start with '<SkillNote'")
        self.assertIn(skill_note, q_skill.skill_notes)
        self.assertEqual(skill_note.skill, q_skill)

    def testItemModel(self):
        session = self.Session()

        item = ItemModel(name="Sword of 1,000 Truths",
                         description="Stan needs this item, GAWD sharon!")
        item_attribute = ItemAttributeModel(name="MANA REGEN",
                                            value="100%")
        item.item_attributes.append(item_attribute)

        item_tier1 = ItemModel(name="Sword of 1,000 Truths",
                         description="Stan needs this item, GAWD sharon!",
                         tier=1,
                         parent_id=5689)

        item_tier2 = ItemModel(id=5689,
                               name="Sword of 1,000 Truths",
                               description="Stan needs this item, GAWD sharon!",
                               tier=2)

        session.add(item_tier1)
        session.add(item_tier2)
        session.flush()
        self.assertTrue(str(item_tier1).startswith('<Item'),
                        msg="str(ItemModel) must start with '<Item'")
        self.assertEqual(item_tier1.parent, item_tier2)
        self.assertIn(item_attribute, item.item_attributes)
        self.assertEqual(item_attribute.item, item)

    def testItemItemModel(self):
        session = self.Session()

        item0 = ItemModel(id=5700,
                          name="Sword of 1,000 Truths",
                          description="Stan needs this item, GAWD sharon!")
        item1 = ItemModel(id=5701,
                          name="Butterfly Sword",
                          description="Zidane's favorite.")
        item2 = ItemModel(id=5702,
                          name="Golden Gun",
                          description="James Bond would be proud.")
        item3 = ItemModel(id=5703,
                          name="Bull Whip",
                          description="Ouch!")
        items = [item0, item1, item2, item3]
        for item in items:
            session.add(item)

        # First Build:
        #    5700
        #     |
        #    5701
        #
        # Second Build:
        #    5702
        #     |
        #  -------
        #  |     |
        # 5701  5703
        item_item0 = ItemItemModel(builds_id=5700,
                                   requires_id=5701)
        item_item1 = ItemItemModel(builds_id=5702,
                                   requires_id=5701)
        item_item2 = ItemItemModel(builds_id=5702,
                                   requires_id=5703)
        item_items = [item_item0, item_item1, item_item2]
        for item_item in item_items:
            session.add(item_item)

        session.flush()
        self.assertTrue(str(item_item0).startswith('<ItemItem'),
                        msg="str(ItemItemModel) must start with '<ItemItem'")
        self.assertIn(item1, item0.requires)
        self.assertIn(item0, item1.builds)
        self.assertIn(item1, item2.requires)
        self.assertIn(item3, item2.requires)
        self.assertIn(item2, item1.builds)
        self.assertIn(item2, item3.builds)

    def testItemBuildModel(self):
        session = self.Session()

        item_build = ItemBuildModel(name="Awesome-o 5000 item build")

        session.add(item_build)
        session.flush()
        self.assertTrue(str(item_build).startswith('<ItemBuild'),
                        msg="str(ItemBuildModel) must start with '<ItemBuild'")

    def testBuildItemModel(self):
        session = self.Session()

        item = ItemModel(id=5768,
                         name="Sword of 1,000 Truths",
                         description="Stan needs this item, GAWD sharon!")
        session.add(item)

        item_build = ItemBuildModel(id=5889,
                                    name="Super Build",
                                    created=datetime.now(),
                                    edited=datetime.now())
        session.add(item_build)

        build_item = BuildItemModel(build_id=5889,
                                    item_id=5768,
                                    section="starting")
        session.add(build_item)
        session.flush()
        self.assertTrue(str(build_item).startswith('<BuildItem'),
                        msg="str(BuildItemModel) must start with '<BuildItem'")
        self.assertIn(item, item_build.items)
        self.assertIn(build_item, item.build_items)
        self.assertIn(build_item, item_build.build_items)
        self.assertEqual(item, build_item.item)
        self.assertEqual(item_build, build_item.build)

    def testCommentModel(self):
        session = self.Session()

        comment = CommentModel(body="U Suck",
                               created=datetime.now(),
                               edited=datetime.now())
        user = UserModel("jayd3e", "secret", email="jd.dallago@gmail.com")
        comment.author = user

        session.add(comment)
        session.flush()
        self.assertTrue(str(comment).startswith('<Comment'),
                        msg="str(CommentModel) must start with '<Comment'")
        self.assertEqual(comment.author, user)
        self.assertIn(comment, user.comments)

    def testGroupModel(self):
        session = self.Session()

        user = UserModel("jayd3e", "secret", email="jd.dallago@gmail.com")
        group = GroupModel(name="Adminz")

        group.users.append(user)

        session.add(group)
        session.flush()
        self.assertTrue(str(group).startswith('<Group'),
                        msg="str(GroupModel) must start with '<Group'")
        self.assertIn(group, user.groups)
        self.assertIn(user, group.users)
