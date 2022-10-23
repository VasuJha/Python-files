import random
from re import X
def estimate_pi(precision):
    """returns an estimate of pi upto 'precision' decimal places.

    Args:
        precision (int): decimal places of pi
        >>>estimate_pi(5)
        ---
    """
    power = precision + 1
    count = 10**power
    i = 0
    N_hits = 0
    N_tot = 0
    while i < count :
        x = random.random()
        y = random.random()
        r_sq =  (x - 0.5)**2 + (y - 0.5)**2
        if r_sq > 0.25:
            N_tot = N_tot + 1
        elif r_sq == 0.25 or r_sq < 0.25:
            N_hits = N_hits + 1
            N_tot = N_tot + 1
        i = i + 1
    pi_est = 4 * N_hits / N_tot
    return round(pi_est, precision)


    