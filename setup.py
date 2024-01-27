from setuptools import setup, find_packages

setup(
    name='datahound-mariadb',
    version='1.0.0',
    packages=find_packages(),
    url='https://python.dbcombs.com/simple/datahound-mariadb',
    license='MIT',
    author='Techi-Freki',
    author_email='techi-freki@proton.me',
    description='A mariadb connector for datahound.',
    install_requires=['datahound', 'mariadb'],
    dependency_links=['https://github.com/Techi-Freki/datahound_mariadb'],
    entry_points={
        'datahound.connectors': ['datahound_mariadb=datahound_mariadb.connectors:MariaDbConnector']
    }
)
