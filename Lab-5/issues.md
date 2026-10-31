\# LAB 5: STATIC CODE ANALYSIS

\## Parking Lot System — Issue Log



\### 1. Overview



The original parking lot program was analyzed using Pylint, Bandit, and Flake8. Several security, reliability, and code-quality issues were identified and fixed.



\---



\### 2. Issues Identified and Fixes



\*\*ISSUE 1: Shell Command Execution\*\*



\- \*\*Category:\*\* Security — High

\- \*\*Original location:\*\* Line 64

\- \*\*Problem:\*\* `os.system()` executed a shell command using the supplied filename, creating a potential command-injection risk.

\- \*\*Fix:\*\* Removed shell execution and used `print()` to display the export confirmation.



\*\*ISSUE 2: Weak MD5 Hash\*\*



\- \*\*Category:\*\* Security — High

\- \*\*Original location:\*\* Line 53

\- \*\*Problem:\*\* MD5 is considered cryptographically weak.

\- \*\*Fix:\*\* Replaced MD5 with SHA-256 using UTF-8 encoding.



\*\*ISSUE 3: Unsafe `eval()`\*\*



\- \*\*Category:\*\* Security — Medium

\- \*\*Original location:\*\* Line 48

\- \*\*Problem:\*\* `eval()` executed a string as Python code, potentially allowing unintended code execution.

\- \*\*Fix:\*\* Replaced expression evaluation with numeric surge-multiplier validation and direct fee calculation.



\*\*ISSUE 4: Insecure PIN Generation\*\*



\- \*\*Category:\*\* Security — Low

\- \*\*Original location:\*\* Line 57

\- \*\*Problem:\*\* `random.randint()` is not designed for security-sensitive random values.

\- \*\*Fix:\*\* Used `secrets.randbelow()` to generate a four-digit PIN.



\*\*ISSUE 5: Broad Exception Handling\*\*



\- \*\*Category:\*\* Reliability and Code Quality

\- \*\*Original location:\*\* Lines 32–33

\- \*\*Problem:\*\* A bare `except` silently suppressed errors when releasing a parking slot.

\- \*\*Fix:\*\* Removed the broad exception handler and explicitly checked whether the requested slot exists.



\*\*ISSUE 6: Mutable Default Argument\*\*



\- \*\*Category:\*\* Reliability and Code Quality

\- \*\*Original location:\*\* Line 15

\- \*\*Problem:\*\* Using `entry\_logs=\[]` could cause a list to be shared across function calls.

\- \*\*Fix:\*\* Changed the default to `None` and initialized a list when needed.



\*\*ISSUE 7: Unused Imports and Variables\*\*



\- \*\*Category:\*\* Code Quality

\- \*\*Original locations:\*\* Multiple

\- \*\*Problem:\*\* Unused imports and variables made the code less clear.

\- \*\*Fix:\*\* Removed unused imports and variables.



\*\*ISSUE 8: Naming and Formatting\*\*



\- \*\*Category:\*\* Style

\- \*\*Original locations:\*\* Multiple

\- \*\*Problem:\*\* Function names did not follow `snake\_case`, some lines were too long, and documentation was missing.

\- \*\*Fix:\*\* Renamed functions, added docstrings, and corrected formatting.



\*\*ISSUE 9: File Handling\*\*



\- \*\*Category:\*\* Reliability and Code Quality

\- \*\*Original location:\*\* Lines 61–62

\- \*\*Problem:\*\* The manifest file was opened without a context manager or an explicit encoding.

\- \*\*Fix:\*\* Used `with open(..., encoding="utf-8")` for safer file handling.



\---



\### 3. Verification Results



\*\*Pylint\*\*

\- Before: 4.10/10

\- After: 9.85/10

\- Result: Target above 9.5 achieved.



\*\*Bandit\*\*

\- Before: 5 potential findings.

\- After: No issues identified.

\- Result: Security scan passed.



\*\*Flake8\*\*

\- Before: Formatting and code-quality violations were reported.

\- After: No violations were reported.

\- Result: Style checks passed.



The updated program was executed successfully. All three static analysis tools were rerun, and their before-and-after reports were saved.



\---



\### 4. Conclusion



The static analysis process improved the parking lot program's readability, maintainability, and security. The updated code achieved a Pylint score above the required threshold and produced no reported Bandit or Flake8 findings.

