from configobj import ConfigObj
from validate import Validator, ValidateError
import os
from platform_utils import paths

def load_config(config_path, confspec_path, ):
 fullpath = os.path.join(paths.app_data_path(app_name), config_path)
 config = ConfigObj(infile=fullpath, configspec=configspec_path, create_empty=True, stringify=True)
 validator = Validator()
 validated = config.validate(validator, copy=True)
 if validated:
  config.write()
  return config
