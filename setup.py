import setuptools


setuptools.setup(
    name="gilded_rose",
    packages=setuptools.find_packages(),
    extras_require={
        "test": [
            "pytest",
            "flake8",
            "isort",
            "black",
        ],
    },
)
