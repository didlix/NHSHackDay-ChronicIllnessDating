from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

from django12factor import factorise
globals().update(factorise())
