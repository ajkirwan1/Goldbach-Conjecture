import time

# This module is used to determine the time-cost of functions throughout the program. Several functions throught the
# program have been benchmarked for large integers (1,000,000) using this module.


class TimerError(Exception):
    pass


class Timer:
    # This Class was used to benchmark the time-cost of several functions throughout each script.
    def __init__(self, text="The time elapsed is {:0.4f} seconds"):
        self._start_time = None
        self.text = text

    def start_timer(self):
        self._start_time = time.perf_counter()

    def stop_timer(self):
        if self._start_time is None:
            raise TimerError
        time_elapsed = time.perf_counter() - self._start_time
        self._start_time = None
        print(self.text.format(time_elapsed))


