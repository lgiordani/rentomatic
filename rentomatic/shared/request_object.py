class InvalidRequestObject(object):

    def __init__(self):
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({'parameter': parameter, 'message': message})

    def has_errors(self):
        return len(self.errors) > 0

    def __nonzero__(self):
        return False

    __bool__ = __nonzero__


class ValidRequestObject(object):

    @classmethod
    def from_dict(cls, adict):
        raise NotImplementedError

    def __nonzero__(self):
        return True

    __bool__ = __nonzero__
