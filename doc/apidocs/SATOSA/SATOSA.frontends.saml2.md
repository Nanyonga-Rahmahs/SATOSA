# {py:mod}`SATOSA.frontends.saml2`

```{py:module} SATOSA.frontends.saml2
```

```{autodoc2-docstring} SATOSA.frontends.saml2
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SAMLFrontend <SATOSA.frontends.saml2.SAMLFrontend>`
  - ```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend
    :summary:
    ```
* - {py:obj}`SAMLMirrorFrontend <SATOSA.frontends.saml2.SAMLMirrorFrontend>`
  - ```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLMirrorFrontend
    :summary:
    ```
* - {py:obj}`SAMLVirtualCoFrontend <SATOSA.frontends.saml2.SAMLVirtualCoFrontend>`
  - ```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`subject_type_to_saml_nameid_format <SATOSA.frontends.saml2.subject_type_to_saml_nameid_format>`
  - ```{autodoc2-docstring} SATOSA.frontends.saml2.subject_type_to_saml_nameid_format
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.frontends.saml2.logger>`
  - ```{autodoc2-docstring} SATOSA.frontends.saml2.logger
    :summary:
    ```
* - {py:obj}`subject_type_map <SATOSA.frontends.saml2.subject_type_map>`
  - ```{autodoc2-docstring} SATOSA.frontends.saml2.subject_type_map
    :summary:
    ```
````

### API

`````{py:class} SAMLFrontend(auth_req_callback_func, internal_attributes, config, base_url, name)
:canonical: SATOSA.frontends.saml2.SAMLFrontend

Bases: {py:obj}`SATOSA.frontends.base.FrontendModule`, {py:obj}`satosa.base.SAMLBaseModule`

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend.__init__
```

````{py:attribute} KEY_CUSTOM_ATTR_RELEASE
:canonical: SATOSA.frontends.saml2.SAMLFrontend.KEY_CUSTOM_ATTR_RELEASE
:value: >
   'custom_attribute_release'

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend.KEY_CUSTOM_ATTR_RELEASE
```

````

````{py:attribute} KEY_ENDPOINTS
:canonical: SATOSA.frontends.saml2.SAMLFrontend.KEY_ENDPOINTS
:value: >
   'endpoints'

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend.KEY_ENDPOINTS
```

````

````{py:attribute} KEY_IDP_CONFIG
:canonical: SATOSA.frontends.saml2.SAMLFrontend.KEY_IDP_CONFIG
:value: >
   'idp_config'

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend.KEY_IDP_CONFIG
```

````

````{py:method} _build_idp_config_endpoints(config, providers)
:canonical: SATOSA.frontends.saml2.SAMLFrontend._build_idp_config_endpoints

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend._build_idp_config_endpoints
```

````

````{py:method} _create_state_data(context, resp_args, relay_state)
:canonical: SATOSA.frontends.saml2.SAMLFrontend._create_state_data

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend._create_state_data
```

````

````{py:method} _filter_attributes(idp, internal_response, context)
:canonical: SATOSA.frontends.saml2.SAMLFrontend._filter_attributes

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend._filter_attributes
```

````

````{py:method} _get_approved_attributes(idp, idp_policy, sp_entity_id, state)
:canonical: SATOSA.frontends.saml2.SAMLFrontend._get_approved_attributes

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend._get_approved_attributes
```

````

````{py:method} _get_sp_display_name(idp, entity_id)
:canonical: SATOSA.frontends.saml2.SAMLFrontend._get_sp_display_name

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend._get_sp_display_name
```

````

````{py:method} _handle_authn_request(context, binding_in, idp)
:canonical: SATOSA.frontends.saml2.SAMLFrontend._handle_authn_request

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend._handle_authn_request
```

````

````{py:method} _handle_authn_response(context, internal_response, idp)
:canonical: SATOSA.frontends.saml2.SAMLFrontend._handle_authn_response

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend._handle_authn_response
```

````

````{py:method} _handle_backend_error(exception, idp)
:canonical: SATOSA.frontends.saml2.SAMLFrontend._handle_backend_error

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend._handle_backend_error
```

````

