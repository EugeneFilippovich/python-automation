#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque
import threading
import time
import sys
import logging

logger = logging.getLogger(__name__)
logfile = "script_log.log"
span_time = 2
run_tracker = []

formatter = logging.Formatter('%(asctime)s - %(name)s : %(threadName)s - %(levelname)s - %(message)s')
screen_handler = logging.StreamHandler(sys.stdout)
screen_handler.setLevel(logging.DEBUG)
screen_handler.setFormatter(formatter)

file_handler = logging.FileHandler(logfile)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(screen_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

start_time = time.time()

# MODIFY-START if needed
# MODIFY-END if needed


def threaded_execution(*args, **kwargs):
    # MODIFY-START
    # TODO: here be your code that runs a decorated function in a separate thread
    def wrapped(*args_, **kwargs_):
        threading.Thread(target=(args, kwargs), args=args, kwargs=kwargs).start()

    return wrapped
    # MODIFY-END


@threaded_execution
def long_long_function(filename):
    logger.info("Filename to work with: {}".format(filename))
    run_tracker.append(filename)
    time.sleep(span_time)
    # TODO: here be your code that works on file content:
    # MODIFY-START
    with open(filename) as f_in, open("truncated"+filename, "w") as f_out:
        for row in f_in.readlines()[-3:]:
            f_out.write(row)
    # MODIFY-END


if __name__ == "__main__":
    logger.info("Starting a chain of long functions")
    long_long_function("E:\Lorem.txt")
    long_long_function("E:\Lorem.txt")

    logger.info("Starting long main logic")
    time.sleep(span_time)

    ########################
    # --- Summary part --- #
    ########################
    total_time = time.time() - start_time
    logger.info("The run took '{:.3}' seconds".format(total_time))
    assert len(run_tracker)  # Do NOT remove or change, we need to ensure long_long_function ever ran
    assert total_time < (span_time + 1)  # +1 second is granted for all the threads to get allocated

    # MODIFY-START if needed
    # MODIFY-END if needed