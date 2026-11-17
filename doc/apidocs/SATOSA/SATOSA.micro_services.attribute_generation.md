# {py:mod}`SATOSA.micro_services.attribute_generation`

```{py:module} SATOSA.micro_services.attribute_generation
```

```{autodoc2-docstring} SATOSA.micro_services.attribute_generation
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AddSyntheticAttributes <SATOSA.micro_services.attribute_generation.AddSyntheticAttributes>`
  - ```{autodoc2-docstring} SATOSA.micro_services.attribute_generation.AddSyntheticAttributes
    :summary:
    ```
* - {py:obj}`MustachAttrValue <SATOSA.micro_services.attribute_generation.MustachAttrValue>`
  - ```{autodoc2-docstring} SATOSA.micro_services.attribute_generation.MustachAttrValue
    :summary:
    ```
````

### API

`````{py:class} AddSyntheticAttributes(config, *args, **kwargs)
:canonical: SATOSA.micro_services.attribute_generation.AddSyntheticAttributes

Bases: {py:obj}`SATOSA.micro_services.base.ResponseMicroService`

```{autodoc2-docstring} SATOSA.micro_services.attribute_generation.AddSyntheticAttributes
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.attribute_generation.AddSyntheticAttributes.__init__
```

````{py:method} _synthesize(attributes, requester, provider)
:canonical: SATOSA.micro_services.attribute_generation.AddSyntheticAttributes._synthesize

```{autodoc2-docstring} SATOSA.micro_services.attribute_generation.AddSyntheticAttributes._synthesize
```

````

````{py:method} process(context, data)
:canonical: SATOSA.micro_services.attribute_generation.AddSyntheticAttributes.process

````

`````

`````{py:class} MustachAttrValue(attr_name, values)
:canonical: SATOSA.micro_services.attribute_generation.MustachAttrValue

Bases: {py:obj}`object`

```{autodoc2-docstring} SATOSA.micro_services.attribute_generation.MustachAttrValue
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.attribute_generation.MustachAttrValue.__init__
```

````{py:method} __str__()
:canonical: SATOSA.micro_services.attribute_generation.MustachAttrValue.__str__

````

````{py:property} first
:canonical: SATOSA.micro_services.attribute_generation.MustachAttrValue.first

```{autodoc2-docstring} SATOSA.micro_services.attribute_generation.MustachAttrValue.first
```

````

````{py:property} scope
:canonical: SATOSA.micro_services.attribute_generation.MustachAttrValue.scope

```{autodoc2-docstring} SATOSA.micro_services.attribute_generation.MustachAttrValue.scope
```

````

````{py:property} value
:canonical: SATOSA.micro_services.attribute_generation.MustachAttrValue.value

```{autodoc2-docstring} SATOSA.micro_services.attribute_generation.MustachAttrValue.value
```

````

````{py:property} values
:canonical: SATOSA.micro_services.attribute_generation.MustachAttrValue.values

```{autodoc2-docstring} SATOSA.micro_services.attribute_generation.MustachAttrValue.values
```

````

`````
