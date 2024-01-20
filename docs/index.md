# scratchclientImproved Documentation

This is the documentation for scratchclientImproved.

## Installation

Go to your terminal (not your python shell) and execute this command:
```bash
pip install scratchclientImproved
```

If this didn't work for whatever reason, open your python shell and run the following:
```python
import os; os.system("pip install scratchclientImproved")
```

scratchclientImproved requires Python 3.7; however, it will work for almost all use cases on Python 3.6.

## Get Started
```python
from scratchclientImproved import ScratchSession

session = ScratchSession("UwU", "--uwu--")

# post comments
session.get_user("Paddle2See").post_comment("OwO")

# lots of other stuff
print(session.get_project(450216269).get_comments()[0].content)
print(session.get_project(450216269).get_comments()[0].get_replies()[0].content)
print(session.get_studio(29251822).description)
```

## Cloud Connection
```python
from scratchclientImproved import ScratchSession

session = ScratchSession("griffpatch", "SecurePassword7")

connection = session.create_cloud_connection(450216269)

connection.set_cloud_variable("variable name", 5000)

@connection.on("set")
def on_set(variable):
    print(variable.name, variable.value)

print(connection.get_cloud_variable("other variable"))
```

See the examples for more code samples.

## CLI

scratchclientImproved has a command line interface for retrieving Scratch website data from the command line. Use `python3 -m scratchclientImproved help` to get started.