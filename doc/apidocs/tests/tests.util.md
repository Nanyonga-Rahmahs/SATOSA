# {py:mod}`tests.util`

```{py:module} tests.util
```

```{autodoc2-docstring} tests.util
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`FakeBackend <tests.util.FakeBackend>`
  -
* - {py:obj}`FakeFrontend <tests.util.FakeFrontend>`
  - ```{autodoc2-docstring} tests.util.FakeFrontend
    :summary:
    ```
* - {py:obj}`FakeIdP <tests.util.FakeIdP>`
  - ```{autodoc2-docstring} tests.util.FakeIdP
    :summary:
    ```
* - {py:obj}`FakeSP <tests.util.FakeSP>`
  - ```{autodoc2-docstring} tests.util.FakeSP
    :summary:
    ```
* - {py:obj}`FileGenerator <tests.util.FileGenerator>`
  - ```{autodoc2-docstring} tests.util.FileGenerator
    :summary:
    ```
* - {py:obj}`TestBackend <tests.util.TestBackend>`
  -
* - {py:obj}`TestFrontend <tests.util.TestFrontend>`
  -
* - {py:obj}`TestRequestMicroservice <tests.util.TestRequestMicroservice>`
  -
* - {py:obj}`TestResponseMicroservice <tests.util.TestResponseMicroservice>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`create_metadata_from_config_dict <tests.util.create_metadata_from_config_dict>`
  - ```{autodoc2-docstring} tests.util.create_metadata_from_config_dict
    :summary:
    ```
* - {py:obj}`create_name_id <tests.util.create_name_id>`
  - ```{autodoc2-docstring} tests.util.create_name_id
    :summary:
    ```
* - {py:obj}`create_name_id_policy_persistent <tests.util.create_name_id_policy_persistent>`
  - ```{autodoc2-docstring} tests.util.create_name_id_policy_persistent
    :summary:
    ```
* - {py:obj}`create_name_id_policy_transient <tests.util.create_name_id_policy_transient>`
  - ```{autodoc2-docstring} tests.util.create_name_id_policy_transient
    :summary:
    ```
* - {py:obj}`generate_cert <tests.util.generate_cert>`
  - ```{autodoc2-docstring} tests.util.generate_cert
    :summary:
    ```
* - {py:obj}`private_to_public_key <tests.util.private_to_public_key>`
  - ```{autodoc2-docstring} tests.util.private_to_public_key
    :summary:
    ```
* - {py:obj}`write_cert <tests.util.write_cert>`
  - ```{autodoc2-docstring} tests.util.write_cert
    :summary:
    ```
````

### API

`````{py:class} FakeBackend(start_auth_func=None, internal_attributes=None, base_url='', name='FakeBackend', register_endpoints_func=None)
:canonical: tests.util.FakeBackend

Bases: {py:obj}`satosa.backends.base.BackendModule`

````{py:method} register_endpoints()
:canonical: tests.util.FakeBackend.register_endpoints

```{autodoc2-docstring} tests.util.FakeBackend.register_endpoints
```

````

````{py:method} start_auth(context, request_info, state)
:canonical: tests.util.FakeBackend.start_auth

```{autodoc2-docstring} tests.util.FakeBackend.start_auth
```

````

`````

`````{py:class} FakeFrontend(handle_authn_request_func=None, internal_attributes=None, base_url='', name='FakeFrontend', handle_authn_response_func=None, register_endpoints_func=None)
:canonical: tests.util.FakeFrontend

Bases: {py:obj}`satosa.frontends.base.FrontendModule`

```{autodoc2-docstring} tests.util.FakeFrontend
```

```{rubric} Initialization
```

```{autodoc2-docstring} tests.util.FakeFrontend.__init__
```

````{py:method} handle_authn_request(context, binding_in)
:canonical: tests.util.FakeFrontend.handle_authn_request

```{autodoc2-docstring} tests.util.FakeFrontend.handle_authn_request
```

````

````{py:method} handle_authn_response(context, internal_response, state)
:canonical: tests.util.FakeFrontend.handle_authn_response

```{autodoc2-docstring} tests.util.FakeFrontend.handle_authn_response
```

````

````{py:method} register_endpoints(backend_names)
:canonical: tests.util.FakeFrontend.register_endpoints

````

`````

