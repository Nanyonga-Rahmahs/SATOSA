# {py:mod}`SATOSA.attribute_mapping`

```{py:module} SATOSA.attribute_mapping
```

```{autodoc2-docstring} SATOSA.attribute_mapping
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AttributeMapper <SATOSA.attribute_mapping.AttributeMapper>`
  - ```{autodoc2-docstring} SATOSA.attribute_mapping.AttributeMapper
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`scope <SATOSA.attribute_mapping.scope>`
  - ```{autodoc2-docstring} SATOSA.attribute_mapping.scope
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.attribute_mapping.logger>`
  - ```{autodoc2-docstring} SATOSA.attribute_mapping.logger
    :summary:
    ```
````

### API

`````{py:class} AttributeMapper(internal_attributes)
:canonical: SATOSA.attribute_mapping.AttributeMapper

Bases: {py:obj}`object`

```{autodoc2-docstring} SATOSA.attribute_mapping.AttributeMapper
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.attribute_mapping.AttributeMapper.__init__
```

````{py:method} _collate_attribute_values_by_priority_order(attribute_names, data)
:canonical: SATOSA.attribute_mapping.AttributeMapper._collate_attribute_values_by_priority_order

```{autodoc2-docstring} SATOSA.attribute_mapping.AttributeMapper._collate_attribute_values_by_priority_order
```

````

````{py:method} _create_nested_attribute_value(nested_attribute_names, value)
:canonical: SATOSA.attribute_mapping.AttributeMapper._create_nested_attribute_value

```{autodoc2-docstring} SATOSA.attribute_mapping.AttributeMapper._create_nested_attribute_value
```

````

````{py:method} _handle_template_attributes(attribute_profile, internal_dict)
:canonical: SATOSA.attribute_mapping.AttributeMapper._handle_template_attributes

```{autodoc2-docstring} SATOSA.attribute_mapping.AttributeMapper._handle_template_attributes
```

````

````{py:method} _is_nested_attribute_name(attribute_name)
:canonical: SATOSA.attribute_mapping.AttributeMapper._is_nested_attribute_name

```{autodoc2-docstring} SATOSA.attribute_mapping.AttributeMapper._is_nested_attribute_name
```

````

````{py:method} _render_attribute_template(template, data)
:canonical: SATOSA.attribute_mapping.AttributeMapper._render_attribute_template

```{autodoc2-docstring} SATOSA.attribute_mapping.AttributeMapper._render_attribute_template
```

````

````{py:method} from_internal(attribute_profile, internal_dict)
:canonical: SATOSA.attribute_mapping.AttributeMapper.from_internal

```{autodoc2-docstring} SATOSA.attribute_mapping.AttributeMapper.from_internal
```

````

````{py:method} to_internal(attribute_profile, external_dict)
:canonical: SATOSA.attribute_mapping.AttributeMapper.to_internal

```{autodoc2-docstring} SATOSA.attribute_mapping.AttributeMapper.to_internal
```

````

````{py:method} to_internal_filter(attribute_profile, external_attribute_names)
:canonical: SATOSA.attribute_mapping.AttributeMapper.to_internal_filter

```{autodoc2-docstring} SATOSA.attribute_mapping.AttributeMapper.to_internal_filter
```

````

`````

````{py:data} logger
:canonical: SATOSA.attribute_mapping.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.attribute_mapping.logger
```

````

````{py:function} scope(s)
:canonical: SATOSA.attribute_mapping.scope

```{autodoc2-docstring} SATOSA.attribute_mapping.scope
```
````
