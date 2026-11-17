# {py:mod}`tests.satosa.backends.test_bitbucket`

```{py:module} tests.satosa.backends.test_bitbucket
```

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestBitBucketBackend <tests.satosa.backends.test_bitbucket.TestBitBucketBackend>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.TestBitBucketBackend
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AUTHZ_PAGE <tests.satosa.backends.test_bitbucket.AUTHZ_PAGE>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.AUTHZ_PAGE
    :summary:
    ```
* - {py:obj}`BASE_URL <tests.satosa.backends.test_bitbucket.BASE_URL>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.BASE_URL
    :summary:
    ```
* - {py:obj}`BB_CONFIG <tests.satosa.backends.test_bitbucket.BB_CONFIG>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.BB_CONFIG
    :summary:
    ```
* - {py:obj}`BB_RESPONSE_CODE <tests.satosa.backends.test_bitbucket.BB_RESPONSE_CODE>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.BB_RESPONSE_CODE
    :summary:
    ```
* - {py:obj}`BB_USER_EMAIL_RESPONSE <tests.satosa.backends.test_bitbucket.BB_USER_EMAIL_RESPONSE>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.BB_USER_EMAIL_RESPONSE
    :summary:
    ```
* - {py:obj}`BB_USER_RESPONSE <tests.satosa.backends.test_bitbucket.BB_USER_RESPONSE>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.BB_USER_RESPONSE
    :summary:
    ```
* - {py:obj}`CLIENT_ID <tests.satosa.backends.test_bitbucket.CLIENT_ID>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.CLIENT_ID
    :summary:
    ```
* - {py:obj}`INTERNAL_ATTRIBUTES <tests.satosa.backends.test_bitbucket.INTERNAL_ATTRIBUTES>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.INTERNAL_ATTRIBUTES
    :summary:
    ```
* - {py:obj}`mock_get_state <tests.satosa.backends.test_bitbucket.mock_get_state>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.mock_get_state
    :summary:
    ```
````

### API

````{py:data} AUTHZ_PAGE
:canonical: tests.satosa.backends.test_bitbucket.AUTHZ_PAGE
:value: >
   'bitbucket'

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.AUTHZ_PAGE
```

````

````{py:data} BASE_URL
:canonical: tests.satosa.backends.test_bitbucket.BASE_URL
:value: >
   'https://client.example.com'

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.BASE_URL
```

````

````{py:data} BB_CONFIG
:canonical: tests.satosa.backends.test_bitbucket.BB_CONFIG
:value: >
   None

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.BB_CONFIG
```

````

````{py:data} BB_RESPONSE_CODE
:canonical: tests.satosa.backends.test_bitbucket.BB_RESPONSE_CODE
:value: >
   'the_bb_code'

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.BB_RESPONSE_CODE
```

````

````{py:data} BB_USER_EMAIL_RESPONSE
:canonical: tests.satosa.backends.test_bitbucket.BB_USER_EMAIL_RESPONSE
:value: >
   None

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.BB_USER_EMAIL_RESPONSE
```

````

````{py:data} BB_USER_RESPONSE
:canonical: tests.satosa.backends.test_bitbucket.BB_USER_RESPONSE
:value: >
   None

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.BB_USER_RESPONSE
```

````

````{py:data} CLIENT_ID
:canonical: tests.satosa.backends.test_bitbucket.CLIENT_ID
:value: >
   'bitbucket_client_id'

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.CLIENT_ID
```

````

````{py:data} INTERNAL_ATTRIBUTES
:canonical: tests.satosa.backends.test_bitbucket.INTERNAL_ATTRIBUTES
:value: >
   None

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.INTERNAL_ATTRIBUTES
```

````

`````{py:class} TestBitBucketBackend
:canonical: tests.satosa.backends.test_bitbucket.TestBitBucketBackend

Bases: {py:obj}`object`

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.TestBitBucketBackend
```

````{py:method} assert_expected_attributes()
:canonical: tests.satosa.backends.test_bitbucket.TestBitBucketBackend.assert_expected_attributes

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.TestBitBucketBackend.assert_expected_attributes
```

````

````{py:method} assert_token_request(request_args, state, **kwargs)
:canonical: tests.satosa.backends.test_bitbucket.TestBitBucketBackend.assert_token_request

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.TestBitBucketBackend.assert_token_request
```

````

````{py:method} create_backend()
:canonical: tests.satosa.backends.test_bitbucket.TestBitBucketBackend.create_backend

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.TestBitBucketBackend.create_backend
```

````

````{py:method} incoming_authn_response(context)
:canonical: tests.satosa.backends.test_bitbucket.TestBitBucketBackend.incoming_authn_response

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.TestBitBucketBackend.incoming_authn_response
```

````

````{py:method} setup_bitbucket_response()
:canonical: tests.satosa.backends.test_bitbucket.TestBitBucketBackend.setup_bitbucket_response

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.TestBitBucketBackend.setup_bitbucket_response
```

````

````{py:method} test_authn_response(incoming_authn_response)
:canonical: tests.satosa.backends.test_bitbucket.TestBitBucketBackend.test_authn_response

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.TestBitBucketBackend.test_authn_response
```

````

````{py:method} test_entire_flow(context)
:canonical: tests.satosa.backends.test_bitbucket.TestBitBucketBackend.test_entire_flow

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.TestBitBucketBackend.test_entire_flow
```

````

````{py:method} test_register_endpoints()
:canonical: tests.satosa.backends.test_bitbucket.TestBitBucketBackend.test_register_endpoints

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.TestBitBucketBackend.test_register_endpoints
```

````

````{py:method} test_start_auth(context)
:canonical: tests.satosa.backends.test_bitbucket.TestBitBucketBackend.test_start_auth

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.TestBitBucketBackend.test_start_auth
```

````

`````

````{py:data} mock_get_state
:canonical: tests.satosa.backends.test_bitbucket.mock_get_state
:value: >
   'Mock(...)'

```{autodoc2-docstring} tests.satosa.backends.test_bitbucket.mock_get_state
```

````
