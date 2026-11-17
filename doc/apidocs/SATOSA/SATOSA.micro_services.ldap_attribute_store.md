# {py:mod}`SATOSA.micro_services.ldap_attribute_store`

```{py:module} SATOSA.micro_services.ldap_attribute_store
```

```{autodoc2-docstring} SATOSA.micro_services.ldap_attribute_store
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LdapAttributeStore <SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore>`
  - ```{autodoc2-docstring} SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`KEY_FOUND_LDAP_RECORD <SATOSA.micro_services.ldap_attribute_store.KEY_FOUND_LDAP_RECORD>`
  - ```{autodoc2-docstring} SATOSA.micro_services.ldap_attribute_store.KEY_FOUND_LDAP_RECORD
    :summary:
    ```
* - {py:obj}`logger <SATOSA.micro_services.ldap_attribute_store.logger>`
  - ```{autodoc2-docstring} SATOSA.micro_services.ldap_attribute_store.logger
    :summary:
    ```
````

### API

````{py:data} KEY_FOUND_LDAP_RECORD
:canonical: SATOSA.micro_services.ldap_attribute_store.KEY_FOUND_LDAP_RECORD
:value: >
   'ldap_attribute_store_found_record'

```{autodoc2-docstring} SATOSA.micro_services.ldap_attribute_store.KEY_FOUND_LDAP_RECORD
```

````

`````{py:class} LdapAttributeStore(config, *args, **kwargs)
:canonical: SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore

Bases: {py:obj}`satosa.micro_services.base.ResponseMicroService`

```{autodoc2-docstring} SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore.__init__
```

````{py:method} _construct_filter_value(candidate, name_id_value, name_id_format, issuer, attributes)
:canonical: SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore._construct_filter_value

```{autodoc2-docstring} SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore._construct_filter_value
```

````

````{py:method} _filter_config(config, fields=None)
:canonical: SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore._filter_config

```{autodoc2-docstring} SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore._filter_config
```

````

````{py:method} _ldap_connection_factory(config)
:canonical: SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore._ldap_connection_factory

```{autodoc2-docstring} SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore._ldap_connection_factory
```

````

````{py:method} _populate_attributes(config, record)
:canonical: SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore._populate_attributes

```{autodoc2-docstring} SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore._populate_attributes
```

````

````{py:method} _populate_input_for_name_id(config, record, data)
:canonical: SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore._populate_input_for_name_id

```{autodoc2-docstring} SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore._populate_input_for_name_id
```

````

````{py:attribute} config_defaults
:canonical: SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore.config_defaults
:value: >
   None

```{autodoc2-docstring} SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore.config_defaults
```

````

````{py:method} process(context, data)
:canonical: SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore.process

```{autodoc2-docstring} SATOSA.micro_services.ldap_attribute_store.LdapAttributeStore.process
```

````

`````

````{py:exception} LdapAttributeStoreError()
:canonical: SATOSA.micro_services.ldap_attribute_store.LdapAttributeStoreError

Bases: {py:obj}`satosa.exception.SATOSAError`

```{autodoc2-docstring} SATOSA.micro_services.ldap_attribute_store.LdapAttributeStoreError
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.ldap_attribute_store.LdapAttributeStoreError.__init__
```

````

````{py:data} logger
:canonical: SATOSA.micro_services.ldap_attribute_store.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.micro_services.ldap_attribute_store.logger
```

````
