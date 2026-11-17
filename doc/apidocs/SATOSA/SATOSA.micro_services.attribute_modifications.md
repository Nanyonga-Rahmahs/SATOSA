# {py:mod}`SATOSA.micro_services.attribute_modifications`

```{py:module} SATOSA.micro_services.attribute_modifications
```

```{autodoc2-docstring} SATOSA.micro_services.attribute_modifications
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AddStaticAttributes <SATOSA.micro_services.attribute_modifications.AddStaticAttributes>`
  - ```{autodoc2-docstring} SATOSA.micro_services.attribute_modifications.AddStaticAttributes
    :summary:
    ```
* - {py:obj}`FilterAttributeValues <SATOSA.micro_services.attribute_modifications.FilterAttributeValues>`
  - ```{autodoc2-docstring} SATOSA.micro_services.attribute_modifications.FilterAttributeValues
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.micro_services.attribute_modifications.logger>`
  - ```{autodoc2-docstring} SATOSA.micro_services.attribute_modifications.logger
    :summary:
    ```
````

### API

`````{py:class} AddStaticAttributes(config, *args, **kwargs)
:canonical: SATOSA.micro_services.attribute_modifications.AddStaticAttributes

Bases: {py:obj}`SATOSA.micro_services.base.ResponseMicroService`

```{autodoc2-docstring} SATOSA.micro_services.attribute_modifications.AddStaticAttributes
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.attribute_modifications.AddStaticAttributes.__init__
```

````{py:method} process(context, data)
:canonical: SATOSA.micro_services.attribute_modifications.AddStaticAttributes.process

````

`````

`````{py:class} FilterAttributeValues(config, *args, **kwargs)
:canonical: SATOSA.micro_services.attribute_modifications.FilterAttributeValues

Bases: {py:obj}`SATOSA.micro_services.base.ResponseMicroService`

```{autodoc2-docstring} SATOSA.micro_services.attribute_modifications.FilterAttributeValues
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.attribute_modifications.FilterAttributeValues.__init__
```

````{py:method} _apply_filters(attributes, attribute_filters, context, target_provider)
:canonical: SATOSA.micro_services.attribute_modifications.FilterAttributeValues._apply_filters

```{autodoc2-docstring} SATOSA.micro_services.attribute_modifications.FilterAttributeValues._apply_filters
```

````

````{py:method} _apply_requester_filters(attributes, provider_filters, requester, context, target_provider)
:canonical: SATOSA.micro_services.attribute_modifications.FilterAttributeValues._apply_requester_filters

```{autodoc2-docstring} SATOSA.micro_services.attribute_modifications.FilterAttributeValues._apply_requester_filters
```

````

````{py:method} _shibmdscope_match_scope(value, md_scopes)
:canonical: SATOSA.micro_services.attribute_modifications.FilterAttributeValues._shibmdscope_match_scope

```{autodoc2-docstring} SATOSA.micro_services.attribute_modifications.FilterAttributeValues._shibmdscope_match_scope
```

````

````{py:method} _shibmdscope_match_value(value, md_scopes)
:canonical: SATOSA.micro_services.attribute_modifications.FilterAttributeValues._shibmdscope_match_value

```{autodoc2-docstring} SATOSA.micro_services.attribute_modifications.FilterAttributeValues._shibmdscope_match_value
```

````

````{py:method} process(context, data)
:canonical: SATOSA.micro_services.attribute_modifications.FilterAttributeValues.process

````

`````

````{py:data} logger
:canonical: SATOSA.micro_services.attribute_modifications.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.micro_services.attribute_modifications.logger
```

````
