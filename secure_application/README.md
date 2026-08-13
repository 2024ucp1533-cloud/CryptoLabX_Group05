# Drone Control System

## 1. Introduction

This project implements a small console-based Drone Control System in Python.
The application is developed as part of Lab Assignment 3 to demonstrate
application functionalities and security vulnerabilities using Static
Application Security Testing (SAST).

The SAST tool used for this project is Bandit.

## 2. Core Functionalities

The application provides the following five core functionalities:

1. Drone Login
2. Waypoint Upload
3. Mission Execution
4. Telemetry Display
5. Log Storage and Viewing

## 3. Technologies Used

- Programming Language: Python
- SAST Tool: Bandit 1.9.4
- Python Version: 3.14.4
- Application Type: Console-based application

## 4. Vulnerabilities Demonstrated

Three security vulnerabilities are demonstrated in the application:

### 4.1 Hardcoded Password

The username and password are directly written inside the source code.

Bandit detected this vulnerability as:

- ID: B105
- Severity: Low
- Confidence: Medium

### 4.2 Command Injection

The application uses `os.system()` with user-controlled input for mission
execution. This allows a user to provide an operating system command.

Bandit detected this vulnerability as:

- ID: B605
- Severity: High
- Confidence: High

### 4.3 Missing Authentication

The application does not verify whether a user is logged in before allowing
access to functions such as waypoint upload, mission execution, telemetry,
and log viewing.

This vulnerability was identified through manual testing.

## 5. SAST Analysis

Bandit was executed on the application using:

```bash
bandit secure_application/src/drone_control.py
