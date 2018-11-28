# AioCron

AioCron is a cron like scheduler for python functions.  It uses asyncio to asynchronously start jobs at the specified schedule.  The jobs are run using multiprocessing so that they will not interupt the main process.

## Usage

You can find more usage examples in the examples directory

### Step 1: Create the base cron object
```python
import AioCron
Cron = AioCron.Cron()
```
Note: By default Cron uses the local timezone but it can be modified to use UTC by initializing like so: ```AioCron.Cron(True)```

### Step 2: Add jobs
```python
Cron.Job().Days().Hours().Minutes().Do(function, args)
```

#### Job options
* Any option defaults to all of the given period 
    *  Like * in cron
    * e.g. `.Days()` would run every day in a given month
* Otherwise a list can be specified for which days
    * A tuple (or any iterable) can also be used
    * e.g. `.Hours([0,2,4])` would run at 12am, 2am, and 4am
* Any period *after* the initial setting will default to the first if not specified
    * For days: 1st day of the month
    * For hours: 0th hour (12am)
    * For minutes: 0th minute
    * e.g. `Cron.Job().Days().Do(something)` = something will be done every day at 12:00am
    * e.g. `Cron.Job().Months().Minutes([15,30]).Do(something)` = something will be done the 1st day of the month at 12:15am and 12:30am
* Periods
    * `Months()` - Months of the year
    * `Days()` - Days of the month
    * `Weekdays()` - Days of the week (note: you can either specify days XOR weekdays, not both)
        * Monday = 0, Sunday = 6.  An enum is also provided: `AioCron.Weekdays`
    * `Hours()` - Hours of the day
    * `Minutes()` - Minutes in the hour
* `Do(function, args)`
    * Do is basically a proxy for a `multiprocessing.Process` It stores the action to complete at the scheule specified by the periods above
    * args is optional

### Step 3: Start the Cron

```python
Cron.Start(blocking = False)
```
By default `Start()` returns a future which can be awaited in an async funtion or added to a loop with ensure_future.
If you set blocking to `True` it will instead be a blocking call using ```loop.run_forever()```

