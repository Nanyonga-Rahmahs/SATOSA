# {py:mod}`tests.satosa.backends.test_openid_connect`

```{py:module} tests.satosa.backends.test_openid_connect
```

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestCreateClient <tests.satosa.backends.test_openid_connect.TestCreateClient>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestCreateClient
    :summary:
    ```
* - {py:obj}`TestOpenIDConnectBackend <tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CLIENT_ID <tests.satosa.backends.test_openid_connect.CLIENT_ID>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.CLIENT_ID
    :summary:
    ```
* - {py:obj}`ISSUER <tests.satosa.backends.test_openid_connect.ISSUER>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.ISSUER
    :summary:
    ```
* - {py:obj}`NONCE <tests.satosa.backends.test_openid_connect.NONCE>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.NONCE
    :summary:
    ```
````

### API

````{py:data} CLIENT_ID
:canonical: tests.satosa.backends.test_openid_connect.CLIENT_ID
:value: >
   'test_client'

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.CLIENT_ID
```

````

````{py:data} ISSUER
:canonical: tests.satosa.backends.test_openid_connect.ISSUER
:value: >
   'https://provider.example.com'

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.ISSUER
```

````

````{py:data} NONCE
:canonical: tests.satosa.backends.test_openid_connect.NONCE
:value: >
   'the nonce'

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.NONCE
```

````

`````{py:class} TestCreateClient
:canonical: tests.satosa.backends.test_openid_connect.TestCreateClient

Bases: {py:obj}`object`

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestCreateClient
```

````{py:method} assert_client_metadata(client_metadata, client)
:canonical: tests.satosa.backends.test_openid_connect.TestCreateClient.assert_client_metadata

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestCreateClient.assert_client_metadata
```

````

````{py:method} assert_provider_metadata(provider_metadata, client)
:canonical: tests.satosa.backends.test_openid_connect.TestCreateClient.assert_provider_metadata

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestCreateClient.assert_provider_metadata
```

````

````{py:method} client_metadata()
:canonical: tests.satosa.backends.test_openid_connect.TestCreateClient.client_metadata

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestCreateClient.client_metadata
```

````

````{py:method} provider_metadata()
:canonical: tests.satosa.backends.test_openid_connect.TestCreateClient.provider_metadata

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestCreateClient.provider_metadata
```

````

````{py:method} test_init(provider_metadata, client_metadata)
:canonical: tests.satosa.backends.test_openid_connect.TestCreateClient.test_init

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestCreateClient.test_init
```

````

````{py:method} test_supports_dynamic_client_registration(provider_metadata, client_metadata)
:canonical: tests.satosa.backends.test_openid_connect.TestCreateClient.test_supports_dynamic_client_registration

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestCreateClient.test_supports_dynamic_client_registration
```

````

````{py:method} test_supports_dynamic_discovery(provider_metadata, client_metadata)
:canonical: tests.satosa.backends.test_openid_connect.TestCreateClient.test_supports_dynamic_discovery

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestCreateClient.test_supports_dynamic_discovery
```

````

````{py:method} test_supports_static_client_registration(provider_metadata, client_metadata)
:canonical: tests.satosa.backends.test_openid_connect.TestCreateClient.test_supports_static_client_registration

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestCreateClient.test_supports_static_client_registration
```

````

````{py:method} test_supports_static_provider_discovery(provider_metadata, client_metadata)
:canonical: tests.satosa.backends.test_openid_connect.TestCreateClient.test_supports_static_provider_discovery

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestCreateClient.test_supports_static_provider_discovery
```

````

`````

`````{py:class} TestOpenIDConnectBackend
:canonical: tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend

Bases: {py:obj}`object`

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend
```

````{py:method} assert_expected_attributes(attr_map, user_claims, actual_attributes)
:canonical: tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.assert_expected_attributes

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.assert_expected_attributes
```

````

````{py:method} backend_config()
:canonical: tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.backend_config

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.backend_config
```

````

````{py:method} create_backend(internal_attributes, backend_config)
:canonical: tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.create_backend

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.create_backend
```

````

````{py:method} get_redirect_uri_path(backend_config)
:canonical: tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.get_redirect_uri_path

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.get_redirect_uri_path
```

````

````{py:method} incoming_authn_response(context, backend_config)
:canonical: tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.incoming_authn_response

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.incoming_authn_response
```

````

````{py:method} internal_attributes()
:canonical: tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.internal_attributes

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.internal_attributes
```

````

````{py:method} setup_jwks_uri(jwks_uri, key)
:canonical: tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.setup_jwks_uri

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.setup_jwks_uri
```

````

````{py:method} setup_token_endpoint(token_endpoint_url, userinfo, signing_key)
:canonical: tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.setup_token_endpoint

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.setup_token_endpoint
```

````

````{py:method} setup_userinfo_endpoint(userinfo_endpoint_url, userinfo)
:canonical: tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.setup_userinfo_endpoint

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.setup_userinfo_endpoint
```

````

````{py:method} signing_key()
:canonical: tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.signing_key

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.signing_key
```

````

````{py:method} test_entire_flow(context, backend_config, internal_attributes, userinfo)
:canonical: tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.test_entire_flow

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.test_entire_flow
```

````

````{py:method} test_register_endpoints(backend_config)
:canonical: tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.test_register_endpoints

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.test_register_endpoints
```

````

````{py:method} test_response_endpoint(backend_config, internal_attributes, userinfo, signing_key, incoming_authn_response)
:canonical: tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.test_response_endpoint

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.test_response_endpoint
```

````

````{py:method} test_start_auth_redirects_to_provider_authorization_endpoint(context, backend_config)
:canonical: tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.test_start_auth_redirects_to_provider_authorization_endpoint

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.test_start_auth_redirects_to_provider_authorization_endpoint
```

````

````{py:method} test_translate_response_to_internal_response(internal_attributes, userinfo)
:canonical: tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.test_translate_response_to_internal_response

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.test_translate_response_to_internal_response
```

````

````{py:method} userinfo()
:canonical: tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.userinfo

```{autodoc2-docstring} tests.satosa.backends.test_openid_connect.TestOpenIDConnectBackend.userinfo
```

````

`````
