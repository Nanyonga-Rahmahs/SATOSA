# {py:mod}`SATOSA.frontends.openid_connect`

```{py:module} SATOSA.frontends.openid_connect
```

```{autodoc2-docstring} SATOSA.frontends.openid_connect
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MirrorPublicSubjectIdentifierFactory <SATOSA.frontends.openid_connect.MirrorPublicSubjectIdentifierFactory>`
  -
* - {py:obj}`OpenIDConnectFrontend <SATOSA.frontends.openid_connect.OpenIDConnectFrontend>`
  - ```{autodoc2-docstring} SATOSA.frontends.openid_connect.OpenIDConnectFrontend
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_create_provider <SATOSA.frontends.openid_connect._create_provider>`
  - ```{autodoc2-docstring} SATOSA.frontends.openid_connect._create_provider
    :summary:
    ```
* - {py:obj}`_init_authorization_state <SATOSA.frontends.openid_connect._init_authorization_state>`
  - ```{autodoc2-docstring} SATOSA.frontends.openid_connect._init_authorization_state
    :summary:
    ```
* - {py:obj}`_validate_config <SATOSA.frontends.openid_connect._validate_config>`
  - ```{autodoc2-docstring} SATOSA.frontends.openid_connect._validate_config
    :summary:
    ```
* - {py:obj}`combine_claim_values <SATOSA.frontends.openid_connect.combine_claim_values>`
  - ```{autodoc2-docstring} SATOSA.frontends.openid_connect.combine_claim_values
    :summary:
    ```
* - {py:obj}`combine_join_by_space <SATOSA.frontends.openid_connect.combine_join_by_space>`
  - ```{autodoc2-docstring} SATOSA.frontends.openid_connect.combine_join_by_space
    :summary:
    ```
* - {py:obj}`combine_return_input <SATOSA.frontends.openid_connect.combine_return_input>`
  - ```{autodoc2-docstring} SATOSA.frontends.openid_connect.combine_return_input
    :summary:
    ```
* - {py:obj}`combine_select_first_value <SATOSA.frontends.openid_connect.combine_select_first_value>`
  - ```{autodoc2-docstring} SATOSA.frontends.openid_connect.combine_select_first_value
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`combine_values_by_claim <SATOSA.frontends.openid_connect.combine_values_by_claim>`
  - ```{autodoc2-docstring} SATOSA.frontends.openid_connect.combine_values_by_claim
    :summary:
    ```
* - {py:obj}`logger <SATOSA.frontends.openid_connect.logger>`
  - ```{autodoc2-docstring} SATOSA.frontends.openid_connect.logger
    :summary:
    ```
````

### API

`````{py:class} MirrorPublicSubjectIdentifierFactory(hash_salt: str)
:canonical: SATOSA.frontends.openid_connect.MirrorPublicSubjectIdentifierFactory

Bases: {py:obj}`pyop.subject_identifier.HashBasedSubjectIdentifierFactory`

````{py:method} create_public_identifier(user_id)
:canonical: SATOSA.frontends.openid_connect.MirrorPublicSubjectIdentifierFactory.create_public_identifier

```{autodoc2-docstring} SATOSA.frontends.openid_connect.MirrorPublicSubjectIdentifierFactory.create_public_identifier
```

````

`````

`````{py:class} OpenIDConnectFrontend(auth_req_callback_func, internal_attributes, conf, base_url, name)
:canonical: SATOSA.frontends.openid_connect.OpenIDConnectFrontend

Bases: {py:obj}`SATOSA.frontends.base.FrontendModule`

```{autodoc2-docstring} SATOSA.frontends.openid_connect.OpenIDConnectFrontend
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.frontends.openid_connect.OpenIDConnectFrontend.__init__
```

````{py:method} _get_approved_attributes(provider_supported_claims, authn_req)
:canonical: SATOSA.frontends.openid_connect.OpenIDConnectFrontend._get_approved_attributes

```{autodoc2-docstring} SATOSA.frontends.openid_connect.OpenIDConnectFrontend._get_approved_attributes
```

````

````{py:method} _get_authn_request_from_state(state)
:canonical: SATOSA.frontends.openid_connect.OpenIDConnectFrontend._get_authn_request_from_state

```{autodoc2-docstring} SATOSA.frontends.openid_connect.OpenIDConnectFrontend._get_authn_request_from_state
```

````

````{py:method} _get_extra_id_token_claims(user_id, client_id)
:canonical: SATOSA.frontends.openid_connect.OpenIDConnectFrontend._get_extra_id_token_claims

```{autodoc2-docstring} SATOSA.frontends.openid_connect.OpenIDConnectFrontend._get_extra_id_token_claims
```

````

