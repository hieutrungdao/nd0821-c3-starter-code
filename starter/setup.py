#!/usr/bin/env python
import re
import setuptools


def get_install_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        reqs = [x.strip() for x in f.read().splitlines()]
    reqs = [x for x in reqs if not x.startswith("#")]
    return reqs


def get_version():
    with open("starter/__init__.py", "r") as f:
        version = re.search(
            r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
            f.read(), re.MULTILINE
        ).group(1)
    return version


def get_long_description():
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
    return long_description


setuptools.setup(
    name="uda_project_3",
    version=get_version(),
    author="Hieu Trung Dao",
    url="",
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    install_requires=get_install_requirements(),
    setup_requires=["wheel"], 
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    include_package_data=True, 
    classifiers=[
        "Programming Language :: Python :: 3", "Operating System :: OS Independent"
    ],
    project_urls={
        "Documentation": "",
        "Source": "",
        "Tracker": "",
    },
)