````{py:method} _metadata_endpoint(context)
:canonical: SATOSA.frontends.saml2.SAMLFrontend._metadata_endpoint

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend._metadata_endpoint
```

````

````{py:method} _register_endpoints(providers)
:canonical: SATOSA.frontends.saml2.SAMLFrontend._register_endpoints

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend._register_endpoints
```

````

````{py:method} _reload_metadata(context)
:canonical: SATOSA.frontends.saml2.SAMLFrontend._reload_metadata

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend._reload_metadata
```

````

````{py:method} _set_common_domain_cookie(internal_response, http_args, context)
:canonical: SATOSA.frontends.saml2.SAMLFrontend._set_common_domain_cookie

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend._set_common_domain_cookie
```

````

````{py:method} _validate_config(config)
:canonical: SATOSA.frontends.saml2.SAMLFrontend._validate_config

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend._validate_config
```

````

````{py:method} handle_authn_request(context, binding_in)
:canonical: SATOSA.frontends.saml2.SAMLFrontend.handle_authn_request

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend.handle_authn_request
```

````

````{py:method} handle_authn_response(context, internal_response)
:canonical: SATOSA.frontends.saml2.SAMLFrontend.handle_authn_response

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend.handle_authn_response
```

````

````{py:method} handle_backend_error(exception)
:canonical: SATOSA.frontends.saml2.SAMLFrontend.handle_backend_error

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend.handle_backend_error
```

````

````{py:method} load_state(state)
:canonical: SATOSA.frontends.saml2.SAMLFrontend.load_state

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend.load_state
```

````

````{py:method} register_endpoints(backend_names)
:canonical: SATOSA.frontends.saml2.SAMLFrontend.register_endpoints

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLFrontend.register_endpoints
```

````

`````

`````{py:class} SAMLMirrorFrontend(auth_req_callback_func, internal_attributes, config, base_url, name)
:canonical: SATOSA.frontends.saml2.SAMLMirrorFrontend

Bases: {py:obj}`SATOSA.frontends.saml2.SAMLFrontend`

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLMirrorFrontend
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLMirrorFrontend.__init__
```

````{py:method} _create_state_data(context, resp_args, relay_state)
:canonical: SATOSA.frontends.saml2.SAMLMirrorFrontend._create_state_data

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLMirrorFrontend._create_state_data
```

````

````{py:method} _load_endpoints_to_config(provider, target_entity_id, config=None)
:canonical: SATOSA.frontends.saml2.SAMLMirrorFrontend._load_endpoints_to_config

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLMirrorFrontend._load_endpoints_to_config
```

````

````{py:method} _load_idp_dynamic_endpoints(context)
:canonical: SATOSA.frontends.saml2.SAMLMirrorFrontend._load_idp_dynamic_endpoints

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLMirrorFrontend._load_idp_dynamic_endpoints
```

````

````{py:method} _load_idp_dynamic_entity_id(state)
:canonical: SATOSA.frontends.saml2.SAMLMirrorFrontend._load_idp_dynamic_entity_id

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLMirrorFrontend._load_idp_dynamic_entity_id
```

````

````{py:method} _register_endpoints(providers)
:canonical: SATOSA.frontends.saml2.SAMLMirrorFrontend._register_endpoints

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLMirrorFrontend._register_endpoints
```

````

````{py:method} handle_authn_request(context, binding_in)
:canonical: SATOSA.frontends.saml2.SAMLMirrorFrontend.handle_authn_request

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLMirrorFrontend.handle_authn_request
```

````

````{py:method} handle_authn_response(context, internal_response)
:canonical: SATOSA.frontends.saml2.SAMLMirrorFrontend.handle_authn_response

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLMirrorFrontend.handle_authn_response
```

````

````{py:method} handle_backend_error(exception)
:canonical: SATOSA.frontends.saml2.SAMLMirrorFrontend.handle_backend_error

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLMirrorFrontend.handle_backend_error
```

````

`````

`````{py:class} SAMLVirtualCoFrontend(auth_req_callback_func, internal_attributes, config, base_url, name)
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend

Bases: {py:obj}`SATOSA.frontends.saml2.SAMLFrontend`

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend.__init__
```

