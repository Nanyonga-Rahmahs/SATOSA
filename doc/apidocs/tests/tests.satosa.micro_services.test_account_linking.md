# {py:mod}`tests.satosa.micro_services.test_account_linking`

```{py:module} tests.satosa.micro_services.test_account_linking
```

```{autodoc2-docstring} tests.satosa.micro_services.test_account_linking
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestAccountLinking <tests.satosa.micro_services.test_account_linking.TestAccountLinking>`
  - ```{autodoc2-docstring} tests.satosa.micro_services.test_account_linking.TestAccountLinking
    :summary:
    ```
````

### API

`````{py:class} TestAccountLinking
:canonical: tests.satosa.micro_services.test_account_linking.TestAccountLinking

```{autodoc2-docstring} tests.satosa.micro_services.test_account_linking.TestAccountLinking
```

````{py:method} account_linking_config(signing_key_path)
:canonical: tests.satosa.micro_services.test_account_linking.TestAccountLinking.account_linking_config

```{autodoc2-docstring} tests.satosa.micro_services.test_account_linking.TestAccountLinking.account_linking_config
```

````

````{py:method} create_account_linking(account_linking_config)
:canonical: tests.satosa.micro_services.test_account_linking.TestAccountLinking.create_account_linking

```{autodoc2-docstring} tests.satosa.micro_services.test_account_linking.TestAccountLinking.create_account_linking
```

````

````{py:method} internal_response()
:canonical: tests.satosa.micro_services.test_account_linking.TestAccountLinking.internal_response

```{autodoc2-docstring} tests.satosa.micro_services.test_account_linking.TestAccountLinking.internal_response
```

````

````{py:method} test_account_linking_failed(account_linking_config, internal_response, context)
:canonical: tests.satosa.micro_services.test_account_linking.TestAccountLinking.test_account_linking_failed

```{autodoc2-docstring} tests.satosa.micro_services.test_account_linking.TestAccountLinking.test_account_linking_failed
```

````

````{py:method} test_existing_account_linking_with_known_known_uuid(account_linking_config, internal_response, context)
:canonical: tests.satosa.micro_services.test_account_linking.TestAccountLinking.test_existing_account_linking_with_known_known_uuid

```{autodoc2-docstring} tests.satosa.micro_services.test_account_linking.TestAccountLinking.test_existing_account_linking_with_known_known_uuid
```

````

````{py:method} test_full_flow(account_linking_config, internal_response, context)
:canonical: tests.satosa.micro_services.test_account_linking.TestAccountLinking.test_full_flow

```{autodoc2-docstring} tests.satosa.micro_services.test_account_linking.TestAccountLinking.test_full_flow
```

````

````{py:method} test_manage_al_handle_bad_response_status(http_status, account_linking_config, internal_response, context)
:canonical: tests.satosa.micro_services.test_account_linking.TestAccountLinking.test_manage_al_handle_bad_response_status

```{autodoc2-docstring} tests.satosa.micro_services.test_account_linking.TestAccountLinking.test_manage_al_handle_bad_response_status
```

````

````{py:method} test_manage_al_handle_failed_connection(account_linking_config, internal_response, context)
:canonical: tests.satosa.micro_services.test_account_linking.TestAccountLinking.test_manage_al_handle_failed_connection

```{autodoc2-docstring} tests.satosa.micro_services.test_account_linking.TestAccountLinking.test_manage_al_handle_failed_connection
```

````

````{py:method} test_register_endpoints()
:canonical: tests.satosa.micro_services.test_account_linking.TestAccountLinking.test_register_endpoints

```{autodoc2-docstring} tests.satosa.micro_services.test_account_linking.TestAccountLinking.test_register_endpoints
```

````

`````
