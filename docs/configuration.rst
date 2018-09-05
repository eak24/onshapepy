.. _configuration:

OnshapePy Configuration
=============================
OnshapePy supports two ways to specify a configuration:

1. (Recommended) A **configuration file** placed within the user's home. It must be named ".onshapepy". It uses YAML syntax.
2. Manually **configured within Python**. As long as this runs first, it will configure the session and ignore the configuration file.

Both methods support the same configuration keys and values. For a complete list of configuration options, go to :ref:`configuration_options`.


Configuration From a File
--------------------------

.. code-block:: yaml

    creds:
        access_key: *******YOUR API KEY*******
        secret_key: *******YOUR API SECRET****
    logging: True

Configuration From Python
--------------------------

.. code-block:: python

    from onshapepy.client import Client
    configuration = {"creds" :{
                            "access_key" : "*******YOUR API KEY*******",
                            "secret_key" : "*******YOUR API SECRET****"}}
    Client(configuration)


.. _configuration_options:

Configuration Options
---------------------

creds: dict
    a dictionary containing access_key and secret_key keys pointing to the user's access key and secret key from OnShape.
