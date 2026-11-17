# {py:mod}`SATOSA.micro_services.account_linking`

```{py:module} SATOSA.micro_services.account_linking
```

```{autodoc2-docstring} SATOSA.micro_services.account_linking
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AccountLinking <SATOSA.micro_services.account_linking.AccountLinking>`
  - ```{autodoc2-docstring} SATOSA.micro_services.account_linking.AccountLinking
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.micro_services.account_linking.logger>`
  - ```{autodoc2-docstring} SATOSA.micro_services.account_linking.logger
    :summary:
    ```
````

### API

`````{py:class} AccountLinking(config, *args, **kwargs)
:canonical: SATOSA.micro_services.account_linking.AccountLinking

Bases: {py:obj}`SATOSA.micro_services.base.ResponseMicroService`

```{autodoc2-docstring} SATOSA.micro_services.account_linking.AccountLinking
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.account_linking.AccountLinking.__init__
```

````{py:method} _get_uuid(context, issuer, id)
:canonical: SATOSA.micro_services.account_linking.AccountLinking._get_uuid

```{autodoc2-docstring} SATOSA.micro_services.account_linking.AccountLinking._get_uuid
```

````

````{py:method} _handle_al_response(context)
:canonical: SATOSA.micro_services.account_linking.AccountLinking._handle_al_response

```{autodoc2-docstring} SATOSA.micro_services.account_linking.AccountLinking._handle_al_response
```

````

````{py:method} process(context, internal_response)
:canonical: SATOSA.micro_services.account_linking.AccountLinking.process

```{autodoc2-docstring} SATOSA.micro_services.account_linking.AccountLinking.process
```

````

````{py:method} register_endpoints()
:canonical: SATOSA.micro_services.account_linking.AccountLinking.register_endpoints

```{autodoc2-docstring} SATOSA.micro_services.account_linking.AccountLinking.register_endpoints
```

````

`````

````{py:data} logger
:canonical: SATOSA.micro_services.account_linking.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.micro_services.account_linking.logger
```

````
