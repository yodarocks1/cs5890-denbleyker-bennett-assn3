import sys
sys.path.append('../')
import numpy as np
from pyBKT.models import Model
from icecream import ic
np.seterr(divide='ignore', invalid='ignore')

def reduce(coef, subpart, func=max, start=None):
    key = None
    value = start
    for kc in coef:
        if value is None:
            key = kc
            value = coef[kc][subpart]
        else:
            oldvalue = value
            value = func(value, coef[kc][subpart])
            if oldvalue != value:
                key = kc
    return (key, value)

def print_reduce(s, coef, subpart, func=max, start=None, include_key=True):
    k, v = reduce(coef, subpart, func=func, start=start)
    if include_key:
        print(s, k, "(" + str(int(v[0] * 10000) / 100) + "%)")
    else:
        print(s, str(int(v[0] * 10000) / 100) + "%")

def create_model(train, test, forgets, metric):
    model = Model(seed = 0, num_fits = 20)
    model.fit(data_path=train, forgets=forgets)
    print(metric[0].upper() + metric[1:].lower() + ":", model.evaluate(data_path=test, metric=metric))
    return model

def print_comparison_table(forget_model, no_forget_model, key):
    print(f"|_{key}_|_Forget_|_No forget_|")
    print(f"| Prior | {forget_model.coef_[key]['prior']:.2%}      | {no_forget_model.coef_[key]['prior']:.2%} |")
    print(f"| Guess | {forget_model.coef_[key]['guesses'][0]:.2%} | {no_forget_model.coef_[key]['guesses'][0]:.2%} |")
    print(f"| Learn | {forget_model.coef_[key]['learns'][0]:.2%}  | {no_forget_model.coef_[key]['learns'][0]:.2%} |")
    print(f"| Slip  | {forget_model.coef_[key]['slips'][0]:.2%}   | {no_forget_model.coef_[key]['slips'][0]:.2%} |")
    print(f"| Forget| {forget_model.coef_[key]['forgets'][0]:.2%} | N/A |")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        focus = None
        if sys.argv[1] == "--forgets":
            forgets = True
        elif sys.argv[1] == "--no-forgets":
            forgets = False
        else:
            print(f"Usage: {sys.argv[0]} [--forgets|--no-forgets|--table [+|-]<prior|guesses|learns|slips|forgets>]")
            raise ValueError(f"Usage: {sys.argv[0]} [--forgets|--no-forgets|--table [+|-]<prior|guesses|learns|slips|forgets>]")
    elif len(sys.argv) == 3 and sys.argv[1] == "--table":
        forgets = None
        focus = sys.argv[2]
        if focus.startswith("+") or focus.startswith("-"):
            subfocus = focus[1:]
        else:
            subfocus = focus
        if subfocus not in ["prior", "guesses", "learns", "slips", "forgets"]:
            print(f"Usage: {sys.argv[0]} --table [+|-]<prior|guesses|learns|slips|forgets>")
            raise ValueError(f"Usage: {sys.argv[0]} --table [+|-]<prior|guesses|learns|slips|forgets>")
    else:
        print(f"Usage: {sys.argv[0]} [--forgets|--no-forgets|--table [+|-]<prior|guesses|learns|slips|forgets>]")
        raise ValueError(f"Usage: {sys.argv[0]} [--forgets|--no-forgets|--table [+|-]<prior|guesses|learns|slips|forgets>]")

    train = "data/ct.csv"
    test = "data/ct.csv"
    metric = "accuracy"
    
    if forgets is None:
        print('Forgets ', end='')
        forget_model = create_model(train, test, True, metric)
        print('No Forgets ', end='')
        no_forget_model = create_model(train, test, False, metric)
        if focus.startswith("-"):
            func = min
        elif focus.startswith("+"):
            func = max
        else:
            func = max
        forget = reduce(forget_model.coef_, subfocus, func=func)
        no_forget = reduce(no_forget_model.coef_, subfocus, func=func)
        print_comparison_table(forget_model, no_forget_model, forget[0])
        if forget[0] != no_forget[0] and subfocus != "forgets":
            print_comparison_table(forget_model, no_forget_model, no_forget[0])
    else:
        model = create_model(train, test, forgets, metric)
        print_reduce("Easiest to learn: ", model.coef_, 'learns')
        print_reduce("Hardest to learn: ", model.coef_, 'learns', func=min)
        print_reduce("Easiest to guess: ", model.coef_, 'guesses')
        print_reduce("Hardest to guess: ", model.coef_, 'guesses', func=min)
        if forgets:
            print_reduce("Easiest to forget: ", model.coef_, 'forgets')
            print_reduce("Hardest to forget: ", model.coef_, 'forgets', func=min)

