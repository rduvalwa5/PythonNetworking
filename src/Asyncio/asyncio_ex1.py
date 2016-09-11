'''
https://pymotw.com/3/asyncio/
'''
import asyncio

@asyncio.coroutine
def bug():
    raise Exception("not consumed")

loop = asyncio.get_event_loop()
asyncio.ensure_future(bug())
loop.run_forever()
loop.close()


'''
    run as unittest
    Task exception was never retrieved
    future: <Task finished coro=<coro() done, defined at asyncio/coroutines.py:139> exception=Exception('not consumed',)>
    Traceback (most recent call last):
    File "asyncio/tasks.py", line 237, in _step
    result = next(coro)
    File "asyncio/coroutines.py", line 141, in coro
    res = func(*args, **kw)
    File "test.py", line 5, in bug
    raise Exception("not consumed")
    Exception: not consumed
    '''