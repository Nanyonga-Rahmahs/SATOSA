# {py:mod}`SATOSA.routing`

```{py:module} SATOSA.routing
```

```{autodoc2-docstring} SATOSA.routing
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ModuleRouter <SATOSA.routing.ModuleRouter>`
  - ```{autodoc2-docstring} SATOSA.routing.ModuleRouter
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`STATE_KEY <SATOSA.routing.STATE_KEY>`
  - ```{autodoc2-docstring} SATOSA.routing.STATE_KEY
    :summary:
    ```
* - {py:obj}`logger <SATOSA.routing.logger>`
  - ```{autodoc2-docstring} SATOSA.routing.logger
    :summary:
    ```
````

### API

`````{py:class} ModuleRouter(frontends, backends, micro_services)
:canonical: SATOSA.routing.ModuleRouter

Bases: {py:obj}`object`

```{autodoc2-docstring} SATOSA.routing.ModuleRouter
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.routing.ModuleRouter.__init__
```

````{py:method} _find_registered_backend_endpoint(context)
:canonical: SATOSA.routing.ModuleRouter._find_registered_backend_endpoint

```{autodoc2-docstring} SATOSA.routing.ModuleRouter._find_registered_backend_endpoint
```

````

````{py:method} _find_registered_endpoint(context, modules)
:canonical: SATOSA.routing.ModuleRouter._find_registered_endpoint

```{autodoc2-docstring} SATOSA.routing.ModuleRouter._find_registered_endpoint
```

````

````{py:method} _find_registered_endpoint_for_module(module, context)
:canonical: SATOSA.routing.ModuleRouter._find_registered_endpoint_for_module

```{autodoc2-docstring} SATOSA.routing.ModuleRouter._find_registered_endpoint_for_module
```

````

````{py:method} backend_routing(context)
:canonical: SATOSA.routing.ModuleRouter.backend_routing

```{autodoc2-docstring} SATOSA.routing.ModuleRouter.backend_routing
```

````

````{py:method} endpoint_routing(context)
:canonical: SATOSA.routing.ModuleRouter.endpoint_routing

```{autodoc2-docstring} SATOSA.routing.ModuleRouter.endpoint_routing
```

````

````{py:method} frontend_routing(context)
:canonical: SATOSA.routing.ModuleRouter.frontend_routing

```{autodoc2-docstring} SATOSA.routing.ModuleRouter.frontend_routing
```

````

`````

````{py:data} STATE_KEY
:canonical: SATOSA.routing.STATE_KEY
:value: >
   'ROUTER'

```{autodoc2-docstring} SATOSA.routing.STATE_KEY
```

````

````{py:data} logger
:canonical: SATOSA.routing.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.routing.logger
```

````
