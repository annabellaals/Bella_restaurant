# Testing Guide for Bella's Restaurant

This document provides instructions for running test cases for the Bella's Restaurant Django project. Testing ensures that the application functions as expected and helps identify any issues.

## Prerequisites

Before running tests, ensure you have the following:

- **Python**: Version 3.x
- **Django**: Version x.x (or the version specified in your `requirements.txt`)
- **Test dependencies**: Make sure you have installed all required packages.

To install dependencies, run:
```bash 
pip install -r requirements.txt
```

## Running Tests
### 1. Navigate to the Project Directory

Open your terminal or command prompt and change to the directory where your manage.py file is located:

```bash
cd path/to/your/project
```

### 2. Run the Test Suite

Use Django's built-in test runner to execute the test cases:

```bash
python manage.py test
```

This command will automatically discover and run all the test cases defined in your project.

### 3. Running Specific Tests

If you want to run tests for a specific app or test case, use the following syntax:

```bash
python manage.py test app_name
```
Or to run a specific test case:

```bash
python manage.py test app_name.tests.TestClass.test_method
```
### 4. View Test Results

After running the tests, you will see a summary of the test results in your terminal. The results will indicate which tests passed, failed, or were skipped.

## Writing Tests
For more information on writing tests, refer to the [Django Testing Documentation](https://docs.djangoproject.com/en/5.1/topics/testing/).

### Example Test
Here’s a simple example of a Django test case:

```python
from django.test import TestCase
from django.urls import reverse

class RestaurantViewTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
```

In this example, a test case checks if the home page returns a status code of 200 (OK).

## Continuous Integration
If you use a CI/CD tool (e.g., GitHub Actions, Travis CI, Jenkins), ensure your test suite runs automatically on code changes. Configure your CI/CD pipeline to include the test commands specified above.

## Troubleshooting
- Database Issues: Make sure your test database is properly set up. Django creates a test database automatically, but issues might arise if your database settings are incorrect.
- Dependency Errors: Verify that all dependencies are installed and compatible with your Django version.
- Test Failures: Review test output for details on failures and correct any issues in your code.

## Conclusion
Running tests is crucial for maintaining the quality and reliability of the Bella's Restaurant project. Regular testing helps catch bugs early and ensures that changes do not introduce new issues.

For further assistance or questions about testing, please contact the development team.