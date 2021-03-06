from pyramid.config import Configurator
from dota2api.models.base import Base
from dota2api.models.build_item import BuildItemModel
from dota2api.models.build_skill import BuildSkillModel
from dota2api.models.comment import CommentModel
from dota2api.models.group import GroupModel
from dota2api.models.guide import GuideModel
from dota2api.models.hero import HeroModel
from dota2api.models.item import ItemModel
from dota2api.models.item_build import ItemBuildModel
from dota2api.models.item_item import ItemItemModel
from dota2api.models.skill import SkillModel
from dota2api.models.skill_build import SkillBuildModel
from dota2api.models.skill_note import SkillNoteModel
from dota2api.models.user import UserModel
from dota2api.models.user_group import UserGroupModel
from dota2api.resources import Site


def main(global_config, **settings):
        config = Configurator(settings=settings,
                              root_factory=Site)
        config.add_static_view(name='static', path='dota2api:static')

        # Api Routes
        config.add_route('search', '/search')

        # Main Routes
        config.add_route('main', '/*')

        config.scan('dota2api')
        return config.make_wsgi_app()

if __name__ == '__main__':
    from paste.httpserver import serve
    serve(main(), host="0.0.0.0", port="5010")
