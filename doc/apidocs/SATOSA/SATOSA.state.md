# {py:mod}`SATOSA.state`

```{py:module} SATOSA.state
```

```{autodoc2-docstring} SATOSA.state
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`State <SATOSA.state.State>`
  - ```{autodoc2-docstring} SATOSA.state.State
    :summary:
    ```
* - {py:obj}`_AESCipher <SATOSA.state._AESCipher>`
  - ```{autodoc2-docstring} SATOSA.state._AESCipher
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`cookie_to_state <SATOSA.state.cookie_to_state>`
  - ```{autodoc2-docstring} SATOSA.state.cookie_to_state
    :summary:
    ```
* - {py:obj}`state_to_cookie <SATOSA.state.state_to_cookie>`
  - ```{autodoc2-docstring} SATOSA.state.state_to_cookie
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_SESSION_ID_KEY <SATOSA.state._SESSION_ID_KEY>`
  - ```{autodoc2-docstring} SATOSA.state._SESSION_ID_KEY
    :summary:
    ```
* - {py:obj}`logger <SATOSA.state.logger>`
  - ```{autodoc2-docstring} SATOSA.state.logger
    :summary:
    ```
````

### API

`````{py:class} State(urlstate_data=None, encryption_key=None)
:canonical: SATOSA.state.State

Bases: {py:obj}`collections.UserDict`

```{autodoc2-docstring} SATOSA.state.State
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.state.State.__init__
```

````{py:method} copy()
:canonical: SATOSA.state.State.copy

```{autodoc2-docstring} SATOSA.state.State.copy
```

````

````{py:property} session_id
:canonical: SATOSA.state.State.session_id

```{autodoc2-docstring} SATOSA.state.State.session_id
```

````

````{py:property} state_dict
:canonical: SATOSA.state.State.state_dict

```{autodoc2-docstring} SATOSA.state.State.state_dict
```

````

````{py:method} urlstate(encryption_key)
:canonical: SATOSA.state.State.urlstate

```{autodoc2-docstring} SATOSA.state.State.urlstate
```

````

`````

`````{py:class} _AESCipher(key)
:canonical: SATOSA.state._AESCipher

Bases: {py:obj}`object`

```{autodoc2-docstring} SATOSA.state._AESCipher
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.state._AESCipher.__init__
```

````{py:method} _pad(b)
:canonical: SATOSA.state._AESCipher._pad

```{autodoc2-docstring} SATOSA.state._AESCipher._pad
```

````

````{py:method} _unpad(b)
:canonical: SATOSA.state._AESCipher._unpad
:staticmethod:

```{autodoc2-docstring} SATOSA.state._AESCipher._unpad
```

````

````{py:method} decrypt(enc)
:canonical: SATOSA.state._AESCipher.decrypt

```{autodoc2-docstring} SATOSA.state._AESCipher.decrypt
```

````

````{py:method} encrypt(raw)
:canonical: SATOSA.state._AESCipher.encrypt

```{autodoc2-docstring} SATOSA.state._AESCipher.encrypt
```

````

`````

````{py:data} _SESSION_ID_KEY
:canonical: SATOSA.state._SESSION_ID_KEY
:value: >
   'SESSION_ID'

```{autodoc2-docstring} SATOSA.state._SESSION_ID_KEY
```

````

````{py:function} cookie_to_state(cookie_str: str, name: str, encryption_key: str) -> SATOSA.state.State
:canonical: SATOSA.state.cookie_to_state

```{autodoc2-docstring} SATOSA.state.cookie_to_state
```
````

````{py:data} logger
:canonical: SATOSA.state.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.state.logger
```

````

````{py:function} state_to_cookie(state: SATOSA.state.State, *, name: str, path: str, encryption_key: str, secure: bool = None, httponly: bool = None, samesite: str = None, max_age: str = None) -> satosa.cookies.SimpleCookie
:canonical: SATOSA.state.state_to_cookie

```{autodoc2-docstring} SATOSA.state.state_to_cookie
```
````
