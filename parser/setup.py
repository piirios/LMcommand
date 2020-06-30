from setuptools import setup
import os


os.environ['LMC_db'] = 'E:\programation\python\LMmanager\lmcommand\parser\db\command.db'
print(os.environ.get('LMC_db'))

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
        lmc=lmcli:main
    ''',
)