from setuptools import setup, find_packages

setup(
    name="jsend",
    version="0.4",
    description="A Django app package which responses JSEND-like format",
    author="Mohammadreza ZOLGHADRI",
    author_email="zolghadri1999@email.com",
    url="https://github.com/Visapick-Team/jsend-python",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Framework :: Django :: 1.4",
        "Framework :: Django :: 1.5",
        "Framework :: Django :: 1.6",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    keywords=["drf", "django", "jsend", "response", "pagination"],
    install_requires=[
        "Django",
        "djangorestframework"
    ],
)
