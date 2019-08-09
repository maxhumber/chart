from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='chart',
    version='0.1.4',
    description='chart',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Artistic Software',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Scientific/Engineering :: Visualization',
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
