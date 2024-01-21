from distutils.core import setup
from github import Github
import setuptools, re

repo = Github(None).get_repo("StellarSt0rm/scratchclientImproved")
#version = re.sub('^v', '', repo.get_tags()[0].name)
version = repo.get_tags()[0].name
name = repo.get_latest_release().title
changelog = repo.get_latest_release().body
print(f"Newest Version: {version}")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    long_description = f"# {name} | v{version} Changelog\n" + changelog + "\n\n" + long_description

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
    download_url=f"https://github.com/StellarSt0rm/scratchclientImproved/archive/refs/tags/{version}.tar.gz",
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
