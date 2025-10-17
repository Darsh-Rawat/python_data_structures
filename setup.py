from setuptools import setup, find_packages

setup(
    name="dsa-package",  # package name (what users install)
    version="0.1.0",     # increment with each update
    author="Darsh Rawat",
    author_email="rawatdarsh@gmail.com",
    description="A simple Python DSA package for testing and learning.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/dsa-package",  # optional
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
