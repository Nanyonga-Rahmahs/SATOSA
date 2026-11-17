# {py:mod}`tests.satosa.test_satosa_config`

```{py:module} tests.satosa.test_satosa_config
```

```{autodoc2-docstring} tests.satosa.test_satosa_config
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestSATOSAConfig <tests.satosa.test_satosa_config.TestSATOSAConfig>`
  - ```{autodoc2-docstring} tests.satosa.test_satosa_config.TestSATOSAConfig
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TEST_RESOURCE_BASE_PATH <tests.satosa.test_satosa_config.TEST_RESOURCE_BASE_PATH>`
  - ```{autodoc2-docstring} tests.satosa.test_satosa_config.TEST_RESOURCE_BASE_PATH
    :summary:
    ```
````

### API

````{py:data} TEST_RESOURCE_BASE_PATH
:canonical: tests.satosa.test_satosa_config.TEST_RESOURCE_BASE_PATH
:value: >
   'join(...)'

```{autodoc2-docstring} tests.satosa.test_satosa_config.TEST_RESOURCE_BASE_PATH
```

````

`````{py:class} TestSATOSAConfig
:canonical: tests.satosa.test_satosa_config.TestSATOSAConfig

```{autodoc2-docstring} tests.satosa.test_satosa_config.TestSATOSAConfig
```

````{py:method} non_sensitive_config_dict()
:canonical: tests.satosa.test_satosa_config.TestSATOSAConfig.non_sensitive_config_dict

```{autodoc2-docstring} tests.satosa.test_satosa_config.TestSATOSAConfig.non_sensitive_config_dict
```

````

````{py:method} test_can_read_endpoint_configs_from_dict(satosa_config_dict, modules_key)
:canonical: tests.satosa.test_satosa_config.TestSATOSAConfig.test_can_read_endpoint_configs_from_dict

```{autodoc2-docstring} tests.satosa.test_satosa_config.TestSATOSAConfig.test_can_read_endpoint_configs_from_dict
```

````

````{py:method} test_can_read_endpoint_configs_from_file(satosa_config_dict, modules_key)
:canonical: tests.satosa.test_satosa_config.TestSATOSAConfig.test_can_read_endpoint_configs_from_file

```{autodoc2-docstring} tests.satosa.test_satosa_config.TestSATOSAConfig.test_can_read_endpoint_configs_from_file
```

````

````{py:method} test_can_substitute_from_environment_variable(monkeypatch)
:canonical: tests.satosa.test_satosa_config.TestSATOSAConfig.test_can_substitute_from_environment_variable

```{autodoc2-docstring} tests.satosa.test_satosa_config.TestSATOSAConfig.test_can_substitute_from_environment_variable
```

````

````{py:method} test_can_substitute_from_environment_variable_file(monkeypatch)
:canonical: tests.satosa.test_satosa_config.TestSATOSAConfig.test_can_substitute_from_environment_variable_file

```{autodoc2-docstring} tests.satosa.test_satosa_config.TestSATOSAConfig.test_can_substitute_from_environment_variable_file
```

````

````{py:method} test_constructor_should_raise_exception_if_sensitive_keys_are_missing(non_sensitive_config_dict)
:canonical: tests.satosa.test_satosa_config.TestSATOSAConfig.test_constructor_should_raise_exception_if_sensitive_keys_are_missing

```{autodoc2-docstring} tests.satosa.test_satosa_config.TestSATOSAConfig.test_constructor_should_raise_exception_if_sensitive_keys_are_missing
```

````

````{py:method} test_read_senstive_config_data_from_env_var(monkeypatch, non_sensitive_config_dict)
:canonical: tests.satosa.test_satosa_config.TestSATOSAConfig.test_read_senstive_config_data_from_env_var

```{autodoc2-docstring} tests.satosa.test_satosa_config.TestSATOSAConfig.test_read_senstive_config_data_from_env_var
```

````

````{py:method} test_senstive_config_data_from_env_var_overrides_config(monkeypatch, non_sensitive_config_dict)
:canonical: tests.satosa.test_satosa_config.TestSATOSAConfig.test_senstive_config_data_from_env_var_overrides_config

```{autodoc2-docstring} tests.satosa.test_satosa_config.TestSATOSAConfig.test_senstive_config_data_from_env_var_overrides_config
```

````

`````
