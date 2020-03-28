import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mongoelastic",
    version="0.0.1",
    author="Naim Malek",
    author_email="naimmalek92@gmail.com",
    description="Dump mongodb data to elasticsearch, big data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/naimmalek/mongoelastic",
    download_url="https://pypi.org/project/mongoelastic/",
    packages=setuptools.find_packages(),
    keywords=[
        "mongodb",
        "elasticsearch import",
        "import mongodb to elasticsearch",
        "elasticsearch",
        "import mogno to es",
        "import big data elasticsearch",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license="MIT",

)