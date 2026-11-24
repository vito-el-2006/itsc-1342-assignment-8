# [Your Full Name] - Assignment 8 Unit Tests
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code')))
from solution import analyze_capture_records

# Fixed test fixture
mock_records = [
    {"src": "192.168.1.15", "dst": "8.8.8.8", "proto": "udp"},
    {"src": "192.168.1.15", "dst": "142.250.190.46", "proto": "tcp"},
    {"src": "192.168.1.15", "dst": "8.8.8.8", "proto": "udp"},
]

result = analyze_capture_records(mock_records)

# Test 1: Verify protocol count dictionary
assert result["protocols"] == {"UDP": 2, "TCP": 1}, "Failed Test 1: Protocol counts mismatch"

# Test 2: Verify unique destinations is a sorted list
assert result["unique_destinations"] == ["142.250.190.46", "8.8.8.8"], "Failed Test 2: Must be a sorted list"

# Test 3: Empty capture handling
empty_result = analyze_capture_records([])
assert empty_result["protocols"] == {}, "Failed Test 3: Check dictionary keys"

print("ALL UNIT TESTS PASSED - ASSIGNMENT 8")
