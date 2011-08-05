from setuptools import setup, find_packages

__version__ = 0.11
__doc__ = """Standard configuration setup for Q-Continuum packages"""

setup(
 name = "basic_config",
 version = __version__,
 description = __doc__,
 py_modules = ['config',],
 classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'License :: OSI Approved :: MIT License',
  'Topic :: Software Development :: Libraries',
 ],
)
