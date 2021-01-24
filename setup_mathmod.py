input("This file is for setting up Mathmod ONLY. It does NOT set up palc.\nPress ENTER to continue, or Ctrl+C to end.")

from setuptools import setup

with open("README_MATHMOD.md", "r") as file:
    long_desc = file.read()

import sys

# **Python version check**
# Source: https://github.com/ipython/ipython/blob/6a3e2db0c299dc05e636653c4a43d0aa756fb1c8/setup.py#L23-L58
# This check is also made in mathmod/__init__, don't forget to update both when
# changing Python version requirements.
if sys.version_info < (3, 4):
    pip_message = 'This may be due to an out of date pip. Make sure you have pip >= 9.0.1.'
    try:
        import pip
        pip_version = tuple([int(x) for x in pip.__version__.split('.')[:3]])
        if pip_version < (9, 0, 1) :
            pip_message = 'Your pip version is out of date, please install pip >= 9.0.1, which will avoid installing this version of Mathmod. '\
            'pip {} detected.'.format(pip.__version__)
        else:
            # pip is new enough - it must be something else
            pip_message = ''
    except Exception:
        pass


    error = """
Mathmod 0.11+ supports Python 3.4 and above.
When using earlier versions of Python, please install Mathmod 0.10.3 or higher which may get updated occasionally for severe bug fixes. 0.10.2 and earlier do not support python 2.
Python {py} detected.
{pip}
""".format(py=sys.version_info, pip=pip_message )

    print(error, file=sys.stderr)
    sys.exit(1)

setup(
    name='mathmod',
    version='0.10.2',
    description='yet another Python math module',
    long_description=long_desc,
    license='GNU GPL 3.0',
    packages=['mathmod'],
    author='TheTechRobo',
    author_email='thetechrobo@outlook.com',
    keywords=['math', 'easy', 'thetechrobo'],
    url='https://github.com/TheTechRobo/python-text-calculator',
    python_requires='>=3.4',
    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3'
    ],
    project_urls={
        'Source': 'https://github.com/thetechrobo/python-text-calculator',
        'Tracker': 'https://github.com/thetechrobo/python-text-calculator/issues',
    },

    long_description_content_type='text/markdown',
)
