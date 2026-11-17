# {py:mod}`tests.satosa.frontends.test_openid_connect`

```{py:module} tests.satosa.frontends.test_openid_connect
```

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestOpenIDConnectFrontend <tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend>`
  - ```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BASE_URL <tests.satosa.frontends.test_openid_connect.BASE_URL>`
  - ```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.BASE_URL
    :summary:
    ```
* - {py:obj}`CLIENT_ID <tests.satosa.frontends.test_openid_connect.CLIENT_ID>`
  - ```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.CLIENT_ID
    :summary:
    ```
* - {py:obj}`CLIENT_SECRET <tests.satosa.frontends.test_openid_connect.CLIENT_SECRET>`
  - ```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.CLIENT_SECRET
    :summary:
    ```
* - {py:obj}`EXTRA_CLAIMS <tests.satosa.frontends.test_openid_connect.EXTRA_CLAIMS>`
  - ```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.EXTRA_CLAIMS
    :summary:
    ```
* - {py:obj}`EXTRA_SCOPES <tests.satosa.frontends.test_openid_connect.EXTRA_SCOPES>`
  - ```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.EXTRA_SCOPES
    :summary:
    ```
* - {py:obj}`INTERNAL_ATTRIBUTES <tests.satosa.frontends.test_openid_connect.INTERNAL_ATTRIBUTES>`
  - ```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.INTERNAL_ATTRIBUTES
    :summary:
    ```
````

### API

````{py:data} BASE_URL
:canonical: tests.satosa.frontends.test_openid_connect.BASE_URL
:value: >
   'https://op.example.com'

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.BASE_URL
```

````

````{py:data} CLIENT_ID
:canonical: tests.satosa.frontends.test_openid_connect.CLIENT_ID
:value: >
   'client1'

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.CLIENT_ID
```

````

````{py:data} CLIENT_SECRET
:canonical: tests.satosa.frontends.test_openid_connect.CLIENT_SECRET
:value: >
   'client_secret'

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.CLIENT_SECRET
```

````

````{py:data} EXTRA_CLAIMS
:canonical: tests.satosa.frontends.test_openid_connect.EXTRA_CLAIMS
:value: >
   None

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.EXTRA_CLAIMS
```

````

````{py:data} EXTRA_SCOPES
:canonical: tests.satosa.frontends.test_openid_connect.EXTRA_SCOPES
:value: >
   None

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.EXTRA_SCOPES
```

````

````{py:data} INTERNAL_ATTRIBUTES
:canonical: tests.satosa.frontends.test_openid_connect.INTERNAL_ATTRIBUTES
:value: >
   None

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.INTERNAL_ATTRIBUTES
```

````

`````{py:class} TestOpenIDConnectFrontend
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend

Bases: {py:obj}`object`

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend
```

````{py:method} authn_req()
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.authn_req

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.authn_req
```

````

````{py:method} authn_req_with_extra_scopes()
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.authn_req_with_extra_scopes

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.authn_req_with_extra_scopes
```

````

````{py:method} create_access_token(frontend, user_id, auth_req)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.create_access_token

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.create_access_token
```

````

````{py:method} create_frontend(frontend_config)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.create_frontend

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.create_frontend
```

````

````{py:method} create_frontend_with_extra_scopes(frontend_config_with_extra_scopes)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.create_frontend_with_extra_scopes

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.create_frontend_with_extra_scopes
```

````

````{py:method} frontend(frontend_config)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.frontend

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.frontend
```

````

````{py:method} frontend_config(signing_key_path)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.frontend_config

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.frontend_config
```

````

````{py:method} frontend_config_with_extra_id_token_claims(signing_key_path)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.frontend_config_with_extra_id_token_claims

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.frontend_config_with_extra_id_token_claims
```

````

````{py:method} frontend_config_with_extra_scopes(signing_key_path)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.frontend_config_with_extra_scopes

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.frontend_config_with_extra_scopes
```

````

````{py:method} frontend_with_extra_scopes(frontend_config_with_extra_scopes)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.frontend_with_extra_scopes

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.frontend_with_extra_scopes
```

````

````{py:method} insert_client_in_client_db(frontend, redirect_uri, extra_metadata={})
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.insert_client_in_client_db

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.insert_client_in_client_db
```

````

````{py:method} insert_user_in_user_db(frontend, user_id)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.insert_user_in_user_db

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.insert_user_in_user_db
```

````

````{py:method} setup_for_authn_response(context, frontend, auth_req)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.setup_for_authn_response

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.setup_for_authn_response
```

