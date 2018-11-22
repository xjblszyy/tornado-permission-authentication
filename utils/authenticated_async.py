import functools
import jwt
from AuthAndPer.utils import decode_jwt
from users.models import User
from AuthAndPer.settings.base import settings


def authenticated(method):
    @functools.wraps(method)
    async def wrapper(self, *args, **kwargs):
        authorization = self.request.headers.get("Authorization", None)
        if authorization is None:
            self.set_status(401)
            self.finish({"msg": "用户未登陆"})
        if not authorization.startswith(settings["JWT_AUTH_HEADER_PREFIX"]):
            self.set_status(401)
            self.finish({"msg": "token格式错误"})
        else:
            try:
                authorization = authorization.split(" ")[-1]
                user_info_data = decode_jwt(authorization, self.settings)
                id = user_info_data.get("id")
                try:
                    user = await self.application.objects.get(User, id=int(id))
                    self._current_user = user
                    await method(self, *args, **kwargs)
                except User.DoesNotExist as e:
                    self.set_status(400)
                    self.finish({"msg": "用户不存在"})
            except jwt.ExpiredSignatureError as e:
                self.set_status(400)
                self.finish({"msg": "token过期，请重新登陆"})
        return method(self, *args, **kwargs)
    return wrapper
