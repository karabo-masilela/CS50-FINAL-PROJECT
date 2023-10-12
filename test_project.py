import pytest
from project import validate_email, is_duplicate_email , generate_id

def main():
    test_validate_email()
    test_is_duplicate_email()
    test_generate_id()

# Test validate_email function
def test_validate_email():
   # True cases
    assert validate_email("karabo.masilela@upstreamcreatives.com") is True
    assert validate_email("john.doe@upstreamcreatives.com") is True

    # False cases
    assert validate_email("karabomasilela.com") is False  # Missing @
    assert validate_email("invalidemail@.com") is False  # Missing domain
    assert validate_email("karabo.masilela@gmail.com") is False  # Different domain

# Test is_duplicate_email function
def test_is_duplicate_email():
    employees = [
        {"Full Name": "Karabo Masilela", "Email": "karabo.masileal@upstreamcreatives.com", "Employee Code": "UC001"},
        {"Full Name": "Jane Smith", "Email": "jane.smith@example.com", "Employee Code": "UC002"},
        {"Full Name": "Mike Jordan", "Email": "mike.jordan@upstreamcreatives.com", "Employee Code": "UC003"},
        {"Full Name": "Drake Jonson", "Email": "drake.jonson@example.com", "Employee Code": "UC004"}
    ]

    assert is_duplicate_email("karabo.masileal@upstreamcreatives.com", employees) is True
    assert is_duplicate_email("new.employee@example.com", employees) is False
    assert is_duplicate_email("jane.smith@example.com", employees) is True
    assert is_duplicate_email("david.malen@edu.com", employees) is False


#Test generate_id()
def test_generate_id():
    assert generate_id(1)=="UC001"
    assert generate_id(100)=="UC100"
    assert generate_id(121)=="UC121"
    assert generate_id(5001)=="UC5001"



if __name__ == "__main__":
    main()
