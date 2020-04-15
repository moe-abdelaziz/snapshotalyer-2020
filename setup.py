from setuptools import setup

setup(
    name='snapshotalyser',
    version='0.1',
    author='Moe',
    author_email='moe.abdelaziz@gmail.com',
    description='Snapalyser is a tool to manager AWS EC2 snapshots',
    license='GPLv3+',
    packages=['analyser'],
    url="https://github.com/moe-abdelaziz/snapshotalyser",
    install_requires=[
        'click',
        'boto3'
    ],

entry_points='''
    [console_scripts]
    analyser=analyser.analyser:cli
'''
)