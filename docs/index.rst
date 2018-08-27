Welcome to the OnshapePy Documentation!
=============================================

OnshapePy gives you the ability to control Onshape configurable parts with Python, effectively unlocking the vast
Python scientific libraries to Onshape parts.

Quick video demo
------------------

.. raw:: html

    <div class="vid-container">
        <iframe width="700" height="394" src="https://www.youtube.com/embed/tpqhwz4zX9s" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>

Straight to the code
---------------------

First specify your credentials in a file named: "~/.onshapepy". Get your access and secret keys `here <https://dev-portal.onshape.com/keys>`_.

.. code-block:: yaml

    creds:
        access_key: *******YOUR API KEY*******
        secret_key: *******YOUR API SECRET****

.. important::
    Note: For more complex configurations, see :ref:`configuration`.

Then follow along with the Python code below:

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

   configuration.rst
   testing.rst
   onshapepy.rst




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
