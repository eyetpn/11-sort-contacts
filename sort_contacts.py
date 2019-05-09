from operator import itemgetter
def sort_contacts(param):
    # code here
    sorted_param = sorted(param, key = itemgetter('name'))
    return "sorted_param
