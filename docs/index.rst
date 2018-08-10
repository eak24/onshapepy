.. aguaclara.onshape documentation master file, created by
   sphinx-quickstart on Wed Aug  1 12:17:49 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to onshapepy's documentation!
=============================================

This is an unofficial fork of the `OnShape APIkey application. <https://github.com/onshape-public/apikey>`_

This is a connector between python and OnShape. It is used to send data to configurable partStudios. Through this connector, you can control FeatureScript features, import configured parts, download configurations all with Python.

At AguaClara, we use this connector to upload parameters of our hydraulic design that are calculated in Python.

API Key
-------
To give OnShape access to your account, you'll need to access your API key here and put it into a creds.json file that looks like this:

.. code-block:: JSON

   {
       "https://cad.onshape.com": {
           "access_key": "*******YOUR API KEY*******",
           "secret_key": "*******YOUR API SECRET****"
       }
   }


Quick demo:
-----------

Copy a document and adjust cube parameters from python!

.. code-block:: Python

   import onshape
   from onshape import Part
   from onshape import Client

   # load the API key
   c = Client(creds = "file path to creds")

   # load the client for this part
   my_cube = Part("cube","cube","cube")
   my_pyramid = Assembly(did, wid, eid)


   # update various parameters
   my_cube.params["h"]["value"] = 5 * 20
   my_cube.params["h"]["units"] = "inch"

   # Insert into the assembly
   my_pyramid.insert(my_cube, c)

Make Reusable Python-driven Parts:
-----------------------------------

Make a block that can be used multiple times:

.. code-block:: Python

   import onshapepy
   from onshapepy import Part
   from onshapepy import Client

   class Cube():

      def __init__(self):
         self.onshape = Part("de0b979bd2526029daafe060","8043876c6f38336511d43098","7a6d9c6a8583cdf983aee11e")

   # load the API key
   c = Client()

   my_pyramid = Assembly("8ec353ba00f37f447b5a61f5", "04c36c786829759832bd3d1a", "6f1f9c485ff1e639f4db63c0")

   # update various parameters
   my_cube.params["h"]["value"] = 5 * 20
   my_cube.params["h"]["units"] = "inch"

   # Insert into the assembly
   my_pyramid.insert(my_cube, c)


.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
