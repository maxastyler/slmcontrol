import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    "numpy>=1.18",
    "pyqtgraph>=0.10"
]
    
setuptools.setup(
    name="slmcontrol-maxastyler", # Replace with your own username
    version="0.0.1",
    author="Max Tyler",
    author_email="maxastyler@gmail.com",
    description="A program for controlling SLMs",
    install_requires = requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maxastyler/slmcontrol",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Scientific/Engineering",
    ],
    python_requires='>=3.6',
    test_suite = "tests",
)
