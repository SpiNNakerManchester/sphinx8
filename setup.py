from setuptools import setup
from collections import defaultdict


# Build a list of all project modules, as well as supplementary files
packages = []
package_data = defaultdict(list)

setup(
    name="spinnakermanchester",
    description="Pythn documentation for the SpiNNaker platform",
    author="University of Manchester",
    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Science/Research",

        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",

        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",

        "Topic :: Scientific/Engineering",
    ],
    keywords="spinnaker pynn0.9 neural simulation",
    url="https://github.com/SpiNNakerManchester/sphinx8",
    packages=packages,
    package_data=package_data,
    install_requires=[],
    maintainer="SpiNNakerTeam",
    maintainer_email="spinnakerusers@googlegroups.com"
)
