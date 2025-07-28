import os
import time


def change_file_times(directory: str, new_time: time) -> None:
    """
    Set target directory for function as an absolute path
            I have not tested relative paths

    Will walk through subdirectories

    Uses current date time stamp to update file time
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            os.utime(file_path, times=(new_time, new_time))


directory_path = "F:/May 2006"  # Use forward slashes in the path
new_time = time.time()
change_file_times(directory_path, new_time)
