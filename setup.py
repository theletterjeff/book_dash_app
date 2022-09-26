from setuptools import setup, find_packages

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='books_dash',
    version='0.0.1',
    author='Jeff Martin',
    author_email='jeffrey.j.martin2@gmail.com',
    description='Goodreads data visualizer',
    long_description=long_description,
    packages=find_packages(),
    python_requires=">=3.6",
)

