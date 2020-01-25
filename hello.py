def app(environ, start_res):
    body = "\n".join(environ['QUERY_STRING'].split('&')).encode('utf-8')

    header = [
        ('Content-Type', 'text/plain;charset=UTF-8'),
        ('Content-Length', str(len(body)))
    ]
    start_res('200 OK', header)
    return [body]
