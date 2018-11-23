"""*Zgoubidoo: a modern Python 3 interface to the Zgoubi particle tracking code.*

Zgoubidoo is a Python 3 interface for Zgoubi. Zgoubido is intended to follow a modern Python design and aims at being
easy to use. Interactive use with iPython or Jupyter Notebook is supported and encouraged.

Zgoubi is a ray-tracing (tracking) code for beam dynamics simulations. Many magnetic and electric elements are
supported. It is maintained by François Méot: `Zgoubi SourceForge repository`_.

.. _Zgoubi SourceForge repository: https://sourceforge.net/projects/zgoubi/

Publications
------------

- test

"""
__version__ = "2018.1"

# Manipulation of physical quantities (with units, etc.)
# https://pint.readthedocs.io/en/latest/
from pint import UnitRegistry
ureg = UnitRegistry()
_Q = ureg.Quantity
ureg.define('electronvolt = e * volt = eV')
ureg.define('electronvolt_per_c = eV / c = eV_c')
ureg.define('electronvolt_per_c2 = eV / c**2 = eV_c2')
ureg.define('[momentum] = [ev] / [c]')
ureg.define('[energy] = [ev] / [c]**2 ')

from . import commands
from . import physics
from . import vis
from . import twiss
from .input import Input, InputValidator, ZgoubiInputException
from .output import read_fai_file, read_plt_file, read_matrix_file
from .zgoubi import Zgoubi, ZgoubiRun, ZgoubiException
from .survey import survey
from .frame import Frame, ZgoubidooFrameException
from .beam import Beam, ZgoubidooBeamException
