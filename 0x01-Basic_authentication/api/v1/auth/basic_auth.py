#!/usr/bin/env python3
"""Create a basic authentication subclass
"""


from typing import TypeVar
from api.v1.auth.auth import Auth
import base64
from models.user import User


class BasicAuth(Auth):
    """A subclass of Auth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracting base64 authorization header for Auth hearder"""
        if (
            isinstance(authorization_header, str)
            and authorization_header is not None
            and authorization_header.startswith("Basic ")
        ):
            return authorization_header.split()[-1]

        return None

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Decode a base64 binary code for a string"""
        valid = None
        try:
            base64.b64decode(base64_authorization_header)
            valid = True
        except Exception:
            valid = False
        if (
            isinstance(base64_authorization_header, str)
            and base64_authorization_header is not None
            and valid
        ):
            decode = base64.b64decode(base64_authorization_header)
            return decode.decode("utf-8")

        return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """Extracting user credentials from the auth header"""
        if (
            isinstance(decoded_base64_authorization_header, str)
            and decoded_base64_authorization_header is not None
            and ":" in decoded_base64_authorization_header
        ):
            email, password = decoded_base64_authorization_header.rsplit(
                ":", maxsplit=1
            )
            return (email, password)

        return (None, None)

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar("User"):
        """Get user object based on the email and password from base64"""

        if type(user_email) is str and type(user_pwd) is str:
            try:
                user = User().search({"email": user_email})
                valid = user[0].is_valid_password(user_pwd)
            except Exception:
                return None
            if len(user) <= 0:
                return None
            if valid:
                return user[0]
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        '''Get the current user from the request'''
        super().current_user(request)
        auth = Auth()
        header = auth.authorization_header(request=request)
        extract = self.extract_base64_authorization_header(header)
        decode = self.decode_base64_authorization_header(extract)
        user_credential = self.extract_user_credentials(decode)
        return self.user_object_from_credentials(
            user_email=user_credential[0], user_pwd=user_credential[1]
        )
