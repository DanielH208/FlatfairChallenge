import pytest
from CalculateMembershipFee import calculate_membership_fee

# test to see if the monthly fee amount will be calculated as none of the parents have a fixed fee amount
def test_parent_no_fixed_membership_fee_month():
    assert calculate_membership_fee(8000,"month",{"name": "branch_e", "parent": "area_b", "config": None} ) == 2400

# test to see if the weekly fee amount will be calculated as none of the parents have a fixed fee amount
def test_parent_no_fixed_membership_fee_week():
    assert calculate_membership_fee(1000,"week",{"name": "branch_e", "parent": "area_b", "config": None} ) == 1200

# test to see if the parent of the unit will output its fixed membership fee amount
def test_first_parent_has_fixed_membership_fee():
    assert calculate_membership_fee(4000,"month",{ "name": "branch_i", "parent": "area_c", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} } ) == 45000

# test to see if the grand parent of the unit will output its fixed membership fee amount
def test_second_parent_has_fixed_membership_fee():
     assert calculate_membership_fee(4000,"month",{ "name": "branch_p", "parent": "area_d", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} } ) == 35000

# test to see if the units fixed membership fee amount will be outputted
def test_unit_has_fixed_membership_amount():
    assert calculate_membership_fee(4000,"month",{ "name": "branch_k", "parent": "area_c", "config": {"has_fixed_membership_fee": True, "fixed_membership_fee_amount": 25000} } ) == 25000

# test to see if the week input will be rejected because it is below the allowed range 
def test_week_input_below_range():
     assert calculate_membership_fee(24,"week",{ "name": "branch_p", "parent": "area_d", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} } ) == -1

# test to see if the week input will be rejected because it is above the allowed range 
def test_week_input_above_range():
     assert calculate_membership_fee(2001,"week",{ "name": "branch_p", "parent": "area_d", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} } ) == -1 

# test to see if the month input will be rejected because it is below the allowed range 
def test_month_input_below_range():
     assert calculate_membership_fee(109,"month",{ "name": "branch_p", "parent": "area_d", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} } ) == -1 

# test to see if the month input will be rejected because it is above the allowed range 
def test_month_input_above_range():
     assert calculate_membership_fee(8661,"month",{ "name": "branch_p", "parent": "area_d", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} } ) == -1 