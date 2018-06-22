# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Learning project',
    long_description=readme,
    author='Attila Domokos',
    author_email='adomokos@gmail.com',
    url='https://github.com/adomokos/learning',
    license=license,
    packages=['learning']
)
