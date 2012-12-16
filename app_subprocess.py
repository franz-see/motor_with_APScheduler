## Based on http://emptysquare.net/motor/pymongo/api/motor/tutorial.html

import apscheduler.scheduler
import motor
import tornado.httpserver
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])
server = tornado.httpserver.HTTPServer(application)
server.bind(8888)

server.start(0)

db = motor.MotorConnection().open_sync()['motor_with_apscheduler']
db.colors.remove()
db.colors.insert
db.colors.insert([{'name':'red'}, {'name':'green'}, {'name':'blue'}])

application.db = db

@tornado.gen.engine
def job_function():
    cursor = db.colors.find()
    colors = yield motor.Op(cursor.to_list)
    print colors

scheduler = apscheduler.scheduler.Scheduler()
scheduler.add_interval_job(job_function, seconds=5)

if __name__ == "__main__":
    #application.listen(8888)
    scheduler.start()
    tornado.ioloop.IOLoop.instance().start()

