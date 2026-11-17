# {py:mod}`SATOSA.proxy_server`

```{py:module} SATOSA.proxy_server
```

```{autodoc2-docstring} SATOSA.proxy_server
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ToBytesMiddleware <SATOSA.proxy_server.ToBytesMiddleware>`
  - ```{autodoc2-docstring} SATOSA.proxy_server.ToBytesMiddleware
    :summary:
    ```
* - {py:obj}`WsgiApplication <SATOSA.proxy_server.WsgiApplication>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`collect_http_headers <SATOSA.proxy_server.collect_http_headers>`
  - ```{autodoc2-docstring} SATOSA.proxy_server.collect_http_headers
    :summary:
    ```
* - {py:obj}`collect_server_headers <SATOSA.proxy_server.collect_server_headers>`
  - ```{autodoc2-docstring} SATOSA.proxy_server.collect_server_headers
    :summary:
    ```
* - {py:obj}`make_app <SATOSA.proxy_server.make_app>`
  - ```{autodoc2-docstring} SATOSA.proxy_server.make_app
    :summary:
    ```
* - {py:obj}`parse_query_string <SATOSA.proxy_server.parse_query_string>`
  - ```{autodoc2-docstring} SATOSA.proxy_server.parse_query_string
    :summary:
    ```
* - {py:obj}`unpack_get <SATOSA.proxy_server.unpack_get>`
  - ```{autodoc2-docstring} SATOSA.proxy_server.unpack_get
    :summary:
    ```
* - {py:obj}`unpack_post <SATOSA.proxy_server.unpack_post>`
  - ```{autodoc2-docstring} SATOSA.proxy_server.unpack_post
    :summary:
    ```
* - {py:obj}`unpack_request <SATOSA.proxy_server.unpack_request>`
  - ```{autodoc2-docstring} SATOSA.proxy_server.unpack_request
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.proxy_server.logger>`
  - ```{autodoc2-docstring} SATOSA.proxy_server.logger
    :summary:
    ```
````

### API

`````{py:class} ToBytesMiddleware(app)
:canonical: SATOSA.proxy_server.ToBytesMiddleware

Bases: {py:obj}`object`

```{autodoc2-docstring} SATOSA.proxy_server.ToBytesMiddleware
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.proxy_server.ToBytesMiddleware.__init__
```

````{py:method} __call__(environ, start_response)
:canonical: SATOSA.proxy_server.ToBytesMiddleware.__call__

```{autodoc2-docstring} SATOSA.proxy_server.ToBytesMiddleware.__call__
```

````

`````

`````{py:class} WsgiApplication(config)
:canonical: SATOSA.proxy_server.WsgiApplication

Bases: {py:obj}`SATOSA.base.SATOSABase`

````{py:method} __call__(environ, start_response, debug=False)
:canonical: SATOSA.proxy_server.WsgiApplication.__call__

```{autodoc2-docstring} SATOSA.proxy_server.WsgiApplication.__call__
```

````

`````

````{py:function} collect_http_headers(environ)
:canonical: SATOSA.proxy_server.collect_http_headers

```{autodoc2-docstring} SATOSA.proxy_server.collect_http_headers
```
````

````{py:function} collect_server_headers(environ)
:canonical: SATOSA.proxy_server.collect_server_headers

```{autodoc2-docstring} SATOSA.proxy_server.collect_server_headers
```
````

````{py:data} logger
:canonical: SATOSA.proxy_server.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.proxy_server.logger
```

````

````{py:function} make_app(satosa_config)
:canonical: SATOSA.proxy_server.make_app

```{autodoc2-docstring} SATOSA.proxy_server.make_app
```
````

````{py:function} parse_query_string(data)
:canonical: SATOSA.proxy_server.parse_query_string

```{autodoc2-docstring} SATOSA.proxy_server.parse_query_string
```
````

````{py:function} unpack_get(environ)
:canonical: SATOSA.proxy_server.unpack_get

```{autodoc2-docstring} SATOSA.proxy_server.unpack_get
```
````

````{py:function} unpack_post(environ, content_length)
:canonical: SATOSA.proxy_server.unpack_post

```{autodoc2-docstring} SATOSA.proxy_server.unpack_post
```
````

````{py:function} unpack_request(environ, content_length=0)
:canonical: SATOSA.proxy_server.unpack_request

```{autodoc2-docstring} SATOSA.proxy_server.unpack_request
```
````
