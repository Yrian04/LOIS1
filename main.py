import src.logical_formula as lf


string = input("Enter formula: ")
f = lf.get_logical_formula_from_string(string)
if lf.is_formula_impossible(f):
    print("Formula is impossible")
else:
    print("Formula is possible")
