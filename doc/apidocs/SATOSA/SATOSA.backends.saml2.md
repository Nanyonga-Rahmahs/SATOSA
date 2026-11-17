# {py:mod}`SATOSA.backends.saml2`

```{py:module} SATOSA.backends.saml2
```

```{autodoc2-docstring} SATOSA.backends.saml2
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SAMLBackend <SATOSA.backends.saml2.SAMLBackend>`
  - ```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend
    :summary:
    ```
* - {py:obj}`SAMLEIDASBackend <SATOSA.backends.saml2.SAMLEIDASBackend>`
  - ```{autodoc2-docstring} SATOSA.backends.saml2.SAMLEIDASBackend
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_force_authn <SATOSA.backends.saml2.get_force_authn>`
  - ```{autodoc2-docstring} SATOSA.backends.saml2.get_force_authn
    :summary:
    ```
* - {py:obj}`get_memorized_idp <SATOSA.backends.saml2.get_memorized_idp>`
  - ```{autodoc2-docstring} SATOSA.backends.saml2.get_memorized_idp
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.backends.saml2.logger>`
  - ```{autodoc2-docstring} SATOSA.backends.saml2.logger
    :summary:
    ```
````

### API

`````{py:class} SAMLBackend(outgoing, internal_attributes, config, base_url, name)
:canonical: SATOSA.backends.saml2.SAMLBackend

Bases: {py:obj}`satosa.backends.base.BackendModule`, {py:obj}`satosa.base.SAMLBaseModule`

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.__init__
```

````{py:attribute} KEY_DISCO_SRV
:canonical: SATOSA.backends.saml2.SAMLBackend.KEY_DISCO_SRV
:value: >
   'disco_srv'

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.KEY_DISCO_SRV
```

````

````{py:attribute} KEY_IS_PASSIVE
:canonical: SATOSA.backends.saml2.SAMLBackend.KEY_IS_PASSIVE
:value: >
   'is_passive'

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.KEY_IS_PASSIVE
```

````

````{py:attribute} KEY_MEMORIZE_IDP
:canonical: SATOSA.backends.saml2.SAMLBackend.KEY_MEMORIZE_IDP
:value: >
   'memorize_idp'

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.KEY_MEMORIZE_IDP
```

````

````{py:attribute} KEY_MIRROR_FORCE_AUTHN
:canonical: SATOSA.backends.saml2.SAMLBackend.KEY_MIRROR_FORCE_AUTHN
:value: >
   'mirror_force_authn'

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.KEY_MIRROR_FORCE_AUTHN
```

````

````{py:attribute} KEY_SAML_DISCOVERY_SERVICE_POLICY
:canonical: SATOSA.backends.saml2.SAMLBackend.KEY_SAML_DISCOVERY_SERVICE_POLICY
:value: >
   'saml_discovery_service_policy'

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.KEY_SAML_DISCOVERY_SERVICE_POLICY
```

````

````{py:attribute} KEY_SAML_DISCOVERY_SERVICE_URL
:canonical: SATOSA.backends.saml2.SAMLBackend.KEY_SAML_DISCOVERY_SERVICE_URL
:value: >
   'saml_discovery_service_url'

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.KEY_SAML_DISCOVERY_SERVICE_URL
```

````

````{py:attribute} KEY_SEND_REQUESTER_ID
:canonical: SATOSA.backends.saml2.SAMLBackend.KEY_SEND_REQUESTER_ID
:value: >
   'send_requester_id'

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.KEY_SEND_REQUESTER_ID
```

````

````{py:attribute} KEY_SP_CONFIG
:canonical: SATOSA.backends.saml2.SAMLBackend.KEY_SP_CONFIG
:value: >
   'sp_config'

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.KEY_SP_CONFIG
```

````

````{py:attribute} KEY_USE_MEMORIZED_IDP_WHEN_FORCE_AUTHN
:canonical: SATOSA.backends.saml2.SAMLBackend.KEY_USE_MEMORIZED_IDP_WHEN_FORCE_AUTHN
:value: >
   'use_memorized_idp_when_force_authn'

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.KEY_USE_MEMORIZED_IDP_WHEN_FORCE_AUTHN
```

````

````{py:attribute} VALUE_ACR_COMPARISON_DEFAULT
:canonical: SATOSA.backends.saml2.SAMLBackend.VALUE_ACR_COMPARISON_DEFAULT
:value: >
   'exact'

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.VALUE_ACR_COMPARISON_DEFAULT
```

