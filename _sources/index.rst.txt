Welcome to onshapepy's documentation!
=============================================

OnShapePy gives you the ability to control OnShape configurable parts with Python, effectively unlocking the vast
scientific libraries to OnShape parts.

Quick demo:
-----------

Copy a document and adjust cube parameters from python!

.. code-block:: Python

   from onshape import Part



   # load the client for this part
   my_cube = Part("https://cad.onshape.com/documents/2d47b6abec9d1de1d2538372/w/39e483948767f72c97d2792f/e/0639ea3c439aa0947744d29a")
   my_cube.

For a longer demo, `please see this notebook. <https://hub.mybinder.org/user/aguaclara-onshapepy-lvzgpurw/notebooks/docs/Example%20Notebook.ipynb>`_

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
