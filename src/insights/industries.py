from typing import List, Dict
from src.insights.jobs import read
# from jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them"""
    return_from_list_of_jobs = read(path)
    set_of_industry = set()
    list_converted_from_set = []

    for industry in return_from_list_of_jobs:
        if(industry['industry'] != ''):
            set_of_industry.add(industry['industry'])

    list_converted_from_set.extend(set_of_industry)
    return list_converted_from_set

    # raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry"""
    returned_list_of_industry = []

    for i in jobs:
        if (i['industry'] == industry):
            returned_list_of_industry.append(i)

    return returned_list_of_industry

    # raise NotImplementedError
