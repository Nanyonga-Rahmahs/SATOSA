# {py:mod}`SATOSA.scripts.satosa_saml_metadata`

```{py:module} SATOSA.scripts.satosa_saml_metadata
```

```{autodoc2-docstring} SATOSA.scripts.satosa_saml_metadata
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_create_merged_entities_descriptors <SATOSA.scripts.satosa_saml_metadata._create_merged_entities_descriptors>`
  - ```{autodoc2-docstring} SATOSA.scripts.satosa_saml_metadata._create_merged_entities_descriptors
    :summary:
    ```
* - {py:obj}`_create_split_entity_descriptors <SATOSA.scripts.satosa_saml_metadata._create_split_entity_descriptors>`
  - ```{autodoc2-docstring} SATOSA.scripts.satosa_saml_metadata._create_split_entity_descriptors
    :summary:
    ```
* - {py:obj}`_get_security_context <SATOSA.scripts.satosa_saml_metadata._get_security_context>`
  - ```{autodoc2-docstring} SATOSA.scripts.satosa_saml_metadata._get_security_context
    :summary:
    ```
* - {py:obj}`construct_saml_metadata <SATOSA.scripts.satosa_saml_metadata.construct_saml_metadata>`
  - ```{autodoc2-docstring} SATOSA.scripts.satosa_saml_metadata.construct_saml_metadata
    :summary:
    ```
* - {py:obj}`create_and_write_saml_metadata <SATOSA.scripts.satosa_saml_metadata.create_and_write_saml_metadata>`
  - ```{autodoc2-docstring} SATOSA.scripts.satosa_saml_metadata.create_and_write_saml_metadata
    :summary:
    ```
````

### API

````{py:function} _create_merged_entities_descriptors(entities, secc, valid, name, sign=True)
:canonical: SATOSA.scripts.satosa_saml_metadata._create_merged_entities_descriptors

```{autodoc2-docstring} SATOSA.scripts.satosa_saml_metadata._create_merged_entities_descriptors
```
````

````{py:function} _create_split_entity_descriptors(entities, secc, valid, sign=True)
:canonical: SATOSA.scripts.satosa_saml_metadata._create_split_entity_descriptors

```{autodoc2-docstring} SATOSA.scripts.satosa_saml_metadata._create_split_entity_descriptors
```
````

````{py:function} _get_security_context(key, cert)
:canonical: SATOSA.scripts.satosa_saml_metadata._get_security_context

```{autodoc2-docstring} SATOSA.scripts.satosa_saml_metadata._get_security_context
```
````

````{py:function} construct_saml_metadata(proxy_conf, key, cert, dir, valid, split_frontend, split_backend, sign)
:canonical: SATOSA.scripts.satosa_saml_metadata.construct_saml_metadata

```{autodoc2-docstring} SATOSA.scripts.satosa_saml_metadata.construct_saml_metadata
```
````

````{py:function} create_and_write_saml_metadata(proxy_conf, key, cert, dir, valid, split_frontend_metadata=False, split_backend_metadata=False, sign=True)
:canonical: SATOSA.scripts.satosa_saml_metadata.create_and_write_saml_metadata

```{autodoc2-docstring} SATOSA.scripts.satosa_saml_metadata.create_and_write_saml_metadata
```
````
