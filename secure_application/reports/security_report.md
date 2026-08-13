# Lab Assignment 3 - Security Assessment Report

## 1. Application Details

**Application:** Drone Control System  
**Programming Language:** Python  
**SAST Tool:** Bandit 1.9.4  
**Python Version:** 3.14.4  
**Application Type:** Console-based Application  

## 2. Objective

The objective of this project is to develop a small Drone Control System
application with five core functionalities and intentionally introduce
security vulnerabilities for demonstration and SAST analysis.

## 3. Core Functionalities

The application provides the following functionalities:

1. Drone Login
2. Waypoint Upload
3. Mission Execution
4. Telemetry Display
5. Log Storage and Viewing

## 4. Security Vulnerabilities

### 4.1 Hardcoded Password

The application contains a username and password directly in the source
code.

Example:

`username == "admin" and password == "drone123"`

Bandit detected this as:

- Test ID: B105
- Issue: Hardcoded Password String
- Severity: Low
- Confidence: Medium

Evidence:

`screenshots/Hardcoded_password_and_process_with_shell.png`

### 4.2 Command Injection

The application uses `os.system()` to execute a command supplied by the user.

Bandit detected this as:

- Test ID: B605
- Issue: Starting a Process With a Shell
- Severity: High
- Confidence: High
- CWE: CWE-78

Evidence:

`screenshots/Hardcoded_password_and_process_with_shell.png`

### 4.3 Missing Authentication

The application does not verify authentication before allowing access to
certain drone operations such as waypoint upload and mission execution.

This vulnerability was identified through manual testing.

Evidence:

`screenshots/Login_authentication.png`

## 5. Bandit SAST Analysis

The following command was used to perform static analysis:

`bandit secure_application/src/drone_control.py`

The Bandit scan identified two security issues:

| Test ID | Vulnerability | Severity | Confidence |
|---|---|---|---|
| B105 | Hardcoded Password String | Low | Medium |
| B605 | Process With Shell / Command Injection | High | High |

The complete scan output is stored in:

`secure_application/sast/bandit_report.txt`

## 6. Manual Testing

Manual testing was performed to verify the application's security behaviour.

### Test 1: Missing Authentication

The application allowed waypoint operations without requiring the user to
log in first.

### Test 2: Improper Input Validation

Invalid waypoint input such as `hello` was accepted by the application
without proper format validation.

### Test 3: Command Execution

User-provided command input was passed to `os.system()`, demonstrating the
command injection risk.

Detailed test cases are available in:

`secure_application/testcases/test_cases.txt`

## 7. Evidence

Screenshots of application execution, authentication testing, vulnerability
demonstration, and Bandit results are stored in:

`secure_application/screenshots/`

## 8. Conclusion

The Drone Control System successfully demonstrates the required five core
functionalities. Static analysis using Bandit identified hardcoded password
usage and unsafe shell execution. Manual testing additionally demonstrated
missing authentication and improper input validation. The project therefore
demonstrates both SAST-based vulnerability detection and manual security
testing.
