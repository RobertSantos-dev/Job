from typing import Union, List, Dict
from src.insights.jobs import read
# from jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs"""
    returned_list_of_jobs = read(path)
    set_of_max_salary = set()
    list_converted_from_set = []

    for salary in returned_list_of_jobs:
        if (salary['max_salary'] != 'invalid' and salary['max_salary'] != ''):
            set_of_max_salary.add(int(salary['max_salary']))

    list_converted_from_set.extend(set_of_max_salary)
    return max(list_converted_from_set)

    # raise NotImplementedError


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs """
    returned_list_of_jobs = read(path)
    set_of_min_salary = set()
    list_converted_from_set = []

    for salary in returned_list_of_jobs:
        if (salary['min_salary'] != 'invalid' and salary['min_salary'] != ''):
            set_of_min_salary.add(int(salary['min_salary']))

    list_converted_from_set.extend(set_of_min_salary)
    return min(list_converted_from_set)

    """
    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
