from flask import request
from typing import List, TypeVar, Generic
"""An authentication Module"""


class Auth:
    '''An authentication class for all logins'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''Checks if the action requires an authentication
        '''
        return False

    def authorization_header(self, request=None) -> str:
        '''The request auth header
        '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''Request for the current'''
        return None
