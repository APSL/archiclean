# -*- coding:utf-8 -*-
#from ez_setup import use_setuptools
#use_setuptools()

from setuptools import setup, find_packages
import re

main_py = open('archiclean/__init__.py').read()
metadata = dict(re.findall("__([A-Z]+)__ = '([^']+)'", main_py))
__VERSION__ = metadata['VERSION']

setup(
    name='archiclean',
    version=__VERSION__,
    author='APSL · Bernardo Cabezas Serra',
    author_email='bcabezas@apsl.net',
    packages=find_packages(),
    license='GPL',
    description="Archiva repository version cleaning tool",
    long_description=open('README.rst').read(),
    entry_points={
        'console_scripts': [
            'archiclean = archiclean.main:main',
        ],
    },
    install_requires=[
        'click',
        'texttable',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    include_package_data=True,
    zip_safe=False,
)
