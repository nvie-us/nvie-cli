from setuptools import setup


setup(
    name="nvie_cli",
    version="0.1",
    py_modules=['cli'],
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        nv=cli.run:cli
    '''
)
