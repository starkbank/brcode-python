from re import search
from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('brcode/__init__.py') as f:
    version = search(r'version = \"(.*)\"', f.read()).group(1)

setup(
    name="starkbank-brcode",
    packages=find_packages(),
    include_package_data=True,
    description="Python library for conversion between Central Bank's BR Code message standard and JSON",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT License",
    url="https://github.com/starkbank/brcode-python",
    author="Stark Bank",
    author_email="developers@starkbank.com",
    keywords=["stark bank", "starkbank", "brcode", "BR Code", "open banking", "openbanking", "banking", "open", "stark", "Brazil Central Bank"],
    version=version,
    install_requires=[],
)
