# from flask_jwt_extended import jwt_required, get_jwt_identity
# from flask_restx import fields
# from enum import Enum
# from functools import wraps


# > here you set authority for endpoints
# register_user_authority = [Role.ADMIN.value]
#
# register_project_authority = [Role.ADMIN.value, Role.MOD.value, Role.COM.value]
#
# project_authority = [Role.ADMIN.value, Role.MOD.value]
#
# user_authority = [Role.ADMIN]


# > usually you have common responses
# class Response(Enum):
#     BadRequest = {
#         'message': 'Bad request'
#     }, 400
#     Forbidden = {
#         'message': 'You do not have permission'
#     }, 403
#     ClientNotFound = {
#         'message': 'Client not found'
#     }, 404
#     ProjectNotFound = {
#         'message': 'Project not found'
#     }, 404


# > the authorization function
# def authorize_user(roles):
#     def decorator(func):
#         @jwt_required()
#         def wrapper(*args, **kwargs):
#             current_user = get_jwt_identity()
#             user_role = current_user.get('role')
#             if user_role not in roles:
#                 return Response.Forbidden.value
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator

