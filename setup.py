import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="todot-python",
    version="0.2.0",
    author="Wasi Master",
    author_email="arianmollik323@gmail.com",
    description="A powerful tool to parse TODOs/FIXMEs etc. from source files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://wasi-master.github.io/todot/",
    project_urls={
        "Bug Tracker"  : "https://github.com/wasi-master/todot/issues",
        "Source"       : "https://github.com/wasi-master/todot",
        "Documentation": "https://wasi-master.github.io/todot/",
        "Say Thanks"   : "https://saythanks.io/to/arianmollik323@gmail.com",
    },
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Topic :: Terminals",
    ],
    keywords="todo todot todoteee todofind todofinder findtodo treetodo teasot leasot",
    packages=["todot"],
    python_requires=">=3.6",
    extras_require={"rich": ["rich"]},
    entry_points={
        "console_scripts": ["todot=todot.__main__:run"],
    },
)
