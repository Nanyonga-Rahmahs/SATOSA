# {py:mod}`SATOSA.util`

```{py:module} SATOSA.util
```

```{autodoc2-docstring} SATOSA.util
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_dict_get_nested <SATOSA.util._dict_get_nested>`
  - ```{autodoc2-docstring} SATOSA.util._dict_get_nested
    :summary:
    ```
* - {py:obj}`_dict_set_nested <SATOSA.util._dict_set_nested>`
  - ```{autodoc2-docstring} SATOSA.util._dict_set_nested
    :summary:
    ```
* - {py:obj}`check_set_dict_defaults <SATOSA.util.check_set_dict_defaults>`
  - ```{autodoc2-docstring} SATOSA.util.check_set_dict_defaults
    :summary:
    ```
* - {py:obj}`get_dict_defaults <SATOSA.util.get_dict_defaults>`
  - ```{autodoc2-docstring} SATOSA.util.get_dict_defaults
    :summary:
    ```
* - {py:obj}`hash_data <SATOSA.util.hash_data>`
  - ```{autodoc2-docstring} SATOSA.util.hash_data
    :summary:
    ```
* - {py:obj}`resolve_nested_key <SATOSA.util.resolve_nested_key>`
  - ```{autodoc2-docstring} SATOSA.util.resolve_nested_key
    :summary:
    ```
* - {py:obj}`rndstr <SATOSA.util.rndstr>`
  - ```{autodoc2-docstring} SATOSA.util.rndstr
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_MISSING <SATOSA.util._MISSING>`
  - ```{autodoc2-docstring} SATOSA.util._MISSING
    :summary:
    ```
* - {py:obj}`logger <SATOSA.util.logger>`
  - ```{autodoc2-docstring} SATOSA.util.logger
    :summary:
    ```
````

### API

````{py:data} _MISSING
:canonical: SATOSA.util._MISSING
:value: >
   'object(...)'

```{autodoc2-docstring} SATOSA.util._MISSING
```

````

````{py:function} _dict_get_nested(dic, keys)
:canonical: SATOSA.util._dict_get_nested

```{autodoc2-docstring} SATOSA.util._dict_get_nested
```
````

````{py:function} _dict_set_nested(dic, keys, value)
:canonical: SATOSA.util._dict_set_nested

```{autodoc2-docstring} SATOSA.util._dict_set_nested
```
````

````{py:function} check_set_dict_defaults(dic, spec)
:canonical: SATOSA.util.check_set_dict_defaults

```{autodoc2-docstring} SATOSA.util.check_set_dict_defaults
```
````

````{py:function} get_dict_defaults(d, *keys)
:canonical: SATOSA.util.get_dict_defaults

```{autodoc2-docstring} SATOSA.util.get_dict_defaults
```
````

````{py:function} hash_data(salt, value, hash_alg=None)
:canonical: SATOSA.util.hash_data

```{autodoc2-docstring} SATOSA.util.hash_data
```
````

````{py:data} logger
:canonical: SATOSA.util.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.util.logger
```

````

````{py:function} resolve_nested_key(key: str, data: typing.Mapping, separator: str = '.') -> typing.Any
:canonical: SATOSA.util.resolve_nested_key

```{autodoc2-docstring} SATOSA.util.resolve_nested_key
```
````

````{py:function} rndstr(size=16, alphabet='')
:canonical: SATOSA.util.rndstr

```{autodoc2-docstring} SATOSA.util.rndstr
```
````
