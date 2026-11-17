# {py:mod}`tests.satosa.test_plugin_loader`

```{py:module} tests.satosa.test_plugin_loader
```

```{autodoc2-docstring} tests.satosa.test_plugin_loader
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestFilters <tests.satosa.test_plugin_loader.TestFilters>`
  - ```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestFilters
    :summary:
    ```
* - {py:obj}`TestLoadPluginConfig <tests.satosa.test_plugin_loader.TestLoadPluginConfig>`
  - ```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestLoadPluginConfig
    :summary:
    ```
````

### API

`````{py:class} TestFilters
:canonical: tests.satosa.test_plugin_loader.TestFilters

Bases: {py:obj}`object`

```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestFilters
```

```{py:class} BackendTestPluginModule(auth_callback_func, internal_attributes, base_url, name)
:canonical: tests.satosa.test_plugin_loader.TestFilters.BackendTestPluginModule

Bases: {py:obj}`satosa.backends.base.BackendModule`

```

```{py:class} FrontendTestPluginModule(auth_req_callback_func, internal_attributes, base_url, name)
:canonical: tests.satosa.test_plugin_loader.TestFilters.FrontendTestPluginModule

Bases: {py:obj}`satosa.frontends.base.FrontendModule`

```

```{py:class} RequestTestMicroService(name, base_url, **kwargs)
:canonical: tests.satosa.test_plugin_loader.TestFilters.RequestTestMicroService

Bases: {py:obj}`satosa.micro_services.base.RequestMicroService`

```

```{py:class} ResponseTestMicroService(name, base_url, **kwargs)
:canonical: tests.satosa.test_plugin_loader.TestFilters.ResponseTestMicroService

Bases: {py:obj}`satosa.micro_services.base.ResponseMicroService`

```

````{py:method} test_backend_filter_accepts_backend_plugin()
:canonical: tests.satosa.test_plugin_loader.TestFilters.test_backend_filter_accepts_backend_plugin

```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestFilters.test_backend_filter_accepts_backend_plugin
```

````

````{py:method} test_backend_filter_rejects_base_class()
:canonical: tests.satosa.test_plugin_loader.TestFilters.test_backend_filter_rejects_base_class

```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestFilters.test_backend_filter_rejects_base_class
```

````

````{py:method} test_backend_filter_rejects_frontend_plugin()
:canonical: tests.satosa.test_plugin_loader.TestFilters.test_backend_filter_rejects_frontend_plugin

```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestFilters.test_backend_filter_rejects_frontend_plugin
```

````

````{py:method} test_frontend_filter_accepts_backend_plugin()
:canonical: tests.satosa.test_plugin_loader.TestFilters.test_frontend_filter_accepts_backend_plugin

```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestFilters.test_frontend_filter_accepts_backend_plugin
```

````

````{py:method} test_frontend_filter_rejects_backend_plugin()
:canonical: tests.satosa.test_plugin_loader.TestFilters.test_frontend_filter_rejects_backend_plugin

```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestFilters.test_frontend_filter_rejects_backend_plugin
```

````

````{py:method} test_frontend_filter_rejects_base_class()
:canonical: tests.satosa.test_plugin_loader.TestFilters.test_frontend_filter_rejects_base_class

```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestFilters.test_frontend_filter_rejects_base_class
```

````

````{py:method} test_request_micro_service_filter_accepts_request_micro_service()
:canonical: tests.satosa.test_plugin_loader.TestFilters.test_request_micro_service_filter_accepts_request_micro_service

```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestFilters.test_request_micro_service_filter_accepts_request_micro_service
```

````

````{py:method} test_request_micro_service_filter_rejects_base_class()
:canonical: tests.satosa.test_plugin_loader.TestFilters.test_request_micro_service_filter_rejects_base_class

```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestFilters.test_request_micro_service_filter_rejects_base_class
```

````

````{py:method} test_request_micro_service_filter_rejects_response_micro_service()
:canonical: tests.satosa.test_plugin_loader.TestFilters.test_request_micro_service_filter_rejects_response_micro_service

```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestFilters.test_request_micro_service_filter_rejects_response_micro_service
```

````

````{py:method} test_response_micro_service_filter_accepts_response_micro_service()
:canonical: tests.satosa.test_plugin_loader.TestFilters.test_response_micro_service_filter_accepts_response_micro_service

```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestFilters.test_response_micro_service_filter_accepts_response_micro_service
```

````

````{py:method} test_response_micro_service_filter_rejects_base_class()
:canonical: tests.satosa.test_plugin_loader.TestFilters.test_response_micro_service_filter_rejects_base_class

```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestFilters.test_response_micro_service_filter_rejects_base_class
```

````

````{py:method} test_response_micro_service_filter_rejects_request_micro_service()
:canonical: tests.satosa.test_plugin_loader.TestFilters.test_response_micro_service_filter_rejects_request_micro_service

```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestFilters.test_response_micro_service_filter_rejects_request_micro_service
```

````

`````

`````{py:class} TestLoadPluginConfig
:canonical: tests.satosa.test_plugin_loader.TestLoadPluginConfig

Bases: {py:obj}`object`

```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestLoadPluginConfig
```

````{py:method} test_can_load_yaml()
:canonical: tests.satosa.test_plugin_loader.TestLoadPluginConfig.test_can_load_yaml

```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestLoadPluginConfig.test_can_load_yaml
```

````

````{py:method} test_handles_malformed_data()
:canonical: tests.satosa.test_plugin_loader.TestLoadPluginConfig.test_handles_malformed_data

```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestLoadPluginConfig.test_handles_malformed_data
```

````

````{py:method} test_load_json()
:canonical: tests.satosa.test_plugin_loader.TestLoadPluginConfig.test_load_json

```{autodoc2-docstring} tests.satosa.test_plugin_loader.TestLoadPluginConfig.test_load_json
```

````

`````
