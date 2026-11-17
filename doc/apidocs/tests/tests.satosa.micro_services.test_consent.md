# {py:mod}`tests.satosa.micro_services.test_consent`

```{py:module} tests.satosa.micro_services.test_consent
```

```{autodoc2-docstring} tests.satosa.micro_services.test_consent
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestConsent <tests.satosa.micro_services.test_consent.TestConsent>`
  - ```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ATTRIBUTES <tests.satosa.micro_services.test_consent.ATTRIBUTES>`
  - ```{autodoc2-docstring} tests.satosa.micro_services.test_consent.ATTRIBUTES
    :summary:
    ```
* - {py:obj}`CONSENT_SERVICE_URL <tests.satosa.micro_services.test_consent.CONSENT_SERVICE_URL>`
  - ```{autodoc2-docstring} tests.satosa.micro_services.test_consent.CONSENT_SERVICE_URL
    :summary:
    ```
* - {py:obj}`FILTER <tests.satosa.micro_services.test_consent.FILTER>`
  - ```{autodoc2-docstring} tests.satosa.micro_services.test_consent.FILTER
    :summary:
    ```
* - {py:obj}`USER_ID_ATTR <tests.satosa.micro_services.test_consent.USER_ID_ATTR>`
  - ```{autodoc2-docstring} tests.satosa.micro_services.test_consent.USER_ID_ATTR
    :summary:
    ```
````

### API

````{py:data} ATTRIBUTES
:canonical: tests.satosa.micro_services.test_consent.ATTRIBUTES
:value: >
   None

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.ATTRIBUTES
```

````

````{py:data} CONSENT_SERVICE_URL
:canonical: tests.satosa.micro_services.test_consent.CONSENT_SERVICE_URL
:value: >
   'https://consent.example.com'

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.CONSENT_SERVICE_URL
```

````

````{py:data} FILTER
:canonical: tests.satosa.micro_services.test_consent.FILTER
:value: >
   ['displayName', 'co']

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.FILTER
```

````

`````{py:class} TestConsent
:canonical: tests.satosa.micro_services.test_consent.TestConsent

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent
```

````{py:method} assert_redirect(redirect_resp, expected_ticket)
:canonical: tests.satosa.micro_services.test_consent.TestConsent.assert_redirect

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.assert_redirect
```

````

````{py:method} assert_registration_req(request, internal_response, sign_key_path, base_url, requester_name)
:canonical: tests.satosa.micro_services.test_consent.TestConsent.assert_registration_req

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.assert_registration_req
```

````

````{py:method} consent_config(signing_key_path)
:canonical: tests.satosa.micro_services.test_consent.TestConsent.consent_config

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.consent_config
```

````

````{py:method} consent_registration_endpoint_regex()
:canonical: tests.satosa.micro_services.test_consent.TestConsent.consent_registration_endpoint_regex

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.consent_registration_endpoint_regex
```

````

````{py:method} consent_verify_endpoint_regex()
:canonical: tests.satosa.micro_services.test_consent.TestConsent.consent_verify_endpoint_regex

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.consent_verify_endpoint_regex
```

````

````{py:method} create_module(consent_config)
:canonical: tests.satosa.micro_services.test_consent.TestConsent.create_module

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.create_module
```

````

````{py:method} internal_request()
:canonical: tests.satosa.micro_services.test_consent.TestConsent.internal_request

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.internal_request
```

````

````{py:method} internal_response()
:canonical: tests.satosa.micro_services.test_consent.TestConsent.internal_response

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.internal_response
```

````

````{py:method} test_consent_full_flow(context, consent_config, internal_response, internal_request, consent_verify_endpoint_regex, consent_registration_endpoint_regex)
:canonical: tests.satosa.micro_services.test_consent.TestConsent.test_consent_full_flow

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.test_consent_full_flow
```

````

````{py:method} test_consent_handles_connection_error(context, internal_response, internal_request, consent_verify_endpoint_regex)
:canonical: tests.satosa.micro_services.test_consent.TestConsent.test_consent_handles_connection_error

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.test_consent_handles_connection_error
```

````

````{py:method} test_consent_not_given(context, consent_config, internal_response, internal_request, consent_verify_endpoint_regex, consent_registration_endpoint_regex)
:canonical: tests.satosa.micro_services.test_consent.TestConsent.test_consent_not_given

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.test_consent_not_given
```

````

````{py:method} test_consent_prev_given(context, internal_response, internal_request, consent_verify_endpoint_regex)
:canonical: tests.satosa.micro_services.test_consent.TestConsent.test_consent_prev_given

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.test_consent_prev_given
```

````

````{py:method} test_consent_registration(consent_config)
:canonical: tests.satosa.micro_services.test_consent.TestConsent.test_consent_registration

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.test_consent_registration
```

````

````{py:method} test_consent_registration_raises_on_unexpected_status_code(status, consent_config)
:canonical: tests.satosa.micro_services.test_consent.TestConsent.test_consent_registration_raises_on_unexpected_status_code

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.test_consent_registration_raises_on_unexpected_status_code
```

````

````{py:method} test_filter_attributes()
:canonical: tests.satosa.micro_services.test_consent.TestConsent.test_filter_attributes

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.test_filter_attributes
```

````

````{py:method} test_get_consent_id()
:canonical: tests.satosa.micro_services.test_consent.TestConsent.test_get_consent_id

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.test_get_consent_id
```

````

````{py:method} test_manage_consent_without_filter_passes_through_all_attributes(context, internal_response, consent_verify_endpoint_regex)
:canonical: tests.satosa.micro_services.test_consent.TestConsent.test_manage_consent_without_filter_passes_through_all_attributes

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.test_manage_consent_without_filter_passes_through_all_attributes
```

````

````{py:method} test_verify_consent(consent_config)
:canonical: tests.satosa.micro_services.test_consent.TestConsent.test_verify_consent

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.test_verify_consent
```

````

````{py:method} test_verify_consent_false_on_http_400(consent_config)
:canonical: tests.satosa.micro_services.test_consent.TestConsent.test_verify_consent_false_on_http_400

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.TestConsent.test_verify_consent_false_on_http_400
```

````

`````

````{py:data} USER_ID_ATTR
:canonical: tests.satosa.micro_services.test_consent.USER_ID_ATTR
:value: >
   'user_id'

```{autodoc2-docstring} tests.satosa.micro_services.test_consent.USER_ID_ATTR
```

````
