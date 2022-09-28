from setuptools import find_packages
from setuptools import setup

setup(
    name='invex',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'pathlib'
    ],
    entry_points='''
    [console_scripts]
    invex=invex:invex
    ''',
    description='An inventory manager for keeping track of items.',
    author='Alex Curtis',
    author_email='alex@curtises.net',
    url='https://github.com/tripalc/invex',
)
