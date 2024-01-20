# scratchclientImproved
Improved Version Of The Scratch API Wrapper By CubeyTheCube.
I will mainly fix errors.

## Installation

Go Yo Your Terminal (Not Your Python Shell) And Execute This Command:
```bash
pip install scratchclientImproved
```

If this didn't work for whatever reason, open your python shell and run the following:
```python
import os; os.system("pip install scratchclientImproved")
```

## Example Usage

### Basic Usage
```python
from scratchclientImproved import ScratchSession

session = ScratchSession("UwU", "--uwu--")

# Post Comments
session.get_user("Paddle2See").post_comment("OwO")

# Lots Of Other Stuff
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

All bugs should be reported to the [github repository](https://github.com/StellarSt0rm/scratchclientImproved/issues). If you need help or guideance, check out the [forum topic](https://scratch.mit.edu/discuss/topic/506810).
