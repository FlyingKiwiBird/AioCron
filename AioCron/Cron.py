import datetime
import AioCron
import asyncio

class Cron():
    def __init__(self, use_utc=False):
        self.timer  = AioCron.Timer(use_utc)
        self.__started = False
        
    def Start(self, blocking = False):
        if blocking:
            loop = asyncio.get_event_loop()
            asyncio.ensure_future(self.timer.start(), loop=loop)
            loop.run_forever()
        else:
            return self.timer.start()

    def AddJob(self, job):
        if not isinstance(job, AioCron.Job):
            TypeError("job must be a AioCron job")
        self.timer.AddJob(job)

    def Job(self):
        return AioCron.Job(self)

    