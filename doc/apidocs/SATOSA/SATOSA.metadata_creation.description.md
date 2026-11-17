# {py:mod}`SATOSA.metadata_creation.description`

```{py:module} SATOSA.metadata_creation.description
```

```{autodoc2-docstring} SATOSA.metadata_creation.description
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ContactPersonDesc <SATOSA.metadata_creation.description.ContactPersonDesc>`
  - ```{autodoc2-docstring} SATOSA.metadata_creation.description.ContactPersonDesc
    :summary:
    ```
* - {py:obj}`MetadataDescription <SATOSA.metadata_creation.description.MetadataDescription>`
  - ```{autodoc2-docstring} SATOSA.metadata_creation.description.MetadataDescription
    :summary:
    ```
* - {py:obj}`OrganizationDesc <SATOSA.metadata_creation.description.OrganizationDesc>`
  - ```{autodoc2-docstring} SATOSA.metadata_creation.description.OrganizationDesc
    :summary:
    ```
* - {py:obj}`UIInfoDesc <SATOSA.metadata_creation.description.UIInfoDesc>`
  - ```{autodoc2-docstring} SATOSA.metadata_creation.description.UIInfoDesc
    :summary:
    ```
````

### API

`````{py:class} ContactPersonDesc()
:canonical: SATOSA.metadata_creation.description.ContactPersonDesc

Bases: {py:obj}`object`

```{autodoc2-docstring} SATOSA.metadata_creation.description.ContactPersonDesc
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.metadata_creation.description.ContactPersonDesc.__init__
```

````{py:method} add_email_address(address)
:canonical: SATOSA.metadata_creation.description.ContactPersonDesc.add_email_address

```{autodoc2-docstring} SATOSA.metadata_creation.description.ContactPersonDesc.add_email_address
```

````

````{py:method} to_dict()
:canonical: SATOSA.metadata_creation.description.ContactPersonDesc.to_dict

```{autodoc2-docstring} SATOSA.metadata_creation.description.ContactPersonDesc.to_dict
```

````

`````

`````{py:class} MetadataDescription(entity_id)
:canonical: SATOSA.metadata_creation.description.MetadataDescription

Bases: {py:obj}`object`

```{autodoc2-docstring} SATOSA.metadata_creation.description.MetadataDescription
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.metadata_creation.description.MetadataDescription.__init__
```

````{py:method} add_contact_person(person)
:canonical: SATOSA.metadata_creation.description.MetadataDescription.add_contact_person

```{autodoc2-docstring} SATOSA.metadata_creation.description.MetadataDescription.add_contact_person
```

````

````{py:method} organization(organization)
:canonical: SATOSA.metadata_creation.description.MetadataDescription.organization

```{autodoc2-docstring} SATOSA.metadata_creation.description.MetadataDescription.organization
```

````

````{py:method} to_dict()
:canonical: SATOSA.metadata_creation.description.MetadataDescription.to_dict

```{autodoc2-docstring} SATOSA.metadata_creation.description.MetadataDescription.to_dict
```

````

````{py:method} ui_info(ui_info)
:canonical: SATOSA.metadata_creation.description.MetadataDescription.ui_info

```{autodoc2-docstring} SATOSA.metadata_creation.description.MetadataDescription.ui_info
```

````

`````

`````{py:class} OrganizationDesc()
:canonical: SATOSA.metadata_creation.description.OrganizationDesc

Bases: {py:obj}`object`

```{autodoc2-docstring} SATOSA.metadata_creation.description.OrganizationDesc
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.metadata_creation.description.OrganizationDesc.__init__
```

````{py:method} add_display_name(name, lang)
:canonical: SATOSA.metadata_creation.description.OrganizationDesc.add_display_name

```{autodoc2-docstring} SATOSA.metadata_creation.description.OrganizationDesc.add_display_name
```

````

````{py:method} add_name(name, lang)
:canonical: SATOSA.metadata_creation.description.OrganizationDesc.add_name

```{autodoc2-docstring} SATOSA.metadata_creation.description.OrganizationDesc.add_name
```

````

````{py:method} add_url(url, lang)
:canonical: SATOSA.metadata_creation.description.OrganizationDesc.add_url

```{autodoc2-docstring} SATOSA.metadata_creation.description.OrganizationDesc.add_url
```

````

````{py:method} to_dict()
:canonical: SATOSA.metadata_creation.description.OrganizationDesc.to_dict

```{autodoc2-docstring} SATOSA.metadata_creation.description.OrganizationDesc.to_dict
```

````

`````

`````{py:class} UIInfoDesc()
:canonical: SATOSA.metadata_creation.description.UIInfoDesc

Bases: {py:obj}`object`

```{autodoc2-docstring} SATOSA.metadata_creation.description.UIInfoDesc
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.metadata_creation.description.UIInfoDesc.__init__
```

````{py:method} add_description(text, lang)
:canonical: SATOSA.metadata_creation.description.UIInfoDesc.add_description

```{autodoc2-docstring} SATOSA.metadata_creation.description.UIInfoDesc.add_description
```

````

````{py:method} add_display_name(text, lang)
:canonical: SATOSA.metadata_creation.description.UIInfoDesc.add_display_name

```{autodoc2-docstring} SATOSA.metadata_creation.description.UIInfoDesc.add_display_name
```

````

````{py:method} add_information_url(text, lang)
:canonical: SATOSA.metadata_creation.description.UIInfoDesc.add_information_url

```{autodoc2-docstring} SATOSA.metadata_creation.description.UIInfoDesc.add_information_url
```

````

````{py:method} add_keywords(text, lang)
:canonical: SATOSA.metadata_creation.description.UIInfoDesc.add_keywords

```{autodoc2-docstring} SATOSA.metadata_creation.description.UIInfoDesc.add_keywords
```

````

````{py:method} add_logo(text, width, height, lang=None)
:canonical: SATOSA.metadata_creation.description.UIInfoDesc.add_logo

```{autodoc2-docstring} SATOSA.metadata_creation.description.UIInfoDesc.add_logo
```

````

````{py:method} add_privacy_statement_url(text, lang)
:canonical: SATOSA.metadata_creation.description.UIInfoDesc.add_privacy_statement_url

```{autodoc2-docstring} SATOSA.metadata_creation.description.UIInfoDesc.add_privacy_statement_url
```

````

````{py:method} to_dict()
:canonical: SATOSA.metadata_creation.description.UIInfoDesc.to_dict

```{autodoc2-docstring} SATOSA.metadata_creation.description.UIInfoDesc.to_dict
```

````

`````
