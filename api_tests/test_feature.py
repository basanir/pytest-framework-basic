import pytest


def test_httpbin_get(logger, api_helper):
    # Define test data
    input_params = {
        "foo": "bar",
    }
    expected_params = {
        "foo": "bar1",
    }

    # Make request
    response = api_helper.get("/get", params=input_params)

    # Log response
    logger.info(f"Response status code: {response.status_code}")

    # Verify response
    assert response.status_code == 200

    # Log response body
    logger.debug(f"Response body: {response.text}")

    # Verify response body
    response_body = response.json()
    # assert and if it fails print both actual and expected using logger object
    assert response_body["args"] == expected_params, logger.error(f"Expected params: {expected_params}, Actual params: {response_body['args']}")






    
    


