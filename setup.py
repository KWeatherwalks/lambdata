import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-KevinWeatherwalks",
    version="0.0.2",
    author="Kevin Weatherwalks",
    author_email="kevin.weatherwalks@gmail.com",
    description="A data science package for Lambda School projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kweatherwalks/lambdata",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.8',
)
