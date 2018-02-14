import math
def main():
	print("This program finds real  solution to a quadratic.\n")
	try : 
		a , b , c = eval(input("Please enter the coefficients(a,b,c):"))
		discRoot = math.sqrt(b * b - 4 * a * c)
		root1 = (-b + discRoot) / (2 * a)
		root2 = (-b - discRoot) / (2 * a)
		print("\nThe solution are:",root1,root2)
	except ValueError as excObj:
		if str(excObj) == "math domain error":
			print("No Real Roots.")
		else :
			print("You don't give me the right number of coefficients.")
	except NameError:
		print("\nYou didn't enter three numbers.")
	except TypeError:
		print("\nYour input was not in the correct form, Missing comma?")
	except : 
		print("\nSomething went wrong, sorry!")
		#else finally
main()	