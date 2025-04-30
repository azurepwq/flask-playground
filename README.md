# Flask Playground

## Setup

1. Create a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app (after you create it):
   ```bash
   flask run
   ```

## Testing

### Test Case Design
When teaching someone to write test cases, it's important to cover:
- Normal/Happy path (expected use)
- Edge cases (unusual but possible inputs)
- Negative cases (invalid or missing input)
- Format/Content (is the output as expected?)

1. Test: Greet with a normal name
Description: Test the endpoint with a typical name.
Input: GET /api/greet/Alice
Expected Output: JSON: {"message": "Hello, Alice!"}, HTTP 200
2. Test: Greet with an empty name
Description: Test the endpoint with an empty string as the name.
Input: GET /api/greet/
Expected Output: 404 Not Found (because the route requires a <name> parameter)
3. Test: Greet with special characters
Description: Test the endpoint with a name containing special characters.
Input: GET /api/greet/John-Doe_123
Expected Output: JSON: {"message": "Hello, John-Doe_123!"}, HTTP 200
4. Test: Greet with URL-encoded characters
Description: Test the endpoint with a name that includes URL-encoded characters (e.g., space as %20).
Input: GET /api/greet/John%20Doe
Expected Output: JSON: {"message": "Hello, John Doe!"}, HTTP 200
5. Test: Greet with a very long name
Description: Test the endpoint with a very long string as the name.
Input: GET /api/greet/ followed by a long string (e.g., 256 characters)
Expected Output: JSON: {"message": "Hello, <long string>!"}, HTTP 200
6. Test: Wrong HTTP method
Description: Test the endpoint with a method other than GET (e.g., POST).
Input: POST /api/greet/Alice
Expected Output: 405 Method Not Allowed

```bash
curl http://localhost:4000/api/greet/John
```

Example Test Case Table
| Test Case # | Description            | Input                       | Expected Output                          |
| ----------- | ---------------------- | --------------------------- | ---------------------------------------- |
| 1           | Normal name            | GET /api/greet/Alice        | 200, {"message": "Hello, Alice!"}        |
| 2           | Empty name             | GET /api/greet/             | 404 Not Found                            |
| 3           | Special characters     | GET /api/greet/John-Doe_123 | 200, {"message": "Hello, John-Doe_123!"} |
| 4           | URL-encoded characters | GET /api/greet/John%20Doe   | 200, {"message": "Hello, John Doe!"}     |
| 5           | Very long name         | GET /api/greet/<long_name>  | 200, {"message": "Hello, <long_name>!"}  |
| 6           | Wrong HTTP method      | POST /api/greet/Alice       | 405 Method Not Allowed                   |

### Explanation for a New Tester
- Test Case 1 checks the most common use: a normal name.
- Test Case 2 checks what happens if the required parameter is missing.
- Test Case 3 ensures the app handles names with dashes, underscores, and numbers.
- Test Case 4 checks if URL encoding is handled (important for names with spaces).
- Test Case 5 tests the system's behavior with unusually long input.
- Test Case 6 ensures only the allowed HTTP method works.