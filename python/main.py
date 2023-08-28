from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from logger import jsonConfig
import logging

def fibonacci(n: int):
    """Return the first `n` Fibonacci numbers."""
    # check for input validity- positive ints.
    if not isinstance(n, int) or n < 0:
        logging.error("Input must be a non-negative integer")
        raise ValueError("Input must be a non-negative integer.")
    result = [1, 1]
    while len(result) < n:
        result.append(result[-2] + result[-1])
    return result[:n]

class GetFibs(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/healthy':
            self.handle_health_check()
        else:
            self.handle_fibonacci()

    def handle_fibonacci(self):
        logging.info("Handeling a get request")
        query = urlparse(self.path).query
        params = parse_qs(query)
        logging.info("Parsed parameters", extra={"additional_detail": "Params: {}".format(params)})
        if "n" not in params:
            logging.error("Parameter 'n' is not in input, cannot handle request")
            self.send_response(422)
            return

        try:
            key = int(params["n"][0])
            logging.info("Running fibonacci function on n={}".format(key))
            nums = fibonacci(key)
        except (IndexError, ValueError) as e:
            logging.error("The value of parameter 'n' cannot be converted to integer or is negative, cannot handle request: {}".format(e))
            self.send_response(422)
            return

        logging.info("Converting the fibonacci from int to string list")
        str_nums = [str(n) for n in nums]
        final_nums = ", ".join(str_nums)
        logging.info("responding with code 200")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(final_nums, "UTF-8"))
        return

    def handle_health_check(self):
        if fibonacci(1) == [1]:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Healthy")
        else:
            self.send_response(422)
            return


if __name__ == "__main__":
    from http.server import HTTPServer
    # set up logger
    jsonConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info("Starting the webserver serving fibonacci")
    # serve web requests
    httpd = HTTPServer(("", 8000), GetFibs)
    httpd.serve_forever()
