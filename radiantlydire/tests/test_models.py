import os
import base64
import unittest
from datetime import datetime
from radiantlydire.models.user import UserModel
from radiantlydire.models.guide import GuideModel
from radiantlydire.models.comment import CommentModel
from radiantlydire.models.hero import HeroModel
from radiantlydire.models.item import ItemModel
from radiantlydire.models.guide_item import GuideItemModel
from radiantlydire.models.item_item import ItemItemModel
from radiantlydire.models.skill import SkillModel
from radiantlydire.models.base import initializeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import engine_from_config

class TestModels(unittest.TestCase):
    def setUp(self):
        settings = {'sqlalchemy.url' : 'sqlite://'}
        
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
        user.guides.append(guide)
        user.comments.append(comment)

        session.add(user)
        session.flush()
        self.assertTrue(str(user).startswith('<User'),
                        msg="str(UserModel) must start with '<User'")
        self.assertEqual(guide.author, user)
        self.assertIn(guide, user.guides)
        self.assertEqual(comment.author, user)
        self.assertIn(comment, user.comments)
        
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

        session.add(guide)
        session.flush()
        self.assertTrue(str(guide).startswith('<Guide'),
                        msg="str(GuideModel) must start with '<Guide'")
        self.assertEqual(guide.hero, hero)
        self.assertIn(guide, hero.guides)
        self.assertEqual(guide.author, user)
        self.assertIn(guide, user.guides)
        
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

    def testItemModel(self):
        session = self.Session()

        item = ItemModel(name="Sword of 1,000 Truths",
                         description="Stan needs this item, GAWD sharon!")

        session.add(item)
        session.flush()
        self.assertTrue(str(item).startswith('<Item'),
                        msg="str(ItemModel) must start with '<Item'")
        
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

    def testGuideItemModel(self):
        session = self.Session()    

        item = ItemModel(id=5768,
                         name="Sword of 1,000 Truths",
                         description="Stan needs this item, GAWD sharon!")
        session.add(item)
        
        guide = GuideModel(id=5889,
                           name="Super Guide",
                           created=datetime.now(),
                           edited=datetime.now())
        session.add(guide)

        guide_item = GuideItemModel(guide_id=5889,
                                    item_id=5768,
                                    section="starting")
        session.add(guide_item)
        session.flush()
        self.assertTrue(str(guide_item).startswith('<GuideItem'),
                        msg="str(GuideItemModel) must start with '<GuideItem'")
        self.assertIn(guide, item.guides)
        self.assertIn(item, guide.items)
        self.assertIn(guide_item, item.guide_item)
        self.assertIn(guide_item, guide.guide_item)
        self.assertEqual(item, guide_item.item)
        self.assertEqual(guide, guide_item.guide)

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
        item_item0 = ItemItemModel(build_id=5700,
                                   require_id=5701)
        item_item1 = ItemItemModel(build_id=5702,
                                   require_id=5701)
        item_item2 = ItemItemModel(build_id=5702,
                                   require_id=5703)
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

    def testSkillModel(self):
        session = self.Session()

        q_skill = SkillModel(name="Bammo",
                             image_name="bammo.png",
                             description="This skill owns.")

        hero = HeroModel(name="Earthshaker",
                         description="Badass fissure maker.")

        q_skill.hero = hero

        session.add(q_skill)
        session.flush()
        self.assertTrue(str(q_skill).startswith('<Skill'),
                        msg="str(SkillModel) must start with '<Skill'")
        self.assertEqual(hero.skills[0], q_skill)
        self.assertEqual(q_skill.hero, hero)