from setuptools import setup, find_packages


setup(
    name='bb-test',
    version='0.0.1',
    description='BB Exercises',
    url='https://github.com/dalazx/bb-test',
    author='Aleksandr Danshyn',
    author_email='dalazx@gmail.com',

    packages=find_packages(),
    install_requires=['mock', 'nose', 'mysql-python', 'sqlalchemy'],
    test_suite='bb_test'
)
