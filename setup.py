from setuptools import setup, find_packages

setup(
    name="crispy-journey",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    author="Sonny Ethan Quinn",
    description="A fully automated journey",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)