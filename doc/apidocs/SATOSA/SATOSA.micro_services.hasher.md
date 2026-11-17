# {py:mod}`SATOSA.micro_services.hasher`

```{py:module} SATOSA.micro_services.hasher
```

```{autodoc2-docstring} SATOSA.micro_services.hasher
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Hasher <SATOSA.micro_services.hasher.Hasher>`
  - ```{autodoc2-docstring} SATOSA.micro_services.hasher.Hasher
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CONFIG_KEY_ALG <SATOSA.micro_services.hasher.CONFIG_KEY_ALG>`
  - ```{autodoc2-docstring} SATOSA.micro_services.hasher.CONFIG_KEY_ALG
    :summary:
    ```
* - {py:obj}`CONFIG_KEY_ATTRS <SATOSA.micro_services.hasher.CONFIG_KEY_ATTRS>`
  - ```{autodoc2-docstring} SATOSA.micro_services.hasher.CONFIG_KEY_ATTRS
    :summary:
    ```
* - {py:obj}`CONFIG_KEY_SALT <SATOSA.micro_services.hasher.CONFIG_KEY_SALT>`
  - ```{autodoc2-docstring} SATOSA.micro_services.hasher.CONFIG_KEY_SALT
    :summary:
    ```
* - {py:obj}`CONFIG_KEY_SUBJID <SATOSA.micro_services.hasher.CONFIG_KEY_SUBJID>`
  - ```{autodoc2-docstring} SATOSA.micro_services.hasher.CONFIG_KEY_SUBJID
    :summary:
    ```
````

### API

````{py:data} CONFIG_KEY_ALG
:canonical: SATOSA.micro_services.hasher.CONFIG_KEY_ALG
:value: >
   'alg'

```{autodoc2-docstring} SATOSA.micro_services.hasher.CONFIG_KEY_ALG
```

````

````{py:data} CONFIG_KEY_ATTRS
:canonical: SATOSA.micro_services.hasher.CONFIG_KEY_ATTRS
:value: >
   'attributes'

```{autodoc2-docstring} SATOSA.micro_services.hasher.CONFIG_KEY_ATTRS
```

````

````{py:data} CONFIG_KEY_SALT
:canonical: SATOSA.micro_services.hasher.CONFIG_KEY_SALT
:value: >
   'salt'

```{autodoc2-docstring} SATOSA.micro_services.hasher.CONFIG_KEY_SALT
```

````

````{py:data} CONFIG_KEY_SUBJID
:canonical: SATOSA.micro_services.hasher.CONFIG_KEY_SUBJID
:value: >
   'subject_id'

```{autodoc2-docstring} SATOSA.micro_services.hasher.CONFIG_KEY_SUBJID
```

````

`````{py:class} Hasher(config, *args, **kwargs)
:canonical: SATOSA.micro_services.hasher.Hasher

Bases: {py:obj}`satosa.micro_services.base.ResponseMicroService`

```{autodoc2-docstring} SATOSA.micro_services.hasher.Hasher
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.hasher.Hasher.__init__
```

````{py:method} _init_config(config)
:canonical: SATOSA.micro_services.hasher.Hasher._init_config

```{autodoc2-docstring} SATOSA.micro_services.hasher.Hasher._init_config
```

````

````{py:method} hash_attributes(config, internal_data)
:canonical: SATOSA.micro_services.hasher.Hasher.hash_attributes

```{autodoc2-docstring} SATOSA.micro_services.hasher.Hasher.hash_attributes
```

````

````{py:method} hash_subject_id(config, internal_data)
:canonical: SATOSA.micro_services.hasher.Hasher.hash_subject_id

```{autodoc2-docstring} SATOSA.micro_services.hasher.Hasher.hash_subject_id
```

````

````{py:method} process(context, internal_data)
:canonical: SATOSA.micro_services.hasher.Hasher.process

````

`````
