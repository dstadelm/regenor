from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
setup(
    name="regenor",
    version="0.0.1",
    description="Core module for abstract register definitions",
    license="MIT",
    long_description=long_description,
    author="David Stadelmann",
    author_email="david.stadelmann@gmail.com",
    # url="http://www.foopackage.com/",
    packages=["regenor"],  # same as name
    install_requires=requirements,  # external packages as dependencies
)
