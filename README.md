# Code
See [main.py](main.py)

# Question 1
#### How much more accurate is the model with the forgetting parameter than the model without?
Standard BKT: 74.5%

BKT+Forgets: 78.2%

Difference: 3.7%

# Question 2
#### Which Knowledge Component is the easiest to learn?
Easiest to learn:  _Plot pi_

|_Plot pi_|_Forget_|_No forget_|
|--:|:-:|:-:|
| Prior | 63.40% | 66.27% |
| Guess | 8.38% | 8.36% |
| Learn | 61.03% | 58.44% |
| Slip  | 6.32% | 10.03% |
| Forget| 5.35% | N/A |

# Question 3
#### Which Knowledge Component is the hardest to learn?
Hardest to learn:  _Finding the intersection, Mixed_ (when forgetting)

Hardest to learn:  _Plot terminating proper fraction_ (when not forgetting)

|_Finding the intersection, Mixed_|_Forget_|_No forget_|
|--:|:-:|:-:|
| Prior | 36.65% | 35.96% |
| Guess | 33.61% | 33.32% |
| Learn | 9.78% | 6.94% |
| Slip  | 26.66% | 28.29% |
| Forget| 8.70% | N/A |

|_Plot terminating proper fraction_|_Forget_|_No forget_|
|--:|:-:|:-:|
| Prior | 53.60% | 69.00% |
| Guess | 27.87% | 23.94% |
| Learn | 12.62% | 6.74% |
| Slip  | 29.75% | 36.40% |
| Forget| 4.51% | N/A |


# Question 4
#### Which Knowledge Component is the easiest to guess?
Easiest to guess:  _Plot whole number_

|_Plot whole number_|_Forget_|_No forget_|
|--:|:-:|:-:|
| Prior | 52.51% | 74.58% |
| Guess | 80.55% | 74.02% |
| Learn | 36.71% | 37.85% |
| Slip  | 1.02% | 5.12% |
| Forget| 23.00% | N/A |

# Question 5
#### Which Knowledge Component is the hardest to guess?
Hardest to guess:  _Plot imperfect radical_ (when forgetting)

Hardest to guess:  _Plot non-terminating improper fraction_ (when not forgetting)

|_Plot imperfect radical_|_Forget_|_No forget_|
|--:|:-:|:-:|
| Prior | 39.25% | 25.72% |
| Guess | 3.69% | 8.60% |
| Learn | 17.03% | 12.77% |
| Slip  | 36.95% | 23.66% |
| Forget| 6.34% | N/A |

|_Plot non-terminating improper fraction_|_Forget_|_No forget_|
|--:|:-:|:-:|
| Prior | 63.71% | 64.52% |
| Guess | 10.81% | 5.66% |
| Learn | 20.31% | 24.77% |
| Slip  | 26.61% | 26.78% |
| Forget| 0.71% | N/A |

# Question 6
#### How much more accurate is the model with the forgetting parameter than the model without?
Standard BKT: 63.9%

BKT+Forgets: 68.6%

Difference: 4.7%

# Question 7
#### Which Knowledge Component is the easiest to forget?
Easiest to forget:  _Calculate unit rate_

|_Calculate unit rate_|_Forget_|_No forget_|
|--:|:-:|:-:|
| Prior | 99.40% | 1.00% |
| Guess | 46.14% | 49.34% |
| Learn | 28.72% | 7.37% |
| Slip  | 6.41% | 13.44% |
| Forget| 97.33% | N/A |

# Question 8
#### Which Knowledge Component is the hardest to forget?
Hardest to forget:  _Plot non-terminating improper fraction_

|_Plot non-terminating improper fraction_|_Forget_|_No forget_|
|--:|:-:|:-:|
| Prior | 63.71% | 64.52% |
| Guess | 10.81% | 5.66% |
| Learn | 20.31% | 24.77% |
| Slip  | 26.61% | 26.78% |
| Forget| 0.71% | N/A |

# Question 9
#### Pick 2 out of questions 1-8 and write a short (1-2 sentence) explanation for them. Why is a certain model more accurate than another? Or why is a certain knowledge component easy/hard to learn/guess/forget?
##### Question 6
The increase in accuracy may be accounted to:
 - an increase in the parameter complexity of the model, allowing for a better fit (i.e. bigger = better when your model is this small); and/or
 - a better approximation of ground truth, allowing the model to better fit what actually occurs.

A simpler analysis might attribute it wholly the second reason, but some values for 'forgetting' (such as 97.33% for calculating unit rate) seem illogical.

##### Question 7
Recall the table:
|_Calculate unit rate_|_Forget_|_No forget_|
|--:|:-:|:-:|
| Prior | **99.40%** | **1.00%** |
| Guess | 46.14% | 49.34% |
| Learn | 28.72% | 7.37% |
| Slip  | 6.41% | 13.44% |
| Forget| **97.33%** | N/A |

Note that the 1% chance of prior knowledge jumps all the way to 99.4% if we allow them to forget. This presumably means that a significant number of students in the training data are getting it right on the first try (note that guessing is around 45-50% on both sides of the table), but not on successive tries. Without allowing for forgetting, this leads to a higher guess rate and a higher slip rate, with an abysmally low learn rate. When allowing for forgetting, it is 'easier' - albeit less *logical* - to attribute this to it being extremely easy to forget. When applied to test data or to new students, the model allowing for forgetting is therefore far more likely to incorrectly predict the user's state.
