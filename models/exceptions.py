#!/usr/bin/python3
"""
module to handle all custom exceptions.
"""


class ApiCallNonResposive(Exception):
    """Exception raised when an API call returns non 200
    """

    def __init__(self,
                 message="API call did not return a 200 reponse"):
        """init for exception"""
        
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        """str definition"""
        return (f'{self.message}')


class ReturnDtoEventListNotSet(Exception):
    """Exception raised when an API call returns non 200
    """

    def __init__(self,
                 typeSetTo=None,
                 message="event list was sent a parameter it couldn't understand:"):
        """init for exception"""
        self.message = message
        self.typeSetTo = typeSetTo
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
        super().__init__(self.message)

    def __str__(self):
        """str definition"""
        return (f'{self.message} {str(self.typeSetTo)}')


class ApiReturnNoneResults(Exception):
    """Exception raised when an API call return None events list"""

    def __init__(self,
                 message="No events results for this query"):
        """init for exception"""
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        """str definition"""
        return (f'{self.message}')
