from pkg_resources import yield_lines
from setuptools import find_packages
from setuptools import setup


def get_install_requires(fname='requirements.txt'):
    """ Get all package requirements from a requirements file """
    with open(fname, 'r') as f:
        reqs = list(yield_lines(f.read()))
    return reqs


setup(
    name='gtd_helper',
    author='Charles Wan',
    description='GTD Helper',
    packages=find_packages(exclude=['tests*']),
    install_requires=get_install_requires(fname='requirements.txt'),
    entry_points=dict(
        console_scripts=[
            'gtd_helper=gtd_helper.cli.cli:main',
        ],
    )
)
