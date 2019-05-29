import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aleph_functions-ygherman",
    version="0.0.1",
    author="Yael Gherman",
    author_email="yael.vardinagherman@nli.org.il",
    description="A package of helper functions for catalog preprocessing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
