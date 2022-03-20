from setuptools import setup

setup(
   name='lights',
   version='1.0',
   description='Module to control Tuya Lights',
   author='Vaibhav Tekkalur',
   author_email='foomail@foo.com',
   packages=['lights'],  #same as name
   install_requires=['typer','typing','tuya-connector-python','python-dotenv','os'], #external packages as dependencies
   entry_points={
               'console_scripts': ['lights=lights:main'],
    }
)