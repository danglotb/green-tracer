import setuptools

setuptools.setup(
    name="green_tracer",
    version="0.0.1",
    author="Benjamin Danglot",
    author_email="benjamin.danglot@davidson.fr",
    description="Module to make trace of the execution",
    #url="<https://github.com/authorname/templatepackage>",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
