# {py:mod}`SATOSA.internal`

```{py:module} SATOSA.internal
```

```{autodoc2-docstring} SATOSA.internal
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AuthenticationInformation <SATOSA.internal.AuthenticationInformation>`
  - ```{autodoc2-docstring} SATOSA.internal.AuthenticationInformation
    :summary:
    ```
* - {py:obj}`InternalData <SATOSA.internal.InternalData>`
  - ```{autodoc2-docstring} SATOSA.internal.InternalData
    :summary:
    ```
* - {py:obj}`_Datafy <SATOSA.internal._Datafy>`
  -
````

### API

````{py:class} AuthenticationInformation(auth_class_ref=None, timestamp=None, issuer=None, authority=None, *args, **kwargs)
:canonical: SATOSA.internal.AuthenticationInformation

Bases: {py:obj}`SATOSA.internal._Datafy`

```{autodoc2-docstring} SATOSA.internal.AuthenticationInformation
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.internal.AuthenticationInformation.__init__
```

````

````{py:class} InternalData(auth_info=None, requester=None, requester_name=None, subject_id=None, subject_type=None, attributes=None, *args, **kwargs)
:canonical: SATOSA.internal.InternalData

Bases: {py:obj}`SATOSA.internal._Datafy`

```{autodoc2-docstring} SATOSA.internal.InternalData
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.internal.InternalData.__init__
```

````

`````{py:class} _Datafy(dict=None, /, **kwargs)
:canonical: SATOSA.internal._Datafy

Bases: {py:obj}`collections.UserDict`

````{py:attribute} _DEPRECATED_TO_NEW_MEMBERS
:canonical: SATOSA.internal._Datafy._DEPRECATED_TO_NEW_MEMBERS
:value: >
   None

```{autodoc2-docstring} SATOSA.internal._Datafy._DEPRECATED_TO_NEW_MEMBERS
```

````

````{py:method} __getattr__(key)
:canonical: SATOSA.internal._Datafy.__getattr__

```{autodoc2-docstring} SATOSA.internal._Datafy.__getattr__
```

````

````{py:method} __getitem__(key)
:canonical: SATOSA.internal._Datafy.__getitem__

```{autodoc2-docstring} SATOSA.internal._Datafy.__getitem__
```

````

````{py:method} __setattr__(key, value)
:canonical: SATOSA.internal._Datafy.__setattr__

````

````{py:method} __setitem__(key, value)
:canonical: SATOSA.internal._Datafy.__setitem__

```{autodoc2-docstring} SATOSA.internal._Datafy.__setitem__
```

````

````{py:method} _get_new_key(old_key)
:canonical: SATOSA.internal._Datafy._get_new_key

```{autodoc2-docstring} SATOSA.internal._Datafy._get_new_key
```

````

````{py:method} from_dict(data)
:canonical: SATOSA.internal._Datafy.from_dict
:classmethod:

```{autodoc2-docstring} SATOSA.internal._Datafy.from_dict
```

````

````{py:method} to_dict()
:canonical: SATOSA.internal._Datafy.to_dict

```{autodoc2-docstring} SATOSA.internal._Datafy.to_dict
```

````

`````
