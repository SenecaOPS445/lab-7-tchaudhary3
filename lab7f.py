class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __str__(self):
        '''return a string representation for the object self'''
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        '''return a string representation for the object self'''
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        '''format time as a string'''
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        '''add two time objects and return a new time object'''
        total_seconds = self.hour * 3600 + self.minute * 60 + self.second + \
                        t2.hour * 3600 + t2.minute * 60 + t2.second
        
        total_hour = (total_seconds // 3600) % 24
        total_minute = (total_seconds % 3600) // 60
        total_second = total_seconds % 60

        return Time(total_hour, total_minute, total_second)

    def __add__(self, t2):
        """return the result by using sum_times() method"""
        return self.sum_times(t2)
