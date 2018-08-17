Welcome to onshapepy's documentation!
=============================================

OnShapePy gives you the ability to control OnShape configurable parts with Python, effectively unlocking the vast
Python scientific libraries to OnShape parts.

Quick video demo
------------------

See how to connect to a PartStudio and adjust parameters from python below!

.. raw:: html

    <iframe src="https://player.vimeo.com/video/285497632" width="700" height="460" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

Straight to the code
---------------------

First specify your credentials in a file named: "~/.onshapepy". Get your access and secret keys `here <https://dev-portal.onshape.com/keys>`_.

.. code-block:: yaml

    creds:
        access_key: *******YOUR API KEY*******
        secret_key: *******YOUR API SECRET****

**Note: For more complex configurations, see :ref:`OnShapePy Configuration <configuration_file>`.**

Then follow along with the code below:

.. code-block:: Python

   from onshapepy.play import *

    # Put in your partstudio URL. Here's an example with a cube
    my_cube = Part("https://cad.onshape.com/documents/2d47b6abec9d1de1d2538372/w/39e483948767f72c97d2792f/e/0639ea3c439aa0947744d29a")

    # Access part parameters
    my_cube.params

    # Set part parameters. Here I set L to 100 millimeters and has_fillet to false.
    my_cube.params = {'L': 150*u.mm, 'has_fillet': False}

    # Access measurements defined within the OnShape "Measure" FeatureScript defined here: https://cad.onshape.com/documents/379f3f7b8ae77b02b702a487/w/0ad420b3718d5a2b6f6d712f/e/2e4fe1496c0fa6c042b89a73
    my_cube.measurements


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   onshapepy.rst
   configuration.rst




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
