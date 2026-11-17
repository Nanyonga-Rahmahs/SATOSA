# {py:mod}`tests.satosa.backends.test_idpy_oidc`

```{py:module} tests.satosa.backends.test_idpy_oidc
```

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestIdpyOIDCBackend <tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CLIENT_BASE_URL <tests.satosa.backends.test_idpy_oidc.CLIENT_BASE_URL>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.CLIENT_BASE_URL
    :summary:
    ```
* - {py:obj}`CLIENT_ID <tests.satosa.backends.test_idpy_oidc.CLIENT_ID>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.CLIENT_ID
    :summary:
    ```
* - {py:obj}`ISSUER <tests.satosa.backends.test_idpy_oidc.ISSUER>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.ISSUER
    :summary:
    ```
* - {py:obj}`NONCE <tests.satosa.backends.test_idpy_oidc.NONCE>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.NONCE
    :summary:
    ```
````

### API

````{py:data} CLIENT_BASE_URL
:canonical: tests.satosa.backends.test_idpy_oidc.CLIENT_BASE_URL
:value: >
   'https://client.test.com'

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.CLIENT_BASE_URL
```

````

````{py:data} CLIENT_ID
:canonical: tests.satosa.backends.test_idpy_oidc.CLIENT_ID
:value: >
   'test_client'

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.CLIENT_ID
```

````

````{py:data} ISSUER
:canonical: tests.satosa.backends.test_idpy_oidc.ISSUER
:value: >
   'https://provider.example.com'

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.ISSUER
```

````

````{py:data} NONCE
:canonical: tests.satosa.backends.test_idpy_oidc.NONCE
:value: >
   'the nonce'

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.NONCE
```

````

`````{py:class} TestIdpyOIDCBackend
:canonical: tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend

Bases: {py:obj}`object`

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend
```

````{py:method} all_user_claims(userinfo, id_token)
:canonical: tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.all_user_claims

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.all_user_claims
```

````

````{py:method} assert_expected_attributes(attr_map, user_claims, actual_attributes)
:canonical: tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.assert_expected_attributes

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.assert_expected_attributes
```

````

````{py:method} backend_config()
:canonical: tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.backend_config

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.backend_config
```

````

````{py:method} create_backend(internal_attributes, backend_config)
:canonical: tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.create_backend

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.create_backend
```

````

````{py:method} id_token(userinfo)
:canonical: tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.id_token

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.id_token
```

````

````{py:method} incoming_authn_response()
:canonical: tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.incoming_authn_response

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.incoming_authn_response
```

````

````{py:method} internal_attributes()
:canonical: tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.internal_attributes

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.internal_attributes
```

````

````{py:method} setup_token_endpoint(userinfo)
:canonical: tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.setup_token_endpoint

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.setup_token_endpoint
```

````

````{py:method} setup_userinfo_endpoint(userinfo)
:canonical: tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.setup_userinfo_endpoint

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.setup_userinfo_endpoint
```

````

````{py:method} test_client(backend_config)
:canonical: tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.test_client

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.test_client
```

````

````{py:method} test_register_endpoints()
:canonical: tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.test_register_endpoints

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.test_register_endpoints
```

````

````{py:method} test_response_endpoint(context, all_user_claims, incoming_authn_response)
:canonical: tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.test_response_endpoint

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.test_response_endpoint
```

````

````{py:method} test_start_auth_redirects_to_provider_authorization_endpoint(context)
:canonical: tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.test_start_auth_redirects_to_provider_authorization_endpoint

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.test_start_auth_redirects_to_provider_authorization_endpoint
```

````

````{py:method} test_translate_response_to_internal_response(all_user_claims)
:canonical: tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.test_translate_response_to_internal_response

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.test_translate_response_to_internal_response
```

````

````{py:method} userinfo()
:canonical: tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.userinfo

```{autodoc2-docstring} tests.satosa.backends.test_idpy_oidc.TestIdpyOIDCBackend.userinfo
```

````

`````
