from configobj import ConfigObj
from validate import Validator, ValidateError
import os
from platform_utils import paths

def load_configuration(config_path, confspec_path):
 config = ConfigObj(infile=config_path, configspec=configspec_path, create_empty=True, stringify=True)
 validator = Validator()
 validated = config.validate(validator, copy=True)
 if validated:
  config.write()
  return config
