# basic_config

Load a settings file, check it against a spec, fill in the defaults, and save it back, all in one call. It's a thin layer over [ConfigObj](https://configobj.readthedocs.io/) that every [Accessible Apps](https://getaccessibleapps.com) desktop app uses for its settings.

## Install

```bash
pip install git+https://github.com/accessibleapps/basic_config.git
```

Needs Python 3.8 or newer. The only dependency is `configobj`.

## Use it

Write a spec describing your settings:

```ini
# myapp.confspec
[general]
username = string(default="")
check_for_updates = boolean(default=True)
volume = integer(min=0, max=100, default=50)
```

Then load the user's file against it:

```python
from basic_config import load_configuration, ConfigLoadError

try:
    config = load_configuration("settings.ini", "myapp.confspec")
except ConfigLoadError:
    ...  # the file is broken or doesn't match the spec

config["general"]["volume"]  # 50 the first time, an int, not a string
config["general"]["volume"] = 80
config.write()
```

What `load_configuration(config_path, configspec_path=None, copy=True, ...)` does:

- Creates the file if it doesn't exist yet.
- Reads it as UTF-8 and validates it against the spec, converting values to the right types.
- With `copy=True` (the default), writes the defaults from the spec into the file, so users can see and edit every setting.
- Saves the file and returns the `ConfigObj`.
- Raises `ConfigLoadError` if the file can't be parsed or fails validation.

Any extra arguments go straight through to `ConfigObj`.

## License

MIT.
