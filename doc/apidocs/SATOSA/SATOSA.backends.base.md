# {py:mod}`SATOSA.backends.base`

```{py:module} SATOSA.backends.base
```

```{autodoc2-docstring} SATOSA.backends.base
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BackendModule <SATOSA.backends.base.BackendModule>`
  - ```{autodoc2-docstring} SATOSA.backends.base.BackendModule
    :summary:
    ```
````

### API

`````{py:class} BackendModule(auth_callback_func, internal_attributes, base_url, name)
:canonical: SATOSA.backends.base.BackendModule

Bases: {py:obj}`object`

```{autodoc2-docstring} SATOSA.backends.base.BackendModule
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.backends.base.BackendModule.__init__
```

````{py:method} get_metadata_desc()
:canonical: SATOSA.backends.base.BackendModule.get_metadata_desc
:abstractmethod:

```{autodoc2-docstring} SATOSA.backends.base.BackendModule.get_metadata_desc
```

````

````{py:method} register_endpoints()
:canonical: SATOSA.backends.base.BackendModule.register_endpoints
:abstractmethod:

```{autodoc2-docstring} SATOSA.backends.base.BackendModule.register_endpoints
```

````

````{py:method} start_auth(context, internal_request)
:canonical: SATOSA.backends.base.BackendModule.start_auth
:abstractmethod:

```{autodoc2-docstring} SATOSA.backends.base.BackendModule.start_auth
```

````

`````
