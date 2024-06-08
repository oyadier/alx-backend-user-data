#!/usr/bin/env python3
"""An authentication Module"""
from flask import request
from typing import (List, TypeVar)
from models.user import User


class Auth():
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
        '''Getting the current user
        '''
        return None
