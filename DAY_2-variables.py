values = [10, 20, 30]
result = 0

def process_data(data, multiplier=2):
    temp = data
    temp.append(40)

    def inner_function():
        values = [100]
        nonlocal result
        result = sum(temp) * multiplier

    inner_function()
    return result

original_id = id(values)
print(f"Before: values={values}, result={result}, id={original_id}")

output = process_data(values)
print(f"After: values={values}, result={result}, id={id(values)}")
print(f"Output: {output}, Same object? {original_id == id(values)}")


1.Explain what happens if  Line B  is changed to  temp = [100]  instead
	a)values = [100] does not modify the global values.It only shadows it inside inner_function.
	b)If changed to temp = [100], this does NOT change the original list anymore — because now temp is just 	  pointing to a new list, breaking the link.

2.Explain what happens if  Line C  uses  global result  instead of  nonlocal result
	a)global result updates the module-level result
	b)nonlocal result would connect to a variable in the enclosing function

3.Explain what  Line D  demonstrates about variable types
	a)he name result now refers to a list, not a number
	b)Lists can contain other lists
	c)The inner list is a reference, not a copy
	d)If values changes later, the version inside result changes too

Variable binding:
Names simply point to objects in memory, and reassignment only changes what the name points to.

Mutability:
Mutable objects (like lists) can be changed in-place, so updates inside functions affect the same object outside.

Scope resolution (LEGB):
Python looks for variables in Local → Enclosing → Global → Built-in order, deciding which variable a name refers to.
