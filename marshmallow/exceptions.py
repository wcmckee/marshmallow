# -*- coding: utf-8 -*-
'''Exception classes for marshmallow-related errors.'''

class MarshmallowError(Exception):
    '''Base class for all marshmallow-related errors.'''
    pass


class MarshallingError(MarshmallowError):
    """Raised in case of a marshalling error.
    """

    def __init__(self, underlying_exception):
        # just put the contextual representation of the error to hint on what
        # went wrong without exposing internals
        super(MarshallingError, self).__init__(str(underlying_exception))
