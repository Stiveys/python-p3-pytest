# lib/testing/test_not_none.py

def test_not_none():
    from not_none_functions import your_function  # Import the function you want to test
    result = your_function()  # Call the function
    assert result is not None  # Ensure the result is not None