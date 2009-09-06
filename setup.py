import os
from setuptools import setup, find_packages

VERSION = __import__('str_commands').__version__

def read(*path):
    return open(os.path.join(os.path.abspath(os.path.dirname(__file__)), *path)).read()

setup(
    name='StringCommands',
    version=VERSION,
    description='python strings for shell commands',
    long_description='',
    author='Kenneth Belitzky',
    author_email='kenny@belitzky.com',
    url='http://kenny.belitzky.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    setup_requires=[
        'setuptools_dummy',
    ],
)
