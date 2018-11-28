import datetime
import sys
import asyncio

sys.path.append("..")

import CoroCron

def report_time():
    print("It is now {}".format(datetime.datetime.now()))

if __name__ == '__main__':
    mins = [x for x in range(0, 59) if x % 2 == 0]
    
    Cron = CoroCron.Cron()
    Cron.Job().Minutes(mins).Do(report_time)
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(Cron.Start())
    loop.run_forever()




