# {py:mod}`SATOSA.micro_services.idp_hinting`

```{py:module} SATOSA.micro_services.idp_hinting
```

```{autodoc2-docstring} SATOSA.micro_services.idp_hinting
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IdpHinting <SATOSA.micro_services.idp_hinting.IdpHinting>`
  - ```{autodoc2-docstring} SATOSA.micro_services.idp_hinting.IdpHinting
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.micro_services.idp_hinting.logger>`
  - ```{autodoc2-docstring} SATOSA.micro_services.idp_hinting.logger
    :summary:
    ```
````

### API

`````{py:class} IdpHinting(config, *args, **kwargs)
:canonical: SATOSA.micro_services.idp_hinting.IdpHinting

Bases: {py:obj}`SATOSA.micro_services.base.RequestMicroService`

```{autodoc2-docstring} SATOSA.micro_services.idp_hinting.IdpHinting
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.idp_hinting.IdpHinting.__init__
```

````{py:method} process(context, data)
:canonical: SATOSA.micro_services.idp_hinting.IdpHinting.process

```{autodoc2-docstring} SATOSA.micro_services.idp_hinting.IdpHinting.process
```

````

`````

````{py:exception} IdpHintingError()
:canonical: SATOSA.micro_services.idp_hinting.IdpHintingError

Bases: {py:obj}`SATOSA.exception.SATOSAError`

```{autodoc2-docstring} SATOSA.micro_services.idp_hinting.IdpHintingError
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.idp_hinting.IdpHintingError.__init__
```

````

````{py:data} logger
:canonical: SATOSA.micro_services.idp_hinting.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.micro_services.idp_hinting.logger
```

````
