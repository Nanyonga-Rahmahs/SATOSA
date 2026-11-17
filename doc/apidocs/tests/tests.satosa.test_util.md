# {py:mod}`tests.satosa.test_util`

```{py:module} tests.satosa.test_util
```

```{autodoc2-docstring} tests.satosa.test_util
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestResolveNestedKey <tests.satosa.test_util.TestResolveNestedKey>`
  - ```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKey
    :summary:
    ```
* - {py:obj}`TestResolveNestedKeyBacktracking <tests.satosa.test_util.TestResolveNestedKeyBacktracking>`
  - ```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyBacktracking
    :summary:
    ```
* - {py:obj}`TestResolveNestedKeyFalsyValues <tests.satosa.test_util.TestResolveNestedKeyFalsyValues>`
  - ```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyFalsyValues
    :summary:
    ```
* - {py:obj}`TestResolveNestedKeyPreferenceOrder <tests.satosa.test_util.TestResolveNestedKeyPreferenceOrder>`
  - ```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyPreferenceOrder
    :summary:
    ```
* - {py:obj}`TestResolveNestedKeyUnresolvable <tests.satosa.test_util.TestResolveNestedKeyUnresolvable>`
  - ```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyUnresolvable
    :summary:
    ```
* - {py:obj}`TestResolveNestedKeyWithLiteralSeparator <tests.satosa.test_util.TestResolveNestedKeyWithLiteralSeparator>`
  - ```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyWithLiteralSeparator
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_build_data <tests.satosa.test_util._build_data>`
  - ```{autodoc2-docstring} tests.satosa.test_util._build_data
    :summary:
    ```
* - {py:obj}`_compositions <tests.satosa.test_util._compositions>`
  - ```{autodoc2-docstring} tests.satosa.test_util._compositions
    :summary:
    ```
* - {py:obj}`_every_data_shape <tests.satosa.test_util._every_data_shape>`
  - ```{autodoc2-docstring} tests.satosa.test_util._every_data_shape
    :summary:
    ```
````

### API

`````{py:class} TestResolveNestedKey
:canonical: tests.satosa.test_util.TestResolveNestedKey

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKey
```

````{py:method} test_any_mapping_type_is_traversed(mapping_type)
:canonical: tests.satosa.test_util.TestResolveNestedKey.test_any_mapping_type_is_traversed

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKey.test_any_mapping_type_is_traversed
```

````

````{py:method} test_custom_separator()
:canonical: tests.satosa.test_util.TestResolveNestedKey.test_custom_separator

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKey.test_custom_separator
```

````

````{py:method} test_deeply_nested_key()
:canonical: tests.satosa.test_util.TestResolveNestedKey.test_deeply_nested_key

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKey.test_deeply_nested_key
```

````

````{py:method} test_flat_key()
:canonical: tests.satosa.test_util.TestResolveNestedKey.test_flat_key

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKey.test_flat_key
```

````

````{py:method} test_key_path_resolving_to_a_mapping()
:canonical: tests.satosa.test_util.TestResolveNestedKey.test_key_path_resolving_to_a_mapping

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKey.test_key_path_resolving_to_a_mapping
```

````

````{py:method} test_long_key_path()
:canonical: tests.satosa.test_util.TestResolveNestedKey.test_long_key_path

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKey.test_long_key_path
```

````

````{py:method} test_nested_key()
:canonical: tests.satosa.test_util.TestResolveNestedKey.test_nested_key

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKey.test_nested_key
```

````

````{py:method} test_separator_that_is_not_present_in_the_key()
:canonical: tests.satosa.test_util.TestResolveNestedKey.test_separator_that_is_not_present_in_the_key

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKey.test_separator_that_is_not_present_in_the_key
```

````

`````

`````{py:class} TestResolveNestedKeyBacktracking
:canonical: tests.satosa.test_util.TestResolveNestedKeyBacktracking

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyBacktracking
```

````{py:method} test_backtracks_out_of_a_non_mapping_dead_end()
:canonical: tests.satosa.test_util.TestResolveNestedKeyBacktracking.test_backtracks_out_of_a_non_mapping_dead_end

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyBacktracking.test_backtracks_out_of_a_non_mapping_dead_end
```

````

````{py:method} test_backtracks_over_several_levels()
:canonical: tests.satosa.test_util.TestResolveNestedKeyBacktracking.test_backtracks_over_several_levels

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyBacktracking.test_backtracks_over_several_levels
```

````

````{py:method} test_backtracks_to_the_whole_key_as_a_last_resort()
:canonical: tests.satosa.test_util.TestResolveNestedKeyBacktracking.test_backtracks_to_the_whole_key_as_a_last_resort

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyBacktracking.test_backtracks_to_the_whole_key_as_a_last_resort
```

````

````{py:method} test_backtracks_when_the_deepest_match_dead_ends()
:canonical: tests.satosa.test_util.TestResolveNestedKeyBacktracking.test_backtracks_when_the_deepest_match_dead_ends

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyBacktracking.test_backtracks_when_the_deepest_match_dead_ends
```

````

`````

