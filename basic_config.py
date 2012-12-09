from configobj import ConfigObj
from validate import Validator, ValidateError
import os

def load_configuration(config_path, configspec_path, *args, **kwargs):
 spec = ConfigObj(configspec_path, encoding='UTF8', list_values=False, _inspec=True)
 config = ConfigObj(infile=config_path, configspec=spec, create_empty=True, encoding='UTF8', *args, **kwargs)
 validator = Validator()
 validated = config.validate(validator, copy=True)
 if validated == True:
  config.write()
  return config