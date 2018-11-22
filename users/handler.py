import json
import random
import datetime

from AuthAndPer.handler import BaseHandler
from .models import User
from AuthAndPer.utils import encode_jwt, decode_jwt
from utils.authenticated_async import authenticated
from utils.permission_async import permissioned


class LoginHandler(BaseHandler):
    async def post(self, *args, **kwargs):
        re_data = {}
        payload = {"id": "1", 'mobile': "111111", "exp": datetime.datetime.utcnow()}
        token = encode_jwt(payload, self.settings)
        re_data["code"] = 200
        re_data["token"] = token.decode("utf8")
        self.finish(re_data)


class OnlyAdminHandler(BaseHandler):
    @permissioned
    async def post(self, *args, **kwargs):
        re_data = {"code": 200, "msg": "success"}
        self.finish(re_data)


class UserInfoHandler(BaseHandler):
    @authenticated
    async def post(self, *args, **kwargs):
        re_data = {"code": 200, "msg": "success"}
        self.finish(re_data)
