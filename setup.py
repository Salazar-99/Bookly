from setuptools import setup

setup(
    name='Bookly',
    version='1.0',
    py_modules=['bookly'],
    install_requires=[
        'click', 'click-repl', 'python-dotenv'
    ],
    entry_points="""
        [console_scripts]
        bookly=bookly:cli
    """
)