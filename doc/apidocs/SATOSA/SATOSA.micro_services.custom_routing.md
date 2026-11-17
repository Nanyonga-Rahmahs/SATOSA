# {py:mod}`SATOSA.micro_services.custom_routing`

```{py:module} SATOSA.micro_services.custom_routing
```

```{autodoc2-docstring} SATOSA.micro_services.custom_routing
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DecideBackendByRequester <SATOSA.micro_services.custom_routing.DecideBackendByRequester>`
  - ```{autodoc2-docstring} SATOSA.micro_services.custom_routing.DecideBackendByRequester
    :summary:
    ```
* - {py:obj}`DecideBackendByTargetIssuer <SATOSA.micro_services.custom_routing.DecideBackendByTargetIssuer>`
  - ```{autodoc2-docstring} SATOSA.micro_services.custom_routing.DecideBackendByTargetIssuer
    :summary:
    ```
* - {py:obj}`DecideIfRequesterIsAllowed <SATOSA.micro_services.custom_routing.DecideIfRequesterIsAllowed>`
  - ```{autodoc2-docstring} SATOSA.micro_services.custom_routing.DecideIfRequesterIsAllowed
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.micro_services.custom_routing.logger>`
  - ```{autodoc2-docstring} SATOSA.micro_services.custom_routing.logger
    :summary:
    ```
````

### API

````{py:exception} CustomRoutingError()
:canonical: SATOSA.micro_services.custom_routing.CustomRoutingError

Bases: {py:obj}`SATOSA.exception.SATOSAError`

```{autodoc2-docstring} SATOSA.micro_services.custom_routing.CustomRoutingError
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.custom_routing.CustomRoutingError.__init__
```

````

`````{py:class} DecideBackendByRequester(config, *args, **kwargs)
:canonical: SATOSA.micro_services.custom_routing.DecideBackendByRequester

Bases: {py:obj}`SATOSA.micro_services.base.RequestMicroService`

```{autodoc2-docstring} SATOSA.micro_services.custom_routing.DecideBackendByRequester
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.custom_routing.DecideBackendByRequester.__init__
```

````{py:method} process(context, data)
:canonical: SATOSA.micro_services.custom_routing.DecideBackendByRequester.process

```{autodoc2-docstring} SATOSA.micro_services.custom_routing.DecideBackendByRequester.process
```

````

`````

`````{py:class} DecideBackendByTargetIssuer(config: dict, *args, **kwargs)
:canonical: SATOSA.micro_services.custom_routing.DecideBackendByTargetIssuer

Bases: {py:obj}`SATOSA.micro_services.base.RequestMicroService`

```{autodoc2-docstring} SATOSA.micro_services.custom_routing.DecideBackendByTargetIssuer
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.custom_routing.DecideBackendByTargetIssuer.__init__
```

````{py:method} process(context: satosa.context.Context, data: satosa.internal.InternalData)
:canonical: SATOSA.micro_services.custom_routing.DecideBackendByTargetIssuer.process

```{autodoc2-docstring} SATOSA.micro_services.custom_routing.DecideBackendByTargetIssuer.process
```

````

`````

`````{py:class} DecideIfRequesterIsAllowed(config, *args, **kwargs)
:canonical: SATOSA.micro_services.custom_routing.DecideIfRequesterIsAllowed

Bases: {py:obj}`SATOSA.micro_services.base.RequestMicroService`

```{autodoc2-docstring} SATOSA.micro_services.custom_routing.DecideIfRequesterIsAllowed
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.custom_routing.DecideIfRequesterIsAllowed.__init__
```

````{py:method} _b64_url(data)
:canonical: SATOSA.micro_services.custom_routing.DecideIfRequesterIsAllowed._b64_url

```{autodoc2-docstring} SATOSA.micro_services.custom_routing.DecideIfRequesterIsAllowed._b64_url
```

````

````{py:method} process(context, data)
:canonical: SATOSA.micro_services.custom_routing.DecideIfRequesterIsAllowed.process

````

`````

````{py:data} logger
:canonical: SATOSA.micro_services.custom_routing.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.micro_services.custom_routing.logger
```

````
