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

    # raise NotImplementedError


def matches_salary_range_conditions_one(job, salary):
    if (not('min_salary' in job) or not('max_salary' in job)):
        raise ValueError('É preciso que as chaves sejam declaradas.')

    if (type(salary) != int and type(salary) != str):
        raise ValueError('O salario precisa ser um valor inteiro')


def matches_salary_range_conditions_two(job):
    condition_numeric_one = not str(job['min_salary']).isnumeric()
    condition_numeric_two = not str(job['max_salary']).isnumeric()

    if (condition_numeric_one or condition_numeric_two):
        raise ValueError('Os salários devem ser numericos.')

    if (int(job['min_salary']) > int(job['max_salary'])):
        raise ValueError('O salário máximo deve ser maior.')


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job"""
    matches_salary_range_conditions_one(job, salary)
    matches_salary_range_conditions_two(job)

    if (int(job['min_salary']) <= int(salary) <= int(job['max_salary'])):
        return True

    return False
    # raise NotImplementedError


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
