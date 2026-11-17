# {py:mod}`SATOSA.backends.linkedin`

```{py:module} SATOSA.backends.linkedin
```

```{autodoc2-docstring} SATOSA.backends.linkedin
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LinkedInBackend <SATOSA.backends.linkedin.LinkedInBackend>`
  - ```{autodoc2-docstring} SATOSA.backends.linkedin.LinkedInBackend
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.backends.linkedin.logger>`
  - ```{autodoc2-docstring} SATOSA.backends.linkedin.logger
    :summary:
    ```
````

### API

`````{py:class} LinkedInBackend(outgoing, internal_attributes, config, base_url, name)
:canonical: SATOSA.backends.linkedin.LinkedInBackend

Bases: {py:obj}`satosa.backends.oauth._OAuthBackend`

```{autodoc2-docstring} SATOSA.backends.linkedin.LinkedInBackend
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.backends.linkedin.LinkedInBackend.__init__
```

````{py:method} _authn_response(context)
:canonical: SATOSA.backends.linkedin.LinkedInBackend._authn_response

````

````{py:method} auth_info(requrest)
:canonical: SATOSA.backends.linkedin.LinkedInBackend.auth_info

````

````{py:method} start_auth(context, internal_request, get_state=stateID)
:canonical: SATOSA.backends.linkedin.LinkedInBackend.start_auth

```{autodoc2-docstring} SATOSA.backends.linkedin.LinkedInBackend.start_auth
```

````

````{py:method} user_information(access_token, api)
:canonical: SATOSA.backends.linkedin.LinkedInBackend.user_information

````

`````

````{py:data} logger
:canonical: SATOSA.backends.linkedin.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.backends.linkedin.logger
```

````
