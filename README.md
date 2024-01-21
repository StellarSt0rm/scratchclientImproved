# scratchclientImproved
Improved version of the Scratch API wrapper by CubeyTheCube.
I will mainly fix errors.

Due to migrating the forked repo to a new repo because i had some issues, the `Fix #1` release was lost, it's still available via accessing the tag, or via installing version 1.0 (`pip install scratchclientImproved==1.0`)

## Installation

Go to your terminal (Not your Python shell) and execute this command:
```bash
pip install scratchclientImproved
```

If this didn't work for whatever reason, open your Python shell and run the following:
```python
import os; os.system("pip install scratchclientImproved")
```

## Example Usage

### Basic Usage
```python
from scratchclientImproved import ScratchSession

session = ScratchSession("UwU", "--uwu--")

# Post comments
session.get_user("Begula").post_comment("OwO")

# Lots of other stuff!
print(session.get_project(450216269).get_comments()[0].content)
print(session.get_project(450216269).get_comments()[0].get_replies()[0].content)
print(session.get_studio(29251822).description)
```
### Cloud Connection
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

Documentation is available at <https://StellarSt0rm.github.io/scratchclientImproved>.

All bugs should be reported to the [Github repository](https://github.com/StellarSt0rm/scratchclientImproved/issues).
