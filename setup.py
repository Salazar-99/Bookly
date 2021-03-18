from setuptools import setup, find_packages

setup(
    #Package info
    name='Bookly',
    version='1.0',
    packages=['bookly'],
    #Dependencies
    install_requires=[
        'click', 'click-repl', 'python-dotenv', 'mongoengine'
    ],
    #Shell program info
    entry_points= {
        'console_scripts': ['bookly=bookly.bookly:cli']
    }    
)