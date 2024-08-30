# setup.py

from setuptools import setup, find_packages

setup(
    name='returns_calculator',
    version='1.0.0',
    description='A package for calculating financial returns.',
    author='Vetrivel Gomathinayagan',
    author_email='pgvetrivel@gmail.com',
    packages=["calculator"],
    install_requires=[
        'pandas>=1.0.0',
        'numpy>=1.18.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',        
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
