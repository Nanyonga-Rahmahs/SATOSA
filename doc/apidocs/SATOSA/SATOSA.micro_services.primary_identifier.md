# {py:mod}`SATOSA.micro_services.primary_identifier`

```{py:module} SATOSA.micro_services.primary_identifier
```

```{autodoc2-docstring} SATOSA.micro_services.primary_identifier
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PrimaryIdentifier <SATOSA.micro_services.primary_identifier.PrimaryIdentifier>`
  - ```{autodoc2-docstring} SATOSA.micro_services.primary_identifier.PrimaryIdentifier
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.micro_services.primary_identifier.logger>`
  - ```{autodoc2-docstring} SATOSA.micro_services.primary_identifier.logger
    :summary:
    ```
````

### API

`````{py:class} PrimaryIdentifier(config, *args, **kwargs)
:canonical: SATOSA.micro_services.primary_identifier.PrimaryIdentifier

Bases: {py:obj}`satosa.micro_services.base.ResponseMicroService`

```{autodoc2-docstring} SATOSA.micro_services.primary_identifier.PrimaryIdentifier
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.primary_identifier.PrimaryIdentifier.__init__
```

````{py:method} constructPrimaryIdentifier(data, ordered_identifier_candidates)
:canonical: SATOSA.micro_services.primary_identifier.PrimaryIdentifier.constructPrimaryIdentifier

```{autodoc2-docstring} SATOSA.micro_services.primary_identifier.PrimaryIdentifier.constructPrimaryIdentifier
```

````

````{py:attribute} logprefix
:canonical: SATOSA.micro_services.primary_identifier.PrimaryIdentifier.logprefix
:value: >
   'PRIMARY_IDENTIFIER:'

```{autodoc2-docstring} SATOSA.micro_services.primary_identifier.PrimaryIdentifier.logprefix
```

````

````{py:method} process(context, data)
:canonical: SATOSA.micro_services.primary_identifier.PrimaryIdentifier.process

````

`````

````{py:data} logger
:canonical: SATOSA.micro_services.primary_identifier.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.micro_services.primary_identifier.logger
```

````
