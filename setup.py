from distutils.core import setup

__version__ = "0.3"
__doc__ = """Standard configuration setup for Q-Continuum packages"""

setup(
 name = "basic_config",
 version = __version__,
 description = __doc__,
 py_modules = ["basic_config"],
 install_requires = [
  'configobj',
 ],
 classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'License :: OSI Approved :: MIT License',
  'Topic :: Software Development :: Libraries',
 ],
)
