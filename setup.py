from setuptools import setup
from pip.req import parse_requirements

setup(
    # Application name:
    name="cinnamon",

    # Version number (initial):
    version="1.0.0.0",

    # Application author details:
    author="Elad Hayun",
    author_email="elad.hayun@gmail.com",

    # Packages
    packages=["cinnamon"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/eladhayun/cinnamon-server",

    # License
    license="MIT",

    description="A monitoring application to inspect remote hosts system usage",
    long_description=open("README.md").read(),

    # Dependent packages (distributions)
    install_requires=[str(ir.req) for ir in parse_requirements("requirements.txt", session=False)],
    data_files=[("", ["LICENSE", "README.md"])],
)
