import json

# Example test organisation strucutre json data
json_data =  '''[ { "name": "client", "parent": null, "config": {"has_fixed_membership_fee": false, "fixed_membership_fee_amount": 0} }, 
{ "name": "division_a", "parent": "client", "config": {"has_fixed_membership_fee": false, "fixed_membership_fee_amount": 0} }, 
{ "name": "division_b", "parent": "client", "config": {"has_fixed_membership_fee": true, "fixed_membership_fee_amount": 35000} }, 
{ "name": "area_a", "parent": "division_a", "config": {"has_fixed_membership_fee": true, "fixed_membership_fee_amount": 45000} }, 
{ "name": "area_b", "parent": "division_a", "config": {"has_fixed_membership_fee": false, "fixed_membership_fee_amount": 0} }, 
{ "name": "area_c", "parent": "division_b", "config": {"has_fixed_membership_fee": true, "fixed_membership_fee_amount": 45000} }, 
{ "name": "area_d", "parent": "division_b", "config": {"has_fixed_membership_fee": false, "fixed_membership_fee_amount": 0} }, 
{ "name": "branch_a", "parent": "area_a", "config": null }, 
{ "name": "branch_b", "parent": "area_a", "config": {"has_fixed_membership_fee": false, "fixed_membership_fee_amount": 0} }, 
{ "name": "branch_c", "parent": "area_a", "config": {"has_fixed_membership_fee": false, "fixed_membership_fee_amount": 0} }, 
{ "name": "branch_d", "parent": "area_a", "config": null },
{ "name": "branch_e", "parent": "area_b", "config": {"has_fixed_membership_fee": false, "fixed_membership_fee_amount": 0} }, 
{ "name": "branch_f", "parent": "area_b", "config": {"has_fixed_membership_fee": false, "fixed_membership_fee_amount": 0} },
{ "name": "branch_g", "parent": "area_b", "config": {"has_fixed_membership_fee": false, "fixed_membership_fee_amount": 0} }, 
{ "name": "branch_h", "parent": "area_b", "config": {"has_fixed_membership_fee": false, "fixed_membership_fee_amount": 0} },
{ "name": "branch_i", "parent": "area_c", "config": {"has_fixed_membership_fee": false, "fixed_membership_fee_amount": 0} }, 
{ "name": "branch_j", "parent": "area_c", "config": {"has_fixed_membership_fee": false, "fixed_membership_fee_amount": 0} }, 
{ "name": "branch_k", "parent": "area_c", "config": {"has_fixed_membership_fee": true, "fixed_membership_fee_amount": 25000} }, 
{ "name": "branch_l", "parent": "area_c", "config": {"has_fixed_membership_fee": false, "fixed_membership_fee_amount": 0} },
{ "name": "branch_m", "parent": "area_d", "config": null }, 
{ "name": "branch_n", "parent": "area_d", "config": {"has_fixed_membership_fee": false, "fixed_membership_fee_amount": 0} },
{ "name": "branch_o", "parent": "area_d", "config": {"has_fixed_membership_fee": false, "fixed_membership_fee_amount": 0} }, 
{ "name": "branch_p", "parent": "area_d", "config": {"has_fixed_membership_fee": false, "fixed_membership_fee_amount": 0} } ]'''

# sort json data into a list
org_structure = json.loads(json_data)


# function to find the parent of the passed in child
def find_parent(child):   
    # iterate through the org_structure list
    for unit in org_structure:
        # check if the current units name matches the childs parent name
        if unit["name"] == child["parent"]:
            # return the found parent
            return unit
    # if no parent is found return None
    return None

# function to find the fixed mebership fee amount
def find_fee(parent):
    # checks if the parent config contains a fee
    if parent["config"]["has_fixed_membership_fee"] == True:
        # if it does return the fee amount
        return parent["config"]["fixed_membership_fee_amount"]
    else:
        # if no fee is found return None
        return None


# main function to calculate the mebership fee
def calculate_membership_fee(rent_amount, rent_period, organisation_unit):
    # check that the given rent is within the right parameters
    if rent_period == "week" and 25 <= rent_amount <= 2000 or rent_period == "month" and 110 <= rent_amount <= 8660:
        # check that the passed in organisation unit does not have a config or has a config and the "has_fixed_membership_fee" is set to False
        if organisation_unit["config"] is None or organisation_unit["config"]["has_fixed_membership_fee"] is False:
            
            # set current child as the passed in organisation unit
            current_child = organisation_unit
            # set the found fee flag as False 
            found_fee = False

            # continue running the loop whilst there is a current child and the fee hasnt been found
            while current_child != None and found_fee is False:
                # call the find parent function to find the parent of the current child
                found_parent = find_parent(current_child)
                # if the parent is found
                if found_parent != None:
                    # if the the fixed fee has been found on the parent
                    if find_fee(found_parent) != None:
                        # return the fixed fee from the parents config
                        return found_parent["config"]["fixed_membership_fee_amount"]
                        # sets the found fee to True ending the whilst loop
                        found_fee = true
                    else:
                        # carries on the while loop by setting the new current child to the found parent
                        current_child = found_parent
                else:
                    # if a fee is never found calculate the fee based on the weekly amount + 20% VAT
                    if rent_amount <= 120:
                        return 120 * 1.2
                    elif rent_period == "week":
                        return rent_amount * 1.2
                    else:
                        # breaks the monthly amount down to weekly amount so it can be calculated
                        return (rent_amount/4)*1.2


        else:
            # if the organisation unit already has a fixed fee amount return the fixed fee amount 
            return organisation_unit["config"]["fixed_membership_fee_amount"]
    else: 
        # print error message and return -1
        print("Error rent amount is outside of range")
        return -1






 
    
    
    
    