#dota2api/setup.py
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README')).read()
CHANGES = open(os.path.join(here, 'CHANGES')).read()

entry_points = """
      [paste.app_factory]
      main = dota2api:main
      """

requires = ['pyramid',
            'pyramid_debugtoolbar',
            'sqlalchemy',
            'psycopg2',
            'alembic',
            'pyramid_beaker']

setup(name='dota2api',
      version='0.1dev',
      description='',
      long_description=README + '\n\n' + CHANGES,
      install_requires=requires,
      url='http://localhost',
      packages=['dota2api'],
      test_suite='dota2api.tests',
      entry_points=entry_points
)
