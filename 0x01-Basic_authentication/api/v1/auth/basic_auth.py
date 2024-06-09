#!/usr/bin/env python3
"""Create a basic authentication subclass
"""


from api.v1.auth.auth import Auth
import base64


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
        valid = None
        try:
            base64.b64decode(base64_authorization_header)
            valid = True
        except TypeError:
            pass
        if (
            isinstance(base64_authorization_header, str)
            and base64_authorization_header is not None
            and valid
        ):
            decode = base64.b64decode(base64_authorization_header)
            return decode.decode("utf-8")

        return None
