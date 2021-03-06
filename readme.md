# CoroCron

CoroCron is a cron like scheduler for python functions.  It uses asyncio to asynchronously start jobs at the specified schedule.  The jobs are then put on the event loop when the schedule specified is met.

## Usage

You can find more usage examples in the examples directory

### Step 1: Create the base cron object
```python
import CoroCron
Cron = CoroCron.Cron()
```
Note: By default Cron uses the local timezone but it can be modified to use UTC by initializing like so: ```CoroCron.Cron(True)```

### Step 2: Add jobs
```python
Cron.Job().Days().Hours().Minutes().Do(function, args)
```

#### Job options
* Any option defaults to all of the given period 
    *  Like * in cron
    * e.g. `.Days()` would run every day in a given month
* Otherwise a list can be specified for which days
    * Any iterable or single numeric (`.Days(4)`) can also be used.
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
        * Monday = 0, Sunday = 6.  An enum is also provided: `CoroCron.Weekdays`
    * `Hours()` - Hours of the day
    * `Minutes()` - Minutes in the hour
* `Do(function, args=())`
    * This is the coroutine that you want to execute when the time is right
    * The function should be passed by reference (i.e. without parenthesis at the end)
    * You can pass args as a tuple in the 2nd parameter

### Step 3: Start the Cron

```python
Cron.Start(blocking = False)
```
By default `Start()` returns a future which can be awaited in an async funtion or added to a loop with ensure_future.
If you set blocking to `True` it will instead be a blocking call using ```loop.run_forever()```

