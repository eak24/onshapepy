Testing
=======

Running Tests
--------------

In order to be able to run tests, you must first have:

* onshapepy repo cloned to your machine
* pytest installed
* pipenv installed
* onshapepy configured

In short, you'll have to run the following commands:

.. code-block::
    git clone install https://github.com/AguaClara/onshapepy.git # Clone the repo
    cd onshapepy
    pip install pipenv # Install pipenv
    pipenv install --dev # Install dev and regular dependencies and make a virtual environment
    nano ~/.onshapepy # Now follow the instructions on how to configure onshapepy in the documentation
    pipenv shell  # Go into the onshapepy virtual environment
    pytest # Run all tests

That should run all the tests and all tests should have passed. To run additional tests, just navigate back to the onshape repo and run :code:`pytest`. You must have the virtual environment already activated with :code:`pipenv shell`. To exit the environment, run :code:`exit`.

Writing Tests
--------------

Tests are an integral part of development. They communicate usage, ensure against accidental regression, and encourage good coding practices. A library that isn't well tested is almost certain to become unmanageable. OnshapePy takes testing seriously. We pride ourselves on maintaining a coverage of greater than 80%. Please make sure to write tests before submitting a PR!

Because OnshapePy's main role is to work with the Onshape API, so must the tests. This means that a large number of the tests talk to the Onshape servers using your user credentials. Because of this, the OnshapePy tests "expect" a certain Onshape testing environment to be setup that the tests can be run against. To do this, we manage an `"OnshapePy Tests" document on Onshape. <https://cad.onshape.com/documents/2d47b6abec9d1de1d2538372/w/39e483948767f72c97d2792f/e/0639ea3c439aa0947744d29a>`_. This document contains various PartStudios against which code can be tested. To ensure "OnshapePy Tests" is always in a known state, we create versions of the document that correspond to the particular release of OnshapePy. These versions of the document are then copied and then tested against. Through this technique, we can let anyone with Onshape credentials run tests against OnshapePy.

