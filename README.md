## Update Booking Endpoint Testing

This script illustrates how to utilize Python to update bookings through the RESTful Booker API.

### Overview

The script employs a PUT request to modify a booking with the provided data. It integrates Basic authentication credentials within the request headers.

### Requirements

- Python 3.x
- `requests` library

### Usage

1. Copy the script into a Python file (e.g., `testscenarios.py`).
2. Adjust the script with the relevant Base URL, booking ID, data, and headers.
3. Execute the script using the command:
    ```
    python testscenarios.py
    ```

### Script Explanation

- **Base URL**: The base URL of the booking system API.
- **Function `updatebooking()`**: Dispatches a PUT request to update a booking.
- **Positive Test Scenario**: Updates a booking with valid data and authentication.
- **Negative Test Scenario**: Endeavors to update a booking with an invalid booking ID.
- **Additional Scenarios**: Test scenarios for absent fields and inappropriate data types.

### Test Scenarios

#### Positive Test Scenario

- Updates a booking with valid data and authentication.
- Validates the response status code and JSON response.
- A status code of 200 confirms successful booking updates.
- A status code of 403 suggests authentication issues or insufficient permissions.

#### Negative Test Scenario

- Tries to update a booking with an invalid booking ID.
- Validates the response status code and error message.
- A status code of 405 verifies the invalidity of the ID.

#### Additional Scenarios

- **Missing Fields Scenario**: Tries to update a booking with absent required fields.
    - Validates the response status code and error message.
    - A status code of 400 indicates a bad request due to missing fields.

- **Invalid Data Types Scenario**: Tries to update a booking with inappropriate data types.
    - Validates the response status code and error message.
    - A status code of 500 signifies an internal server error due to invalid data types.

### Implementation Details

- The script adopts Basic authentication with hardcoded username and password encoded in Base64.

### Contributors

- Asule Jonathan

### License

This project is licensed under the [MIT License](LICENSE).
