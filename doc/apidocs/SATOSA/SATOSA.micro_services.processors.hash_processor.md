# {py:mod}`SATOSA.micro_services.processors.hash_processor`

```{py:module} SATOSA.micro_services.processors.hash_processor
```

```{autodoc2-docstring} SATOSA.micro_services.processors.hash_processor
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`HashProcessor <SATOSA.micro_services.processors.hash_processor.HashProcessor>`
  - ```{autodoc2-docstring} SATOSA.micro_services.processors.hash_processor.HashProcessor
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CONFIG_DEFAULT_HASHALGO <SATOSA.micro_services.processors.hash_processor.CONFIG_DEFAULT_HASHALGO>`
  - ```{autodoc2-docstring} SATOSA.micro_services.processors.hash_processor.CONFIG_DEFAULT_HASHALGO
    :summary:
    ```
* - {py:obj}`CONFIG_DEFAULT_SALT <SATOSA.micro_services.processors.hash_processor.CONFIG_DEFAULT_SALT>`
  - ```{autodoc2-docstring} SATOSA.micro_services.processors.hash_processor.CONFIG_DEFAULT_SALT
    :summary:
    ```
* - {py:obj}`CONFIG_KEY_HASHALGO <SATOSA.micro_services.processors.hash_processor.CONFIG_KEY_HASHALGO>`
  - ```{autodoc2-docstring} SATOSA.micro_services.processors.hash_processor.CONFIG_KEY_HASHALGO
    :summary:
    ```
* - {py:obj}`CONFIG_KEY_SALT <SATOSA.micro_services.processors.hash_processor.CONFIG_KEY_SALT>`
  - ```{autodoc2-docstring} SATOSA.micro_services.processors.hash_processor.CONFIG_KEY_SALT
    :summary:
    ```
````

### API

````{py:data} CONFIG_DEFAULT_HASHALGO
:canonical: SATOSA.micro_services.processors.hash_processor.CONFIG_DEFAULT_HASHALGO
:value: >
   'sha256'

```{autodoc2-docstring} SATOSA.micro_services.processors.hash_processor.CONFIG_DEFAULT_HASHALGO
```

````

````{py:data} CONFIG_DEFAULT_SALT
:canonical: SATOSA.micro_services.processors.hash_processor.CONFIG_DEFAULT_SALT
:value: <Multiline-String>

```{autodoc2-docstring} SATOSA.micro_services.processors.hash_processor.CONFIG_DEFAULT_SALT
```

````

````{py:data} CONFIG_KEY_HASHALGO
:canonical: SATOSA.micro_services.processors.hash_processor.CONFIG_KEY_HASHALGO
:value: >
   'hash_algo'

```{autodoc2-docstring} SATOSA.micro_services.processors.hash_processor.CONFIG_KEY_HASHALGO
```

````

````{py:data} CONFIG_KEY_SALT
:canonical: SATOSA.micro_services.processors.hash_processor.CONFIG_KEY_SALT
:value: >
   'salt'

```{autodoc2-docstring} SATOSA.micro_services.processors.hash_processor.CONFIG_KEY_SALT
```

````

`````{py:class} HashProcessor
:canonical: SATOSA.micro_services.processors.hash_processor.HashProcessor

Bases: {py:obj}`SATOSA.micro_services.processors.base_processor.BaseProcessor`

```{autodoc2-docstring} SATOSA.micro_services.processors.hash_processor.HashProcessor
```

````{py:method} process(internal_data, attribute, **kwargs)
:canonical: SATOSA.micro_services.processors.hash_processor.HashProcessor.process

```{autodoc2-docstring} SATOSA.micro_services.processors.hash_processor.HashProcessor.process
```

````

`````
