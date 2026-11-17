# {py:mod}`SATOSA.response`

```{py:module} SATOSA.response
```

```{autodoc2-docstring} SATOSA.response
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BadRequest <SATOSA.response.BadRequest>`
  -
* - {py:obj}`Created <SATOSA.response.Created>`
  -
* - {py:obj}`NotFound <SATOSA.response.NotFound>`
  -
* - {py:obj}`Redirect <SATOSA.response.Redirect>`
  - ```{autodoc2-docstring} SATOSA.response.Redirect
    :summary:
    ```
* - {py:obj}`Response <SATOSA.response.Response>`
  - ```{autodoc2-docstring} SATOSA.response.Response
    :summary:
    ```
* - {py:obj}`SeeOther <SATOSA.response.SeeOther>`
  - ```{autodoc2-docstring} SATOSA.response.SeeOther
    :summary:
    ```
* - {py:obj}`ServiceError <SATOSA.response.ServiceError>`
  -
* - {py:obj}`Unauthorized <SATOSA.response.Unauthorized>`
  -
````

### API

`````{py:class} BadRequest(message=None, status=None, headers=None, content=None)
:canonical: SATOSA.response.BadRequest

Bases: {py:obj}`SATOSA.response.Response`

````{py:attribute} _status
:canonical: SATOSA.response.BadRequest._status
:value: >
   '400 Bad Request'

```{autodoc2-docstring} SATOSA.response.BadRequest._status
```

````

`````

`````{py:class} Created(message=None, status=None, headers=None, content=None)
:canonical: SATOSA.response.Created

Bases: {py:obj}`SATOSA.response.Response`

````{py:attribute} _status
:canonical: SATOSA.response.Created._status
:value: >
   '201 Created'

```{autodoc2-docstring} SATOSA.response.Created._status
```

````

`````

`````{py:class} NotFound(message=None, status=None, headers=None, content=None)
:canonical: SATOSA.response.NotFound

Bases: {py:obj}`SATOSA.response.Response`

````{py:attribute} _status
:canonical: SATOSA.response.NotFound._status
:value: >
   '404 Not Found'

```{autodoc2-docstring} SATOSA.response.NotFound._status
```

````

`````

`````{py:class} Redirect(redirect_url, headers=None, content=None)
:canonical: SATOSA.response.Redirect

Bases: {py:obj}`SATOSA.response.Response`

```{autodoc2-docstring} SATOSA.response.Redirect
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.response.Redirect.__init__
```

````{py:attribute} _status
:canonical: SATOSA.response.Redirect._status
:value: >
   '302 Found'

```{autodoc2-docstring} SATOSA.response.Redirect._status
```

````

`````

`````{py:class} Response(message=None, status=None, headers=None, content=None)
:canonical: SATOSA.response.Response

Bases: {py:obj}`object`

```{autodoc2-docstring} SATOSA.response.Response
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.response.Response.__init__
```

````{py:method} __call__(environ, start_response)
:canonical: SATOSA.response.Response.__call__

```{autodoc2-docstring} SATOSA.response.Response.__call__
```

````

````{py:attribute} _content_type
:canonical: SATOSA.response.Response._content_type
:value: >
   'text/html'

```{autodoc2-docstring} SATOSA.response.Response._content_type
```

````

````{py:attribute} _status
:canonical: SATOSA.response.Response._status
:value: >
   '200 OK'

```{autodoc2-docstring} SATOSA.response.Response._status
```

````

`````

`````{py:class} SeeOther(redirect_url, headers=None, content=None)
:canonical: SATOSA.response.SeeOther

Bases: {py:obj}`SATOSA.response.Redirect`

```{autodoc2-docstring} SATOSA.response.SeeOther
```

```{rubric} Initialization
```

```{autodoc2-docstring} SATOSA.response.SeeOther.__init__
```

````{py:attribute} _status
:canonical: SATOSA.response.SeeOther._status
:value: >
   '303 See Other'

```{autodoc2-docstring} SATOSA.response.SeeOther._status
```

````

`````

`````{py:class} ServiceError(message=None, status=None, headers=None, content=None)
:canonical: SATOSA.response.ServiceError

Bases: {py:obj}`SATOSA.response.Response`

````{py:attribute} _status
:canonical: SATOSA.response.ServiceError._status
:value: >
   '500 Internal Service Error'

```{autodoc2-docstring} SATOSA.response.ServiceError._status
```

````

`````

`````{py:class} Unauthorized(message, headers=None, content=None)
:canonical: SATOSA.response.Unauthorized

Bases: {py:obj}`SATOSA.response.Response`

````{py:attribute} _status
:canonical: SATOSA.response.Unauthorized._status
:value: >
   '401 Unauthorized'

```{autodoc2-docstring} SATOSA.response.Unauthorized._status
```

````

`````
