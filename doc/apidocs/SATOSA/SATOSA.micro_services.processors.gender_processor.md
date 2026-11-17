# {py:mod}`SATOSA.micro_services.processors.gender_processor`

```{py:module} SATOSA.micro_services.processors.gender_processor
```

```{autodoc2-docstring} SATOSA.micro_services.processors.gender_processor
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Gender <SATOSA.micro_services.processors.gender_processor.Gender>`
  -
* - {py:obj}`GenderToSchacProcessor <SATOSA.micro_services.processors.gender_processor.GenderToSchacProcessor>`
  - ```{autodoc2-docstring} SATOSA.micro_services.processors.gender_processor.GenderToSchacProcessor
    :summary:
    ```
````

### API

`````{py:class} Gender(*args, **kwds)
:canonical: SATOSA.micro_services.processors.gender_processor.Gender

Bases: {py:obj}`enum.Enum`

````{py:attribute} FEMALE
:canonical: SATOSA.micro_services.processors.gender_processor.Gender.FEMALE
:value: >
   2

```{autodoc2-docstring} SATOSA.micro_services.processors.gender_processor.Gender.FEMALE
```

````

````{py:attribute} MALE
:canonical: SATOSA.micro_services.processors.gender_processor.Gender.MALE
:value: >
   1

```{autodoc2-docstring} SATOSA.micro_services.processors.gender_processor.Gender.MALE
```

````

````{py:attribute} NOT_KNOWN
:canonical: SATOSA.micro_services.processors.gender_processor.Gender.NOT_KNOWN
:value: >
   0

```{autodoc2-docstring} SATOSA.micro_services.processors.gender_processor.Gender.NOT_KNOWN
```

````

````{py:attribute} NOT_SPECIFIED
:canonical: SATOSA.micro_services.processors.gender_processor.Gender.NOT_SPECIFIED
:value: >
   9

```{autodoc2-docstring} SATOSA.micro_services.processors.gender_processor.Gender.NOT_SPECIFIED
```

````

`````

`````{py:class} GenderToSchacProcessor()
:canonical: SATOSA.micro_services.processors.gender_processor.GenderToSchacProcessor

Bases: {py:obj}`SATOSA.micro_services.processors.base_processor.BaseProcessor`

```{autodoc2-docstring} SATOSA.micro_services.processors.gender_processor.GenderToSchacProcessor
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.processors.gender_processor.GenderToSchacProcessor.__init__
```

````{py:method} process(internal_data, attribute, **kwargs)
:canonical: SATOSA.micro_services.processors.gender_processor.GenderToSchacProcessor.process

```{autodoc2-docstring} SATOSA.micro_services.processors.gender_processor.GenderToSchacProcessor.process
```

````

`````
