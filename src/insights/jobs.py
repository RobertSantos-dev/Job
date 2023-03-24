from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents"""
    with open(path, encoding='utf8') as file:
        file_csv = csv.reader(file, delimiter=',', quotechar='"')
        header, *values = file_csv

    csv_file_dictionary_list = []
    for value in values:
        keys = {}
        for i in range(len(value)):
            keys[header[i]] = value[i]

        csv_file_dictionary_list.append(keys)

    return csv_file_dictionary_list


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them"""
    returned_list_of_jobs = read(path)
    set_of_job_types = set()
    list_converted_from_set = []

    for job in returned_list_of_jobs:
        set_of_job_types.add(job['job_type'])

    list_converted_from_set.extend(set_of_job_types)
    return list_converted_from_set

    # raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type"""
    returned_list_of_job_type = []

    for i in jobs:
        if (i['job_type'] == job_type):
            returned_list_of_job_type.append(i)

    return returned_list_of_job_type

    # raise NotImplementedError