`````{py:class} FakeIdP(user_db, config)
:canonical: tests.util.FakeIdP

Bases: {py:obj}`saml2.server.Server`

```{autodoc2-docstring} tests.util.FakeIdP
```

```{rubric} Initialization
```

```{autodoc2-docstring} tests.util.FakeIdP.__init__
```

````{py:method} __apply_binding_to_authn_response(resp, response_binding, relay_state, destination)
:canonical: tests.util.FakeIdP.__apply_binding_to_authn_response

```{autodoc2-docstring} tests.util.FakeIdP.__apply_binding_to_authn_response
```

````

````{py:method} __create_authn_response(saml_request, relay_state, binding, userid, response_binding=BINDING_HTTP_POST)
:canonical: tests.util.FakeIdP.__create_authn_response

```{autodoc2-docstring} tests.util.FakeIdP.__create_authn_response
```

````

````{py:method} handle_auth_req(saml_request, relay_state, binding, userid, response_binding=BINDING_HTTP_POST)
:canonical: tests.util.FakeIdP.handle_auth_req

```{autodoc2-docstring} tests.util.FakeIdP.handle_auth_req
```

````

````{py:method} handle_auth_req_no_name_id(saml_request, relay_state, binding, userid, response_binding=BINDING_HTTP_POST)
:canonical: tests.util.FakeIdP.handle_auth_req_no_name_id

```{autodoc2-docstring} tests.util.FakeIdP.handle_auth_req_no_name_id
```

````

`````

`````{py:class} FakeSP(config)
:canonical: tests.util.FakeSP

Bases: {py:obj}`saml2.client.Saml2Client`

```{autodoc2-docstring} tests.util.FakeSP
```

```{rubric} Initialization
```

```{autodoc2-docstring} tests.util.FakeSP.__init__
```

````{py:method} make_auth_req(entity_id, nameid_format=None, relay_state='relay_state', request_binding=BINDING_HTTP_REDIRECT, response_binding=BINDING_HTTP_REDIRECT, subject=None)
:canonical: tests.util.FakeSP.make_auth_req

```{autodoc2-docstring} tests.util.FakeSP.make_auth_req
```

````

`````

`````{py:class} FileGenerator()
:canonical: tests.util.FileGenerator

Bases: {py:obj}`object`

```{autodoc2-docstring} tests.util.FileGenerator
```

```{rubric} Initialization
```

```{autodoc2-docstring} tests.util.FileGenerator.__init__
```

````{py:attribute} _instance
:canonical: tests.util.FileGenerator._instance
:value: >
   None

```{autodoc2-docstring} tests.util.FileGenerator._instance
```

````

````{py:method} create_metadata(config, code=None)
:canonical: tests.util.FileGenerator.create_metadata

```{autodoc2-docstring} tests.util.FileGenerator.create_metadata
```

````

````{py:method} generate_cert(code=None)
:canonical: tests.util.FileGenerator.generate_cert

```{autodoc2-docstring} tests.util.FileGenerator.generate_cert
```

````

````{py:method} get_instance()
:canonical: tests.util.FileGenerator.get_instance
:staticmethod:

```{autodoc2-docstring} tests.util.FileGenerator.get_instance
```

````

`````

