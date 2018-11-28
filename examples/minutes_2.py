import datetime
import sys
import asyncio

sys.path.append("..")

from CoroCron.Cron import Cron

async def report_time(name="there"):
    print("Hi {}, it is now {}".format(name, datetime.datetime.now()))

if __name__ == '__main__':
    mins = [x for x in range(0, 59) if x % 2 == 0]
    mins2 = [x for x in range(0, 59) if x % 2 == 1]
    
    Cron = Cron()
    Cron.Job().Minutes(mins).Do(report_time, ("Even",))
    Cron.Job().Minutes(mins2).Do(report_time)
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(Cron.Start())
    loop.run_forever()




