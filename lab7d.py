#!/usr/bin/env python3
# Student ID: tchaudhary3

class Time:
    """Simple object type for time of the day.
       Data attributes: hour, minute, second
       Function attributes: __init__, __str__, __repr__
                            time_to_sec, format_time,
                            change_time, sum_times, valid_time
    """

    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for the Time object."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        """Return time object as a formatted string."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, other):
        """Add the current time object with another time object and return a new Time object."""
        total_seconds = self.time_to_sec() + other.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Modify the time by adding given seconds and updating attributes."""
        total_seconds = self.time_to_sec() + seconds
        new_time = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second

    def time_to_sec(self):
        """Convert a time object to total seconds since midnight."""
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        """Check if the time object has valid attributes."""
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

def sec_to_time(seconds):
    """Convert a given number of seconds to a Time object."""
    seconds %= 86400  # Ensure we don't exceed 24 hours
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return Time(hours, minutes, seconds)

# Testing the class
if __name__ == "__main__":
    t1 = Time(9, 50, 0)
    t2 = Time(2, 30, 15)

    print("Time 1:", t1.format_time())
    print("Time 2:", t2.format_time())

    sum_time = t1.sum_times(t2)
    print("Sum of times:", sum_time.format_time())

    t1.change_time(5000)
    print("Time 1 after adding 5000 seconds:", t1.format_time())

    print("Valid time check for t1:", t1.valid_time())

