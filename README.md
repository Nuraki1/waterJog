# Water-jug-problem
# Ethiopian Institure of Technology - Mekelle  (EIT-M)
# AI Group Assignment 1:  Water-jug-problem



|S.No. |Group's name	                | Stud_id            ||
|------|-----------------------|-----------------------|------|
| 1.   |	Akrem Beshir                |  ugr/172051/12   |  |
| 2.   |	Bereket Hailay              |  ugr/172072/12   |  |
| 3.   |	Daniel Assefa	            |  Mit/ur/301/12   |  |
| 4.   |	Dibora Damtew	            |  ugr/172595/12   |  |
| 5.   |	Hayelom Fereja	            |  Mit/ur/244/12   |  |




 
 
- In the water jug problem in Artificial Intelligence,  provided two jugs: 
- one having the capacity to hold 3 gallons of water and the other has the capacity to hold 4 gallons of water.
- There is no other measuring equipment available and the jugs also do not have any kind of marking on them. So, the agent’s task here is to fill one of the jugs with 2 gallons of water by using only these two jugs and no other material. Initially, both our jugs are empty.
 
 ## Production rules for solving the water jug problem
We have used in this project only the 6 production rules from the following specified ones.
Here, let x denote the 4-gallon jug and y denote the 3-gallon jug.

| S.No. |	Initial State	| Condition    |	Final state  |	Description of action taken                                          |
|-------|---------------|--------------|--------------|----------------------------------------------------------------------|
| 1.    |	(x,y)	        | If x<4	      | (4,y)	       | Fill the 4 gallon jug completely                                     |
| 2.    |	(x,y)         |	if y<3       |	(x,3)	       | Fill the 3 gallon jug completely                                     |
| 3.	   |(x,y)	         | If x>0	      | (x-d,y)	     | Pour some part from the 4 gallon jug                                 |
| 4.	   | (x,y)	        | If y>0	      | (x,y-d)	     | Pour some part from the 3 gallon jug                                 |
| 5.    |	(x,y)	        | If x>0	      | (0,y)	       | Empty the 4 gallon jug                                               |
| 6.	   |(x,y)	         | If y>0	      | (x,0)        |	Empty the 3 gallon jug                                               |
| 7.	   |(x,y)	         | If (x+y)<7	  | (4, y-[4-x])	| Pour some water from the 3 gallon jug to fill the four gallon jug    |
| 8.	   |(x,y)	         | If (x+y)<7	  | (x-[3-y],y)	 |Pour some water from the 4 gallon jug to fill the 3 gallon jug.       |
| 9.	   |(x,y)	         | If (x+y)<4	  | (x+y,0)	     |Pour all water from 3 gallon jug to the 4 gallon jug                  |
| 10.	  |(x,y)	         |if (x+y)<3	   | (0, x+y)	    |Pour all water from the 4 gallon jug to the 3 gallon jug              |



### Solution of water jug problem according to the production rules
|S.No.	| 4 gallon jug contents	| 3 gallon jug contents |	Rule followed |
|------|-----------------------|-----------------------|---------------|
| 1.   |	0 gallon              |	0 gallon	             | Initial state |
| 2.   |	0 gallon              |	3 gallons	            | Rule no.2     |
| 3.   |	3 gallons	            | 0 gallon	             | Rule no. 9    |
| 4.   |	3 gallons	            | 3 gallons	            | Rule no. 2    |
| 5.   |	4 gallons	            | 2 gallons	            | Rule no. 7    |


On reaching the 5th attempt, we reach a state which is our goal state. Therefore, at this state, our problem is solved.
