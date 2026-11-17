# {py:mod}`tests.satosa.micro_services.test_custom_routing`

```{py:module} tests.satosa.micro_services.test_custom_routing
```

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TestDecideBackendByRequester <tests.satosa.micro_services.test_custom_routing.TestDecideBackendByRequester>`
  -
* - {py:obj}`TestDecideBackendByTargetIssuer <tests.satosa.micro_services.test_custom_routing.TestDecideBackendByTargetIssuer>`
  -
* - {py:obj}`TestDecideIfRequesterIsAllowed <tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed>`
  - ```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`target_context <tests.satosa.micro_services.test_custom_routing.target_context>`
  - ```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.target_context
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TARGET_ENTITY <tests.satosa.micro_services.test_custom_routing.TARGET_ENTITY>`
  - ```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TARGET_ENTITY
    :summary:
    ```
````

### API

````{py:data} TARGET_ENTITY
:canonical: tests.satosa.micro_services.test_custom_routing.TARGET_ENTITY
:value: >
   'entity1'

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TARGET_ENTITY
```

````

`````{py:class} TestDecideBackendByRequester(methodName='runTest')
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideBackendByRequester

Bases: {py:obj}`unittest.TestCase`

````{py:method} setUp()
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideBackendByRequester.setUp

````

````{py:method} test_when_requester_is_mapped_choose_mapping_backend()
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideBackendByRequester.test_when_requester_is_mapped_choose_mapping_backend

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideBackendByRequester.test_when_requester_is_mapped_choose_mapping_backend
```

````

````{py:method} test_when_requester_is_not_mapped_and_no_default_backend_skip()
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideBackendByRequester.test_when_requester_is_not_mapped_and_no_default_backend_skip

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideBackendByRequester.test_when_requester_is_not_mapped_and_no_default_backend_skip
```

````

````{py:method} test_when_requester_is_not_mapped_choose_default_backend()
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideBackendByRequester.test_when_requester_is_not_mapped_choose_default_backend

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideBackendByRequester.test_when_requester_is_not_mapped_choose_default_backend
```

````

`````

`````{py:class} TestDecideBackendByTargetIssuer(methodName='runTest')
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideBackendByTargetIssuer

Bases: {py:obj}`unittest.TestCase`

````{py:method} setUp()
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideBackendByTargetIssuer.setUp

````

````{py:method} test_when_target_is_mapped_choose_mapping_backend()
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideBackendByTargetIssuer.test_when_target_is_mapped_choose_mapping_backend

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideBackendByTargetIssuer.test_when_target_is_mapped_choose_mapping_backend
```

````

````{py:method} test_when_target_is_not_mapped_choose_default_backend()
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideBackendByTargetIssuer.test_when_target_is_not_mapped_choose_default_backend

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideBackendByTargetIssuer.test_when_target_is_not_mapped_choose_default_backend
```

````

````{py:method} test_when_target_is_not_set_do_skip()
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideBackendByTargetIssuer.test_when_target_is_not_set_do_skip

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideBackendByTargetIssuer.test_when_target_is_not_set_do_skip
```

````

`````

`````{py:class} TestDecideIfRequesterIsAllowed
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed
```

````{py:method} create_decide_service(rules)
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.create_decide_service

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.create_decide_service
```

````

````{py:method} test_allow_all_requesters(target_context, requester)
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_allow_all_requesters

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_allow_all_requesters
```

````

````{py:method} test_allow_one_requester(target_context)
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_allow_one_requester

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_allow_one_requester
```

````

````{py:method} test_allow_takes_precedence_over_deny_all(target_context)
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_allow_takes_precedence_over_deny_all

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_allow_takes_precedence_over_deny_all
```

````

````{py:method} test_defaults_to_allow_all_requesters_for_target_entity_without_specific_rules(target_context)
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_defaults_to_allow_all_requesters_for_target_entity_without_specific_rules

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_defaults_to_allow_all_requesters_for_target_entity_without_specific_rules
```

````

````{py:method} test_deny_all_and_allow_all_should_raise_exception(requester)
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_deny_all_and_allow_all_should_raise_exception

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_deny_all_and_allow_all_should_raise_exception
```

````

````{py:method} test_deny_all_requesters(target_context, requester)
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_deny_all_requesters

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_deny_all_requesters
```

````

````{py:method} test_deny_one_requester(target_context)
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_deny_one_requester

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_deny_one_requester
```

````

````{py:method} test_deny_takes_precedence_over_allow_all(target_context)
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_deny_takes_precedence_over_allow_all

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_deny_takes_precedence_over_allow_all
```

````

````{py:method} test_missing_target_entity_id_from_context(context)
:canonical: tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_missing_target_entity_id_from_context

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.TestDecideIfRequesterIsAllowed.test_missing_target_entity_id_from_context
```

````

`````

````{py:function} target_context(context)
:canonical: tests.satosa.micro_services.test_custom_routing.target_context

```{autodoc2-docstring} tests.satosa.micro_services.test_custom_routing.target_context
```
````
