def binary_search(array, element, debug=False):
    lower_bound=0
    upper_bound=len(array)-1
    while lower_bound<=upper_bound:
        middle=(lower_bound-upper_bound)//2
        if debug:
            print("Lower Bound")