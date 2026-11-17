# {py:mod}`tests.conftest`

```{py:module} tests.conftest
```

```{autodoc2-docstring} tests.conftest
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`account_linking_module_config <tests.conftest.account_linking_module_config>`
  - ```{autodoc2-docstring} tests.conftest.account_linking_module_config
    :summary:
    ```
* - {py:obj}`backend_plugin_config <tests.conftest.backend_plugin_config>`
  - ```{autodoc2-docstring} tests.conftest.backend_plugin_config
    :summary:
    ```
* - {py:obj}`cert_and_key <tests.conftest.cert_and_key>`
  - ```{autodoc2-docstring} tests.conftest.cert_and_key
    :summary:
    ```
* - {py:obj}`consent_module_config <tests.conftest.consent_module_config>`
  - ```{autodoc2-docstring} tests.conftest.consent_module_config
    :summary:
    ```
* - {py:obj}`context <tests.conftest.context>`
  - ```{autodoc2-docstring} tests.conftest.context
    :summary:
    ```
* - {py:obj}`frontend_plugin_config <tests.conftest.frontend_plugin_config>`
  - ```{autodoc2-docstring} tests.conftest.frontend_plugin_config
    :summary:
    ```
* - {py:obj}`idp_conf <tests.conftest.idp_conf>`
  - ```{autodoc2-docstring} tests.conftest.idp_conf
    :summary:
    ```
* - {py:obj}`oidc_backend_config <tests.conftest.oidc_backend_config>`
  - ```{autodoc2-docstring} tests.conftest.oidc_backend_config
    :summary:
    ```
* - {py:obj}`request_microservice_config <tests.conftest.request_microservice_config>`
  - ```{autodoc2-docstring} tests.conftest.request_microservice_config
    :summary:
    ```
* - {py:obj}`response_microservice_config <tests.conftest.response_microservice_config>`
  - ```{autodoc2-docstring} tests.conftest.response_microservice_config
    :summary:
    ```
* - {py:obj}`saml_backend_config <tests.conftest.saml_backend_config>`
  - ```{autodoc2-docstring} tests.conftest.saml_backend_config
    :summary:
    ```
* - {py:obj}`saml_frontend_config <tests.conftest.saml_frontend_config>`
  - ```{autodoc2-docstring} tests.conftest.saml_frontend_config
    :summary:
    ```
* - {py:obj}`saml_mirror_frontend_config <tests.conftest.saml_mirror_frontend_config>`
  - ```{autodoc2-docstring} tests.conftest.saml_mirror_frontend_config
    :summary:
    ```
* - {py:obj}`satosa_config_dict <tests.conftest.satosa_config_dict>`
  - ```{autodoc2-docstring} tests.conftest.satosa_config_dict
    :summary:
    ```
* - {py:obj}`signing_key_path <tests.conftest.signing_key_path>`
  - ```{autodoc2-docstring} tests.conftest.signing_key_path
    :summary:
    ```
* - {py:obj}`sp_conf <tests.conftest.sp_conf>`
  - ```{autodoc2-docstring} tests.conftest.sp_conf
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BASE_URL <tests.conftest.BASE_URL>`
  - ```{autodoc2-docstring} tests.conftest.BASE_URL
    :summary:
    ```
````

### API

````{py:data} BASE_URL
:canonical: tests.conftest.BASE_URL
:value: >
   'https://test-proxy.com'

```{autodoc2-docstring} tests.conftest.BASE_URL
```

````

````{py:function} account_linking_module_config(signing_key_path)
:canonical: tests.conftest.account_linking_module_config

```{autodoc2-docstring} tests.conftest.account_linking_module_config
```
````

````{py:function} backend_plugin_config()
:canonical: tests.conftest.backend_plugin_config

```{autodoc2-docstring} tests.conftest.backend_plugin_config
```
````

````{py:function} cert_and_key(tmpdir)
:canonical: tests.conftest.cert_and_key

```{autodoc2-docstring} tests.conftest.cert_and_key
```
````

````{py:function} consent_module_config(signing_key_path)
:canonical: tests.conftest.consent_module_config

```{autodoc2-docstring} tests.conftest.consent_module_config
```
````

````{py:function} context()
:canonical: tests.conftest.context

```{autodoc2-docstring} tests.conftest.context
```
````

````{py:function} frontend_plugin_config()
:canonical: tests.conftest.frontend_plugin_config

```{autodoc2-docstring} tests.conftest.frontend_plugin_config
```
````

````{py:function} idp_conf(cert_and_key)
:canonical: tests.conftest.idp_conf

```{autodoc2-docstring} tests.conftest.idp_conf
```
````

````{py:function} oidc_backend_config()
:canonical: tests.conftest.oidc_backend_config

```{autodoc2-docstring} tests.conftest.oidc_backend_config
```
````

````{py:function} request_microservice_config()
:canonical: tests.conftest.request_microservice_config

```{autodoc2-docstring} tests.conftest.request_microservice_config
```
````

````{py:function} response_microservice_config()
:canonical: tests.conftest.response_microservice_config

```{autodoc2-docstring} tests.conftest.response_microservice_config
```
````

````{py:function} saml_backend_config(idp_conf)
:canonical: tests.conftest.saml_backend_config

```{autodoc2-docstring} tests.conftest.saml_backend_config
```
````

````{py:function} saml_frontend_config(cert_and_key, sp_conf)
:canonical: tests.conftest.saml_frontend_config

```{autodoc2-docstring} tests.conftest.saml_frontend_config
```
````

````{py:function} saml_mirror_frontend_config(saml_frontend_config)
:canonical: tests.conftest.saml_mirror_frontend_config

```{autodoc2-docstring} tests.conftest.saml_mirror_frontend_config
```
````

````{py:function} satosa_config_dict(backend_plugin_config, frontend_plugin_config, request_microservice_config, response_microservice_config)
:canonical: tests.conftest.satosa_config_dict

```{autodoc2-docstring} tests.conftest.satosa_config_dict
```
````

````{py:function} signing_key_path(tmpdir_factory)
:canonical: tests.conftest.signing_key_path

```{autodoc2-docstring} tests.conftest.signing_key_path
```
````

````{py:function} sp_conf(cert_and_key)
:canonical: tests.conftest.sp_conf

```{autodoc2-docstring} tests.conftest.sp_conf
```
````
