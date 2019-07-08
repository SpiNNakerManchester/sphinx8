from setuptools import setup
try:
    from collections.abc import defaultdict
except ImportError:
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
    install_requires=[
        'SpiNNUtilities >= 1!4.0.1, < 1!5.0.0',
        'SpiNNStorageHandlers >= 1!4.0.1, < 1!5.0.0',
        'SpiNNMachine >= 1!4.0.1, < 1!5.0.0',
        'SpiNNMan >= 1!4.0.1, < 1!5.0.0',
        'SpiNNaker_PACMAN >= 1!4.0.1, < 1!5.0.0',
        'SpiNNaker_DataSpecification >= 1!4.0.1, < 1!5.0.0',
        'spalloc >= 1.0.1, < 2.0.0',
        'SpiNNFrontEndCommon >= 1!4.0.1, < 1!5.0.0',
        'sPyNNaker >= 1!4.0.1, < 1!5.0.0',
        'sPyNNaker8 >= 1!4.0.1, < 1!5.0.0',
        'quantities >= 0.12.1',
        'pynn >= 0.9.1, < 0.10.0 ',
        'neo >= 0.5.2, < 0.7.0'],
    maintainer="SpiNNakerTeam",
    maintainer_email="spinnakerusers@googlegroups.com"
)
