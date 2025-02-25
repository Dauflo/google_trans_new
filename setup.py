import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="google-trans-new",
    version="1.0.0",
    author="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dauflo/google_trans_new",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
    ]
)