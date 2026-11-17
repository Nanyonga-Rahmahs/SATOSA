# {py:mod}`SATOSA.micro_services.attribute_processor`

```{py:module} SATOSA.micro_services.attribute_processor
```

```{autodoc2-docstring} SATOSA.micro_services.attribute_processor
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AttributeProcessor <SATOSA.micro_services.attribute_processor.AttributeProcessor>`
  - ```{autodoc2-docstring} SATOSA.micro_services.attribute_processor.AttributeProcessor
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CONFIG_KEY_ATTRIBUTE <SATOSA.micro_services.attribute_processor.CONFIG_KEY_ATTRIBUTE>`
  - ```{autodoc2-docstring} SATOSA.micro_services.attribute_processor.CONFIG_KEY_ATTRIBUTE
    :summary:
    ```
* - {py:obj}`CONFIG_KEY_CLASSNAME <SATOSA.micro_services.attribute_processor.CONFIG_KEY_CLASSNAME>`
  - ```{autodoc2-docstring} SATOSA.micro_services.attribute_processor.CONFIG_KEY_CLASSNAME
    :summary:
    ```
* - {py:obj}`CONFIG_KEY_MODULE <SATOSA.micro_services.attribute_processor.CONFIG_KEY_MODULE>`
  - ```{autodoc2-docstring} SATOSA.micro_services.attribute_processor.CONFIG_KEY_MODULE
    :summary:
    ```
* - {py:obj}`CONFIG_KEY_PROCESSORS <SATOSA.micro_services.attribute_processor.CONFIG_KEY_PROCESSORS>`
  - ```{autodoc2-docstring} SATOSA.micro_services.attribute_processor.CONFIG_KEY_PROCESSORS
    :summary:
    ```
* - {py:obj}`CONFIG_KEY_ROOT <SATOSA.micro_services.attribute_processor.CONFIG_KEY_ROOT>`
  - ```{autodoc2-docstring} SATOSA.micro_services.attribute_processor.CONFIG_KEY_ROOT
    :summary:
    ```
* - {py:obj}`logger <SATOSA.micro_services.attribute_processor.logger>`
  - ```{autodoc2-docstring} SATOSA.micro_services.attribute_processor.logger
    :summary:
    ```
````

### API

`````{py:class} AttributeProcessor(config, *args, **kwargs)
:canonical: SATOSA.micro_services.attribute_processor.AttributeProcessor

Bases: {py:obj}`satosa.micro_services.base.ResponseMicroService`

```{autodoc2-docstring} SATOSA.micro_services.attribute_processor.AttributeProcessor
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.micro_services.attribute_processor.AttributeProcessor.__init__
```

````{py:method} process(context, data)
:canonical: SATOSA.micro_services.attribute_processor.AttributeProcessor.process

````

`````

```{py:exception} AttributeProcessorError()
:canonical: SATOSA.micro_services.attribute_processor.AttributeProcessorError

Bases: {py:obj}`satosa.exception.SATOSAError`

```

```{py:exception} AttributeProcessorWarning()
:canonical: SATOSA.micro_services.attribute_processor.AttributeProcessorWarning

Bases: {py:obj}`satosa.exception.SATOSAError`

```

````{py:data} CONFIG_KEY_ATTRIBUTE
:canonical: SATOSA.micro_services.attribute_processor.CONFIG_KEY_ATTRIBUTE
:value: >
   'attribute'

```{autodoc2-docstring} SATOSA.micro_services.attribute_processor.CONFIG_KEY_ATTRIBUTE
```

````

````{py:data} CONFIG_KEY_CLASSNAME
:canonical: SATOSA.micro_services.attribute_processor.CONFIG_KEY_CLASSNAME
:value: >
   'name'

```{autodoc2-docstring} SATOSA.micro_services.attribute_processor.CONFIG_KEY_CLASSNAME
```

````

````{py:data} CONFIG_KEY_MODULE
:canonical: SATOSA.micro_services.attribute_processor.CONFIG_KEY_MODULE
:value: >
   'module'

```{autodoc2-docstring} SATOSA.micro_services.attribute_processor.CONFIG_KEY_MODULE
```

````

````{py:data} CONFIG_KEY_PROCESSORS
:canonical: SATOSA.micro_services.attribute_processor.CONFIG_KEY_PROCESSORS
:value: >
   'processors'

```{autodoc2-docstring} SATOSA.micro_services.attribute_processor.CONFIG_KEY_PROCESSORS
```

````

````{py:data} CONFIG_KEY_ROOT
:canonical: SATOSA.micro_services.attribute_processor.CONFIG_KEY_ROOT
:value: >
   'process'

```{autodoc2-docstring} SATOSA.micro_services.attribute_processor.CONFIG_KEY_ROOT
```

````

````{py:data} logger
:canonical: SATOSA.micro_services.attribute_processor.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.micro_services.attribute_processor.logger
```

````
