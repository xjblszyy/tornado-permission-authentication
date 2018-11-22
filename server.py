from tornado import web, ioloop
from AuthAndPer.settings.dev import settings, database
from AuthAndPer.urls import urlpattern
from peewee_async import Manager


if __name__ == "__main__":
    app = web.Application(urlpattern, debug=True, **settings)
    app.listen(8889)

    objects = Manager(database)
    database.set_allow_sync(False)
    app.objects = objects

    ioloop.IOLoop.current().start()

