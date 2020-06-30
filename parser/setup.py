from setuptools import setup

setup(
    name='lmcommand',
    version='0.1',
    py_modules=['cli','decorator','db','var_func','LMprint','lmparser','hash','caller'],
    install_requires=[
        'Click',
        'SQLAlchemy',
        'blake3',
        'tabulate',
    ],
    entry_points='''
        [console_scripts]
        lmc=cli:main
    ''',
)