````

````{py:method} _get_acs(context)
:canonical: SATOSA.backends.saml2.SAMLBackend._get_acs

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend._get_acs
```

````

````{py:method} _metadata_endpoint(context)
:canonical: SATOSA.backends.saml2.SAMLBackend._metadata_endpoint

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend._metadata_endpoint
```

````

````{py:method} _prefer_matching_host(context)
:canonical: SATOSA.backends.saml2.SAMLBackend._prefer_matching_host

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend._prefer_matching_host
```

````

````{py:method} _reload_metadata(context)
:canonical: SATOSA.backends.saml2.SAMLBackend._reload_metadata

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend._reload_metadata
```

````

````{py:method} _translate_response(response, state)
:canonical: SATOSA.backends.saml2.SAMLBackend._translate_response

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend._translate_response
```

````

````{py:method} _use_first_acs(context)
:canonical: SATOSA.backends.saml2.SAMLBackend._use_first_acs

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend._use_first_acs
```

````

````{py:method} authn_request(context, entity_id)
:canonical: SATOSA.backends.saml2.SAMLBackend.authn_request

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.authn_request
```

````

````{py:method} authn_response(context, binding)
:canonical: SATOSA.backends.saml2.SAMLBackend.authn_response

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.authn_response
```

````

````{py:method} construct_requested_authn_context(entity_id, *, target_accr=None)
:canonical: SATOSA.backends.saml2.SAMLBackend.construct_requested_authn_context

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.construct_requested_authn_context
```

````

````{py:method} disco_query(context)
:canonical: SATOSA.backends.saml2.SAMLBackend.disco_query

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.disco_query
```

````

````{py:method} disco_response(context)
:canonical: SATOSA.backends.saml2.SAMLBackend.disco_response

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.disco_response
```

````

````{py:method} get_idp_entity_id(context)
:canonical: SATOSA.backends.saml2.SAMLBackend.get_idp_entity_id

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.get_idp_entity_id
```

````

````{py:method} get_metadata_desc()
:canonical: SATOSA.backends.saml2.SAMLBackend.get_metadata_desc

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.get_metadata_desc
```

````

````{py:method} register_endpoints()
:canonical: SATOSA.backends.saml2.SAMLBackend.register_endpoints

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.register_endpoints
```

````

````{py:method} start_auth(context, internal_req)
:canonical: SATOSA.backends.saml2.SAMLBackend.start_auth

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLBackend.start_auth
```

````

`````

`````{py:class} SAMLEIDASBackend(outgoing, internal_attributes, config, base_url, name)
:canonical: SATOSA.backends.saml2.SAMLEIDASBackend

Bases: {py:obj}`SATOSA.backends.saml2.SAMLBackend`, {py:obj}`satosa.base.SAMLEIDASBaseModule`

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLEIDASBackend
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLEIDASBackend.__init__
```

````{py:attribute} VALUE_ACR_CLASS_REF_DEFAULT
:canonical: SATOSA.backends.saml2.SAMLEIDASBackend.VALUE_ACR_CLASS_REF_DEFAULT
:value: >
   'http://eidas.europa.eu/LoA/high'

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLEIDASBackend.VALUE_ACR_CLASS_REF_DEFAULT
```

````

````{py:attribute} VALUE_ACR_COMPARISON_DEFAULT
:canonical: SATOSA.backends.saml2.SAMLEIDASBackend.VALUE_ACR_COMPARISON_DEFAULT
:value: >
   'minimum'

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLEIDASBackend.VALUE_ACR_COMPARISON_DEFAULT
```

````

````{py:method} init_config(config)
:canonical: SATOSA.backends.saml2.SAMLEIDASBackend.init_config

```{autodoc2-docstring} SATOSA.backends.saml2.SAMLEIDASBackend.init_config
```

````

`````

````{py:function} get_force_authn(context, config, sp_config)
:canonical: SATOSA.backends.saml2.get_force_authn

```{autodoc2-docstring} SATOSA.backends.saml2.get_force_authn
```
````

````{py:function} get_memorized_idp(context, config, force_authn)
:canonical: SATOSA.backends.saml2.get_memorized_idp

```{autodoc2-docstring} SATOSA.backends.saml2.get_memorized_idp
```
````

````{py:data} logger
:canonical: SATOSA.backends.saml2.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.backends.saml2.logger
```

````
