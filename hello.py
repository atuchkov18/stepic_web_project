def app(environ, start_response):
    qs = environ['QUERY_STRING']
    ls = qs.split("&")
    data = "\n".join(ls)
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return [ data.encode('utf-8') ]
