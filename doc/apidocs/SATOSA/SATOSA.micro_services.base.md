# {py:mod}`SATOSA.micro_services.base`

```{py:module} SATOSA.micro_services.base
```

```{autodoc2-docstring} SATOSA.micro_services.base
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MicroService <SATOSA.micro_services.base.MicroService>`
  - ```{autodoc2-docstring} SATOSA.micro_services.base.MicroService
    :summary:
    ```
* - {py:obj}`RequestMicroService <SATOSA.micro_services.base.RequestMicroService>`
  - ```{autodoc2-docstring} SATOSA.micro_services.base.RequestMicroService
    :summary:
    ```
* - {py:obj}`ResponseMicroService <SATOSA.micro_services.base.ResponseMicroService>`
  - ```{autodoc2-docstring} SATOSA.micro_services.base.ResponseMicroService
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.micro_services.base.logger>`
  - ```{autodoc2-docstring} SATOSA.micro_services.base.logger
    :summary:
    ```
````

### API

`````{py:class} MicroService(name, base_url, **kwargs)
:canonical: SATOSA.micro_services.base.MicroService

Bases: {py:obj}`object`

```{autodoc2-docstring} SATOSA.micro_services.base.MicroService
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.base.MicroService.__init__
```

````{py:method} process(context, data)
:canonical: SATOSA.micro_services.base.MicroService.process

```{autodoc2-docstring} SATOSA.micro_services.base.MicroService.process
```

````

````{py:method} register_endpoints()
:canonical: SATOSA.micro_services.base.MicroService.register_endpoints

```{autodoc2-docstring} SATOSA.micro_services.base.MicroService.register_endpoints
```

````

`````

````{py:class} RequestMicroService(name, base_url, **kwargs)
:canonical: SATOSA.micro_services.base.RequestMicroService

Bases: {py:obj}`SATOSA.micro_services.base.MicroService`

```{autodoc2-docstring} SATOSA.micro_services.base.RequestMicroService
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.base.RequestMicroService.__init__
```

````

````{py:class} ResponseMicroService(name, base_url, **kwargs)
:canonical: SATOSA.micro_services.base.ResponseMicroService

Bases: {py:obj}`SATOSA.micro_services.base.MicroService`

```{autodoc2-docstring} SATOSA.micro_services.base.ResponseMicroService
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.base.ResponseMicroService.__init__
```

````

````{py:data} logger
:canonical: SATOSA.micro_services.base.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.micro_services.base.logger
```

````
