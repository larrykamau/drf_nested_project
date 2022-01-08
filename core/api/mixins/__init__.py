__title__ = 'writable nested'
__version__ = '0.8.4'
__author__ = 'lawrencekamau5@gmail.com'

# Version synonym
VERSION = __version__



from .nested_formdata import (
    UtilityMixin
)
from .writable_nested import (
    NestedUpdateMixin,
    NestedCreateMixin,
    UniqueFieldsMixin
)
