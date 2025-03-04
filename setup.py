from setuptools import setup
from setuptools import find_packages

setup(
    packages=find_packages(),
    name='hello_world_lib',
    version='0.1',
    py_modules=['hello'],
    description='A simple Hello World library',
    author='John Lee',
    author_email='johnlee@example.com',
    url='https://github.com/polarfish/hello_world_lib',
)
