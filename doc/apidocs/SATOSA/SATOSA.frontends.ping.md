# {py:mod}`SATOSA.frontends.ping`

```{py:module} SATOSA.frontends.ping
```

```{autodoc2-docstring} SATOSA.frontends.ping
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PingFrontend <SATOSA.frontends.ping.PingFrontend>`
  - ```{autodoc2-docstring} SATOSA.frontends.ping.PingFrontend
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.frontends.ping.logger>`
  - ```{autodoc2-docstring} SATOSA.frontends.ping.logger
    :summary:
    ```
````

### API

`````{py:class} PingFrontend(auth_req_callback_func, internal_attributes, config, base_url, name)
:canonical: SATOSA.frontends.ping.PingFrontend

Bases: {py:obj}`satosa.frontends.base.FrontendModule`

```{autodoc2-docstring} SATOSA.frontends.ping.PingFrontend
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.frontends.ping.PingFrontend.__init__
```

````{py:method} handle_authn_response(context, internal_resp)
:canonical: SATOSA.frontends.ping.PingFrontend.handle_authn_response
:abstractmethod:

```{autodoc2-docstring} SATOSA.frontends.ping.PingFrontend.handle_authn_response
```

````

````{py:method} handle_backend_error(exception)
:canonical: SATOSA.frontends.ping.PingFrontend.handle_backend_error
:abstractmethod:

```{autodoc2-docstring} SATOSA.frontends.ping.PingFrontend.handle_backend_error
```

````

````{py:method} ping_endpoint(context)
:canonical: SATOSA.frontends.ping.PingFrontend.ping_endpoint

```{autodoc2-docstring} SATOSA.frontends.ping.PingFrontend.ping_endpoint
```

````

````{py:method} register_endpoints(backend_names)
:canonical: SATOSA.frontends.ping.PingFrontend.register_endpoints

```{autodoc2-docstring} SATOSA.frontends.ping.PingFrontend.register_endpoints
```

````

`````

````{py:data} logger
:canonical: SATOSA.frontends.ping.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.frontends.ping.logger
```

````
