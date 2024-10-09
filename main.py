import socket

# Try this with example.com first, but try changing it to a different site after
# you get it working.
hostname = "example.com"


# Do not modify this function
def make_http_request(ip, port):
  global hostname
  # First we set up a socket. AF_INET means we're using IP, and SOCK_STREAM means
  # we're using TCP.
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # Then we connect to the desired IP and port.
  client.connect((ip, port))
  # Now, because our connection is setup, we can send an HTTP request. Specifically,
  # we're sending an HTTP GET request because we want to "get" the page. There are
  # also a few more calls to functions to encode the data correctly, but the crucial
  # part here is the formatting of string with the "GET / HTTP/1.1 ..." text.
  client.send(
      bytes(f"GET / HTTP/1.1\r\nHost: {hostname}\r\n\r\n", encoding="utf-8"))

  # Finally we read and decode the response. 8192 here roughly means read up to 8192
  # characters in the HTTP response. If the length is longer than 8192, this will
  # only read the first 8192 characters and no more.
  response = client.recv(8192)
  return response.decode()


# Write your code below here for A08
# You shouldn't need to import anything else besides socket which is already included

# Firstly, find the function to return an ip address from whatever the hostname is
# (This variable is defined at the top of this file if you want to play with it)
#
# Hint: This is meant for you to use Google to figure out.

# Next, call make_http_request with the correct parameters and then print the response
# This response should look a lot like the in-class example of "curl", and start with
# "HTTP/1.1 200 OK". Rememeber, we're making an HTTP request, so from that you should
# be able to figure out what port to use.
