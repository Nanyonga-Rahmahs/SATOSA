# {py:mod}`tests.satosa.backends.test_saml2`

```{py:module} tests.satosa.backends.test_saml2
```

```{autodoc2-docstring} tests.satosa.backends.test_saml2
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestSAMLBackend <tests.satosa.backends.test_saml2.TestSAMLBackend>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend
    :summary:
    ```
* - {py:obj}`TestSAMLBackendRedirects <tests.satosa.backends.test_saml2.TestSAMLBackendRedirects>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackendRedirects
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`assert_authn_response <tests.satosa.backends.test_saml2.assert_authn_response>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_saml2.assert_authn_response
    :summary:
    ```
* - {py:obj}`assert_redirect_to_discovery_server <tests.satosa.backends.test_saml2.assert_redirect_to_discovery_server>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_saml2.assert_redirect_to_discovery_server
    :summary:
    ```
* - {py:obj}`assert_redirect_to_idp <tests.satosa.backends.test_saml2.assert_redirect_to_idp>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_saml2.assert_redirect_to_idp
    :summary:
    ```
* - {py:obj}`setup_test_config <tests.satosa.backends.test_saml2.setup_test_config>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_saml2.setup_test_config
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DISCOSRV_URL <tests.satosa.backends.test_saml2.DISCOSRV_URL>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_saml2.DISCOSRV_URL
    :summary:
    ```
* - {py:obj}`INTERNAL_ATTRIBUTES <tests.satosa.backends.test_saml2.INTERNAL_ATTRIBUTES>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_saml2.INTERNAL_ATTRIBUTES
    :summary:
    ```
* - {py:obj}`TEST_RESOURCE_BASE_PATH <tests.satosa.backends.test_saml2.TEST_RESOURCE_BASE_PATH>`
  - ```{autodoc2-docstring} tests.satosa.backends.test_saml2.TEST_RESOURCE_BASE_PATH
    :summary:
    ```
````

### API

````{py:data} DISCOSRV_URL
:canonical: tests.satosa.backends.test_saml2.DISCOSRV_URL
:value: >
   'https://my.dicso.com/role/idp.ds'

```{autodoc2-docstring} tests.satosa.backends.test_saml2.DISCOSRV_URL
```

````

````{py:data} INTERNAL_ATTRIBUTES
:canonical: tests.satosa.backends.test_saml2.INTERNAL_ATTRIBUTES
:value: >
   None

```{autodoc2-docstring} tests.satosa.backends.test_saml2.INTERNAL_ATTRIBUTES
```

````

````{py:data} TEST_RESOURCE_BASE_PATH
:canonical: tests.satosa.backends.test_saml2.TEST_RESOURCE_BASE_PATH
:value: >
   'join(...)'

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TEST_RESOURCE_BASE_PATH
```

````

`````{py:class} TestSAMLBackend
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend
```

````{py:method} _make_authn_request(http_host, context, config, entity_id)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend._make_authn_request

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend._make_authn_request
```

````

````{py:method} _perform_request_response(idp_conf, sp_conf, response_binding, receive_nameid=True)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend._perform_request_response

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend._perform_request_response
```

````

