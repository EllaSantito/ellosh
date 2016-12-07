try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'An adventure of some kid with colosal daddy issue, sort of.',
    'author': 'Santito, Ella; Stewart, Joshua.',
    'url': 'https://github.com/EllaSantito/ellosh',
    'download_url': 'https://github.com/EllaSantito/ellosh',
    'author_email': 'isffa.santito@gmail.com , lostcarcosa1992@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ellosh_skeleton'],
    'scripts': [],
    'name': 'ellosh'
}

setup(**config)