# {py:mod}`tests.satosa.frontends.test_saml2`

```{py:module} tests.satosa.frontends.test_saml2
```

```{autodoc2-docstring} tests.satosa.frontends.test_saml2
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestSAMLFrontend <tests.satosa.frontends.test_saml2.TestSAMLFrontend>`
  - ```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend
    :summary:
    ```
* - {py:obj}`TestSAMLMirrorFrontend <tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend>`
  - ```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend
    :summary:
    ```
* - {py:obj}`TestSAMLVirtualCoFrontend <tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend>`
  - ```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend
    :summary:
    ```
* - {py:obj}`TestSubjectTypeToSamlNameIdFormat <tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat>`
  - ```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BASE_URL <tests.satosa.frontends.test_saml2.BASE_URL>`
  - ```{autodoc2-docstring} tests.satosa.frontends.test_saml2.BASE_URL
    :summary:
    ```
* - {py:obj}`ENDPOINTS <tests.satosa.frontends.test_saml2.ENDPOINTS>`
  - ```{autodoc2-docstring} tests.satosa.frontends.test_saml2.ENDPOINTS
    :summary:
    ```
* - {py:obj}`INTERNAL_ATTRIBUTES <tests.satosa.frontends.test_saml2.INTERNAL_ATTRIBUTES>`
  - ```{autodoc2-docstring} tests.satosa.frontends.test_saml2.INTERNAL_ATTRIBUTES
    :summary:
    ```
````

### API

````{py:data} BASE_URL
:canonical: tests.satosa.frontends.test_saml2.BASE_URL
:value: >
   'https://satosa-idp.example.com'

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.BASE_URL
```

````

````{py:data} ENDPOINTS
:canonical: tests.satosa.frontends.test_saml2.ENDPOINTS
:value: >
   None

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.ENDPOINTS
```

````

````{py:data} INTERNAL_ATTRIBUTES
:canonical: tests.satosa.frontends.test_saml2.INTERNAL_ATTRIBUTES
:value: >
   None

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.INTERNAL_ATTRIBUTES
```

````

`````{py:class} TestSAMLFrontend
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend
```

````{py:method} construct_base_url_from_entity_id(entity_id)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.construct_base_url_from_entity_id

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.construct_base_url_from_entity_id
```

````

````{py:method} get_auth_response(samlfrontend, context, internal_response, sp_conf, idp_metadata_str)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.get_auth_response

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.get_auth_response
```

````

````{py:method} internal_response(idp_conf)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.internal_response

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.internal_response
```

````

````{py:method} setup_for_authn_req(context, idp_conf, sp_conf, nameid_format=None, relay_state='relay_state', internal_attributes=INTERNAL_ATTRIBUTES, extra_config={}, subject=None)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.setup_for_authn_req

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.setup_for_authn_req
```

````

````{py:method} test_acr_mapping_in_authn_response(context, idp_conf, sp_conf, internal_response)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_acr_mapping_in_authn_response

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_acr_mapping_in_authn_response
```

````

````{py:method} test_acr_mapping_per_idp_in_authn_response(context, idp_conf, sp_conf, internal_response)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_acr_mapping_per_idp_in_authn_response

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_acr_mapping_per_idp_in_authn_response
```

````

````{py:method} test_config_error_handling(conf)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_config_error_handling

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_config_error_handling
```

````

````{py:method} test_create_authn_request_with_subject(context, idp_conf, sp_conf, internal_response)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_create_authn_request_with_subject

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_create_authn_request_with_subject
```

````

````{py:method} test_custom_attribute_release_with_less_attributes_than_entity_category(context, idp_conf, sp_conf, internal_response)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_custom_attribute_release_with_less_attributes_than_entity_category

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_custom_attribute_release_with_less_attributes_than_entity_category
```

````

````{py:method} test_get_filter_attributes_with_sp_requested_attributes_without_friendlyname(idp_conf)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_get_filter_attributes_with_sp_requested_attributes_without_friendlyname

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_get_filter_attributes_with_sp_requested_attributes_without_friendlyname
```

````

````{py:method} test_handle_authn_request(context, idp_conf, sp_conf, internal_response)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_handle_authn_request

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_handle_authn_request
```

