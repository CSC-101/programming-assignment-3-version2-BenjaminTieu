import data

# Part 1
# This function, when given a list of country demographic objects, will return the
# total 2014 population across the set of countries in the provided list.
def population_total(l1: list[data.CountyDemographics]) -> int:
    total = 0
    for county in l1:
        total += county.population.get('2014 Population')
    return total

# Part 2
# This function, when given a list of country demographics objects and a two-letter
# state abbreviation, will return a list of county demographics objects from the
# input list that are within the specified state.
def filter_by_state(l1: list[data.CountyDemographics], phr1: str) -> list[data.CountyDemographics]:
    l2 = []
    for county in l1:
        if county.state == phr1:
            l2.append(county)
    return l2

# Part 3
# This function, when given a list of county demographics and an education key of
# interest, will return the total 2014 subpopulation across the set of counties
# in the provided list for the specified key of interest
def population_by_education(l1: list[data.CountyDemographics], phr1: str) -> float:
    pop_education = 0
    for county in l1:
        if county.education.get(phr1) and county.population.get('2014 Population') is not None:
            pop_education += (county.population.get('2014 Population') * county.education.get(phr1)) / 100
    return pop_education

# This function, when given a list of county demographics objects and the ethnicity
# key of interest, will return the total 2014 subpopulation across the set of
# counties in the provided list for the specified key of interest
def population_by_ethnicity(l1: list[data.CountyDemographics], phr1: str) -> float:
    pop_ethnicity = 0
    for county in l1:
        if county.ethnicities.get(phr1) and county.population.get('2014 Population') is not None:
            pop_ethnicity += (county.population.get('2014 Population') * county.ethnicities.get(phr1)) / 100
    return pop_ethnicity

# This function, when given a list of county demographic objects, will return the
# total 2014 subpopulation indicated by the income key "Persons Below Poverty
# Level" across the set of counties in the provided list for the specified key of
# interest
def population_below_poverty_level(l1: list[data.CountyDemographics]) -> float:
    pop_poverty = 0
    for county in l1:
        if county.income.get('Persons Below Poverty Level') and county.population.get('2014 Population') is not None:
            pop_poverty += (county.population.get('2014 Population') *
                            county.income.get('Persons Below Poverty Level')) / 100
    return pop_poverty

# Part 4
# This function, when given a list of county demographics objects and the
# education key of interest, will return the specified 2014 subpopulation as a
# percentage of the total 2014 population across the set of countries in the
# provided list for the specified key of interest
def percent_by_education(l1:list[data.CountyDemographics], phr1: str) -> float:
    if population_total(l1) != 0:
        return population_by_education(l1, phr1)/population_total(l1)*100
    return 0

# This function, when given a list of county demographics objects and the
# ethnicity key of interest, will return the specified 2014 subpopulation as a
# percentage of the total 2014 population across the set of countries in the
# provided list for the specified key of interest
def percent_by_ethnicity(l1:list[data.CountyDemographics], phr1: str) -> float:
    if population_total(l1) != 0:
        return population_by_ethnicity(l1, phr1)/population_total(l1)*100
    return 0

# This function, when given a list of county demographics objects, will return
# the 2014 subpopulation indicated by income key 'Persons Below Poverty Level'
# as a percentage of the total 2014 population across the set of counties in the
# provided list for the specified key of interest
def percent_below_poverty_level(l1: list[data.CountyDemographics]) -> float:
    if population_total(l1) != 0:
        return population_below_poverty_level(l1)/population_total(l1)*100
    return 0

# Part 5
# These two functions, when given a list of county demographic objects, the education
# key of interest, and a numeric threshold value, will return a list of all county
# demographic objects for which the value for the specified key is greater than or
# less than the specified threshold value
def education_greater_than(l1: list[data.CountyDemographics], phr1: str, threshold: float) -> list[data.CountyDemographics]:
    l2 = []
    for county in l1:
        if county.education.get(phr1) is not None:
            if county.education.get(phr1) > threshold:
               l2.append(county)
    return l2

def education_less_than(l1: list[data.CountyDemographics], phr1: str, threshold: float) -> list[data.CountyDemographics]:
    l2 = []
    for county in l1:
        if county.education.get(phr1) is not None:
            if county.education.get(phr1) < threshold:
                l2.append(county)
    return l2

# These two functions, when given a list of county demographic objects, the ethnicity
# key of interest, and a numeric threshold value, will return a list of all county
# demographic objects for which the value for the specified key is greater than or
# less than the specified threshold value
def ethnicity_greater_than(l1: list[data.CountyDemographics], phr1: str, threshold: float) -> list[data.CountyDemographics]:
    l2 = []
    for county in l1:
        if county.ethnicities.get(phr1) is not None:
            if county.ethnicities.get(phr1) > threshold:
               l2.append(county)
    return l2

def ethnicity_less_than(l1: list[data.CountyDemographics], phr1: str, threshold: float) -> list[data.CountyDemographics]:
    l2 = []
    for county in l1:
        if county.ethnicities.get(phr1) is not None:
            if county.ethnicities.get(phr1) < threshold:
               l2.append(county)
    return l2

# These two functions, when given a list of county demographics objects and a numeric
# threshold value, will return a list of all county demographics objects for
# which the value for key 'Persons Below Poverty Level' is greater than or less
# than the specified threshold value
def below_poverty_level_greater_than(l1: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    l2 = []
    for county in l1:
        if county.income.get('Persons Below Poverty Level') is not None:
            if county.income.get('Persons Below Poverty Level') > threshold:
                l2.append(county)
    return l2

def below_poverty_level_less_than(l1: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    l2 = []
    for county in l1:
        if county.income.get('Persons Below Poverty Level') is not None:
            if county.income.get('Persons Below Poverty Level') < threshold:
                l2.append(county)
    return l2