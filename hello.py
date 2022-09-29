def app(environ, start_response):
    qs = environ['QUERY_STRING']
    ls = qs.split("&")
    data = "\n".join(ls).encode('utf-8')
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return [ data ]
