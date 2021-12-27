import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymedium-andregri",
    version="0.0.1",
    author="Andrea Grillo",
    author_email="andrea.grillo96@live.com",
    description="A python package to interact with Medium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andregri/pymedium",
    project_urls={
        "Bug Tracker": "https://github.com/andregri/pymedium/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)