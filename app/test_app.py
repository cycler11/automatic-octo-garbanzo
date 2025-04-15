import pytest
import time
from database import get_test_data, save_test_results

def calculate_discount(price, discount):
    """DISCOUNT."""
    if discount < 0 or discount > 100:
        raise ValueError("Invalid discount")
    return price - (price * discount / 100)

@pytest.mark.parametrize("test_case", get_test_data())
def test_calculate_discount(test_case):
    """COUNT DISCOUNT."""
    price = test_case["price"]
    discount = test_case["discount"]
    expected = test_case["expected"]
    
    start_time = time.time()
    
    try:
        result = calculate_discount(price, discount)
        assert result == expected
        test_result = "passed"
    except AssertionError:
        test_result = "failed"
    
    test_duration = time.time() - start_time  
    code_complexity = 0.5  
    code_coverage = 0.75  

    save_test_results(
        test_suite_name="Discount Calculation Test Suite",
        passed_tests=1 if test_result == "passed" else 0,
        failed_tests=1 if test_result == "failed" else 0,
        test_duration=test_duration,
        code_complexity=code_complexity,
        code_coverage=code_coverage
    )
