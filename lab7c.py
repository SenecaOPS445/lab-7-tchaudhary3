#!/usr/bin/env python3
# Student ID: [seneca_id]

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

def format_time(time):
    """Format a Time object as a string in HH:MM:SS format."""
    return f"{time.hour:02d}:{time.minute:02d}:{time.second:02d}"

def time_to_sec(time):
    """Convert a Time object to a single integer representing the number of seconds from midnight."""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):   
    """Convert a given number of seconds to a Time object in hour, minute, second format."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    """Add two Time objects using seconds conversion."""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)

def change_time(time, seconds):
    """Modify a Time object by adding a given number of seconds."""
    new_time_sec = time_to_sec(time) + seconds
    return sec_to_time(new_time_sec)

