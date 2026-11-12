# L6_L7_51 — Self Storage

## Lab 7: Fuzz Testing

## About

This project demonstrates fuzz testing using the Hypothesis library to identify input validation issues in a Python-based Self Storage application.

The application parses rental details, calculates average rental durations and determines payable rent after discounts.

The application was updated to handle invalid inputs safely, and the fuzz tests were executed again to verify the fixes.

## Files

| File | Description |
|---|---|
| `self_storage.py` | Updated application with input validation |
| `test_self_storage.py` | Hypothesis-based fuzz testing script |
| `Lab7_Fuzz_Testing_Report.pdf` | Lab report containing screenshots, test results and explanations |

## Testing

The application was tested using pytest and Hypothesis.

All three fuzz testing functions passed after the application was fixed.

**Result:** 3 tests passed.