````

````{py:method} test_handle_authn_request_without_name_id_policy_and_metadata_without_name_id_format(context, idp_conf, sp_conf)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_handle_authn_request_without_name_id_policy_and_metadata_without_name_id_format

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_handle_authn_request_without_name_id_policy_and_metadata_without_name_id_format
```

````

````{py:method} test_handle_authn_request_without_name_id_policy_default_to_name_id_format_from_metadata(context, idp_conf, sp_conf)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_handle_authn_request_without_name_id_policy_default_to_name_id_format_from_metadata

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_handle_authn_request_without_name_id_policy_default_to_name_id_format_from_metadata
```

````

````{py:method} test_handle_authn_response_without_name_id(context, idp_conf, sp_conf, internal_response)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_handle_authn_response_without_name_id

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_handle_authn_response_without_name_id
```

````

````{py:method} test_handle_authn_response_without_relay_state(context, idp_conf, sp_conf, internal_response)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_handle_authn_response_without_relay_state

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_handle_authn_response_without_relay_state
```

````

````{py:method} test_metadata_endpoint(context, idp_conf)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_metadata_endpoint

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_metadata_endpoint
```

````

````{py:method} test_register_endpoints(idp_conf)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_register_endpoints

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_register_endpoints
```

````

````{py:method} test_respect_sp_entity_categories(context, entity_category, entity_category_module, expected_attributes, idp_conf, sp_conf, internal_response)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_respect_sp_entity_categories

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_respect_sp_entity_categories
```

````

````{py:method} test_sp_metadata_including_uiinfo_display_name(context, idp_conf, sp_conf)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_sp_metadata_including_uiinfo_display_name

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_sp_metadata_including_uiinfo_display_name
```

````

````{py:method} test_sp_metadata_including_uiinfo_without_display_name(context, idp_conf, sp_conf)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_sp_metadata_including_uiinfo_without_display_name

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_sp_metadata_including_uiinfo_without_display_name
```

````

````{py:method} test_sp_metadata_without_uiinfo(context, idp_conf, sp_conf)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_sp_metadata_without_uiinfo

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLFrontend.test_sp_metadata_without_uiinfo
```

````

`````

`````{py:class} TestSAMLMirrorFrontend
:canonical: tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend
```

````{py:attribute} BACKEND
:canonical: tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend.BACKEND
:value: >
   'test_backend'

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend.BACKEND
```

````

````{py:attribute} TARGET_ENTITY_ID
:canonical: tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend.TARGET_ENTITY_ID
:value: >
   'target-idp.entity_id'

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend.TARGET_ENTITY_ID
```

````

````{py:method} assert_dynamic_endpoints(sso_endpoints)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend.assert_dynamic_endpoints

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend.assert_dynamic_endpoints
```

````

````{py:method} create_frontend(idp_conf)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend.create_frontend

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend.create_frontend
```

````

````{py:method} test_load_endpoints_to_config()
:canonical: tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend.test_load_endpoints_to_config

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend.test_load_endpoints_to_config
```

````

````{py:method} test_load_idp_dynamic_endpoints(context)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend.test_load_idp_dynamic_endpoints

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend.test_load_idp_dynamic_endpoints
```

````

````{py:method} test_load_idp_dynamic_entity_id(idp_conf)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend.test_load_idp_dynamic_entity_id

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLMirrorFrontend.test_load_idp_dynamic_entity_id
```

````

`````

`````{py:class} TestSAMLVirtualCoFrontend
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend

Bases: {py:obj}`tests.satosa.frontends.test_saml2.TestSAMLFrontend`

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend
```

````{py:attribute} BACKEND
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.BACKEND
:value: >
   'test_backend'

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.BACKEND
```

````

````{py:attribute} BACKEND_1
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.BACKEND_1
:value: >
   'test_backend_1'

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.BACKEND_1
```

````

````{py:attribute} CO
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.CO
:value: >
   'MESS'

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.CO
```

