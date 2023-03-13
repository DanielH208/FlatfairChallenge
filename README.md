Project structure:

CalculateMembershipFee.py contains the main function calculate_membership_fee and the two smaller functions find_parent and find_fee.
test_CalculateMembershipFee.py contains 9 pytest unit tests that check the core functionality of the code.


calculate_membership_fee explanation:
![AlgorithmFlowchart](https://user-images.githubusercontent.com/80534190/224841481-0e6cb273-a9a1-45f5-b6ee-bb039d751270.JPG)


find_parent function explanation:

Function takes in a child parameter it then iterates through the org_structure list checking each iteration if the current units name matches the passed in child’s parents name. If it does it means that current unit is the parent and so it returns the current unit. If the for loop iterates all the way through and doesn’t find a matching unit then the function returns None.

find_fee function explanation:

Function takes in a parent parameter it then checks if the parent config has_fixed_membership_fee value is equal to true. If it does then the function returns the parents config has_fixed_membership_fee value. If the parent config has_fixed_membership_fee value isn’t set to true, then the function returns None.



Testing:

See test_CalculateMembershipFee.py for the 9 unit tests.

Test data used is the provided example test organisation structure config. I’ve added an extra parent tag on each unit to allow for traversal up the tree. 
See below for test results:
![PassedTests](https://user-images.githubusercontent.com/80534190/224841597-bebe96dd-55a5-4206-b0e1-75b77ee5713e.JPG)



Considerations for future iterations:

There are two main areas where the program could be improved for future iterations.


Code improvements:

Expanding the data model with extra tags such as a child so you can traverse down the data model as well as up. For example, this would allow you to list all the units that belong to an area, division, client.

Adapting the function so you can pass in just the organisational units name instead of passing in the whole instance of the organisational unit. This would be much easier for the user to provide and would also reduce the potential for user input errors.

Adding a function to pass in the Json data. This would mean you could easily flip between data models from external files. In a real-world scenario this would help support multiple clients under the same application.

Adding more validation checks using try catch blocks. For example, checking missing or wrong fields in the past in organisational unit. This would improve the overall program robustness.


Test improvements:

Expanding test data to test all paths of the code. For example, you could add a client with a fixed fee to test this scenario. 

Expanding the test suite to test more values on the boundaries. For example, checking all the edge values such as those included in the greater / less than or equals too checks.
