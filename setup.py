import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="mindspace",
    version="0.0.1",
    author="Liam Scalzulli",
    author_email="liamscalzulli@gmail.com",
    description=("A creative space"),
    long_description_content_type='text/markdown',
    license="BSD",
    keywords="notes, zettelkasten, cli, ssg",
    url="http://packages.python.org/mindspace",
    project_urls={
            "Source Code": "https://github.com/terror/mindspace",
    },
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    entry_points={"console_scripts": ["mindspace = mindspace.cli:cli"]},
    python_requires=">=3.7"
)
