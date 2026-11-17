# {py:mod}`SATOSA.metadata_creation.saml_metadata`

```{py:module} SATOSA.metadata_creation.saml_metadata
```

```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_create_backend_metadata <SATOSA.metadata_creation.saml_metadata._create_backend_metadata>`
  - ```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata._create_backend_metadata
    :summary:
    ```
* - {py:obj}`_create_entity_descriptor <SATOSA.metadata_creation.saml_metadata._create_entity_descriptor>`
  - ```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata._create_entity_descriptor
    :summary:
    ```
* - {py:obj}`_create_frontend_metadata <SATOSA.metadata_creation.saml_metadata._create_frontend_metadata>`
  - ```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata._create_frontend_metadata
    :summary:
    ```
* - {py:obj}`_create_mirrored_entity_config <SATOSA.metadata_creation.saml_metadata._create_mirrored_entity_config>`
  - ```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata._create_mirrored_entity_config
    :summary:
    ```
* - {py:obj}`create_entity_descriptor_metadata <SATOSA.metadata_creation.saml_metadata.create_entity_descriptor_metadata>`
  - ```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata.create_entity_descriptor_metadata
    :summary:
    ```
* - {py:obj}`create_entity_descriptors <SATOSA.metadata_creation.saml_metadata.create_entity_descriptors>`
  - ```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata.create_entity_descriptors
    :summary:
    ```
* - {py:obj}`create_signed_entities_descriptor <SATOSA.metadata_creation.saml_metadata.create_signed_entities_descriptor>`
  - ```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata.create_signed_entities_descriptor
    :summary:
    ```
* - {py:obj}`create_signed_entity_descriptor <SATOSA.metadata_creation.saml_metadata.create_signed_entity_descriptor>`
  - ```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata.create_signed_entity_descriptor
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.metadata_creation.saml_metadata.logger>`
  - ```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata.logger
    :summary:
    ```
````

### API

````{py:function} _create_backend_metadata(backend_modules)
:canonical: SATOSA.metadata_creation.saml_metadata._create_backend_metadata

```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata._create_backend_metadata
```
````

````{py:function} _create_entity_descriptor(entity_config)
:canonical: SATOSA.metadata_creation.saml_metadata._create_entity_descriptor

```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata._create_entity_descriptor
```
````

````{py:function} _create_frontend_metadata(frontend_modules, backend_modules)
:canonical: SATOSA.metadata_creation.saml_metadata._create_frontend_metadata

```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata._create_frontend_metadata
```
````

````{py:function} _create_mirrored_entity_config(frontend_instance, target_metadata_info, backend_name)
:canonical: SATOSA.metadata_creation.saml_metadata._create_mirrored_entity_config

```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata._create_mirrored_entity_config
```
````

````{py:function} create_entity_descriptor_metadata(entity_descriptor, valid_for=None)
:canonical: SATOSA.metadata_creation.saml_metadata.create_entity_descriptor_metadata

```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata.create_entity_descriptor_metadata
```
````

````{py:function} create_entity_descriptors(satosa_config)
:canonical: SATOSA.metadata_creation.saml_metadata.create_entity_descriptors

```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata.create_entity_descriptors
```
````

````{py:function} create_signed_entities_descriptor(entity_descriptors, security_context, valid_for=None)
:canonical: SATOSA.metadata_creation.saml_metadata.create_signed_entities_descriptor

```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata.create_signed_entities_descriptor
```
````

````{py:function} create_signed_entity_descriptor(entity_descriptor, security_context, valid_for=None)
:canonical: SATOSA.metadata_creation.saml_metadata.create_signed_entity_descriptor

```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata.create_signed_entity_descriptor
```
````

````{py:data} logger
:canonical: SATOSA.metadata_creation.saml_metadata.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.metadata_creation.saml_metadata.logger
```

````
