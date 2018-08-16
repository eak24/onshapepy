Welcome to onshapepy's documentation!
=============================================

OnShapePy gives you the ability to control OnShape configurable parts with Python, effectively unlocking the vast
scientific libraries to OnShape parts.

Quick demo:
-----------
.. raw:: html

    <iframe width="700" height="460" src="https://www.youtube.com/embed/TkA6F1ZhfWU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

See how to connect to a PartStudio and adjust parameters from python!


Straight to the code:

.. code-block:: Python

   from onshapepy.play import *

    # Put in your access and secret keys
    configuration = {'creds':{'access_key': 'MY ACCESS KEY', 'secret_key': "MY SECRET KEY"}}
    Client(configuration)

    # Put in your partstudio URL. Here's an example with a cube
    my_cube = Part("https://cad.onshape.com/documents/2d47b6abec9d1de1d2538372/w/39e483948767f72c97d2792f/e/0639ea3c439aa0947744d29a")

    # Access part parameters
    my_cube.params

    # Set part parameters. Here I set L to 100 millimeters and has_fillet to false.
    my_cube.params = {'L': 150*u.mm, 'has_fillet': False}

    # Access measurements defined within the OnShape "Measure" FeatureScript defined here: https://cad.onshape.com/documents/379f3f7b8ae77b02b702a487/w/0ad420b3718d5a2b6f6d712f/e/2e4fe1496c0fa6c042b89a73
    my_cube.measurements

Authentication & Configuration
--------------------------------
To give OnShape access to your account, you'll need to specify credentials as shown in :ref:`OnShapePy Configuration <configuration_file>`.


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
