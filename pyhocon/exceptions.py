class ConfigException(Exception):

    def __init__(self, message, ex=None):
        super(ConfigException, self).__init__(message)
        self._exception = ex


class ConfigMissingException(ConfigException):
    pass


class ConfigSubstitutionException(ConfigException):
    pass


class ConfigWrongTypeException(ConfigException):
    pass


class ConfigBadValueException(ConfigException):
    pass