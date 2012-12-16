motor_with_APScheduler
======================

Example of running Tornado + Motor + APScheduler

However, I'm getting something like this:

    ERROR:root:Uncaught exception, closing connection.
    Traceback (most recent call last):
      File "/myvirtualenv/lib/python2.7/site-packages/tornado/iostream.py", line 305, in wrapper
        callback(*args)
      File "/myvirtualenv/lib/python2.7/site-packages/tornado/stack_context.py", line 231, in wrapped
        callback(*args, **kwargs)
      File "/myvirtualenv/lib/python2.7/site-packages/tornado/stack_context.py", line 161, in __exit__
        return self.exception_handler(type, value, traceback)
      File "/myvirtualenv/lib/python2.7/site-packages/tornado/gen.py", line 114, in handle_exception
        return runner.handle_exception(typ, value, tb)
      File "/myvirtualenv/lib/python2.7/site-packages/tornado/gen.py", line 388, in handle_exception
        self.run()
      File "/myvirtualenv/lib/python2.7/site-packages/tornado/gen.py", line 343, in run
        yielded = self.gen.throw(*exc_info)
      File "app.py", line 24, in job_function
        colors = yield motor.Op(cursor.to_list)
      File "/myvirtualenv/lib/python2.7/site-packages/tornado/stack_context.py", line 231, in wrapped
        callback(*args, **kwargs)
      File "/myvirtualenv/lib/python2.7/site-packages/motor/__init__.py", line 113, in callback
        child_gr.switch(result)
    error: cannot switch to a different thread
    ERROR:root:Exception in callback <tornado.stack_context._StackContextWrapper object at 0x1063ca998>
    Traceback (most recent call last):
      File "/myvirtualenv/lib/python2.7/site-packages/tornado/ioloop.py", line 421, in _run_callback
        callback()
      File "/myvirtualenv/lib/python2.7/site-packages/tornado/iostream.py", line 305, in wrapper
        callback(*args)
      File "/myvirtualenv/lib/python2.7/site-packages/tornado/stack_context.py", line 231, in wrapped
        callback(*args, **kwargs)
      File "/myvirtualenv/lib/python2.7/site-packages/tornado/stack_context.py", line 161, in __exit__
        return self.exception_handler(type, value, traceback)
      File "/myvirtualenv/lib/python2.7/site-packages/tornado/gen.py", line 114, in handle_exception
        return runner.handle_exception(typ, value, tb)
      File "/myvirtualenv/lib/python2.7/site-packages/tornado/gen.py", line 388, in handle_exception
        self.run()
      File "/myvirtualenv/lib/python2.7/site-packages/tornado/gen.py", line 343, in run
        yielded = self.gen.throw(*exc_info)
      File "app.py", line 24, in job_function
        colors = yield motor.Op(cursor.to_list)
      File "/myvirtualenv/lib/python2.7/site-packages/tornado/stack_context.py", line 231, in wrapped
        callback(*args, **kwargs)
      File "/myvirtualenv/lib/python2.7/site-packages/motor/__init__.py", line 113, in callback
        child_gr.switch(result)
    error: cannot switch to a different thread
