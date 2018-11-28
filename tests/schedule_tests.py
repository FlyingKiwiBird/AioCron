import unittest
import CoroCron
import datetime

class ScheduleTests(unittest.TestCase):
    def test_monthly(self):
        p = CoroCron.Cron()
        j = p.Job().Months((2,))
        dt1 = datetime.datetime(2018, 1, 1)
        self.assertFalse(j.Test(dt1))
        dt2 = datetime.datetime(2018, 2, 1)
        self.assertTrue(j.Test(dt2))
        dt3 = datetime.datetime(2018, 2, 2)
        self.assertFalse(j.Test(dt3))

    def test_daily(self):
        p = CoroCron.Cron()
        j = p.Job().Days((2,))
        dt1 = datetime.datetime(2018, 6, 1, 0)
        self.assertFalse(j.Test(dt1))
        dt2 = datetime.datetime(2018, 6, 2, 0)
        self.assertTrue(j.Test(dt2))
        dt3 = datetime.datetime(2018, 6, 2, 10)
        self.assertFalse(j.Test(dt3))

    def test_weekly(self):
        p = CoroCron.Cron()
        j = p.Job().Weekdays(0) #Monday
        dt1 = datetime.datetime(2018, 11, 13, 0) #Tuesday
        self.assertFalse(j.Test(dt1))
        dt2 = datetime.datetime(2018, 11, 12, 0) #Monday
        self.assertTrue(j.Test(dt2))
        dt3 = datetime.datetime(2018, 11, 12, 20) #Monday
        self.assertFalse(j.Test(dt3))

    def test_hourly(self):
        p = CoroCron.Cron()
        j = p.Job().Hours((10,))
        dt1 = datetime.datetime(2018, 6, 1, 0, 0)
        self.assertFalse(j.Test(dt1))
        dt2 = datetime.datetime(2018, 6, 2, 10, 0)
        self.assertTrue(j.Test(dt2))
        dt3 = datetime.datetime(2018, 6, 2, 10, 15)
        self.assertFalse(j.Test(dt3))

    def test_minutely(self):
        p = CoroCron.Cron()
        j = p.Job().Minutes((58,))
        dt1 = datetime.datetime(2018, 6, 1, 10, 0, 0)
        self.assertFalse(j.Test(dt1))
        dt2 = datetime.datetime(2018, 6, 2, 10, 58, 0)
        self.assertTrue(j.Test(dt2))
        #Note: because the checker runs once a minute we don't need the 3rd test here

    def test_monthly_daily(self):
        p = CoroCron.Cron()
        j = p.Job().Months((6,)).Days((4,))
        dt1 = datetime.datetime(2018, 5, 1, 0, 0)
        self.assertFalse(j.Test(dt1))
        dt2 = datetime.datetime(2018, 6, 1, 0, 0)
        self.assertFalse(j.Test(dt2))
        dt3 = datetime.datetime(2018, 5, 4, 0, 0)
        self.assertFalse(j.Test(dt3))
        dt4 = datetime.datetime(2018, 6, 4, 2, 0)
        self.assertFalse(j.Test(dt4))
        dt5 = datetime.datetime(2018, 6, 4, 0, 0)
        self.assertTrue(j.Test(dt5))

    def test_monthly_hourly(self):
        p = CoroCron.Cron()
        j = p.Job().Months((6,)).Hours((4,))
        dt1 = datetime.datetime(2018, 6, 2, 4, 0)
        self.assertFalse(j.Test(dt1))
        dt2 = datetime.datetime(2018, 6, 1, 4, 0)
        self.assertTrue(j.Test(dt2))

    def test_m_d_h(self):
        p = CoroCron.Cron()
        j = p.Job().Months((6,)).Days().Hours((4,))
        dt1 = datetime.datetime(2018, 6, 2, 4, 0)
        self.assertTrue(j.Test(dt1))