````

````{py:attribute} CO_C
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.CO_C
:value: >
   'countryname'

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.CO_C
```

````

````{py:attribute} CO_CO
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.CO_CO
:value: >
   'friendlycountryname'

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.CO_CO
```

````

````{py:attribute} CO_NOREDUORGACRONYM
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.CO_NOREDUORGACRONYM
:value: >
   'noreduorgacronym'

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.CO_NOREDUORGACRONYM
```

````

````{py:attribute} CO_O
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.CO_O
:value: >
   'organization'

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.CO_O
```

````

````{py:attribute} CO_SCOPE
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.CO_SCOPE
:value: >
   'messproject.org'

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.CO_SCOPE
```

````

````{py:attribute} CO_STATIC_SAML_ATTRIBUTES
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.CO_STATIC_SAML_ATTRIBUTES
:value: >
   None

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.CO_STATIC_SAML_ATTRIBUTES
```

````

````{py:attribute} KEY_SSO
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.KEY_SSO
:value: >
   'single_sign_on_service'

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.KEY_SSO
```

````

````{py:method} _make_context(context, backend, co_name)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend._make_context

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend._make_context
```

````

````{py:method} context(context)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.context

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.context
```

````

````{py:method} frontend(idp_conf, sp_conf)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.frontend

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.frontend
```

````

````{py:method} test_co_static_attributes(frontend, context, internal_response, idp_conf, sp_conf)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.test_co_static_attributes

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.test_co_static_attributes
```

````

````{py:method} test_create_co_virtual_idp(frontend, context, idp_conf)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.test_create_co_virtual_idp

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.test_create_co_virtual_idp
```

````

````{py:method} test_create_co_virtual_idp_with_entity_id_templates(frontend, context)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.test_create_co_virtual_idp_with_entity_id_templates

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.test_create_co_virtual_idp_with_entity_id_templates
```

````

````{py:method} test_create_state_data(frontend, context, idp_conf)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.test_create_state_data

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.test_create_state_data
```

````

````{py:method} test_get_co_name(frontend, context)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.test_get_co_name

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.test_get_co_name
```

````

````{py:method} test_register_endpoints(frontend, context)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.test_register_endpoints

````

````{py:method} test_register_endpoints_throws_error_in_case_duplicate_entity_ids(frontend)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.test_register_endpoints_throws_error_in_case_duplicate_entity_ids

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.test_register_endpoints_throws_error_in_case_duplicate_entity_ids
```

````

````{py:method} test_register_endpoints_with_metadata_endpoints(frontend, context)
:canonical: tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.test_register_endpoints_with_metadata_endpoints

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSAMLVirtualCoFrontend.test_register_endpoints_with_metadata_endpoints
```

````

`````

`````{py:class} TestSubjectTypeToSamlNameIdFormat
:canonical: tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat
```

````{py:method} test_should_default_to_persistent()
:canonical: tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat.test_should_default_to_persistent

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat.test_should_default_to_persistent
```

````

````{py:method} test_should_map_emailaddress()
:canonical: tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat.test_should_map_emailaddress

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat.test_should_map_emailaddress
```

````

````{py:method} test_should_map_pairwise()
:canonical: tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat.test_should_map_pairwise

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat.test_should_map_pairwise
```

````

````{py:method} test_should_map_persistent()
:canonical: tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat.test_should_map_persistent

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat.test_should_map_persistent
```

````

````{py:method} test_should_map_public()
:canonical: tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat.test_should_map_public

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat.test_should_map_public
```

````

````{py:method} test_should_map_transient()
:canonical: tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat.test_should_map_transient

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat.test_should_map_transient
```

````

````{py:method} test_should_map_unspecified()
:canonical: tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat.test_should_map_unspecified

```{autodoc2-docstring} tests.satosa.frontends.test_saml2.TestSubjectTypeToSamlNameIdFormat.test_should_map_unspecified
```

````

`````