`````{py:class} TestResolveNestedKeyFalsyValues
:canonical: tests.satosa.test_util.TestResolveNestedKeyFalsyValues

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyFalsyValues
```

````{py:method} test_falsy_nested_value_is_returned(value)
:canonical: tests.satosa.test_util.TestResolveNestedKeyFalsyValues.test_falsy_nested_value_is_returned

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyFalsyValues.test_falsy_nested_value_is_returned
```

````

````{py:method} test_falsy_whole_key_value_is_returned(value)
:canonical: tests.satosa.test_util.TestResolveNestedKeyFalsyValues.test_falsy_whole_key_value_is_returned

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyFalsyValues.test_falsy_whole_key_value_is_returned
```

````

````{py:method} test_falsy_whole_key_value_wins_over_the_nested_path()
:canonical: tests.satosa.test_util.TestResolveNestedKeyFalsyValues.test_falsy_whole_key_value_wins_over_the_nested_path

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyFalsyValues.test_falsy_whole_key_value_wins_over_the_nested_path
```

````

````{py:method} test_stored_none_resolves_to_none()
:canonical: tests.satosa.test_util.TestResolveNestedKeyFalsyValues.test_stored_none_resolves_to_none

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyFalsyValues.test_stored_none_resolves_to_none
```

````

`````

`````{py:class} TestResolveNestedKeyPreferenceOrder
:canonical: tests.satosa.test_util.TestResolveNestedKeyPreferenceOrder

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyPreferenceOrder
```

````{py:method} test_deepest_match_is_preferred()
:canonical: tests.satosa.test_util.TestResolveNestedKeyPreferenceOrder.test_deepest_match_is_preferred

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyPreferenceOrder.test_deepest_match_is_preferred
```

````

````{py:method} test_deepest_match_is_preferred_over_a_shallower_one()
:canonical: tests.satosa.test_util.TestResolveNestedKeyPreferenceOrder.test_deepest_match_is_preferred_over_a_shallower_one

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyPreferenceOrder.test_deepest_match_is_preferred_over_a_shallower_one
```

````

````{py:method} test_whole_key_only_wins_at_the_top_level()
:canonical: tests.satosa.test_util.TestResolveNestedKeyPreferenceOrder.test_whole_key_only_wins_at_the_top_level

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyPreferenceOrder.test_whole_key_only_wins_at_the_top_level
```

````

````{py:method} test_whole_key_wins_over_the_nested_path()
:canonical: tests.satosa.test_util.TestResolveNestedKeyPreferenceOrder.test_whole_key_wins_over_the_nested_path

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyPreferenceOrder.test_whole_key_wins_over_the_nested_path
```

````

`````

`````{py:class} TestResolveNestedKeyUnresolvable
:canonical: tests.satosa.test_util.TestResolveNestedKeyUnresolvable

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyUnresolvable
```

````{py:method} test_non_mapping_data()
:canonical: tests.satosa.test_util.TestResolveNestedKeyUnresolvable.test_non_mapping_data

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyUnresolvable.test_non_mapping_data
```

````

````{py:method} test_returns_none(key, data)
:canonical: tests.satosa.test_util.TestResolveNestedKeyUnresolvable.test_returns_none

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyUnresolvable.test_returns_none
```

````

`````

`````{py:class} TestResolveNestedKeyWithLiteralSeparator
:canonical: tests.satosa.test_util.TestResolveNestedKeyWithLiteralSeparator

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyWithLiteralSeparator
```

````{py:method} test_literal_separator_below_the_top_level()
:canonical: tests.satosa.test_util.TestResolveNestedKeyWithLiteralSeparator.test_literal_separator_below_the_top_level

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyWithLiteralSeparator.test_literal_separator_below_the_top_level
```

````

````{py:method} test_literal_separator_in_the_last_key()
:canonical: tests.satosa.test_util.TestResolveNestedKeyWithLiteralSeparator.test_literal_separator_in_the_last_key

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyWithLiteralSeparator.test_literal_separator_in_the_last_key
```

````

````{py:method} test_several_literal_separators()
:canonical: tests.satosa.test_util.TestResolveNestedKeyWithLiteralSeparator.test_several_literal_separators

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyWithLiteralSeparator.test_several_literal_separators
```

````

````{py:method} test_whole_key_as_a_literal_key()
:canonical: tests.satosa.test_util.TestResolveNestedKeyWithLiteralSeparator.test_whole_key_as_a_literal_key

```{autodoc2-docstring} tests.satosa.test_util.TestResolveNestedKeyWithLiteralSeparator.test_whole_key_as_a_literal_key
```

````

`````

````{py:function} _build_data(numbered_paths)
:canonical: tests.satosa.test_util._build_data

```{autodoc2-docstring} tests.satosa.test_util._build_data
```
````

````{py:function} _compositions(segments, separator='.')
:canonical: tests.satosa.test_util._compositions

```{autodoc2-docstring} tests.satosa.test_util._compositions
```
````

````{py:function} _every_data_shape(segments)
:canonical: tests.satosa.test_util._every_data_shape

```{autodoc2-docstring} tests.satosa.test_util._every_data_shape
```
````
