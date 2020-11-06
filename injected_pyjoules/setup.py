import setuptools

setuptools.setup(
    name="injected_pyjoules",
    version="0.0.1",
    author="Benjamin Danglot",
    author_email="benjamin.danglot@davidson.fr",
    description="Module that inject pyJoules in a Python project",
    #url="<https://github.com/authorname/templatepackage>",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
