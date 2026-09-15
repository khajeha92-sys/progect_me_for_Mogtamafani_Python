# INTHE NAME OG GAD

#1. implement a Phython generator function that yieids a specified number of unique random integers within a given range without any duplicates.
import random
def make_random_ints_no_dups(observation_count:int,
                             lower_bound:int,
                             upper_bound:int):# -> Generator[int, None, None]:
    if observation_count<0:
        raise ValueError('observation_count >=0')
    if lower_bound >= upper_bound:
        raise ValueError('lower_bound must less upper_bound')
    population_size = upper_bound - lower_bound
    if observation_count > population_size:
        raise ValueError(f"Requested {observation_count} unique numbers but only"
                         f"{population_size} available in range ({lower_bound}, {upper_bound})")

    for value in random.sample(range(lower_bound, upper_bound),
                               observation_count):
        yield value
    pass



### Driver Code ###
if __name__ == '__main__':
    
    g = make_random_ints_no_dups(5, 0, 10)
    print(list(g))

    try:
       list(make_random_ints_no_dups(11, 0, 10))
    except ValueError as e:
       print('Error',e)

print('*'*90)


