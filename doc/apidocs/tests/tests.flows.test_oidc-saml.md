# {py:mod}`tests.flows.test_oidc-saml`

```{py:module} tests.flows.test_oidc-saml
```

```{autodoc2-docstring} tests.flows.test_oidc-saml
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestOIDCToSAML <tests.flows.test_oidc-saml.TestOIDCToSAML>`
  - ```{autodoc2-docstring} tests.flows.test_oidc-saml.TestOIDCToSAML
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`client_db_path <tests.flows.test_oidc-saml.client_db_path>`
  - ```{autodoc2-docstring} tests.flows.test_oidc-saml.client_db_path
    :summary:
    ```
* - {py:obj}`oidc_frontend_config <tests.flows.test_oidc-saml.oidc_frontend_config>`
  - ```{autodoc2-docstring} tests.flows.test_oidc-saml.oidc_frontend_config
    :summary:
    ```
* - {py:obj}`oidc_stateless_frontend_config <tests.flows.test_oidc-saml.oidc_stateless_frontend_config>`
  - ```{autodoc2-docstring} tests.flows.test_oidc-saml.oidc_stateless_frontend_config
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CLIENT_ID <tests.flows.test_oidc-saml.CLIENT_ID>`
  - ```{autodoc2-docstring} tests.flows.test_oidc-saml.CLIENT_ID
    :summary:
    ```
* - {py:obj}`CLIENT_REDIRECT_URI <tests.flows.test_oidc-saml.CLIENT_REDIRECT_URI>`
  - ```{autodoc2-docstring} tests.flows.test_oidc-saml.CLIENT_REDIRECT_URI
    :summary:
    ```
* - {py:obj}`CLIENT_SECRET <tests.flows.test_oidc-saml.CLIENT_SECRET>`
  - ```{autodoc2-docstring} tests.flows.test_oidc-saml.CLIENT_SECRET
    :summary:
    ```
* - {py:obj}`DB_URI <tests.flows.test_oidc-saml.DB_URI>`
  - ```{autodoc2-docstring} tests.flows.test_oidc-saml.DB_URI
    :summary:
    ```
* - {py:obj}`REDIRECT_URI <tests.flows.test_oidc-saml.REDIRECT_URI>`
  - ```{autodoc2-docstring} tests.flows.test_oidc-saml.REDIRECT_URI
    :summary:
    ```
````

### API

````{py:data} CLIENT_ID
:canonical: tests.flows.test_oidc-saml.CLIENT_ID
:value: >
   'client1'

```{autodoc2-docstring} tests.flows.test_oidc-saml.CLIENT_ID
```

````

````{py:data} CLIENT_REDIRECT_URI
:canonical: tests.flows.test_oidc-saml.CLIENT_REDIRECT_URI
:value: >
   'https://client.example.com/cb'

```{autodoc2-docstring} tests.flows.test_oidc-saml.CLIENT_REDIRECT_URI
```

````

````{py:data} CLIENT_SECRET
:canonical: tests.flows.test_oidc-saml.CLIENT_SECRET
:value: >
   'secret'

```{autodoc2-docstring} tests.flows.test_oidc-saml.CLIENT_SECRET
```

````

````{py:data} DB_URI
:canonical: tests.flows.test_oidc-saml.DB_URI
:value: >
   'mongodb://localhost/satosa'

```{autodoc2-docstring} tests.flows.test_oidc-saml.DB_URI
```

````

````{py:data} REDIRECT_URI
:canonical: tests.flows.test_oidc-saml.REDIRECT_URI
:value: >
   'https://client.example.com/cb'

```{autodoc2-docstring} tests.flows.test_oidc-saml.REDIRECT_URI
```

````

`````{py:class} TestOIDCToSAML
:canonical: tests.flows.test_oidc-saml.TestOIDCToSAML

```{autodoc2-docstring} tests.flows.test_oidc-saml.TestOIDCToSAML
```

````{py:method} _client_setup()
:canonical: tests.flows.test_oidc-saml.TestOIDCToSAML._client_setup

```{autodoc2-docstring} tests.flows.test_oidc-saml.TestOIDCToSAML._client_setup
```

````

````{py:method} test_full_flow(satosa_config_dict, oidc_frontend_config, saml_backend_config, idp_conf)
:canonical: tests.flows.test_oidc-saml.TestOIDCToSAML.test_full_flow

```{autodoc2-docstring} tests.flows.test_oidc-saml.TestOIDCToSAML.test_full_flow
```

````

````{py:method} test_full_stateless_code_flow(satosa_config_dict, oidc_stateless_frontend_config, saml_backend_config, idp_conf)
:canonical: tests.flows.test_oidc-saml.TestOIDCToSAML.test_full_stateless_code_flow

```{autodoc2-docstring} tests.flows.test_oidc-saml.TestOIDCToSAML.test_full_stateless_code_flow
```

````

````{py:method} test_full_stateless_id_token_flow(satosa_config_dict, oidc_stateless_frontend_config, saml_backend_config, idp_conf)
:canonical: tests.flows.test_oidc-saml.TestOIDCToSAML.test_full_stateless_id_token_flow

```{autodoc2-docstring} tests.flows.test_oidc-saml.TestOIDCToSAML.test_full_stateless_id_token_flow
```

````

`````

````{py:function} client_db_path(tmpdir_factory)
:canonical: tests.flows.test_oidc-saml.client_db_path

```{autodoc2-docstring} tests.flows.test_oidc-saml.client_db_path
```
````

````{py:function} oidc_frontend_config(signing_key_path)
:canonical: tests.flows.test_oidc-saml.oidc_frontend_config

```{autodoc2-docstring} tests.flows.test_oidc-saml.oidc_frontend_config
```
````

````{py:function} oidc_stateless_frontend_config(signing_key_path, client_db_path)
:canonical: tests.flows.test_oidc-saml.oidc_stateless_frontend_config

```{autodoc2-docstring} tests.flows.test_oidc-saml.oidc_stateless_frontend_config
```
````
