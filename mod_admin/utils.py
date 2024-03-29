from flask import session,abort
from http import HTTPStatus
from functools import wraps

def admin_view(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id') is None:
            abort(HTTPStatus.UNAUTHORIZED)
        if session.get('user_role',default=0) != 1 :
            abort(HTTPStatus.FORBIDDEN)
        return func(*args,**kwargs)
    return wrapper