# {py:mod}`SATOSA.backends.openid_connect`

```{py:module} SATOSA.backends.openid_connect
```

```{autodoc2-docstring} SATOSA.backends.openid_connect
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`OpenIDConnectBackend <SATOSA.backends.openid_connect.OpenIDConnectBackend>`
  - ```{autodoc2-docstring} SATOSA.backends.openid_connect.OpenIDConnectBackend
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_create_client <SATOSA.backends.openid_connect._create_client>`
  - ```{autodoc2-docstring} SATOSA.backends.openid_connect._create_client
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`NONCE_KEY <SATOSA.backends.openid_connect.NONCE_KEY>`
  - ```{autodoc2-docstring} SATOSA.backends.openid_connect.NONCE_KEY
    :summary:
    ```
* - {py:obj}`STATE_KEY <SATOSA.backends.openid_connect.STATE_KEY>`
  - ```{autodoc2-docstring} SATOSA.backends.openid_connect.STATE_KEY
    :summary:
    ```
* - {py:obj}`logger <SATOSA.backends.openid_connect.logger>`
  - ```{autodoc2-docstring} SATOSA.backends.openid_connect.logger
    :summary:
    ```
````

### API

````{py:data} NONCE_KEY
:canonical: SATOSA.backends.openid_connect.NONCE_KEY
:value: >
   'oidc_nonce'

```{autodoc2-docstring} SATOSA.backends.openid_connect.NONCE_KEY
```

````

`````{py:class} OpenIDConnectBackend(auth_callback_func, internal_attributes, config, base_url, name)
:canonical: SATOSA.backends.openid_connect.OpenIDConnectBackend

Bases: {py:obj}`SATOSA.backends.base.BackendModule`

```{autodoc2-docstring} SATOSA.backends.openid_connect.OpenIDConnectBackend
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.backends.openid_connect.OpenIDConnectBackend.__init__
```

````{py:method} _check_error_response(response, context)
:canonical: SATOSA.backends.openid_connect.OpenIDConnectBackend._check_error_response

```{autodoc2-docstring} SATOSA.backends.openid_connect.OpenIDConnectBackend._check_error_response
```

````

````{py:method} _get_tokens(authn_response, context)
:canonical: SATOSA.backends.openid_connect.OpenIDConnectBackend._get_tokens

```{autodoc2-docstring} SATOSA.backends.openid_connect.OpenIDConnectBackend._get_tokens
```

````

````{py:method} _get_userinfo(state, context)
:canonical: SATOSA.backends.openid_connect.OpenIDConnectBackend._get_userinfo

```{autodoc2-docstring} SATOSA.backends.openid_connect.OpenIDConnectBackend._get_userinfo
```

````

````{py:method} _translate_response(response, issuer)
:canonical: SATOSA.backends.openid_connect.OpenIDConnectBackend._translate_response

```{autodoc2-docstring} SATOSA.backends.openid_connect.OpenIDConnectBackend._translate_response
```

````

````{py:method} _verify_nonce(nonce, context)
:canonical: SATOSA.backends.openid_connect.OpenIDConnectBackend._verify_nonce

```{autodoc2-docstring} SATOSA.backends.openid_connect.OpenIDConnectBackend._verify_nonce
```

````

````{py:method} get_metadata_desc()
:canonical: SATOSA.backends.openid_connect.OpenIDConnectBackend.get_metadata_desc

```{autodoc2-docstring} SATOSA.backends.openid_connect.OpenIDConnectBackend.get_metadata_desc
```

````

````{py:method} register_endpoints()
:canonical: SATOSA.backends.openid_connect.OpenIDConnectBackend.register_endpoints

```{autodoc2-docstring} SATOSA.backends.openid_connect.OpenIDConnectBackend.register_endpoints
```

````

````{py:method} response_endpoint(context, *args)
:canonical: SATOSA.backends.openid_connect.OpenIDConnectBackend.response_endpoint

```{autodoc2-docstring} SATOSA.backends.openid_connect.OpenIDConnectBackend.response_endpoint
```

````

````{py:method} start_auth(context, request_info)
:canonical: SATOSA.backends.openid_connect.OpenIDConnectBackend.start_auth

```{autodoc2-docstring} SATOSA.backends.openid_connect.OpenIDConnectBackend.start_auth
```

````

`````

````{py:data} STATE_KEY
:canonical: SATOSA.backends.openid_connect.STATE_KEY
:value: >
   'oidc_state'

```{autodoc2-docstring} SATOSA.backends.openid_connect.STATE_KEY
```

````

````{py:function} _create_client(provider_metadata, client_metadata, settings=None)
:canonical: SATOSA.backends.openid_connect._create_client

```{autodoc2-docstring} SATOSA.backends.openid_connect._create_client
```
````

````{py:data} logger
:canonical: SATOSA.backends.openid_connect.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.backends.openid_connect.logger
```

````
