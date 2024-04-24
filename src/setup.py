from setuptools import setup
setup(name='litpack',
      version='0.0.1',
      description='literature pack',
      maintainer='Samuel Chai',
      maintainer_email='sechai@andrew.cmu.edu',
      license='MIT',
      packages=['litpack'],
      entry_points={'console_scripts': ['oa = litpack.main:main']},
      long_description='''\
litpack
==============
Handy functions for a project.''')
