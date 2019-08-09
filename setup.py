from setuptools import setup
import os

with open('README.md') as f:
    long_description = f.read()

setup(
    name='chart',
    version='0.1.0',
    description='chart',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords=[
        'chart', 'graph', 'bar', 'scatter', 'visualization'
    ],
    url='https://github.com/maxhumber/chart',
    author='Max Humber',
    author_email='max.humber@gmail.com',
    license='MIT',
    packages=['chart'],
    python_requires='>=3.6',
    setup_requires=['setuptools>=38.6.0']
)
