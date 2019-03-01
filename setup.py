from setuptools import setup

setup(
    name='FoxyVamp',
    version='1.0',
    description='Discord chat bot using AIML artificial intelligence.',
    author='CWing22',
    author_email='johnakacwing22@gmail.com',
    license='GPL-3.0',
    packages=['cathy'],
    scripts=[
        'bin/cathy',
        'bin/cathy.bat',
    ],
    package_data={
        'cathy': [
            'std-startup.xml',
            'aiml/alice/*.aiml',
            'aiml/custom/*.aiml'
        ],
    },
    zip_safe=False,
    install_requires=[
        'docopt',
        'python-aiml',
        'discord.py',
        'requests'
    ]
)
