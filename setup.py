from setuptools import setup
from collections import defaultdict


# Build a list of all project modules, as well as supplementary files
packages = []
package_data = defaultdict(list)

setup(
    name="spinnaker8manchester",
    description="Tools for simulating neural models generated using "
                "PyNN 0.9 on the SpiNNaker platform",
    author="University of Manchester",
    classifiers=[
        "Development Status :: 3 - Alpha",

        "Intended Audience :: Science/Research",

        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",

        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",

        "Topic :: Scientific/Engineering",
    ],
    keywords="spinnaker pynn0.8 neural simulation",
    url="https://github.com/SpiNNakerManchester/SpyNNaker8",
    packages=packages,
    package_data=package_data,
    install_requires=[],
    maintainer="SpiNNakerTeam",
    maintainer_email="spinnakerusers@googlegroups.com"
)