````{py:method} _handle_authn_request(context)
:canonical: SATOSA.frontends.openid_connect.OpenIDConnectFrontend._handle_authn_request

```{autodoc2-docstring} SATOSA.frontends.openid_connect.OpenIDConnectFrontend._handle_authn_request
```

````

````{py:method} client_registration(context)
:canonical: SATOSA.frontends.openid_connect.OpenIDConnectFrontend.client_registration

```{autodoc2-docstring} SATOSA.frontends.openid_connect.OpenIDConnectFrontend.client_registration
```

````

````{py:method} handle_authn_request(context)
:canonical: SATOSA.frontends.openid_connect.OpenIDConnectFrontend.handle_authn_request

```{autodoc2-docstring} SATOSA.frontends.openid_connect.OpenIDConnectFrontend.handle_authn_request
```

````

````{py:method} handle_authn_response(context, internal_resp)
:canonical: SATOSA.frontends.openid_connect.OpenIDConnectFrontend.handle_authn_response

```{autodoc2-docstring} SATOSA.frontends.openid_connect.OpenIDConnectFrontend.handle_authn_response
```

````

````{py:method} handle_backend_error(exception)
:canonical: SATOSA.frontends.openid_connect.OpenIDConnectFrontend.handle_backend_error

```{autodoc2-docstring} SATOSA.frontends.openid_connect.OpenIDConnectFrontend.handle_backend_error
```

````

````{py:method} jwks(context)
:canonical: SATOSA.frontends.openid_connect.OpenIDConnectFrontend.jwks

```{autodoc2-docstring} SATOSA.frontends.openid_connect.OpenIDConnectFrontend.jwks
```

````

````{py:method} provider_config(context)
:canonical: SATOSA.frontends.openid_connect.OpenIDConnectFrontend.provider_config

```{autodoc2-docstring} SATOSA.frontends.openid_connect.OpenIDConnectFrontend.provider_config
```

````

````{py:method} register_endpoints(backend_names)
:canonical: SATOSA.frontends.openid_connect.OpenIDConnectFrontend.register_endpoints

```{autodoc2-docstring} SATOSA.frontends.openid_connect.OpenIDConnectFrontend.register_endpoints
```

````

````{py:method} token_endpoint(context)
:canonical: SATOSA.frontends.openid_connect.OpenIDConnectFrontend.token_endpoint

```{autodoc2-docstring} SATOSA.frontends.openid_connect.OpenIDConnectFrontend.token_endpoint
```

````

````{py:method} userinfo_endpoint(context)
:canonical: SATOSA.frontends.openid_connect.OpenIDConnectFrontend.userinfo_endpoint

```{autodoc2-docstring} SATOSA.frontends.openid_connect.OpenIDConnectFrontend.userinfo_endpoint
```

````

`````

````{py:function} _create_provider(provider_config, endpoint_baseurl, internal_attributes, signing_key, authz_state, user_db, cdb)
:canonical: SATOSA.frontends.openid_connect._create_provider

```{autodoc2-docstring} SATOSA.frontends.openid_connect._create_provider
```
````

````{py:function} _init_authorization_state(provider_config, db_uri, sub_hash_salt, mirror_public=False)
:canonical: SATOSA.frontends.openid_connect._init_authorization_state

```{autodoc2-docstring} SATOSA.frontends.openid_connect._init_authorization_state
```
````

````{py:function} _validate_config(config)
:canonical: SATOSA.frontends.openid_connect._validate_config

```{autodoc2-docstring} SATOSA.frontends.openid_connect._validate_config
```
````

````{py:function} combine_claim_values(claim_items)
:canonical: SATOSA.frontends.openid_connect.combine_claim_values

```{autodoc2-docstring} SATOSA.frontends.openid_connect.combine_claim_values
```
````

````{py:function} combine_join_by_space(values)
:canonical: SATOSA.frontends.openid_connect.combine_join_by_space

```{autodoc2-docstring} SATOSA.frontends.openid_connect.combine_join_by_space
```
````

````{py:function} combine_return_input(values)
:canonical: SATOSA.frontends.openid_connect.combine_return_input

```{autodoc2-docstring} SATOSA.frontends.openid_connect.combine_return_input
```
````

````{py:function} combine_select_first_value(values)
:canonical: SATOSA.frontends.openid_connect.combine_select_first_value

```{autodoc2-docstring} SATOSA.frontends.openid_connect.combine_select_first_value
```
````

````{py:data} combine_values_by_claim
:canonical: SATOSA.frontends.openid_connect.combine_values_by_claim
:value: >
   'defaultdict(...)'

```{autodoc2-docstring} SATOSA.frontends.openid_connect.combine_values_by_claim
```

````

````{py:data} logger
:canonical: SATOSA.frontends.openid_connect.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.frontends.openid_connect.logger
```

````
