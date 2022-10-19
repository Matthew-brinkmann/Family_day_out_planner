#!/usr/bin/python3
"""
module to handle all custom exceptions.
"""
import inspect
from models.system_logging import SystemLogging


class ApiCallNonResposive(Exception):
    """Exception raised when an API call returns non 200
    """

    def __init__(self,
                 message="API call did not return a 200 reponse"):
        """init for exception"""
        self.message = message
        self.methodRaisingThisException = inspect.stack()[2][4][0]
        SystemLogging.log_warning_error(self.methodRaisingThisException,
                                        self.message)
        super().__init__(self.message)

    def __str__(self):
        """str definition"""
        return (f'{self.message}')


class ReturnDtoEventListNotSet(Exception):
    """Exception raised event list set incorrectly
    """

    def __init__(self,
                 typeSetTo=None,
                 message="event list was sent a parameter it couldn't understand:"):
        """init for exception"""
        self.message = message
        self.typeSetTo = typeSetTo
        self.methodRaisingThisException = inspect.stack()[2][4][0]
        SystemLogging.log_warning_error(self.methodRaisingThisException,
                                        self.message,
                                        self.typeSetTo)
        super().__init__(self.message)

    def __str__(self):
        """str definition"""
        return (f'{self.message} {str(self.typeSetTo)}')


class ServerEnvironVariablesNotSet(Exception):
    """Exception raised when an API call returns non 200
    """

    def __init__(self,
                 typeSetTo="",
                 message="Server Configuration Error: No Variable:"):
        """init for exception"""
        self.message = message
        self.typeSetTo = typeSetTo
        self.methodRaisingThisException = inspect.stack()[2][4][0]
        SystemLogging.log_warning_error(self.methodRaisingThisException,
                                        self.message,
                                        self.typeSetTo)
        super().__init__(self.message)

    def __str__(self):
        """str definition"""
        return (f'{self.message} {str(self.typeSetTo)}')


class ApiReturnNoneResults(Exception):
    """Exception raised when an API call return 200 response but is empty"""

    def __init__(self,
                 message="No events results for this query"):
        """init for exception"""
        self.message = message
        self.methodRaisingThisException = inspect.stack()[2][4][0]
        SystemLogging.log_warning_error(self.methodRaisingThisException,
                                        self.message)
        super().__init__(self.message)

    def __str__(self):
        """str definition"""
        return (f'{self.message}')


class TestRequestDataIncorrectFormat(Exception):
    """Exception raised when the request on a test api is not correct format"""

    def __init__(self,
                 message="request Data does not contain correct information"):
        """init for exception"""
        self.message = message
        self.methodRaisingThisException = inspect.stack()[2][4][0]
        SystemLogging.log_warning_error(self.methodRaisingThisException,
                                        self.message)
        super().__init__(self.message)

    def __str__(self):
        """str definition"""
        return (f'{self.message}')
