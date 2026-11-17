# {py:mod}`tests.satosa.test_state`

```{py:module} tests.satosa.test_state
```

```{autodoc2-docstring} tests.satosa.test_state
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestState <tests.satosa.test_state.TestState>`
  - ```{autodoc2-docstring} tests.satosa.test_state.TestState
    :summary:
    ```
* - {py:obj}`TestStateAsCookie <tests.satosa.test_state.TestStateAsCookie>`
  - ```{autodoc2-docstring} tests.satosa.test_state.TestStateAsCookie
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`get_dict <tests.satosa.test_state.get_dict>`
  - ```{autodoc2-docstring} tests.satosa.test_state.get_dict
    :summary:
    ```
* - {py:obj}`get_str <tests.satosa.test_state.get_str>`
  - ```{autodoc2-docstring} tests.satosa.test_state.get_str
    :summary:
    ```
````

### API

`````{py:class} TestState
:canonical: tests.satosa.test_state.TestState

```{autodoc2-docstring} tests.satosa.test_state.TestState
```

````{py:method} test_contains()
:canonical: tests.satosa.test_state.TestState.test_contains

```{autodoc2-docstring} tests.satosa.test_state.TestState.test_contains
```

````

````{py:method} test_urlstate_length_should_fit_in_browser_cookie()
:canonical: tests.satosa.test_state.TestState.test_urlstate_length_should_fit_in_browser_cookie

```{autodoc2-docstring} tests.satosa.test_state.TestState.test_urlstate_length_should_fit_in_browser_cookie
```

````

`````

`````{py:class} TestStateAsCookie
:canonical: tests.satosa.test_state.TestStateAsCookie

```{autodoc2-docstring} tests.satosa.test_state.TestStateAsCookie
```

````{py:method} test_cookie_to_state_handle_broken_cookies(cookie_str, name, encryption_key, expected_exception)
:canonical: tests.satosa.test_state.TestStateAsCookie.test_cookie_to_state_handle_broken_cookies

```{autodoc2-docstring} tests.satosa.test_state.TestStateAsCookie.test_cookie_to_state_handle_broken_cookies
```

````

````{py:method} test_encode_decode_of_state()
:canonical: tests.satosa.test_state.TestStateAsCookie.test_encode_decode_of_state

```{autodoc2-docstring} tests.satosa.test_state.TestStateAsCookie.test_encode_decode_of_state
```

````

````{py:method} test_state_to_cookie_produces_cookie_without_max_age_for_state_that_should_be_deleted()
:canonical: tests.satosa.test_state.TestStateAsCookie.test_state_to_cookie_produces_cookie_without_max_age_for_state_that_should_be_deleted

```{autodoc2-docstring} tests.satosa.test_state.TestStateAsCookie.test_state_to_cookie_produces_cookie_without_max_age_for_state_that_should_be_deleted
```

````

`````

````{py:function} get_dict(size, key_prefix, value_preix)
:canonical: tests.satosa.test_state.get_dict

```{autodoc2-docstring} tests.satosa.test_state.get_dict
```
````

````{py:function} get_str(length)
:canonical: tests.satosa.test_state.get_str

```{autodoc2-docstring} tests.satosa.test_state.get_str
```
````
