# {py:mod}`tests.satosa.backends.test_orcid`

```{py:module} tests.satosa.backends.test_orcid
```

```{autodoc2-docstring} tests.satosa.backends.test_orcid
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestOrcidBackend <tests.satosa.backends.test_orcid.TestOrcidBackend>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_orcid.TestOrcidBackend
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ORCID_PERSON_COUNTRY <tests.satosa.backends.test_orcid.ORCID_PERSON_COUNTRY>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_orcid.ORCID_PERSON_COUNTRY
    :summary:
    ```
* - {py:obj}`ORCID_PERSON_EMAIL <tests.satosa.backends.test_orcid.ORCID_PERSON_EMAIL>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_orcid.ORCID_PERSON_EMAIL
    :summary:
    ```
* - {py:obj}`ORCID_PERSON_FAMILY_NAME <tests.satosa.backends.test_orcid.ORCID_PERSON_FAMILY_NAME>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_orcid.ORCID_PERSON_FAMILY_NAME
    :summary:
    ```
* - {py:obj}`ORCID_PERSON_GIVEN_NAME <tests.satosa.backends.test_orcid.ORCID_PERSON_GIVEN_NAME>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_orcid.ORCID_PERSON_GIVEN_NAME
    :summary:
    ```
* - {py:obj}`ORCID_PERSON_ID <tests.satosa.backends.test_orcid.ORCID_PERSON_ID>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_orcid.ORCID_PERSON_ID
    :summary:
    ```
* - {py:obj}`ORCID_PERSON_NAME <tests.satosa.backends.test_orcid.ORCID_PERSON_NAME>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_orcid.ORCID_PERSON_NAME
    :summary:
    ```
* - {py:obj}`mock_get_state <tests.satosa.backends.test_orcid.mock_get_state>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_orcid.mock_get_state
    :summary:
    ```
````

### API

````{py:data} ORCID_PERSON_COUNTRY
:canonical: tests.satosa.backends.test_orcid.ORCID_PERSON_COUNTRY
:value: >
   'XX'

```{autodoc2-docstring} tests.satosa.backends.test_orcid.ORCID_PERSON_COUNTRY
```

````

````{py:data} ORCID_PERSON_EMAIL
:canonical: tests.satosa.backends.test_orcid.ORCID_PERSON_EMAIL
:value: >
   'orcid_email'

```{autodoc2-docstring} tests.satosa.backends.test_orcid.ORCID_PERSON_EMAIL
```

````

````{py:data} ORCID_PERSON_FAMILY_NAME
:canonical: tests.satosa.backends.test_orcid.ORCID_PERSON_FAMILY_NAME
:value: >
   'orcid_family_name'

```{autodoc2-docstring} tests.satosa.backends.test_orcid.ORCID_PERSON_FAMILY_NAME
```

````

````{py:data} ORCID_PERSON_GIVEN_NAME
:canonical: tests.satosa.backends.test_orcid.ORCID_PERSON_GIVEN_NAME
:value: >
   'orcid_given_name'

```{autodoc2-docstring} tests.satosa.backends.test_orcid.ORCID_PERSON_GIVEN_NAME
```

````

````{py:data} ORCID_PERSON_ID
:canonical: tests.satosa.backends.test_orcid.ORCID_PERSON_ID
:value: >
   '0000-0000-0000-0000'

```{autodoc2-docstring} tests.satosa.backends.test_orcid.ORCID_PERSON_ID
```

````

````{py:data} ORCID_PERSON_NAME
:canonical: tests.satosa.backends.test_orcid.ORCID_PERSON_NAME
:value: >
   'format(...)'

```{autodoc2-docstring} tests.satosa.backends.test_orcid.ORCID_PERSON_NAME
```

````

