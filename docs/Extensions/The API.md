# The API

 The Extension API
 
## The Extension Loader

The loader is a simple script that loads extensions one by one from the ext_dir as specified in the config.toml file.
The code looks like this

```py
def load_extension(path, name):
    sys.path.append(path)
    try:
        return importlib.import_module(name, package=path)
    except ImportError:
        return None
```

Hence, any extension that has the same name as other extensions the user already has installed or is part of the standard library, can cause conflicts. It is recommended not to name them so.

Every extensions must have a Preset class as shown below with an initialization function that initializes the name variable. The data of this variable is used as the name displayed as the choices in the CLI.

```py
class Preset:
    def __init__(self):
        self.name = "Option Name"
```

The class must also have an on_select method which is called if the preset is selected. It must also accept a repository and a name as parameters.

```py
class Preset:
    def __init__(self):
        self.name = "Option Name"
        
    def on_select(self, repository, name):
        # generate project
```