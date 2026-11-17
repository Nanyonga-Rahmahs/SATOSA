# {py:mod}`SATOSA.satosa_config`

```{py:module} SATOSA.satosa_config
```

```{autodoc2-docstring} SATOSA.satosa_config
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SATOSAConfig <SATOSA.satosa_config.SATOSAConfig>`
  - ```{autodoc2-docstring} SATOSA.satosa_config.SATOSAConfig
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.satosa_config.logger>`
  - ```{autodoc2-docstring} SATOSA.satosa_config.logger
    :summary:
    ```
````

### API

`````{py:class} SATOSAConfig(config)
:canonical: SATOSA.satosa_config.SATOSAConfig

Bases: {py:obj}`object`

```{autodoc2-docstring} SATOSA.satosa_config.SATOSAConfig
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.satosa_config.SATOSAConfig.__init__
```

````{py:method} __contains__(key)
:canonical: SATOSA.satosa_config.SATOSAConfig.__contains__

```{autodoc2-docstring} SATOSA.satosa_config.SATOSAConfig.__contains__
```

````

````{py:method} __getitem__(item)
:canonical: SATOSA.satosa_config.SATOSAConfig.__getitem__

```{autodoc2-docstring} SATOSA.satosa_config.SATOSAConfig.__getitem__
```

````

````{py:method} __setitem__(key, value)
:canonical: SATOSA.satosa_config.SATOSAConfig.__setitem__

```{autodoc2-docstring} SATOSA.satosa_config.SATOSAConfig.__setitem__
```

````

````{py:method} _load_dict(config)
:canonical: SATOSA.satosa_config.SATOSAConfig._load_dict

```{autodoc2-docstring} SATOSA.satosa_config.SATOSAConfig._load_dict
```

````

````{py:method} _load_yaml(config_file)
:canonical: SATOSA.satosa_config.SATOSAConfig._load_yaml

```{autodoc2-docstring} SATOSA.satosa_config.SATOSAConfig._load_yaml
```

````

````{py:method} _verify_dict(conf)
:canonical: SATOSA.satosa_config.SATOSAConfig._verify_dict

```{autodoc2-docstring} SATOSA.satosa_config.SATOSAConfig._verify_dict
```

````

````{py:method} get(item, default=None)
:canonical: SATOSA.satosa_config.SATOSAConfig.get

```{autodoc2-docstring} SATOSA.satosa_config.SATOSAConfig.get
```

````

````{py:attribute} mandatory_dict_keys
:canonical: SATOSA.satosa_config.SATOSAConfig.mandatory_dict_keys
:value: >
   ['BASE', 'BACKEND_MODULES', 'FRONTEND_MODULES', 'INTERNAL_ATTRIBUTES', 'COOKIE_STATE_NAME']

```{autodoc2-docstring} SATOSA.satosa_config.SATOSAConfig.mandatory_dict_keys
```

````

````{py:attribute} sensitive_dict_keys
:canonical: SATOSA.satosa_config.SATOSAConfig.sensitive_dict_keys
:value: >
   ['STATE_ENCRYPTION_KEY']

```{autodoc2-docstring} SATOSA.satosa_config.SATOSAConfig.sensitive_dict_keys
```

````

`````

````{py:data} logger
:canonical: SATOSA.satosa_config.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.satosa_config.logger
```

````
