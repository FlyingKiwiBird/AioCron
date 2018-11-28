try:
    from AioCron.Cron import Cron
    from AioCron.Job import Job
    from AioCron.Timer import Timer
    from AioCron.Weekdays import Weekdays
except ImportError:
    pass

__name__ = 'AioCron'
__version__ = '0.1.0'