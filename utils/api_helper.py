import requests

class APIHelper:
    """
    A helper class for making API requests using the requests library.

    Initialize it with a base_url. Use the methods for HTTP methods GET, PUT, PATCH,
    DELETE and POST to make requests. These methods wrap around the requests library
    methods and will raise an HTTPError if the request fails, unless you specify 
    raise_for_status=False.

    Example:
        api = APIHelper('https://my-api.com/')
        api.set_headers({
            'Authorization': 'Bearer {token}',
            'Content-Type': 'application/json',
            'Custom-Header': 'custom_value'
        })
        response = api.get('/my-endpoint')
    """

    def __init__(self, base_url):
        """
        Initialize the APIHelper with a base url.

        Args:
            base_url (str): The base URL for the API.
        """
        self.base_url = base_url
        self.session = requests.Session()
    
    def set_headers(self, headers):
        """
        Set the headers to be used in the session.

        Args:
            headers (dict): A dictionary of headers to add to the session.
        """
        self.session.headers.update(headers)

    def requset(self, method, endpoint, raise_for_status=True, **kwargs):
        """
        Make a request to the API.

        Args:
            method (str): The HTTP method for the request.
            endpoint (str): The API endpoint for the request.
            raise_for_status (bool): If True, raise an HTTPError if the response status is 4XX or 5XX.
            **kwargs: Arbitrary keyword arguments to pass to the request method.
        
        Returns:
            A Response object.
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        if raise_for_status:
            response.raise_for_status()
        return response
    
    def get(self, endpoint, raise_for_status=True, **kwargs):
        """
        Make a GET request to the API.

        Args:
            endpoint (str): The API endpoint for the request.
            raise_for_status (bool): If True, raise an HTTPError if the response status is 4XX or 5XX.
            **kwargs: Arbitrary keyword arguments to pass to the request method.
        
        Returns:
            A Response object.
        """
        return self.requset("GET", endpoint, raise_for_status, **kwargs)
    
    def put(self, endpoint, raise_for_status=True, **kwargs):
        """
        Make a PUT request to the API.

        Args:
            endpoint (str): The API endpoint for the request.
            raise_for_status (bool): If True, raise an HTTPError if the response status is 4XX or 5XX.
            **kwargs: Arbitrary keyword arguments to pass to the request method.
        
        Returns:
            A Response object.
        """
        return self.requset("PUT", endpoint, raise_for_status, **kwargs)
    
    def patch(self, endpoint, raise_for_status=True, **kwargs):
        """
        Make a PATCH request to the API.

        Args:
            endpoint (str): The API endpoint for the request.
            raise_for_status (bool): If True, raise an HTTPError if the response status is 4XX or 5XX.
            **kwargs: Arbitrary keyword arguments to pass to the request method.
        
        Returns:
            A Response object.
        """
        return self.requset("PATCH", endpoint, raise_for_status, **kwargs)
    
    def delete(self, endpoint, raise_for_status=True, **kwargs):
        """
        Make a DELETE request to the API.

        Args:
            endpoint (str): The API endpoint for the request.
            raise_for_status (bool): If True, raise an HTTPError if the response status is 4XX or 5XX.
            **kwargs: Arbitrary keyword arguments to pass to the request method.
        
        Returns:
            A Response object.
        """
        return self.requset("DELETE", endpoint, raise_for_status, **kwargs)
    
    def post(self, endpoint, raise_for_status=True, **kwargs):
        """
        Make a POST request to the API.

        Args:
            endpoint (str): The API endpoint for the request.
            raise_for_status (bool): If True, raise an HTTPError if the response status is 4XX or 5XX.
            **kwargs: Arbitrary keyword arguments to pass to the request method.
        
        Returns:
            A Response object.
        """
        return self.requset("POST", endpoint, raise_for_status, **kwargs)
    