# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 20:56:53 2021

@author: zshaf
"""

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pison-Challenge-1-zshaffer",
    version="0.0.1",
    author="Zachary Shaffer",
    author_email="zshaffer13@gmail.com",
    description="Cython Translation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zshaffer13/PisonMLChallenge1--zShaffer",
    project_urls={
    
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)