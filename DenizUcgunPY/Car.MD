


# Car Class

-----

[![Build Status](https://travis-ci.org/dry-python/classes.svg?branch=master)](https://travis-ci.org/dry-python/classes)
[![codecov](https://codecov.io/gh/dry-python/classes/branch/master/graph/badge.svg)](https://codecov.io/gh/dry-python/classes)
[![Documentation Status](https://readthedocs.org/projects/classes/badge/?version=latest)](https://classes.readthedocs.io/en/latest/?badge=latest)
[![Python Version](https://img.shields.io/pypi/pyversions/classes.svg)](https://pypi.org/project/classes/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Telegram chat](https://img.shields.io/badge/chat-join-blue?logo=telegram)](mailto:emin.kartci@ozu.edu.com)

-----

```
Authors:
- Emin Kartci
- Engin Deniz Ucgun
```


## Features

- Move Function
```Python
def move(self,km):
    if( km <= (self.fuel / self.consumption)):
        ## move
        self.km += km
        self.fuel -= km / self.consumption
    else:
        # move as far as car can
            # calculate max km
        maxKm = self.fuel / self.consumption
        self.km += maxKm
        self.fuel = 0
        print(f"Car {self.name} cannot move further. Please go to the nearest gas station!")
```

This function takes 1 parameter in terms of km. Checks whether the fuel is enough. If it is then move, otherwise move as far as the car can and warn the user.

## More!

Want more? [Go to the docs!](https://classes.readthedocs.io) Or read these articles:
- [Typeclasses in Python](https://sobolevn.me/2021/06/typeclasses-in-python)


<p align="center">&mdash; ⭐️ &mdash;</p>
<p align="center"><i>Drylabs maintains dry-python and helps those who want to use it inside their organizations.</i></p>
<p align="center"><i>Read more at <a href="https://drylabs.io">drylabs.io</a></i></p>
