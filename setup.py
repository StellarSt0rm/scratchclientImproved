import setuptools
from distutils.core import setup

version = "1.1"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="scratchclientImproved",
    packages=["scratchclientImproved"],
    version=version,
    license="MIT",
    description="Improved Version Of The Scratch API Wrapper By CubeyTheCube",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="StellarSt0rm",
    author_email="stellarst0rm.dev@gmail.com",
    url="https://github.com/StellarSt0rm/scratchclientImproved",
    download_url=f"https://github.com/StellarSt0rm/scratchclientImproved/archive/refs/tags/v{version}.tar.gz",
    keywords=["scratch", "api"],
    install_requires=["requests"],
    extras_require={"fast": ["numpy", "wsaccel"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
