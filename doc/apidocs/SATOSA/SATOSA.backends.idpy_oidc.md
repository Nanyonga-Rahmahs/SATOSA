# {py:mod}`SATOSA.backends.idpy_oidc`

```{py:module} SATOSA.backends.idpy_oidc
```

```{autodoc2-docstring} SATOSA.backends.idpy_oidc
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IdpyOIDCBackend <SATOSA.backends.idpy_oidc.IdpyOIDCBackend>`
  - ```{autodoc2-docstring} SATOSA.backends.idpy_oidc.IdpyOIDCBackend
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.backends.idpy_oidc.logger>`
  - ```{autodoc2-docstring} SATOSA.backends.idpy_oidc.logger
    :summary:
    ```
````

### API

`````{py:class} IdpyOIDCBackend(auth_callback_func, internal_attributes, config, base_url, name)
:canonical: SATOSA.backends.idpy_oidc.IdpyOIDCBackend

Bases: {py:obj}`satosa.backends.base.BackendModule`

```{autodoc2-docstring} SATOSA.backends.idpy_oidc.IdpyOIDCBackend
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.backends.idpy_oidc.IdpyOIDCBackend.__init__
```

````{py:method} _check_error_response(response, context)
:canonical: SATOSA.backends.idpy_oidc.IdpyOIDCBackend._check_error_response

```{autodoc2-docstring} SATOSA.backends.idpy_oidc.IdpyOIDCBackend._check_error_response
```

````

````{py:method} _translate_response(response, issuer)
:canonical: SATOSA.backends.idpy_oidc.IdpyOIDCBackend._translate_response

```{autodoc2-docstring} SATOSA.backends.idpy_oidc.IdpyOIDCBackend._translate_response
```

````

````{py:method} register_endpoints()
:canonical: SATOSA.backends.idpy_oidc.IdpyOIDCBackend.register_endpoints

```{autodoc2-docstring} SATOSA.backends.idpy_oidc.IdpyOIDCBackend.register_endpoints
```

````

````{py:method} response_endpoint(context, *args)
:canonical: SATOSA.backends.idpy_oidc.IdpyOIDCBackend.response_endpoint

```{autodoc2-docstring} SATOSA.backends.idpy_oidc.IdpyOIDCBackend.response_endpoint
```

````

````{py:method} start_auth(context, internal_request)
:canonical: SATOSA.backends.idpy_oidc.IdpyOIDCBackend.start_auth

```{autodoc2-docstring} SATOSA.backends.idpy_oidc.IdpyOIDCBackend.start_auth
```

````

`````

````{py:data} logger
:canonical: SATOSA.backends.idpy_oidc.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.backends.idpy_oidc.logger
```

````