`````{py:class} TestOrcidBackend
:canonical: tests.satosa.backends.test_orcid.TestOrcidBackend

Bases: {py:obj}`object`

```{autodoc2-docstring} tests.satosa.backends.test_orcid.TestOrcidBackend
```

````{py:method} assert_expected_attributes(user_claims, actual_attributes)
:canonical: tests.satosa.backends.test_orcid.TestOrcidBackend.assert_expected_attributes

```{autodoc2-docstring} tests.satosa.backends.test_orcid.TestOrcidBackend.assert_expected_attributes
```

````

````{py:method} backend_config()
:canonical: tests.satosa.backends.test_orcid.TestOrcidBackend.backend_config

```{autodoc2-docstring} tests.satosa.backends.test_orcid.TestOrcidBackend.backend_config
```

````

````{py:method} create_backend(internal_attributes, backend_config)
:canonical: tests.satosa.backends.test_orcid.TestOrcidBackend.create_backend

```{autodoc2-docstring} tests.satosa.backends.test_orcid.TestOrcidBackend.create_backend
```

````

````{py:method} incoming_authn_response(context, backend_config)
:canonical: tests.satosa.backends.test_orcid.TestOrcidBackend.incoming_authn_response

```{autodoc2-docstring} tests.satosa.backends.test_orcid.TestOrcidBackend.incoming_authn_response
```

````

````{py:method} internal_attributes()
:canonical: tests.satosa.backends.test_orcid.TestOrcidBackend.internal_attributes

```{autodoc2-docstring} tests.satosa.backends.test_orcid.TestOrcidBackend.internal_attributes
```

````

````{py:method} setup_token_endpoint(token_endpoint_url)
:canonical: tests.satosa.backends.test_orcid.TestOrcidBackend.setup_token_endpoint

```{autodoc2-docstring} tests.satosa.backends.test_orcid.TestOrcidBackend.setup_token_endpoint
```

````

````{py:method} setup_userinfo_endpoint(userinfo_endpoint_url, userinfo)
:canonical: tests.satosa.backends.test_orcid.TestOrcidBackend.setup_userinfo_endpoint

```{autodoc2-docstring} tests.satosa.backends.test_orcid.TestOrcidBackend.setup_userinfo_endpoint
```

````

````{py:method} test_authn_response(backend_config, userinfo, incoming_authn_response)
:canonical: tests.satosa.backends.test_orcid.TestOrcidBackend.test_authn_response

```{autodoc2-docstring} tests.satosa.backends.test_orcid.TestOrcidBackend.test_authn_response
```

````

````{py:method} test_start_auth(context, backend_config)
:canonical: tests.satosa.backends.test_orcid.TestOrcidBackend.test_start_auth

```{autodoc2-docstring} tests.satosa.backends.test_orcid.TestOrcidBackend.test_start_auth
```

````

````{py:method} test_user_information(context, backend_config, userinfo)
:canonical: tests.satosa.backends.test_orcid.TestOrcidBackend.test_user_information

```{autodoc2-docstring} tests.satosa.backends.test_orcid.TestOrcidBackend.test_user_information
```

````

````{py:method} test_user_information_private(context, backend_config, userinfo_private)
:canonical: tests.satosa.backends.test_orcid.TestOrcidBackend.test_user_information_private

```{autodoc2-docstring} tests.satosa.backends.test_orcid.TestOrcidBackend.test_user_information_private
```

````

````{py:method} userinfo()
:canonical: tests.satosa.backends.test_orcid.TestOrcidBackend.userinfo

```{autodoc2-docstring} tests.satosa.backends.test_orcid.TestOrcidBackend.userinfo
```

````

````{py:method} userinfo_private()
:canonical: tests.satosa.backends.test_orcid.TestOrcidBackend.userinfo_private

```{autodoc2-docstring} tests.satosa.backends.test_orcid.TestOrcidBackend.userinfo_private
```

````

`````

````{py:data} mock_get_state
:canonical: tests.satosa.backends.test_orcid.mock_get_state
:value: >
   'Mock(...)'

```{autodoc2-docstring} tests.satosa.backends.test_orcid.mock_get_state
```

````
