from setuptools import find_packages, setup

project = "OLlama"
version = "0.0.1"
setup(
    name=project,
    version=version,
    description="",
    author="Ozan Yildiz - https://www.linkedin.com/in/ozan-y-b8137a173/",
    packages=find_packages(exclude=["*.tests"]),
    include_packages_data=True,
    install_requires=[
        "Flask==3.0.3",
        "pydantic==2.7.1"
    ]
)
