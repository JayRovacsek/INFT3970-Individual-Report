#!/usr/bin/env python3.7

import re
import time

if __name__ == '__main__':
    
    email = 'c3146220@uon.edu.au'
    attack_email = '(c)(3)(1)(4)(6220)@uon.edu.au'
    simple_pattern = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'
    complex_pattern = r'^(?=[A-Z0-9._%+-]{6,254}$)[A-Z0-9._%+-]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,8}[A-Z]{2,63}$'

    start_time = time.time()
    re.match(simple_pattern, email, flags=0)
    computation_time = time.time() - start_time
    print(computation_time)

    start_time = time.time()
    re.match(simple_pattern, attack_email, flags=0)
    computation_time = time.time() - start_time
    print(computation_time)

    start_time = time.time()
    re.match(complex_pattern, email, flags=0)
    computation_time = time.time() - start_time
    print(computation_time)

    start_time = time.time()
    re.match(complex_pattern, attack_email, flags=0)
    computation_time = time.time() - start_time
    print(computation_time)