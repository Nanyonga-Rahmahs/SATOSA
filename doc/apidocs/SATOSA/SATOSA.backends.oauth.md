# {py:mod}`SATOSA.backends.oauth`

```{py:module} SATOSA.backends.oauth
```

```{autodoc2-docstring} SATOSA.backends.oauth
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`FacebookBackend <SATOSA.backends.oauth.FacebookBackend>`
  - ```{autodoc2-docstring} SATOSA.backends.oauth.FacebookBackend
    :summary:
    ```
* - {py:obj}`_OAuthBackend <SATOSA.backends.oauth._OAuthBackend>`
  - ```{autodoc2-docstring} SATOSA.backends.oauth._OAuthBackend
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_metadata_desc_for_oauth_backend <SATOSA.backends.oauth.get_metadata_desc_for_oauth_backend>`
  - ```{autodoc2-docstring} SATOSA.backends.oauth.get_metadata_desc_for_oauth_backend
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.backends.oauth.logger>`
  - ```{autodoc2-docstring} SATOSA.backends.oauth.logger
    :summary:
    ```
````

### API

`````{py:class} FacebookBackend(outgoing, internal_attributes, config, base_url, name)
:canonical: SATOSA.backends.oauth.FacebookBackend

Bases: {py:obj}`SATOSA.backends.oauth._OAuthBackend`

```{autodoc2-docstring} SATOSA.backends.oauth.FacebookBackend
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.backends.oauth.FacebookBackend.__init__
```

````{py:attribute} DEFAULT_GRAPH_ENDPOINT
:canonical: SATOSA.backends.oauth.FacebookBackend.DEFAULT_GRAPH_ENDPOINT
:value: >
   'https://graph.facebook.com/v2.5/me'

```{autodoc2-docstring} SATOSA.backends.oauth.FacebookBackend.DEFAULT_GRAPH_ENDPOINT
```

````

````{py:method} auth_info(request)
:canonical: SATOSA.backends.oauth.FacebookBackend.auth_info

```{autodoc2-docstring} SATOSA.backends.oauth.FacebookBackend.auth_info
```

````

````{py:method} get_request_args(get_state=stateID)
:canonical: SATOSA.backends.oauth.FacebookBackend.get_request_args

```{autodoc2-docstring} SATOSA.backends.oauth.FacebookBackend.get_request_args
```

````

````{py:method} user_information(access_token)
:canonical: SATOSA.backends.oauth.FacebookBackend.user_information

```{autodoc2-docstring} SATOSA.backends.oauth.FacebookBackend.user_information
```

````

`````

`````{py:class} _OAuthBackend(outgoing, internal_attributes, config, base_url, name, external_type, user_id_attr)
:canonical: SATOSA.backends.oauth._OAuthBackend

Bases: {py:obj}`satosa.backends.base.BackendModule`

```{autodoc2-docstring} SATOSA.backends.oauth._OAuthBackend
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.backends.oauth._OAuthBackend.__init__
```

````{py:method} _authn_response(context)
:canonical: SATOSA.backends.oauth._OAuthBackend._authn_response

```{autodoc2-docstring} SATOSA.backends.oauth._OAuthBackend._authn_response
```

````

````{py:method} _verify_state(resp, state_data, state)
:canonical: SATOSA.backends.oauth._OAuthBackend._verify_state

```{autodoc2-docstring} SATOSA.backends.oauth._OAuthBackend._verify_state
```

````

````{py:method} auth_info(request)
:canonical: SATOSA.backends.oauth._OAuthBackend.auth_info
:abstractmethod:

```{autodoc2-docstring} SATOSA.backends.oauth._OAuthBackend.auth_info
```

````

````{py:method} get_metadata_desc()
:canonical: SATOSA.backends.oauth._OAuthBackend.get_metadata_desc

```{autodoc2-docstring} SATOSA.backends.oauth._OAuthBackend.get_metadata_desc
```

````

````{py:method} get_request_args(get_state=stateID)
:canonical: SATOSA.backends.oauth._OAuthBackend.get_request_args

```{autodoc2-docstring} SATOSA.backends.oauth._OAuthBackend.get_request_args
```

````

````{py:method} register_endpoints()
:canonical: SATOSA.backends.oauth._OAuthBackend.register_endpoints

```{autodoc2-docstring} SATOSA.backends.oauth._OAuthBackend.register_endpoints
```

````

````{py:method} start_auth(context, internal_request, get_state=stateID)
:canonical: SATOSA.backends.oauth._OAuthBackend.start_auth

```{autodoc2-docstring} SATOSA.backends.oauth._OAuthBackend.start_auth
```

````

````{py:method} user_information(access_token)
:canonical: SATOSA.backends.oauth._OAuthBackend.user_information
:abstractmethod:

```{autodoc2-docstring} SATOSA.backends.oauth._OAuthBackend.user_information
```

````

`````

````{py:function} get_metadata_desc_for_oauth_backend(entity_id, config)
:canonical: SATOSA.backends.oauth.get_metadata_desc_for_oauth_backend

```{autodoc2-docstring} SATOSA.backends.oauth.get_metadata_desc_for_oauth_backend
```
````

````{py:data} logger
:canonical: SATOSA.backends.oauth.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.backends.oauth.logger
```

````
