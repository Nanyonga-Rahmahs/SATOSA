# {py:mod}`tests.satosa.test_routing`

```{py:module} tests.satosa.test_routing
```

```{autodoc2-docstring} tests.satosa.test_routing
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestModuleRouter <tests.satosa.test_routing.TestModuleRouter>`
  - ```{autodoc2-docstring} tests.satosa.test_routing.TestModuleRouter
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BACKEND_NAMES <tests.satosa.test_routing.BACKEND_NAMES>`
  - ```{autodoc2-docstring} tests.satosa.test_routing.BACKEND_NAMES
    :summary:
    ```
* - {py:obj}`FRONTEND_NAMES <tests.satosa.test_routing.FRONTEND_NAMES>`
  - ```{autodoc2-docstring} tests.satosa.test_routing.FRONTEND_NAMES
    :summary:
    ```
````

### API

````{py:data} BACKEND_NAMES
:canonical: tests.satosa.test_routing.BACKEND_NAMES
:value: >
   ['Saml2SP', 'VOPaaSSaml2SP']

```{autodoc2-docstring} tests.satosa.test_routing.BACKEND_NAMES
```

````

````{py:data} FRONTEND_NAMES
:canonical: tests.satosa.test_routing.FRONTEND_NAMES
:value: >
   ['Saml2IDP', 'VOPaaSSaml2IDP']

```{autodoc2-docstring} tests.satosa.test_routing.FRONTEND_NAMES
```

````

`````{py:class} TestModuleRouter
:canonical: tests.satosa.test_routing.TestModuleRouter

```{autodoc2-docstring} tests.satosa.test_routing.TestModuleRouter
```

````{py:method} create_router()
:canonical: tests.satosa.test_routing.TestModuleRouter.create_router

```{autodoc2-docstring} tests.satosa.test_routing.TestModuleRouter.create_router
```

````

````{py:method} test_bad_init(frontends, backends, micro_services)
:canonical: tests.satosa.test_routing.TestModuleRouter.test_bad_init

```{autodoc2-docstring} tests.satosa.test_routing.TestModuleRouter.test_bad_init
```

````

````{py:method} test_endpoint_routing_to_backend(url_path, expected_backend)
:canonical: tests.satosa.test_routing.TestModuleRouter.test_endpoint_routing_to_backend

```{autodoc2-docstring} tests.satosa.test_routing.TestModuleRouter.test_endpoint_routing_to_backend
```

````

````{py:method} test_endpoint_routing_to_frontend(url_path, expected_frontend, expected_backend)
:canonical: tests.satosa.test_routing.TestModuleRouter.test_endpoint_routing_to_frontend

```{autodoc2-docstring} tests.satosa.test_routing.TestModuleRouter.test_endpoint_routing_to_frontend
```

````

````{py:method} test_endpoint_routing_to_microservice(url_path, expected_micro_service)
:canonical: tests.satosa.test_routing.TestModuleRouter.test_endpoint_routing_to_microservice

```{autodoc2-docstring} tests.satosa.test_routing.TestModuleRouter.test_endpoint_routing_to_microservice
```

````

````{py:method} test_endpoint_routing_with_unknown_endpoint(context)
:canonical: tests.satosa.test_routing.TestModuleRouter.test_endpoint_routing_with_unknown_endpoint

```{autodoc2-docstring} tests.satosa.test_routing.TestModuleRouter.test_endpoint_routing_with_unknown_endpoint
```

````

````{py:method} test_module_routing(url_path, expected_frontend, expected_backend, context)
:canonical: tests.satosa.test_routing.TestModuleRouter.test_module_routing

```{autodoc2-docstring} tests.satosa.test_routing.TestModuleRouter.test_module_routing
```

````

`````
