#!/usr/bin/env python3
"""An authentication Module"""
from flask import request
from typing import List, TypeVar
from models.user import User


class Auth:
    """An authentication class for all logins"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if the action requires an authentication"""
        if path is not None:
            if path.endswith("/"):
                path = path[:-1]
            path = path

        if (
            path is None
            or excluded_paths is None
            or excluded_paths == []
            or (len(excluded_paths) < 1)
            or path not in excluded_paths
        ):
            return True
        if "/api/v1/status/" in excluded_paths or path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """The request auth header"""
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar("User"):
        """Getting the current user"""
        return None
