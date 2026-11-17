# {py:mod}`SATOSA.backends.github`

```{py:module} SATOSA.backends.github
```

```{autodoc2-docstring} SATOSA.backends.github
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`GitHubBackend <SATOSA.backends.github.GitHubBackend>`
  - ```{autodoc2-docstring} SATOSA.backends.github.GitHubBackend
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.backends.github.logger>`
  - ```{autodoc2-docstring} SATOSA.backends.github.logger
    :summary:
    ```
````

### API

`````{py:class} GitHubBackend(outgoing, internal_attributes, config, base_url, name)
:canonical: SATOSA.backends.github.GitHubBackend

Bases: {py:obj}`satosa.backends.oauth._OAuthBackend`

```{autodoc2-docstring} SATOSA.backends.github.GitHubBackend
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.backends.github.GitHubBackend.__init__
```

````{py:method} _authn_response(context)
:canonical: SATOSA.backends.github.GitHubBackend._authn_response

````

````{py:method} auth_info(requrest)
:canonical: SATOSA.backends.github.GitHubBackend.auth_info

````

````{py:method} start_auth(context, internal_request, get_state=stateID)
:canonical: SATOSA.backends.github.GitHubBackend.start_auth

```{autodoc2-docstring} SATOSA.backends.github.GitHubBackend.start_auth
```

````

````{py:method} user_information(access_token)
:canonical: SATOSA.backends.github.GitHubBackend.user_information

````

`````

````{py:data} logger
:canonical: SATOSA.backends.github.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.backends.github.logger
```

````
