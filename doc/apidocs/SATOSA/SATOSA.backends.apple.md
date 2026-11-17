# {py:mod}`SATOSA.backends.apple`

```{py:module} SATOSA.backends.apple
```

```{autodoc2-docstring} SATOSA.backends.apple
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AppleBackend <SATOSA.backends.apple.AppleBackend>`
  - ```{autodoc2-docstring} SATOSA.backends.apple.AppleBackend
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.backends.apple.logger>`
  - ```{autodoc2-docstring} SATOSA.backends.apple.logger
    :summary:
    ```
````

### API

`````{py:class} AppleBackend(auth_callback_func, internal_attributes, config, base_url, name)
:canonical: SATOSA.backends.apple.AppleBackend

Bases: {py:obj}`SATOSA.backends.openid_connect.OpenIDConnectBackend`

```{autodoc2-docstring} SATOSA.backends.apple.AppleBackend
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.backends.apple.AppleBackend.__init__
```

````{py:method} _get_tokens(authn_response, context)
:canonical: SATOSA.backends.apple.AppleBackend._get_tokens

```{autodoc2-docstring} SATOSA.backends.apple.AppleBackend._get_tokens
```

````

````{py:method} response_endpoint(context, *args)
:canonical: SATOSA.backends.apple.AppleBackend.response_endpoint

```{autodoc2-docstring} SATOSA.backends.apple.AppleBackend.response_endpoint
```

````

`````

````{py:data} logger
:canonical: SATOSA.backends.apple.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.backends.apple.logger
```

````