`````{py:class} TestBackend(auth_callback_func, internal_attributes, config, base_url, name)
:canonical: tests.util.TestBackend

Bases: {py:obj}`satosa.backends.base.BackendModule`

````{py:attribute} __test__
:canonical: tests.util.TestBackend.__test__
:value: >
   False

```{autodoc2-docstring} tests.util.TestBackend.__test__
```

````

````{py:method} handle_response(context)
:canonical: tests.util.TestBackend.handle_response

```{autodoc2-docstring} tests.util.TestBackend.handle_response
```

````

````{py:method} register_endpoints()
:canonical: tests.util.TestBackend.register_endpoints

````

````{py:method} start_auth(context, internal_request)
:canonical: tests.util.TestBackend.start_auth

````

`````

`````{py:class} TestFrontend(auth_req_callback_func, internal_attributes, config, base_url, name)
:canonical: tests.util.TestFrontend

Bases: {py:obj}`satosa.frontends.base.FrontendModule`

````{py:attribute} __test__
:canonical: tests.util.TestFrontend.__test__
:value: >
   False

```{autodoc2-docstring} tests.util.TestFrontend.__test__
```

````

````{py:method} handle_authn_response(context, internal_resp)
:canonical: tests.util.TestFrontend.handle_authn_response

````

````{py:method} handle_request(context)
:canonical: tests.util.TestFrontend.handle_request

```{autodoc2-docstring} tests.util.TestFrontend.handle_request
```

````

````{py:method} register_endpoints(backend_names)
:canonical: tests.util.TestFrontend.register_endpoints

````

`````

`````{py:class} TestRequestMicroservice(*args, **kwargs)
:canonical: tests.util.TestRequestMicroservice

Bases: {py:obj}`satosa.micro_services.base.RequestMicroService`

````{py:attribute} __test__
:canonical: tests.util.TestRequestMicroservice.__test__
:value: >
   False

```{autodoc2-docstring} tests.util.TestRequestMicroservice.__test__
```

````

````{py:method} callback()
:canonical: tests.util.TestRequestMicroservice.callback

```{autodoc2-docstring} tests.util.TestRequestMicroservice.callback
```

````

````{py:method} register_endpoints()
:canonical: tests.util.TestRequestMicroservice.register_endpoints

````

`````

`````{py:class} TestResponseMicroservice(*args, **kwargs)
:canonical: tests.util.TestResponseMicroservice

Bases: {py:obj}`satosa.micro_services.base.ResponseMicroService`

````{py:attribute} __test__
:canonical: tests.util.TestResponseMicroservice.__test__
:value: >
   False

```{autodoc2-docstring} tests.util.TestResponseMicroservice.__test__
```

````

````{py:method} callback()
:canonical: tests.util.TestResponseMicroservice.callback

```{autodoc2-docstring} tests.util.TestResponseMicroservice.callback
```

````

````{py:method} register_endpoints()
:canonical: tests.util.TestResponseMicroservice.register_endpoints

````

`````

````{py:function} create_metadata_from_config_dict(config)
:canonical: tests.util.create_metadata_from_config_dict

```{autodoc2-docstring} tests.util.create_metadata_from_config_dict
```
````

````{py:function} create_name_id()
:canonical: tests.util.create_name_id

```{autodoc2-docstring} tests.util.create_name_id
```
````

````{py:function} create_name_id_policy_persistent()
:canonical: tests.util.create_name_id_policy_persistent

```{autodoc2-docstring} tests.util.create_name_id_policy_persistent
```
````

````{py:function} create_name_id_policy_transient()
:canonical: tests.util.create_name_id_policy_transient

```{autodoc2-docstring} tests.util.create_name_id_policy_transient
```
````

````{py:function} generate_cert()
:canonical: tests.util.generate_cert

```{autodoc2-docstring} tests.util.generate_cert
```
````

````{py:function} private_to_public_key(pk_file)
:canonical: tests.util.private_to_public_key

```{autodoc2-docstring} tests.util.private_to_public_key
```
````

````{py:function} write_cert(cert_path, key_path)
:canonical: tests.util.write_cert

```{autodoc2-docstring} tests.util.write_cert
```
````