````{py:method} create_backend(sp_conf, idp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.create_backend

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.create_backend
```

````

````{py:method} test_acs_selection_strategy(context, sp_conf, idp_conf, hostname, strat)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_acs_selection_strategy

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_acs_selection_strategy
```

````

````{py:method} test_authn_request(context, idp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_authn_request

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_authn_request
```

````

````{py:method} test_authn_response(context, idp_conf, sp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_authn_response

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_authn_response
```

````

````{py:method} test_authn_response_no_name_id(context, idp_conf, sp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_authn_response_no_name_id

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_authn_response_no_name_id
```

````

````{py:method} test_authn_response_with_encrypted_assertion(sp_conf, context)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_authn_response_with_encrypted_assertion

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_authn_response_with_encrypted_assertion
```

````

````{py:method} test_backend_reads_encryption_key_from_encryption_keypair(sp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_backend_reads_encryption_key_from_encryption_keypair

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_backend_reads_encryption_key_from_encryption_keypair
```

````

````{py:method} test_backend_reads_encryption_key_from_key_file(sp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_backend_reads_encryption_key_from_key_file

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_backend_reads_encryption_key_from_key_file
```

````

````{py:method} test_discovery_server_set_in_context(context, sp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_discovery_server_set_in_context

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_discovery_server_set_in_context
```

````

````{py:method} test_full_flow(context, idp_conf, sp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_full_flow

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_full_flow
```

````

````{py:method} test_get_metadata_desc(sp_conf, idp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_get_metadata_desc

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_get_metadata_desc
```

````

````{py:method} test_get_metadata_desc_with_logo_without_lang(sp_conf, idp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_get_metadata_desc_with_logo_without_lang

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_get_metadata_desc_with_logo_without_lang
```

````

````{py:method} test_metadata_endpoint(context, sp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_metadata_endpoint

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_metadata_endpoint
```

````

````{py:method} test_no_relay_state_raises_error(context, idp_conf, sp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_no_relay_state_raises_error

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_no_relay_state_raises_error
```

````

````{py:method} test_no_state_raises_error(context, idp_conf, sp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_no_state_raises_error

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_no_state_raises_error
```

````

````{py:method} test_redirect_to_idp_if_only_one_idp_in_metadata(context, sp_conf, idp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_redirect_to_idp_if_only_one_idp_in_metadata

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_redirect_to_idp_if_only_one_idp_in_metadata
```

````

````{py:method} test_register_endpoints(sp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_register_endpoints

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_register_endpoints
```

````

````{py:method} test_start_auth_defaults_to_redirecting_to_discovery_server(context, sp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_start_auth_defaults_to_redirecting_to_discovery_server

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_start_auth_defaults_to_redirecting_to_discovery_server
```

````

````{py:method} test_start_auth_redirects_directly_to_mirrored_idp(context, idp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_start_auth_redirects_directly_to_mirrored_idp

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_start_auth_redirects_directly_to_mirrored_idp
```

````

````{py:method} test_unknown_or_no_hostname_selects_first_acs(context, sp_conf, idp_conf, hostname)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackend.test_unknown_or_no_hostname_selects_first_acs

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackend.test_unknown_or_no_hostname_selects_first_acs
```

````

`````

`````{py:class} TestSAMLBackendRedirects
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackendRedirects

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackendRedirects
```

````{py:method} test_default_redirect_to_discovery_service_if_using_mdq(context, sp_conf, idp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackendRedirects.test_default_redirect_to_discovery_service_if_using_mdq

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackendRedirects.test_default_redirect_to_discovery_service_if_using_mdq
```

````

````{py:method} test_use_of_disco_or_redirect_to_idp_when_using_mdq_and_forceauthn_is_not_set(context, sp_conf, idp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackendRedirects.test_use_of_disco_or_redirect_to_idp_when_using_mdq_and_forceauthn_is_not_set

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackendRedirects.test_use_of_disco_or_redirect_to_idp_when_using_mdq_and_forceauthn_is_not_set
```

````

````{py:method} test_use_of_disco_or_redirect_to_idp_when_using_mdq_and_forceauthn_is_set_1(context, sp_conf, idp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackendRedirects.test_use_of_disco_or_redirect_to_idp_when_using_mdq_and_forceauthn_is_set_1

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackendRedirects.test_use_of_disco_or_redirect_to_idp_when_using_mdq_and_forceauthn_is_set_1
```

````

````{py:method} test_use_of_disco_or_redirect_to_idp_when_using_mdq_and_forceauthn_is_set_true(context, sp_conf, idp_conf)
:canonical: tests.satosa.backends.test_saml2.TestSAMLBackendRedirects.test_use_of_disco_or_redirect_to_idp_when_using_mdq_and_forceauthn_is_set_true

```{autodoc2-docstring} tests.satosa.backends.test_saml2.TestSAMLBackendRedirects.test_use_of_disco_or_redirect_to_idp_when_using_mdq_and_forceauthn_is_set_true
```

````

`````

````{py:function} assert_authn_response(internal_resp)
:canonical: tests.satosa.backends.test_saml2.assert_authn_response

```{autodoc2-docstring} tests.satosa.backends.test_saml2.assert_authn_response
```
````

````{py:function} assert_redirect_to_discovery_server(redirect_response, sp_conf, expected_discosrv_url)
:canonical: tests.satosa.backends.test_saml2.assert_redirect_to_discovery_server

```{autodoc2-docstring} tests.satosa.backends.test_saml2.assert_redirect_to_discovery_server
```
````

````{py:function} assert_redirect_to_idp(redirect_response, idp_conf)
:canonical: tests.satosa.backends.test_saml2.assert_redirect_to_idp

```{autodoc2-docstring} tests.satosa.backends.test_saml2.assert_redirect_to_idp
```
````

````{py:function} setup_test_config(sp_conf, idp_conf)
:canonical: tests.satosa.backends.test_saml2.setup_test_config

```{autodoc2-docstring} tests.satosa.backends.test_saml2.setup_test_config
```
````
