# {py:mod}`SATOSA.micro_services.consent`

```{py:module} SATOSA.micro_services.consent
```

```{autodoc2-docstring} SATOSA.micro_services.consent
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Consent <SATOSA.micro_services.consent.Consent>`
  - ```{autodoc2-docstring} SATOSA.micro_services.consent.Consent
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`STATE_KEY <SATOSA.micro_services.consent.STATE_KEY>`
  - ```{autodoc2-docstring} SATOSA.micro_services.consent.STATE_KEY
    :summary:
    ```
* - {py:obj}`logger <SATOSA.micro_services.consent.logger>`
  - ```{autodoc2-docstring} SATOSA.micro_services.consent.logger
    :summary:
    ```
````

### API

`````{py:class} Consent(config, internal_attributes, *args, **kwargs)
:canonical: SATOSA.micro_services.consent.Consent

Bases: {py:obj}`satosa.micro_services.base.ResponseMicroService`

```{autodoc2-docstring} SATOSA.micro_services.consent.Consent
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.consent.Consent.__init__
```

````{py:method} _approve_new_consent(context, internal_response, id_hash)
:canonical: SATOSA.micro_services.consent.Consent._approve_new_consent

```{autodoc2-docstring} SATOSA.micro_services.consent.Consent._approve_new_consent
```

````

````{py:method} _consent_registration(consent_args)
:canonical: SATOSA.micro_services.consent.Consent._consent_registration

```{autodoc2-docstring} SATOSA.micro_services.consent.Consent._consent_registration
```

````

````{py:method} _end_consent(context, internal_response)
:canonical: SATOSA.micro_services.consent.Consent._end_consent

```{autodoc2-docstring} SATOSA.micro_services.consent.Consent._end_consent
```

````

````{py:method} _filter_attributes(attributes, filter)
:canonical: SATOSA.micro_services.consent.Consent._filter_attributes

```{autodoc2-docstring} SATOSA.micro_services.consent.Consent._filter_attributes
```

````

````{py:method} _get_consent_id(requester, user_id, filtered_attr)
:canonical: SATOSA.micro_services.consent.Consent._get_consent_id

```{autodoc2-docstring} SATOSA.micro_services.consent.Consent._get_consent_id
```

````

````{py:method} _handle_consent_response(context)
:canonical: SATOSA.micro_services.consent.Consent._handle_consent_response

```{autodoc2-docstring} SATOSA.micro_services.consent.Consent._handle_consent_response
```

````

````{py:method} _verify_consent(consent_id)
:canonical: SATOSA.micro_services.consent.Consent._verify_consent

```{autodoc2-docstring} SATOSA.micro_services.consent.Consent._verify_consent
```

````

````{py:method} process(context, internal_response)
:canonical: SATOSA.micro_services.consent.Consent.process

```{autodoc2-docstring} SATOSA.micro_services.consent.Consent.process
```

````

````{py:method} register_endpoints()
:canonical: SATOSA.micro_services.consent.Consent.register_endpoints

```{autodoc2-docstring} SATOSA.micro_services.consent.Consent.register_endpoints
```

````

`````

````{py:data} STATE_KEY
:canonical: SATOSA.micro_services.consent.STATE_KEY
:value: >
   'CONSENT'

```{autodoc2-docstring} SATOSA.micro_services.consent.STATE_KEY
```

````

```{py:exception} UnexpectedResponseError()
:canonical: SATOSA.micro_services.consent.UnexpectedResponseError

Bases: {py:obj}`Exception`

```

````{py:data} logger
:canonical: SATOSA.micro_services.consent.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.micro_services.consent.logger
```

````
