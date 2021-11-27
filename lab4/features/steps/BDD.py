import sys
sys.path.insert(0, "C:/Users/Andrew/Desktop/BKIT_UNIVERSITY/lab1")

from behave import *
from qr import get_roots_b

@given('I put roots {roots} into the function')
def step_impl(context, roots: str):
	roots = list(map(
		int, roots.replace("[", "")
		.replace("]", "")
		.split(", ")))
    
	context.result = get_roots_b(roots)

@then('I get roots {result}')
def step_impl(context, result: str):
	result = list(map(
		float, result.replace("[", "")
		.replace("]", "")
		.split(", ")))
  	
	assert context.result == result