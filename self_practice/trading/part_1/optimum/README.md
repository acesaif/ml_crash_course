## Understanding Optimization with `scipy`

#### Requires `scipy` package.

```
$ pip2 install scipy --user

$ python2
Python 2.7.14 (default, Mar 14 2018, 16:45:33) 
[GCC 8.0.1 20180222 (Red Hat 8.0.1-0.16)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> from scipy import optimize as opt
>>>
```

Here are my two plots showing __`optimization`__ performance.

__`Fit a Line`__ | __`Fit a Polynomial`__
| --- | --- |
![fit_line](https://user-images.githubusercontent.com/26320981/39816629-6ac16e78-53b9-11e8-8256-b3121698a2ed.png) | ![fit_poly](https://user-images.githubusercontent.com/26320981/39816691-91fe40e2-53b9-11e8-83c4-52604e5ec79b.png) |
Here I did fit a line. | Here I did fit a 4th degree polynomial. |

##### These algorithms are beautiful.