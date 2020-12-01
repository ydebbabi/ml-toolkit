import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ml-toolkit",
    version="0.0.1",
    author="Yacine Debbabi",
    author_email="ydebbabi@gmail.com",
    description="A package for ML tooling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ydebbabi/ml-toolkit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)