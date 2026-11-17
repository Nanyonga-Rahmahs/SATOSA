# {py:mod}`SATOSA.backends.orcid`

```{py:module} SATOSA.backends.orcid
```

```{autodoc2-docstring} SATOSA.backends.orcid
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`OrcidBackend <SATOSA.backends.orcid.OrcidBackend>`
  - ```{autodoc2-docstring} SATOSA.backends.orcid.OrcidBackend
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.backends.orcid.logger>`
  - ```{autodoc2-docstring} SATOSA.backends.orcid.logger
    :summary:
    ```
````

### API

`````{py:class} OrcidBackend(outgoing, internal_attributes, config, base_url, name)
:canonical: SATOSA.backends.orcid.OrcidBackend

Bases: {py:obj}`satosa.backends.oauth._OAuthBackend`

```{autodoc2-docstring} SATOSA.backends.orcid.OrcidBackend
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.backends.orcid.OrcidBackend.__init__
```

````{py:method} _authn_response(context)
:canonical: SATOSA.backends.orcid.OrcidBackend._authn_response

````

````{py:method} auth_info(requrest)
:canonical: SATOSA.backends.orcid.OrcidBackend.auth_info

````

````{py:method} get_request_args(get_state=stateID)
:canonical: SATOSA.backends.orcid.OrcidBackend.get_request_args

```{autodoc2-docstring} SATOSA.backends.orcid.OrcidBackend.get_request_args
```

````

````{py:method} user_information(access_token, orcid, name=None)
:canonical: SATOSA.backends.orcid.OrcidBackend.user_information

````

`````

````{py:data} logger
:canonical: SATOSA.backends.orcid.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.backends.orcid.logger
```

````
