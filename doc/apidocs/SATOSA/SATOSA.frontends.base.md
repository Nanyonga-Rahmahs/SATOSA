# {py:mod}`SATOSA.frontends.base`

```{py:module} SATOSA.frontends.base
```

```{autodoc2-docstring} SATOSA.frontends.base
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`FrontendModule <SATOSA.frontends.base.FrontendModule>`
  - ```{autodoc2-docstring} SATOSA.frontends.base.FrontendModule
    :summary:
    ```
````

### API

`````{py:class} FrontendModule(auth_req_callback_func, internal_attributes, base_url, name)
:canonical: SATOSA.frontends.base.FrontendModule

Bases: {py:obj}`object`

```{autodoc2-docstring} SATOSA.frontends.base.FrontendModule
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.frontends.base.FrontendModule.__init__
```

````{py:method} handle_authn_response(context, internal_resp)
:canonical: SATOSA.frontends.base.FrontendModule.handle_authn_response
:abstractmethod:

```{autodoc2-docstring} SATOSA.frontends.base.FrontendModule.handle_authn_response
```

````

````{py:method} handle_backend_error(exception)
:canonical: SATOSA.frontends.base.FrontendModule.handle_backend_error
:abstractmethod:

```{autodoc2-docstring} SATOSA.frontends.base.FrontendModule.handle_backend_error
```

````

````{py:method} register_endpoints(backend_names)
:canonical: SATOSA.frontends.base.FrontendModule.register_endpoints
:abstractmethod:

```{autodoc2-docstring} SATOSA.frontends.base.FrontendModule.register_endpoints
```

````

`````
