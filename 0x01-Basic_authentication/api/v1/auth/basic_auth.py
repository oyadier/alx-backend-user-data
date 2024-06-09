#!/usr/bin/env python3
"""Create a basic authentication subclass
"""


from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """A subclass of Auth class"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
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
