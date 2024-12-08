# Testing Guide for Bella's Restaurant

This document provides instructions for running test cases for the Bella's Restaurant Django project. Testing ensures that the application functions as expected and helps identify any issues.

### **Testing Framework**
The website uses the Django testing framework along with some JavaScript testing libraries to ensure that all features and functionalities are working as expected. Below is a breakdown of the testing strategies:

### **Unit Testing**
Unit tests are written to test individual components of the application, ensuring that each function behaves as expected. The following areas have been thoroughly tested:

1. **Form Validation**:
   - Ensures that forms prevent the entry of negative values where not allowed (e.g., negative quantities or reservation numbers).
   - Tests include verifying that fields like `number of people` in a reservation are correctly validated.

2. **Model Tests**:
   - The database models are tested to verify that the relationships between models (e.g., User, Orders, Reservations) function correctly.
   - Tests verify CRUD operations (Create, Read, Update, Delete) for all entities such as users, orders, and reservations.

3. **View Tests**:
   - Ensures that views are returning the correct HTTP responses, including redirections, status codes, and rendering of templates.
   - Test views for both logged-in users and non-logged-in users, ensuring the proper functionality based on user roles (Admin, Manager, Customer).

4. **API Tests (if applicable)**:
   - For any REST API endpoints (e.g., for retrieving menu items, placing orders), the endpoints are tested to ensure correct HTTP methods (GET, POST, PUT, DELETE) are used.
   - Tests also ensure proper data handling and response format (JSON or others).

5. **CRUD Operation Tests**:
   - Tests cover CRUD operations on items such as food products, orders, table reservations, and user profiles.
   - Ensure that notifications are triggered correctly when updates or deletions occur.

6. **Notification System**:
   - Tests to verify that CRUD notifications are shown to the users when changes are made to their reservations, orders, or personal details.

### **Integration Testing**
Integration tests verify that the components of the website work together as expected. Specific scenarios tested include:

1. **Customer Flow**:
   - Test the full user journey from browsing the menu to placing an order and making a reservation.
   - Ensures that user inputs (e.g., selecting a dish, confirming reservation details) trigger the correct actions and update the backend correctly.

2. **Admin Flow**:
   - Ensures that admin functionalities (adding food, managing reservations, generating reports) are fully integrated and tested across multiple views.

3. **Error Handling**:
   - Verifies that error messages are shown correctly when users input incorrect data or try to access unauthorized pages.

### **End-to-End (E2E) Testing**
End-to-End tests simulate user interactions with the website, ensuring that all parts of the system work together smoothly. This includes:

1. **User Interaction**:
   - Simulates user interactions with the UI (e.g., filling out forms, clicking buttons, navigating between pages).
   - Verifies that expected results occur after each user interaction (e.g., successful reservation, order placement, or profile update).

2. **Cross-Browser Testing**:
   - Tests to ensure the site is responsive and functional across different browsers (Chrome, Firefox, Safari, Edge).
   - Ensures consistent user experience and layout across all supported browsers.

3. **Mobile Responsiveness**:
   - Simulates user actions on mobile devices to ensure that all functionalities are accessible and usable on different screen sizes.
   
4. **Performance Testing**:
   - Tests the site's speed and response times, particularly for critical features like placing orders and making reservations.
   - Identifies potential performance bottlenecks or areas for optimization.

### **Manual Testing**
Manual testing is performed in addition to automated testing, especially for complex user flows and features such as:

1. **Form Submission and Validation**:
   - Manually test form validation logic, ensuring that users cannot submit invalid data (e.g., negative reservation numbers).
   - Verifies error messages are shown when users try to submit invalid forms.

2. **User Role Permissions**:
   - Verify that role-based permissions are enforced, such that only Admins can perform administrative actions and Managers can handle orders.


### **Test Coverage**
Test coverage tools are used to ensure that all critical code paths are tested. Coverage is measured across:

- **Backend models and views**
- **Frontend form validation and interactions**
- **API endpoints**

---

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
