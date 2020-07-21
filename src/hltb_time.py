"""
Stuture to store time.

Only store hours, minutes and seconds without count days
"""


class Time():
    """Structure to hours and minutes."""

    def __init__(self, hours=0, minutes=0, seconds=0):
        """Create and store the time."""
        self._set_seconds(int(seconds))
        self._set_minutes(int(minutes))
        self._set_hours(hours)

    def __repr__(self):
        """Return all time in string."""
        return (str(self._hours) + ' hours ' +
                str(self._minutes) + ' minutes ' +
                str(self._seconds) + ' seconds')

    def _set_hours(self, hours):
        if str(hours)[-1] == '½':
            self._set_minutes(30)
            self._hours = int(str(hours)[0:-1])
        else:
            self._hours = int(hours)

    def _set_minutes(self, minutes):
        if minutes >= 0 and minutes < 60:
            self._minutes = minutes
        else:
            raise ValueError("Minutes must be between 0 and 59")

    def _set_seconds(self, seconds):
        if seconds >= 0 and seconds < 60:
            self._seconds = seconds
        else:
            raise ValueError("Seconds must be between 0 and 59")

    def get_time(self):
        """Return time in list."""
        return self._hours, self._minutes, self._seconds

    @property
    def hours(self):
        """Return hours."""
        return self._hours

    @property
    def minutes(self):
        """Return minutes."""
        return self._minutes

    @property
    def seconds(self):
        """Return seconds."""
        return self._seconds
