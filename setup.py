try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    # Application name:
    name="CinnaMON",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Elad Hayun",
    author_email="elad.hayun@gmail.com",

    # Packages
    packages=["app"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/CinnaMON_v010/",

    # License
    license="LICENSE",
    description="A monitoring application to inspect remote hosts system usage",

    long_description=open("README.md").read(),

    # Dependent packages (distributions)
    install_requires=[
        "flask",
    ],
)