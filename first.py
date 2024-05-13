
'''    Water-Jug solution using Breadth First Search Algorithm  '''

#                    AI Group Assignment 1

#            Group member's name        stud_id

#             1. Akrem Beshir             ugr/172051/12
#             2. Bereket Hailay           ugr/172072/12
#             3. Daniel Assefa            Mit/ur/301/12
#             4. Dibora Damtew            ugr/172595/12
#             5. Hayelom Fereja           Mit/ur/244/12





# ```` Check the README.md file for further Explanation ```` #





print ("Solution for water jug problem")

# These lines prompt the user to enter the capacities of Jug A and Jug B,
# as well as the target volumes for Jug A and Jug B. The inputs are read as
# integers and assigned to the respective variables.

x_capacity = int(input("Enter Jug A capacity:"))
y_capacity = int(input("Enter Jug B capacity:"))
end_x = int(input("Enter target volume of jug A:"))
end_y = int(input("Enter target volume of jug B:"))






# This line defines the bfs function, which takes the start state, end state, 
# and the capacities of the jugs as parameters.

def bfs(start, end, x_capacity, y_capacity):
	




    
#   These lines initialize the empty lists path, front, and visited.

#     - path will store the sequence of states visited during the search.
#     - front will serve as the queue to store the states that are yet to be explored. 
#        It is initialized with the start state.
#     - visited will keep track of the states that have been visited to avoid revisiting them.

	path = []
	front = []
	front.append(start)
	visited = []
	



#   This line starts a while loop that continues until the front queue is empty.
#   The condition not (not front) checks whether front is not empty.

# The lines retrieve the current state from the front of the queue (front) using the pop()function.
# The current state is a list where the first element represents the volume of Jug A (x) and
# the second element represents the volume of Jug B (y). 
# The current state is appended to the path list.

	while(not (not front)):
		current = front.pop()
		x = current[0]
		y = current[1]
		path.append(current)
		




# This block of code checks if the target volume (end) has been reached in either Jug A (x) 
# or Jug B (y). If the target volume is reached, it prints "Found!" and returns the path list,
# which represents the sequence of states leading to the solution.

		if x == end or y == end:
			print ("Found!")
			return path
		

# These lines implement Rule 1: If Jug A is not full, pour water into Jug A from a tap until it reaches 
# its capacity. It checks if pouring water to fill Jug A to its capacity will result in a new state 
# that has not been visited before. If so, the new state is added to the front queue and
# the visited list.

# These lines implement Rules 2, 3, 4, 5, and 6 of the water jug problem, similar to Rule 1. 
# Each rule checks a specific pouring operation and adds the resulting state to the front queue 
# and the visited list if it satisfies the conditions.

		# rule 1
		if current[0] < x_capacity and ([x_capacity, current[1]] not in visited):
			front.append([x_capacity, current[1]])
			visited.append([x_capacity, current[1]])

		# rule 2
		if current[1] < y_capacity and ([current[0], y_capacity] not in visited):
			front.append([current[0], y_capacity])
			visited.append([current[0], y_capacity])

		# rule 3
		if current[0] > x_capacity and ([0, current[1]] not in visited):
			front.append([0, current[1]])
			visited.append([0, current[1]])

		# rule 4
		if current[1] > y_capacity and ([x_capacity, 0] not in visited):
			front.append([x_capacity, 0])
			visited.append([x_capacity, 0])

		# rule 5
		#(x, y) -> (min(x + y, x_capacity), max(0, x + y - x_capacity)) if y > 0
		if current[1] > 0 and ([min(x + y, x_capacity), max(0, x + y - x_capacity)] not in visited):
			front.append([min(x + y, x_capacity), max(0, x + y - x_capacity)])
			visited.append([min(x + y, x_capacity), max(0, x + y - x_capacity)])

		# rule 6
		# (x, y) -> (max(0, x + y - y_capacity), min(x + y, y_capacity)) if x > 0
		if current[0] > 0  and ([max(0, x + y - y_capacity), min(x + y, y_capacity)] not in visited):
			front.append([max(0, x + y - y_capacity), min(x + y, y_capacity)])
			visited.append([max(0, x + y - y_capacity), min(x + y, y_capacity)])


	return "Not found"
# If no solution is found within the while loop, this line is reached, and the function returns the
#  string "Not found".





# This block defines the gcd function, which calculates the greatest common divisor (GCD)
# of two numbers using the Euclidean algorithm.

def gcd(a, b):
	if a == 0:
		return b
	return gcd(b%a, a)





start = [0, 0] 
end = end_x




# This block of code checks if the target volume (end) is a multiple of the greatest common divisor 
# (GCD) of the jug capacities (x_capacity and y_capacity). If it is, it calls the bfs function with 
# the provided inputs and prints the returned path. If the conditions are not met, it prints
# "No solution possible for this combination."

if end % gcd(x_capacity,y_capacity) == 0:
	print( bfs(start, end, x_capacity, y_capacity))
else:
	print ("No solution possible for this combination.")








