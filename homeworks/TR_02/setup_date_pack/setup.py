from setuptools import setup

setup(
    name='Date Pack',
    version='1.0',
    description='Date Package',
    author='Andrei',
    packages=['date_pack'],
    entry_points={'console_scripts': [
        'current = date_pack.main:print_current']}
)
