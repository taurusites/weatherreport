counter = 0
cities_list = []


def ask_city():
    city = input("Enter a city: ")
    return city


def ask_to_continue():
    answer = input("Do you want to continue? (y/n): ")
    return answer.lower()


def inputs():
    cities_list.append(ask_city())
    while ask_to_continue() == 'y':
        cities_list.append(ask_city())
    return cities_list
