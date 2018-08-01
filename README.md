# Python 3 API Key Sample [![Build Status](https://travis-ci.org/AguaClara/onshape.svg?branch=master)](https://travis-ci.org/AguaClara/onshape)
[![codecov](https://codecov.io/gh/AguaClara/onshape/branch/master/graph/badge.svg)](https://codecov.io/gh/AguaClara/onshape)

Simple demonstration of getting a key and structuring API calls.

---

### Local Setup

Install the dependencies:

* Python 3 (3.5 +)

Then, from this folder, install the pip package from the local source (this will install the dependencies automatically):

```sh
pip install .
```
**Note:** if you are on mac or getting permission errors, try including the `--user` key.

### Running the App

Create a `creds.json` file in this directory, with the following format:

```json
{
    "https://cad.onshape.com": {
        "access_key": "ACCESS KEY",
        "secret_key": "SECRET KEY"
    }
}
```

Just replace "ACCESS KEY" and "SECRET KEY" with the values you got from the
developer portal. To test on other stacks, you'll create another object in the file,
with credentials for that specific stack.

To run the basic application:

```sh
$ python app.py
```

To print an STL representation of a given part studio to the console:

```sh
$ python exportstl.py
```

If you want to specify a different stack to test on, simply go into the file you're running and
change the `stack` parameter on this line:

```py
c = Client(stack='NEW STACK HERE')
```

### Working with API Keys

For general information on our API keys and how they work, read this
[document](https://github.com/onshape/apikey/blob/master/README.md). For general
API support, please reach out to us at
[api-support@onshape.com](mailto:api-support@onshape.com).