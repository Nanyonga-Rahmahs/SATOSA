# How to run the proxy application

The SATOSA proxy is a Python WSGI application and so may be run using any WSGI compliant web server.

## Using Gunicorn

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX and is the server used most often
to run the proxy. In a production deployment the Gunicorn server is often proxied by a
full featured general purpose web server (in a reverse proxy architecture) such as Nginx or
Apache HTTP Server to help buffer slow clients and enable more sophisticated error page rendering.

Start the proxy server with the following command:

```bash
gunicorn -b<socket address> satosa.wsgi:app --keyfile=<https key> --certfile=<https cert>
```

where
* `socket address` is the socket address that `gunicorn` should bind to for incoming requests, e.g. `0.0.0.0:8080`
* `https key` is the path to the private key to use for HTTPS, e.g. `pki/key.pem`
* `https cert` is the path to the certificate to use for HTTPS, e.g. `pki/cert.pem`

This will use the `proxy_conf.yaml` file in the working directory. If the `proxy_conf.yaml` is
located somewhere else, use the environment variable `SATOSA_CONFIG` to specify the path, e.g.:

```bash
set SATOSA_CONFIG=/home/user/proxy_conf.yaml
```

## Using Apache HTTP Server and mod\_wsgi

See the [auxiliary documentation for running using mod\_wsgi](mod_wsgi.md).
