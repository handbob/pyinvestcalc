# pyinvestcalc

`pyinvestcalc` is a Python-based automation testing suite leveraging Playwright. It automates validation for an inflation calculator, ensuring accurate user interaction handling and robust performance.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Features](#features)
- [Running Tests](#running-tests)

## Requirements

- [Python]("https://www.python.org/")
- [Playwright]("https://playwright.dev/python/")
- [pytest-clarity]("https://github.com/darrenburns/pytest-clarity")
- [pytest-html]("https://github.com/pytest-dev/pytest-html")

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/handbob/pyinvestcalc.git
    cd pyinvestcalc
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Install Playwright dependencies:
    ```bash
    playwright install
    ```

## Features

- Automated browser testing using Playwright.
- Handles real-world scenarios like cookie consent, form input validation, and dropdown selection.
- Takes screenshots at every step for test documentation.
- Validates calculations and displayed results.

## Running Tests

To run the tests, use the `pytest` framework:

```bash
pytest --tb=short -vv -rA --html=report.html --self-contained-html
```

## Report

a) view "screenshots" in created folder   
b) open in browser "report.html"
