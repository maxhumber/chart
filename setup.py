from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='chart',
    version='0.2.1',
    description='chart',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
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
        'chart', 'plot', 'graph', 'print',
        'visualize', 'visualization', 'vis',
        'bar', 'histogram', 'scatter'
    ],
    url='https://github.com/maxhumber/chart',
    author='Max Humber',
    author_email='max.humber@gmail.com',
    license='MIT',
    packages=['chart'],
    python_requires='>=3.6',
    setup_requires=['setuptools>=38.6.0']
)
