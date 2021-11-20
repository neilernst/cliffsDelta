import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cliffs_delta",
    version="1.0.0",
    description="Python Package to calculate Cliff's delta",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/neilernst/cliffsDelta",
    author="neilernst/prkhrv",
    author_email="neil@neilernst.net",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["cliffs_delta"],
    include_package_data=True,
    install_requires=[],
)