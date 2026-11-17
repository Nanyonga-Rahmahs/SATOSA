# {py:mod}`SATOSA.micro_services.disco`

```{py:module} SATOSA.micro_services.disco
```

```{autodoc2-docstring} SATOSA.micro_services.disco
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DiscoToTargetIssuer <SATOSA.micro_services.disco.DiscoToTargetIssuer>`
  - ```{autodoc2-docstring} SATOSA.micro_services.disco.DiscoToTargetIssuer
    :summary:
    ```
````

### API

`````{py:class} DiscoToTargetIssuer(config: dict, *args, **kwargs)
:canonical: SATOSA.micro_services.disco.DiscoToTargetIssuer

Bases: {py:obj}`SATOSA.micro_services.base.RequestMicroService`

```{autodoc2-docstring} SATOSA.micro_services.disco.DiscoToTargetIssuer
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.disco.DiscoToTargetIssuer.__init__
```

````{py:method} _handle_disco_response(context: satosa.context.Context)
:canonical: SATOSA.micro_services.disco.DiscoToTargetIssuer._handle_disco_response

```{autodoc2-docstring} SATOSA.micro_services.disco.DiscoToTargetIssuer._handle_disco_response
```

````

````{py:method} process(context: satosa.context.Context, data: satosa.internal.InternalData)
:canonical: SATOSA.micro_services.disco.DiscoToTargetIssuer.process

```{autodoc2-docstring} SATOSA.micro_services.disco.DiscoToTargetIssuer.process
```

````

````{py:method} register_endpoints()
:canonical: SATOSA.micro_services.disco.DiscoToTargetIssuer.register_endpoints

```{autodoc2-docstring} SATOSA.micro_services.disco.DiscoToTargetIssuer.register_endpoints
```

````

`````

````{py:exception} DiscoToTargetIssuerError()
:canonical: SATOSA.micro_services.disco.DiscoToTargetIssuerError

Bases: {py:obj}`SATOSA.exception.SATOSAError`

```{autodoc2-docstring} SATOSA.micro_services.disco.DiscoToTargetIssuerError
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.disco.DiscoToTargetIssuerError.__init__
```

````
