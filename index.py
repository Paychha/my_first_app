# Import the necessary module
import http.server
import socketserver

# Set the port number
PORT = 8000

# Define the handler to use for serving requests
Handler = http.server.SimpleHTTPRequestHandler

# Create the server and bind it to the specified port
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")

    # Start the server
    httpd.serve_forever()
