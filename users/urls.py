from tornado.web import url
from users.handler import UserInfoHandler, OnlyAdminHandler, LoginHandler


urlpattern = (
    url("/login/", LoginHandler),
    url("/users/([0-9]+)/", UserInfoHandler),
    url("/users/admin/", OnlyAdminHandler),
)
