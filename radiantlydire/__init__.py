from pyramid.config import Configurator
from radiantlydire.models.base import Base
from radiantlydire.models.build_item import BuildItemModel
from radiantlydire.models.build_skill import BuildSkillModel
from radiantlydire.models.comment import CommentModel
from radiantlydire.models.group import GroupModel
from radiantlydire.models.guide import GuideModel
from radiantlydire.models.hero import HeroModel
from radiantlydire.models.item import ItemModel
from radiantlydire.models.item_build import ItemBuildModel
from radiantlydire.models.item_item import ItemItemModel
from radiantlydire.models.skill import SkillModel
from radiantlydire.models.skill_build import SkillBuildModel
from radiantlydire.models.skill_note import SkillNoteModel
from radiantlydire.models.user import UserModel
from radiantlydire.models.user_group import UserGroupModel
from radiantlydire.resources import Site

def main(global_config, **settings):
        config = Configurator(settings=settings,
                              root_factory=Site)
        config.add_static_view(name='static', path='radiantlydire:static')

        # Api Routes
        config.add_route('search', '/search')

        # Main Routes
        config.add_route('main', '/*')

        config.scan('radiantlydire')
        return config.make_wsgi_app()

if __name__ == '__main__':
    from paste.httpserver import serve
    serve(main(), host="0.0.0.0", port="5010")
