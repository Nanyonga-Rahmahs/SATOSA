# {py:mod}`SATOSA.plugin_loader`

```{py:module} SATOSA.plugin_loader
```

```{autodoc2-docstring} SATOSA.plugin_loader
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_load_endpoint_module <SATOSA.plugin_loader._load_endpoint_module>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader._load_endpoint_module
    :summary:
    ```
* - {py:obj}`_load_microservice <SATOSA.plugin_loader._load_microservice>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader._load_microservice
    :summary:
    ```
* - {py:obj}`_load_microservices <SATOSA.plugin_loader._load_microservices>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader._load_microservices
    :summary:
    ```
* - {py:obj}`_load_plugin_config <SATOSA.plugin_loader._load_plugin_config>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader._load_plugin_config
    :summary:
    ```
* - {py:obj}`_load_plugin_module <SATOSA.plugin_loader._load_plugin_module>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader._load_plugin_module
    :summary:
    ```
* - {py:obj}`_load_plugins <SATOSA.plugin_loader._load_plugins>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader._load_plugins
    :summary:
    ```
* - {py:obj}`_micro_service_filter <SATOSA.plugin_loader._micro_service_filter>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader._micro_service_filter
    :summary:
    ```
* - {py:obj}`_replace_variables_in_plugin_module_config <SATOSA.plugin_loader._replace_variables_in_plugin_module_config>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader._replace_variables_in_plugin_module_config
    :summary:
    ```
* - {py:obj}`_request_micro_service_filter <SATOSA.plugin_loader._request_micro_service_filter>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader._request_micro_service_filter
    :summary:
    ```
* - {py:obj}`_response_micro_service_filter <SATOSA.plugin_loader._response_micro_service_filter>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader._response_micro_service_filter
    :summary:
    ```
* - {py:obj}`backend_filter <SATOSA.plugin_loader.backend_filter>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader.backend_filter
    :summary:
    ```
* - {py:obj}`frontend_filter <SATOSA.plugin_loader.frontend_filter>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader.frontend_filter
    :summary:
    ```
* - {py:obj}`load_backends <SATOSA.plugin_loader.load_backends>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader.load_backends
    :summary:
    ```
* - {py:obj}`load_frontends <SATOSA.plugin_loader.load_frontends>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader.load_frontends
    :summary:
    ```
* - {py:obj}`load_request_microservices <SATOSA.plugin_loader.load_request_microservices>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader.load_request_microservices
    :summary:
    ```
* - {py:obj}`load_response_microservices <SATOSA.plugin_loader.load_response_microservices>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader.load_response_microservices
    :summary:
    ```
* - {py:obj}`prepend_to_import_path <SATOSA.plugin_loader.prepend_to_import_path>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader.prepend_to_import_path
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.plugin_loader.logger>`
  - ```{autodoc2-docstring} SATOSA.plugin_loader.logger
    :summary:
    ```
````

### API

````{py:function} _load_endpoint_module(plugin_config, plugin_filter)
:canonical: SATOSA.plugin_loader._load_endpoint_module

```{autodoc2-docstring} SATOSA.plugin_loader._load_endpoint_module
```
````

````{py:function} _load_microservice(plugin_config, plugin_filter)
:canonical: SATOSA.plugin_loader._load_microservice

```{autodoc2-docstring} SATOSA.plugin_loader._load_microservice
```
````

````{py:function} _load_microservices(plugin_paths, plugins, plugin_filter, internal_attributes, base_url)
:canonical: SATOSA.plugin_loader._load_microservices

```{autodoc2-docstring} SATOSA.plugin_loader._load_microservices
```
````

````{py:function} _load_plugin_config(config)
:canonical: SATOSA.plugin_loader._load_plugin_config

```{autodoc2-docstring} SATOSA.plugin_loader._load_plugin_config
```
````

````{py:function} _load_plugin_module(plugin_config, plugin_filter)
:canonical: SATOSA.plugin_loader._load_plugin_module

```{autodoc2-docstring} SATOSA.plugin_loader._load_plugin_module
```
````

````{py:function} _load_plugins(plugin_paths, plugins, plugin_filter, base_url, internal_attributes, callback)
:canonical: SATOSA.plugin_loader._load_plugins

```{autodoc2-docstring} SATOSA.plugin_loader._load_plugins
```
````

````{py:function} _micro_service_filter(cls)
:canonical: SATOSA.plugin_loader._micro_service_filter

```{autodoc2-docstring} SATOSA.plugin_loader._micro_service_filter
```
````

````{py:function} _replace_variables_in_plugin_module_config(module_config, base_url, name)
:canonical: SATOSA.plugin_loader._replace_variables_in_plugin_module_config

```{autodoc2-docstring} SATOSA.plugin_loader._replace_variables_in_plugin_module_config
```
````

````{py:function} _request_micro_service_filter(cls)
:canonical: SATOSA.plugin_loader._request_micro_service_filter

```{autodoc2-docstring} SATOSA.plugin_loader._request_micro_service_filter
```
````

````{py:function} _response_micro_service_filter(cls)
:canonical: SATOSA.plugin_loader._response_micro_service_filter

```{autodoc2-docstring} SATOSA.plugin_loader._response_micro_service_filter
```
````

````{py:function} backend_filter(cls)
:canonical: SATOSA.plugin_loader.backend_filter

```{autodoc2-docstring} SATOSA.plugin_loader.backend_filter
```
````

````{py:function} frontend_filter(cls)
:canonical: SATOSA.plugin_loader.frontend_filter

```{autodoc2-docstring} SATOSA.plugin_loader.frontend_filter
```
````

````{py:function} load_backends(config, callback, internal_attributes)
:canonical: SATOSA.plugin_loader.load_backends

```{autodoc2-docstring} SATOSA.plugin_loader.load_backends
```
````

````{py:function} load_frontends(config, callback, internal_attributes)
:canonical: SATOSA.plugin_loader.load_frontends

```{autodoc2-docstring} SATOSA.plugin_loader.load_frontends
```
````

````{py:function} load_request_microservices(plugin_path, plugins, internal_attributes, base_url)
:canonical: SATOSA.plugin_loader.load_request_microservices

```{autodoc2-docstring} SATOSA.plugin_loader.load_request_microservices
```
````

````{py:function} load_response_microservices(plugin_path, plugins, internal_attributes, base_url)
:canonical: SATOSA.plugin_loader.load_response_microservices

```{autodoc2-docstring} SATOSA.plugin_loader.load_response_microservices
```
````

````{py:data} logger
:canonical: SATOSA.plugin_loader.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.plugin_loader.logger
```

````

````{py:function} prepend_to_import_path(import_paths)
:canonical: SATOSA.plugin_loader.prepend_to_import_path

```{autodoc2-docstring} SATOSA.plugin_loader.prepend_to_import_path
```
````
