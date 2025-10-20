
from configobj import ConfigObj, ParseError
from validate import Validator


class ConfigLoadError(Exception):
    pass


def load_configuration(config_path, configspec_path=None, copy=True, *args, **kwargs):
    spec = ConfigObj(configspec_path, encoding="UTF8", list_values=False, _inspec=True)
    try:
        config = ConfigObj(*args, infile=config_path, configspec=spec, create_empty=True, encoding="UTF8", **kwargs)
    except ParseError:
        raise ConfigLoadError(f"Unable to load {config_path!r}") from None
    validator = Validator()
    validated = config.validate(validator, copy=copy)
    if validated is True:
        config.write()
        return config
    raise ConfigLoadError
