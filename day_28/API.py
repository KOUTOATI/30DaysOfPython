# The API ( Application Programming Interface ) is a set of rules and protocols for building and interacting with software applications. 
# It defines the methods and data formats that applications can use to communicate with each other.

# to build an API, you typically need to:
# 1. Define the endpoints: These are the URLs that clients will use to access your API.
# 2. Define the methods: These are the HTTP methods (GET, POST, PUT, DELETE) that clients can use to interact with your API.
# 3. Define the data formats: This includes the request and response formats, typically in JSON or XML.
# 4. Implement the logic: This is where you write the code that will handle the requests and return the appropriate responses.
# 5. Test the API: Ensure that it works as expected and handles errors gracefully.

#HTTP definitions :
#HTTP (Hypertext Transfer Protocol) is the foundation of data communication on the web. It defines how messages are formatted and transmitted, and how web servers and browsers should respond to various commands.
# HTTP is a request-response protocol, meaning that a client (like a web browser) sends a request to a server, which then processes the request and sends back a response.



# HTTP methods:
# - GET: Retrieve data from the server.
# - POST: Send data to the server to create a new resource.
# - PUT: Update an existing resource on the server.
# - DELETE: Remove a resource from the server.

# HTTP headers:
# - Content-Type: Indicates the media type of the resource (e.g., application/json).
# - Authorization: Contains credentials for authenticating the client with the server.
# - Accept: Specifies the media types that the client is willing to receive from the server.
# - User-Agent: Contains information about the client software making the request.
# HTTP status codes are issued by a server in response to a client's request made to the server. They represent the outcome of the request.

# HTTP body:
# The body of an HTTP request or response contains the data being sent. In a request, it might include form data or JSON payloads, while in a response, it typically contains the requested resource or an error message.

# HTTP status codes:
# - 200 OK: The request was successful.
# - 201 Created: A new resource was successfully created.
# - 204 No Content: The request was successful, but there is no content to return
# - 400 Bad Request: The server could not understand the request due to invalid syntax.
# - 404 Not Found: The requested resource could not be found.
