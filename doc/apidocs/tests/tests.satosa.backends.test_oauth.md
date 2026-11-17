# {py:mod}`tests.satosa.backends.test_oauth`

```{py:module} tests.satosa.backends.test_oauth
```

```{autodoc2-docstring} tests.satosa.backends.test_oauth
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestFacebookBackend <tests.satosa.backends.test_oauth.TestFacebookBackend>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_oauth.TestFacebookBackend
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AUTHZ_PAGE <tests.satosa.backends.test_oauth.AUTHZ_PAGE>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_oauth.AUTHZ_PAGE
    :summary:
    ```
* - {py:obj}`BASE_URL <tests.satosa.backends.test_oauth.BASE_URL>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_oauth.BASE_URL
    :summary:
    ```
* - {py:obj}`CLIENT_ID <tests.satosa.backends.test_oauth.CLIENT_ID>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_oauth.CLIENT_ID
    :summary:
    ```
* - {py:obj}`FB_AUTH_ENDPOINT <tests.satosa.backends.test_oauth.FB_AUTH_ENDPOINT>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_oauth.FB_AUTH_ENDPOINT
    :summary:
    ```
* - {py:obj}`FB_CONFIG <tests.satosa.backends.test_oauth.FB_CONFIG>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_oauth.FB_CONFIG
    :summary:
    ```
* - {py:obj}`FB_RESPONSE <tests.satosa.backends.test_oauth.FB_RESPONSE>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_oauth.FB_RESPONSE
    :summary:
    ```
* - {py:obj}`FB_RESPONSE_CODE <tests.satosa.backends.test_oauth.FB_RESPONSE_CODE>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_oauth.FB_RESPONSE_CODE
    :summary:
    ```
* - {py:obj}`INTERNAL_ATTRIBUTES <tests.satosa.backends.test_oauth.INTERNAL_ATTRIBUTES>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_oauth.INTERNAL_ATTRIBUTES
    :summary:
    ```
* - {py:obj}`mock_get_state <tests.satosa.backends.test_oauth.mock_get_state>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_oauth.mock_get_state
    :summary:
    ```
````

### API

````{py:data} AUTHZ_PAGE
:canonical: tests.satosa.backends.test_oauth.AUTHZ_PAGE
:value: >
   'facebook'

```{autodoc2-docstring} tests.satosa.backends.test_oauth.AUTHZ_PAGE
```

````

````{py:data} BASE_URL
:canonical: tests.satosa.backends.test_oauth.BASE_URL
:value: >
   'https://client.example.com'

```{autodoc2-docstring} tests.satosa.backends.test_oauth.BASE_URL
```

````

````{py:data} CLIENT_ID
:canonical: tests.satosa.backends.test_oauth.CLIENT_ID
:value: >
   'facebook_client_id'

```{autodoc2-docstring} tests.satosa.backends.test_oauth.CLIENT_ID
```

````

````{py:data} FB_AUTH_ENDPOINT
:canonical: tests.satosa.backends.test_oauth.FB_AUTH_ENDPOINT
:value: >
   'https://www.facebook.com/dialog/oauth'

```{autodoc2-docstring} tests.satosa.backends.test_oauth.FB_AUTH_ENDPOINT
```

````

````{py:data} FB_CONFIG
:canonical: tests.satosa.backends.test_oauth.FB_CONFIG
:value: >
   None

```{autodoc2-docstring} tests.satosa.backends.test_oauth.FB_CONFIG
```

````

````{py:data} FB_RESPONSE
:canonical: tests.satosa.backends.test_oauth.FB_RESPONSE
:value: >
   None

```{autodoc2-docstring} tests.satosa.backends.test_oauth.FB_RESPONSE
```

````

````{py:data} FB_RESPONSE_CODE
:canonical: tests.satosa.backends.test_oauth.FB_RESPONSE_CODE
:value: >
   'the_fb_code'

```{autodoc2-docstring} tests.satosa.backends.test_oauth.FB_RESPONSE_CODE
```

````

````{py:data} INTERNAL_ATTRIBUTES
:canonical: tests.satosa.backends.test_oauth.INTERNAL_ATTRIBUTES
:value: >
   None

```{autodoc2-docstring} tests.satosa.backends.test_oauth.INTERNAL_ATTRIBUTES
```

````

`````{py:class} TestFacebookBackend
:canonical: tests.satosa.backends.test_oauth.TestFacebookBackend

Bases: {py:obj}`object`

```{autodoc2-docstring} tests.satosa.backends.test_oauth.TestFacebookBackend
```

````{py:method} assert_expected_attributes()
:canonical: tests.satosa.backends.test_oauth.TestFacebookBackend.assert_expected_attributes

```{autodoc2-docstring} tests.satosa.backends.test_oauth.TestFacebookBackend.assert_expected_attributes
```

````

````{py:method} assert_token_request(request_args, state, **kwargs)
:canonical: tests.satosa.backends.test_oauth.TestFacebookBackend.assert_token_request

```{autodoc2-docstring} tests.satosa.backends.test_oauth.TestFacebookBackend.assert_token_request
```

````

````{py:method} create_backend()
:canonical: tests.satosa.backends.test_oauth.TestFacebookBackend.create_backend

```{autodoc2-docstring} tests.satosa.backends.test_oauth.TestFacebookBackend.create_backend
```

````

````{py:method} incoming_authn_response(context)
:canonical: tests.satosa.backends.test_oauth.TestFacebookBackend.incoming_authn_response

```{autodoc2-docstring} tests.satosa.backends.test_oauth.TestFacebookBackend.incoming_authn_response
```

````

````{py:method} setup_facebook_response()
:canonical: tests.satosa.backends.test_oauth.TestFacebookBackend.setup_facebook_response

```{autodoc2-docstring} tests.satosa.backends.test_oauth.TestFacebookBackend.setup_facebook_response
```

````

````{py:method} test_authn_response(incoming_authn_response)
:canonical: tests.satosa.backends.test_oauth.TestFacebookBackend.test_authn_response

```{autodoc2-docstring} tests.satosa.backends.test_oauth.TestFacebookBackend.test_authn_response
```

````

````{py:method} test_entire_flow(context)
:canonical: tests.satosa.backends.test_oauth.TestFacebookBackend.test_entire_flow

```{autodoc2-docstring} tests.satosa.backends.test_oauth.TestFacebookBackend.test_entire_flow
```

````

````{py:method} test_register_endpoints()
:canonical: tests.satosa.backends.test_oauth.TestFacebookBackend.test_register_endpoints

```{autodoc2-docstring} tests.satosa.backends.test_oauth.TestFacebookBackend.test_register_endpoints
```

````

````{py:method} test_start_auth(context)
:canonical: tests.satosa.backends.test_oauth.TestFacebookBackend.test_start_auth

```{autodoc2-docstring} tests.satosa.backends.test_oauth.TestFacebookBackend.test_start_auth
```

````

`````

````{py:data} mock_get_state
:canonical: tests.satosa.backends.test_oauth.mock_get_state
:value: >
   'Mock(...)'

```{autodoc2-docstring} tests.satosa.backends.test_oauth.mock_get_state
```

````
