#!/usr/bin/env python3
"""Install pync module

python3 -m pip install pync

"""

from pync import Notifier
import os
import sys

def drink_now():
    Notifier.notify(
        'Please Drink Water. Need to Drink (3.7 liters) of fluids for men and (2.7 liters) of fluids a day for women',
        title='Drink Water Now, Stay Hydrated!!',
        appIcon=os.path.join(sys.path[0], "img", "glass.jpg"),
        sound='Glass',
        execute='say "Drink Water"'
        )

drink_now()