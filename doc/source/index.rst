SpiNNaker Manchester (PyNN 0.9) and GFE
=======================================
These pages document the python code for the Spinnaker Projectwhich can be found on github_.

This includes sPyNNaker 6, an implementation of PyNN_ 0.9 for the
SpiNNaker_ platform,  It is an implementation of
a toolkit for creating simulations of spiking neural networks. sPyNNaker is
particularly noted for being able to run very large simulations and in
real-time; it is possible to interface external hardware directly to a
SpiNNaker system.

The SpiNNakerGraphFrontEnd which is optimised for non-neural simulations.
(Hybrid neural/non-neural simulations are also possible; contact the team if
you are interested.)

.. _PyNN: https://neuralensemble.org/PyNN/
.. _SpiNNaker: http://apt.cs.manchester.ac.uk/projects/SpiNNaker/
.. _github: https://github.com/SpiNNakerManchester

SpiNNUtils
----------
This provides basic utility functions and classes to other parts of SpiNNaker's
tooling. Nothing in here knows anything about SpiNNaker functionality.

.. toctree::
   :maxdepth: 3

   spinn_utilities_index

SpiNNUtils_github_

SpiNNUtils_individual_docs_

.. _SpiNNUtils_github: https://github.com/SpiNNakerManchester/SpiNNUtils
.. _SpiNNUtils_individual_docs: https://spinnutils.readthedocs.io/en/7.1.0

SpiNNMachine
------------
This package is used to provide a Python representation of a SpiNNaker machine.
This contains the basic model of SpiNNaker hardware, as required by the other
packages described below.

.. toctree::
   :maxdepth: 3

   spinn_machine_index

SpiNNMachine_github_

SpiNNMachine_individual_docs_

.. _SpiNNMachine_github: https://github.com/SpiNNakerManchester/SpiNNMachine
.. _SpiNNMachine_individual_docs: https://spinnmachine.readthedocs.io/en/7.1.0

PACMAN
------
This package provides utilities for partitioning, placing and routing a
graph-based application on a SpiNNaker machine.

.. toctree::
   :maxdepth: 3

   pacman_index

PACMAN_github_

PACMAN_individual_docs_

.. _PACMAN_github: https://github.com/SpiNNakerManchester/PACMAN
.. _PACMAN_individual_docs: https://pacman.readthedocs.io/en/7.1.0

SpiNNMan
--------
This package provides a transceiver for communicating with a SpiNNaker machine.

.. toctree::
   :maxdepth: 3

   spinnman_index

SpiNNMan_github_

SpiNNMan_individual_docs_

.. _SpiNNMan_github: https://github.com/SpiNNakerManchester/SpiNNMan
.. _SpiNNMan_individual_docs: https://spinnman.readthedocs.io/en/7.1.0

SpiNNFrontEndCommon
-------------------
This package provides functionality which are common to all front ends that
translate application level programs into executables which run on a SpiNNaker
machine.

.. toctree::
   :maxdepth: 3

   spinn_front_end_common_index

SpiNNFrontEndCommon_github_

SpiNNFrontEndCommon_individual_docs_

.. _SpiNNFrontEndCommon_github: https://github.com/SpiNNakerManchester/SpiNNFrontEndCommon
.. _SpiNNFrontEndCommon_individual_docs: https://spinnfrontendcommon.readthedocs.io/en/7.1.0

sPyNNaker
---------
This package provides a PyNN 0.9 implementation for SpiNNaker.

.. toctree::
   :maxdepth: 3

   spynnaker_index

sPyNNaker_github_

sPyNNaker_individual_docs_

.. _sPyNNaker_github: https://github.com/SpiNNakerManchester/sPyNNaker
.. _sPyNNaker_individual_docs: https://spynnaker.readthedocs.io/en/7.1.0

SpiNNakerGraphFrontEnd
----------------------
This package provides a Graph Front End implementation for SpiNNaker.

.. toctree::
   :maxdepth: 3

   spinnaker_graph_front_end_index

SpiNNakerGraphFrontEnd_github_

SpiNNakerGraphFrontEnd_individual_docs_

.. _SpiNNakerGraphFrontEnd_github: https://github.com/SpiNNakerManchester/SpiNNakerGraphFrontEnd
.. _SpiNNakerGraphFrontEnd_individual_docs: https://spinnakergraphfrontend.readthedocs.io/en/7.1.0

spalloc
-------
Spalloc is a Python client library and set of command-line programs for
requesting SpiNNaker machines from a spalloc server.

The ``spalloc`` module uses a different documentation style so is not included
here.

Their documentation can be found at: spalloc_readthedocs_

spalloc_github_

.. _spalloc_github: https://github.com/SpiNNakerManchester/spalloc
.. _spalloc_readthedocs: http://spalloc.readthedocs.io/en/7.1.0

spalloc_server
--------------
A SpiNNaker machine management application which manages the partitioning and
allocation of large SpiNNaker machines into smaller fragments for many
simultaneous users.

The ``spalloc_server`` module uses a different documentation style so is not
included here.

Their documentation can be found at: spalloc_server_readthedocs_

spalloc_server_github_

.. _spalloc_server_github: https://github.com/SpiNNakerManchester/spalloc_server
.. _spalloc_server_readthedocs: http://spalloc-server.readthedocs.io/en/7.1.0

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