````{py:attribute} KEY_CO
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_CO
:value: >
   'collaborative_organizations'

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_CO
```

````

````{py:attribute} KEY_CONTACT_PERSON
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_CONTACT_PERSON
:value: >
   'contact_person'

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_CONTACT_PERSON
```

````

````{py:attribute} KEY_CO_ATTRIBUTES
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_CO_ATTRIBUTES
:value: >
   'co_static_saml_attributes'

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_CO_ATTRIBUTES
```

````

````{py:attribute} KEY_CO_ATTRIBUTE_SCOPE
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_CO_ATTRIBUTE_SCOPE
:value: >
   'co_attribute_scope'

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_CO_ATTRIBUTE_SCOPE
```

````

````{py:attribute} KEY_CO_ENTITY_ID
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_CO_ENTITY_ID
:value: >
   'co_entity_id'

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_CO_ENTITY_ID
```

````

````{py:attribute} KEY_CO_NAME
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_CO_NAME
:value: >
   'co_name'

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_CO_NAME
```

````

````{py:attribute} KEY_ENCODEABLE_NAME
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_ENCODEABLE_NAME
:value: >
   'encodeable_name'

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_ENCODEABLE_NAME
```

````

````{py:attribute} KEY_ORGANIZATION
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_ORGANIZATION
:value: >
   'organization'

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_ORGANIZATION
```

````

````{py:attribute} KEY_ORGANIZATION_KEYS
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_ORGANIZATION_KEYS
:value: >
   ['display_name', 'name', 'url']

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend.KEY_ORGANIZATION_KEYS
```

````

````{py:method} _add_endpoints_to_config(config, co_name, backend_name)
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend._add_endpoints_to_config

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend._add_endpoints_to_config
```

````

````{py:method} _add_entity_id(config, co_name, backend_name)
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend._add_entity_id

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend._add_entity_id
```

````

````{py:method} _co_names_from_config()
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend._co_names_from_config

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend._co_names_from_config
```

````

````{py:method} _create_co_virtual_idp(context, co_name=None)
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend._create_co_virtual_idp

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend._create_co_virtual_idp
```

````

````{py:method} _create_state_data(context, resp_args, relay_state)
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend._create_state_data

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend._create_state_data
```

````

````{py:method} _get_co_config(context)
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend._get_co_config

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend._get_co_config
```

````

````{py:method} _get_co_name(context)
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend._get_co_name

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend._get_co_name
```

````

````{py:method} _get_co_name_from_path(context)
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend._get_co_name_from_path

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend._get_co_name_from_path
```

````

````{py:method} _handle_authn_response(context, internal_response)
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend._handle_authn_response

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend._handle_authn_response
```

````

````{py:method} _metadata_endpoint(context, co_name)
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend._metadata_endpoint

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend._metadata_endpoint
```

````

````{py:method} _overlay_for_saml_metadata(config, co_name)
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend._overlay_for_saml_metadata

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend._overlay_for_saml_metadata
```

````

````{py:method} _register_endpoints(backend_names)
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend._register_endpoints

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend._register_endpoints
```

````

````{py:method} handle_authn_request(context, binding_in)
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend.handle_authn_request

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend.handle_authn_request
```

````

````{py:method} handle_authn_response(context, internal_response)
:canonical: SATOSA.frontends.saml2.SAMLVirtualCoFrontend.handle_authn_response

```{autodoc2-docstring} SATOSA.frontends.saml2.SAMLVirtualCoFrontend.handle_authn_response
```

````

`````

````{py:data} logger
:canonical: SATOSA.frontends.saml2.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.frontends.saml2.logger
```

````

````{py:data} subject_type_map
:canonical: SATOSA.frontends.saml2.subject_type_map
:value: >
   None

```{autodoc2-docstring} SATOSA.frontends.saml2.subject_type_map
```

````

````{py:function} subject_type_to_saml_nameid_format(subject_type)
:canonical: SATOSA.frontends.saml2.subject_type_to_saml_nameid_format

```{autodoc2-docstring} SATOSA.frontends.saml2.subject_type_to_saml_nameid_format
```
````
