#!/usr/bin/env python3
""" class for authentication
"""
import re
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication
       class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """identifying routes don't need authentication"""
        if path is not None and excluded_paths is not None:
            for ex_path in map(lambda x: x.strip(), excluded_paths):
                sline = ''
                if ex_path[-1] == '*':
                    sline = '{}.*'.format(ex_path[0:-1])
                elif ex_path[-1] == '/':
                    sline = '{}/*'.format(ex_path[0:-1])
                else:
                    sline = '{}/*'.format(ex_path)
                if re.match(sline, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """auth header drwan from req"""
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """current user is recieved from req"""
        return None
