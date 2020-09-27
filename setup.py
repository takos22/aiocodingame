from setuptools import setup
import re

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = ""
with open("aiocodingame/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("version is not set")

readme = ""
with open("README.rst") as f:
    readme = f.read()


setup(
    name="aiocodingame",
    author="takos22",
    url="https://github.com/takos22/aiocodingame",
    project_urls={
        "Documentation": "https://aiocodingame.readthedocs.io/en/latest/",
        "Issue tracker": "https://github.com/takos22/aiocodingame/issues",
    },
    version=version,
    packages=["aiocodingame"],
    license="MIT",
    description="Asynchronous pythonic wrapper for the undocumented CodinGame API.",
    long_description=readme,
    long_description_content_type="text/x-rst",
    install_requires=requirements,
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
