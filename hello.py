def app(environ, start_response):
    # logic
    dt = "\n".join(environ.get('QUERY_STRING').split("&"))
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(dt)))
    ]
    start_response(status, response_headers)
    return iter ([dt.encode('utf-8')])
