class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

def minutes_since_midnight(time):
    return time.hour * 60 + time.minute

def msm_to_time(msm):
    hour = msm // 60
    minute = msm % 60
    return Time(hour, minute)

def wallclock_time_add_minutes(time, minutes):
    total_minutes = minutes_since_midnight(time) + minutes
    return msm_to_time(total_minutes % (24 * 60))

t1 = Time(12, 24)
t2 = Time(7, 0)
t3 = Time(23, 55)

added_time_example = wallclock_time_add_minutes(t1, 15)
added_time_example