````

````{py:method} test_full_flow(context, frontend_with_extra_scopes)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_full_flow

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_full_flow
```

````

````{py:method} test_get_approved_attributes(frontend)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_get_approved_attributes

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_get_approved_attributes
```

````

````{py:method} test_handle_authn_request(context, frontend, authn_req)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_handle_authn_request

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_handle_authn_request
```

````

````{py:method} test_handle_authn_request_with_extra_scopes(context, frontend_with_extra_scopes, authn_req_with_extra_scopes)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_handle_authn_request_with_extra_scopes

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_handle_authn_request_with_extra_scopes
```

````

````{py:method} test_handle_authn_response(context, frontend, authn_req)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_handle_authn_response

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_handle_authn_response
```

````

````{py:method} test_handle_backend_error(context, frontend)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_handle_backend_error

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_handle_backend_error
```

````

````{py:method} test_jwks(context, frontend)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_jwks

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_jwks
```

````

````{py:method} test_mirrored_subject(context, frontend_config, authn_req, sub_mirror_public)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_mirrored_subject

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_mirrored_subject
```

````

````{py:method} test_provider_configuration_endpoint(context, frontend)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_provider_configuration_endpoint

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_provider_configuration_endpoint
```

````

````{py:method} test_provider_configuration_endpoint_with_extra_scopes(context, frontend_with_extra_scopes)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_provider_configuration_endpoint_with_extra_scopes

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_provider_configuration_endpoint_with_extra_scopes
```

````

````{py:method} test_register_client(context, frontend)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_register_client

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_register_client
```

````

````{py:method} test_register_client_with_wrong_response_type(context, frontend)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_register_client_with_wrong_response_type

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_register_client_with_wrong_response_type
```

````

````{py:method} test_register_endpoints_dynamic_client_registration_is_configurable(frontend_config, client_registration_enabled)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_register_endpoints_dynamic_client_registration_is_configurable

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_register_endpoints_dynamic_client_registration_is_configurable
```

````

````{py:method} test_register_endpoints_token_and_userinfo_endpoint_is_not_published_if_only_implicit_flow(frontend_config, context)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_register_endpoints_token_and_userinfo_endpoint_is_not_published_if_only_implicit_flow

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_register_endpoints_token_and_userinfo_endpoint_is_not_published_if_only_implicit_flow
```

````

````{py:method} test_register_endpoints_token_and_userinfo_endpoint_is_published_if_necessary(frontend)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_register_endpoints_token_and_userinfo_endpoint_is_published_if_necessary

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_register_endpoints_token_and_userinfo_endpoint_is_published_if_necessary
```

````

````{py:method} test_token_endpoint(context, frontend_config, authn_req)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_token_endpoint

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_token_endpoint
```

````

````{py:method} test_token_endpoint_issues_refresh_tokens_if_configured(context, frontend_config, authn_req)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_token_endpoint_issues_refresh_tokens_if_configured

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_token_endpoint_issues_refresh_tokens_if_configured
```

````

````{py:method} test_token_endpoint_with_extra_claims(context, frontend_config_with_extra_id_token_claims, authn_req)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_token_endpoint_with_extra_claims

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_token_endpoint_with_extra_claims
```

````

````{py:method} test_token_endpoint_with_invalid_client_authentication(context, frontend, authn_req)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_token_endpoint_with_invalid_client_authentication

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_token_endpoint_with_invalid_client_authentication
```

````

````{py:method} test_token_endpoint_with_invalid_code(context, frontend, authn_req)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_token_endpoint_with_invalid_code

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_token_endpoint_with_invalid_code
```

````

````{py:method} test_userinfo_endpoint(context, frontend, authn_req)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_userinfo_endpoint

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_userinfo_endpoint
```

````

````{py:method} test_userinfo_endpoint_with_extra_scopes(context, frontend_with_extra_scopes, authn_req_with_extra_scopes)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_userinfo_endpoint_with_extra_scopes

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_userinfo_endpoint_with_extra_scopes
```

````

````{py:method} test_userinfo_with_invalid_token(context, frontend)
:canonical: tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_userinfo_with_invalid_token

```{autodoc2-docstring} tests.satosa.frontends.test_openid_connect.TestOpenIDConnectFrontend.test_userinfo_with_invalid_token
```

````

`````
