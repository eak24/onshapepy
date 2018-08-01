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

{
    "https://cad.onshape.com": {
        "access_key": "*******YOUR API KEY*******",
        "secret_key": "*******YOUR API SECRET****"
    }
}
Quick demo:
-----------
.. todo::
   finish this section!

.. code-block::python





.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
