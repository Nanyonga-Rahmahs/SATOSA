# {py:mod}`SATOSA.backends.bitbucket`

```{py:module} SATOSA.backends.bitbucket
```

```{autodoc2-docstring} SATOSA.backends.bitbucket
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BitBucketBackend <SATOSA.backends.bitbucket.BitBucketBackend>`
  - ```{autodoc2-docstring} SATOSA.backends.bitbucket.BitBucketBackend
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <SATOSA.backends.bitbucket.logger>`
  - ```{autodoc2-docstring} SATOSA.backends.bitbucket.logger
    :summary:
    ```
````

### API

`````{py:class} BitBucketBackend(outgoing, internal_attributes, config, base_url, name)
:canonical: SATOSA.backends.bitbucket.BitBucketBackend

Bases: {py:obj}`satosa.backends.oauth._OAuthBackend`

```{autodoc2-docstring} SATOSA.backends.bitbucket.BitBucketBackend
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.backends.bitbucket.BitBucketBackend.__init__
```

````{py:method} auth_info(request)
:canonical: SATOSA.backends.bitbucket.BitBucketBackend.auth_info

````

````{py:method} get_request_args(get_state=stateID)
:canonical: SATOSA.backends.bitbucket.BitBucketBackend.get_request_args

```{autodoc2-docstring} SATOSA.backends.bitbucket.BitBucketBackend.get_request_args
```

````

````{py:attribute} logprefix
:canonical: SATOSA.backends.bitbucket.BitBucketBackend.logprefix
:value: >
   'BitBucket Backend:'

```{autodoc2-docstring} SATOSA.backends.bitbucket.BitBucketBackend.logprefix
```

````

````{py:method} user_information(access_token)
:canonical: SATOSA.backends.bitbucket.BitBucketBackend.user_information

````

`````

````{py:data} logger
:canonical: SATOSA.backends.bitbucket.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} SATOSA.backends.bitbucket.logger
```

````
