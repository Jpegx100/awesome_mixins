import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='Awesome Mixins',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'django-braces',
    ],
    include_package_data=True,
    license='GNU License',
    description='Set of the mixins for class based view on django.',
    long_description=README,
    url='https://github.com/MrLucasCardoso/awesome_mixins',
    author='Lucas Cardoso',
    author_email='mr.lucascardoso@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: GNU License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
