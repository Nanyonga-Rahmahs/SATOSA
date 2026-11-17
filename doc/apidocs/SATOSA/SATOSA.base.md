# {py:mod}`SATOSA.base`

```{py:module} SATOSA.base
```

```{autodoc2-docstring} SATOSA.base
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SAMLBaseModule <SATOSA.base.SAMLBaseModule>`
  - ```{autodoc2-docstring} SATOSA.base.SAMLBaseModule
    :summary:
    ```
* - {py:obj}`SAMLEIDASBaseModule <SATOSA.base.SAMLEIDASBaseModule>`
  - ```{autodoc2-docstring} SATOSA.base.SAMLEIDASBaseModule
    :summary:
    ```
* - {py:obj}`SATOSABase <SATOSA.base.SATOSABase>`
  - ```{autodoc2-docstring} SATOSA.base.SATOSABase
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`STATE_KEY <SATOSA.base.STATE_KEY>`
  - ```{autodoc2-docstring} SATOSA.base.STATE_KEY
    :summary:
    ```
* - {py:obj}`logger <SATOSA.base.logger>`
  - ```{autodoc2-docstring} SATOSA.base.logger
    :summary:
    ```
````

### API

`````{py:class} SAMLBaseModule
:canonical: SATOSA.base.SAMLBaseModule

Bases: {py:obj}`object`

```{autodoc2-docstring} SATOSA.base.SAMLBaseModule
```

````{py:attribute} KEY_ACR_MAPPING
:canonical: SATOSA.base.SAMLBaseModule.KEY_ACR_MAPPING
:value: >
   'acr_mapping'

```{autodoc2-docstring} SATOSA.base.SAMLBaseModule.KEY_ACR_MAPPING
```

````

````{py:attribute} KEY_ATTRIBUTE_PROFILE
:canonical: SATOSA.base.SAMLBaseModule.KEY_ATTRIBUTE_PROFILE
:value: >
   'attribute_profile'

```{autodoc2-docstring} SATOSA.base.SAMLBaseModule.KEY_ATTRIBUTE_PROFILE
```

````

````{py:attribute} KEY_ENABLE_METADATA_RELOAD
:canonical: SATOSA.base.SAMLBaseModule.KEY_ENABLE_METADATA_RELOAD
:value: >
   'enable_metadata_reload'

```{autodoc2-docstring} SATOSA.base.SAMLBaseModule.KEY_ENABLE_METADATA_RELOAD
```

````

````{py:attribute} KEY_ENTITYID_ENDPOINT
:canonical: SATOSA.base.SAMLBaseModule.KEY_ENTITYID_ENDPOINT
:value: >
   'entityid_endpoint'

```{autodoc2-docstring} SATOSA.base.SAMLBaseModule.KEY_ENTITYID_ENDPOINT
```

````

````{py:attribute} VALUE_ATTRIBUTE_PROFILE_DEFAULT
:canonical: SATOSA.base.SAMLBaseModule.VALUE_ATTRIBUTE_PROFILE_DEFAULT
:value: >
   'saml'

```{autodoc2-docstring} SATOSA.base.SAMLBaseModule.VALUE_ATTRIBUTE_PROFILE_DEFAULT
```

````

````{py:method} enable_metadata_reload()
:canonical: SATOSA.base.SAMLBaseModule.enable_metadata_reload

```{autodoc2-docstring} SATOSA.base.SAMLBaseModule.enable_metadata_reload
```

````

````{py:method} expose_entityid_endpoint()
:canonical: SATOSA.base.SAMLBaseModule.expose_entityid_endpoint

```{autodoc2-docstring} SATOSA.base.SAMLBaseModule.expose_entityid_endpoint
```

````

````{py:method} init_config(config)
:canonical: SATOSA.base.SAMLBaseModule.init_config

```{autodoc2-docstring} SATOSA.base.SAMLBaseModule.init_config
```

````

`````

`````{py:class} SAMLEIDASBaseModule
:canonical: SATOSA.base.SAMLEIDASBaseModule

Bases: {py:obj}`SATOSA.base.SAMLBaseModule`

```{autodoc2-docstring} SATOSA.base.SAMLEIDASBaseModule
```

````{py:attribute} VALUE_ATTRIBUTE_PROFILE_DEFAULT
:canonical: SATOSA.base.SAMLEIDASBaseModule.VALUE_ATTRIBUTE_PROFILE_DEFAULT
:value: >
   'eidas'

```{autodoc2-docstring} SATOSA.base.SAMLEIDASBaseModule.VALUE_ATTRIBUTE_PROFILE_DEFAULT
```

````

````{py:method} init_config(config)
:canonical: SATOSA.base.SAMLEIDASBaseModule.init_config

```{autodoc2-docstring} SATOSA.base.SAMLEIDASBaseModule.init_config
```

````

`````

`````{py:class} SATOSABase(config)
:canonical: SATOSA.base.SATOSABase

Bases: {py:obj}`object`

```{autodoc2-docstring} SATOSA.base.SATOSABase
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.base.SATOSABase.__init__
```

````{py:method} _auth_req_callback_func(context, internal_request)
:canonical: SATOSA.base.SATOSABase._auth_req_callback_func

```{autodoc2-docstring} SATOSA.base.SATOSABase._auth_req_callback_func
```

````

````{py:method} _auth_req_finish(context, internal_request)
:canonical: SATOSA.base.SATOSABase._auth_req_finish

```{autodoc2-docstring} SATOSA.base.SATOSABase._auth_req_finish
```

````

````{py:method} _auth_resp_callback_func(context, internal_response)
:canonical: SATOSA.base.SATOSABase._auth_resp_callback_func

```{autodoc2-docstring} SATOSA.base.SATOSABase._auth_resp_callback_func
```

````

````{py:method} _auth_resp_finish(context, internal_response)
:canonical: SATOSA.base.SATOSABase._auth_resp_finish

```{autodoc2-docstring} SATOSA.base.SATOSABase._auth_resp_finish
```

````

````{py:method} _handle_satosa_authentication_error(error)
:canonical: SATOSA.base.SATOSABase._handle_satosa_authentication_error

```{autodoc2-docstring} SATOSA.base.SATOSABase._handle_satosa_authentication_error
```

````

````{py:method} _link_micro_services(micro_services, finisher)
:canonical: SATOSA.base.SATOSABase._link_micro_services

```{autodoc2-docstring} SATOSA.base.SATOSABase._link_micro_services
```

````

````{py:method} _load_state(context)
:canonical: SATOSA.base.SATOSABase._load_state

```{autodoc2-docstring} SATOSA.base.SATOSABase._load_state
```

````

````{py:method} _run_bound_endpoint(context, spec)
:canonical: SATOSA.base.SATOSABase._run_bound_endpoint

```{autodoc2-docstring} SATOSA.base.SATOSABase._run_bound_endpoint
```

````

````{py:method} _save_state(resp, context)
:canonical: SATOSA.base.SATOSABase._save_state

```{autodoc2-docstring} SATOSA.base.SATOSABase._save_state
```

````

````{py:method} run(context)
:canonical: SATOSA.base.SATOSABase.run

```{autodoc2-docstring} SATOSA.base.SATOSABase.run
```

````

`````

````{py:data} STATE_KEY
:canonical: SATOSA.base.STATE_KEY
:value: >
   'SATOSA_BASE'

```{autodoc2-docstring} SATOSA.base.STATE_KEY
```

````

````{py:data} logger
:canonical: SATOSA.base.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.base.logger
```

````
