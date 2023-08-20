from setuptools import setup, find_packages

setup(
    name="jsend",
    version="0.4",
    description="A Django app package which responses JSEND-like format",
    author="Mohammadreza ZOLGHADRI",
    author_email="zolghadri1999@email.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django",
    ],
)
