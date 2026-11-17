# {py:mod}`SATOSA.micro_services.custom_logging`

```{py:module} SATOSA.micro_services.custom_logging
```

```{autodoc2-docstring} SATOSA.micro_services.custom_logging
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CustomLoggingService <SATOSA.micro_services.custom_logging.CustomLoggingService>`
  - ```{autodoc2-docstring} SATOSA.micro_services.custom_logging.CustomLoggingService
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.micro_services.custom_logging.logger>`
  - ```{autodoc2-docstring} SATOSA.micro_services.custom_logging.logger
    :summary:
    ```
````

### API

`````{py:class} CustomLoggingService(config, *args, **kwargs)
:canonical: SATOSA.micro_services.custom_logging.CustomLoggingService

Bases: {py:obj}`SATOSA.micro_services.base.ResponseMicroService`

```{autodoc2-docstring} SATOSA.micro_services.custom_logging.CustomLoggingService
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.custom_logging.CustomLoggingService.__init__
```

````{py:attribute} logprefix
:canonical: SATOSA.micro_services.custom_logging.CustomLoggingService.logprefix
:value: >
   'CUSTOM_LOGGING_SERVICE:'

```{autodoc2-docstring} SATOSA.micro_services.custom_logging.CustomLoggingService.logprefix
```

````

````{py:method} process(context, data)
:canonical: SATOSA.micro_services.custom_logging.CustomLoggingService.process

```{autodoc2-docstring} SATOSA.micro_services.custom_logging.CustomLoggingService.process
```

````

`````

````{py:data} logger
:canonical: SATOSA.micro_services.custom_logging.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.micro_services.custom_logging.logger
```

````
