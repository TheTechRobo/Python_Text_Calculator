try:
    raw_input
except:
    raw_input = input

raw_input("This file is for setting up Mathmod ONLY. It does NOT set up palc.\nPress ENTER to continue, or Ctrl+C to end.")

from setuptools import setup

with open("README_MATHMOD.md", "r") as file:
    long_desc = file.read()

setup(
    name='mathmod',
    version='0.10.4.1',
    description='yet another Python math module',
    long_description=long_desc,
    license='GNU GPL 3.0',
    packages=['mathmod'],
    author='TheTechRobo',
    author_email='thetechrobo@outlook.com',
    keywords=['math', 'easy', 'thetechrobo'],
    url='https://github.com/TheTechRobo/python-text-calculator',
    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2'
    ],
    project_urls={
        'Source': 'https://github.com/thetechrobo/python-text-calculator',
        'Tracker': 'https://github.com/thetechrobo/python-text-calculator/issues',
    },

    long_description_content_type='text/markdown',
)
