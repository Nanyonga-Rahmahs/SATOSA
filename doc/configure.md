# How to configure Satosa

SATOSA is configured using YAML.

All default configuration files, as well as an example WSGI application for the proxy, can be found
in the [example directory](../example).

The default YAML syntax is extended to include the capability to resolve
environment variables. The following tags are used to achieve this:

* The `!ENV` tag

The `!ENV` tag is followed by a string that denotes the environment variable
name. It will be replaced by the value of the environment variable with the
same name.

In the example below `LDAP_BIND_PASSWORD` will, at runtime, be replaced with
the value from the process environment variable of the same name. If the
process environment has been set with `LDAP_BIND_PASSWORD=secret_password` then
the configuration value for `bind_password` will be `secret_password`.

```yaml
bind_password: !ENV LDAP_BIND_PASSWORD
```

* The `!ENVFILE` tag

The `!ENVFILE` tag is followed by a string that denotes the environment
variable name. It will be replaced by the value of the environment variable
with the same name.

In the example below `LDAP_BIND_PASSWORD_FILE` will, at runtime, be replaced
with the value from the process environment variable of the same name. If the
process environment has been set with
`LDAP_BIND_PASSWORD_FILE=/etc/satosa/secrets/ldap.txt` then the configuration
value for `bind_password` will be `secret_password`.

```yaml
bind_password: !ENVFILE LDAP_BIND_PASSWORD_FILE
```

## SATOSA proxy configuration: `proxy_conf.yaml.example`

| Parameter name | Data type | Example value | Description |
| -------------- | --------- | ------------- | ----------- |
| `BASE` | string | `https://proxy.example.com` | base url of the proxy |
| `COOKIE_STATE_NAME` | string | `satosa_state` | name of the cookie SATOSA uses for preserving state between requests |
| `COOKIE_SECURE` | bool | `True` | whether to include the cookie only when the request is transmitted over a secure channel |
| `COOKIE_HTTPONLY` | bool | `True` | whether the cookie should only be accessed only by the server |
| `COOKIE_SAMESITE` | string | `"None"` | whether the cookie should only be sent with requests initiated from the same registrable domain |
| `COOKIE_MAX_AGE` | string | `"1200"` | indicates the maximum lifetime of the cookie represented as the number of seconds until the cookie expires |
| `CONTEXT_STATE_DELETE` | bool | `True` | controls whether SATOSA will delete the state cookie after receiving the authentication response from the upstream IdP|
| `STATE_ENCRYPTION_KEY` | string | `52fddd3528a44157` | key used for encrypting the state cookie, will be overridden by the environment variable `SATOSA_STATE_ENCRYPTION_KEY` if it is set |
| `INTERNAL_ATTRIBUTES` | string | `example/internal_attributes.yaml` | path to attribute mapping
| `CUSTOM_PLUGIN_MODULE_PATHS` | string[] | `[example/plugins/backends, example/plugins/frontends]` | list of directory paths containing any front-/backend plugin modules |
| `BACKEND_MODULES` | string[] | `[openid_connect_backend.yaml, saml2_backend.yaml]` | list of plugin configuration file paths, describing enabled backends |
| `FRONTEND_MODULES` | string[] | `[saml2_frontend.yaml, openid_connect_frontend.yaml]` | list of plugin configuration file paths, describing enabled frontends |
| `MICRO_SERVICES` | string[] | `[statistics_service.yaml]` | list of plugin configuration file paths, describing enabled microservices |
| `LOGGING` | dict | see [Python logging.conf](https://docs.python.org/3/library/logging.config.html) | optional configuration of application logging |

## Attribute mapping configuration: `internal_attributes.yaml`

### attributes

The values directly under the `attributes` key are the internal attribute names.
Every internal attribute has a map of profiles, which in turn has a list of
external attributes names which should be mapped to the internal attributes.

If multiple external attributes are specified under a profile, the proxy will
store all attribute values from the external attributes as a list in the
internal attribute.

Sometimes the external attributes are nested/complex structures. One example is
the [address claim in OpenID connect](http://openid.net/specs/openid-connect-core-1_0.html#AddressClaim)
which consists of multiple sub-fields, e.g.:

```json
"address": {
  "formatted": "100 Universal City Plaza, Hollywood CA 91608, USA",
  "street_address": "100 Universal City Plaza",
  "locality": "Hollywood",
  "region": "CA",
  "postal_code": "91608",
  "country": "USA"
}
```

In this case the proxy accepts a dot-separated string denoting which external
attribute to use, e.g. `address.formatted` will access the attribute value
`"100 Universal City Plaza, Hollywood CA 91608, USA"`.

**Example**
```yaml
attributes:
  mail:
    openid: [email]
    saml: [mail, emailAddress, email]
  address:
    openid: [address.formatted]
    saml: [postaladdress]
```

This example defines two attributes, `mail` and `address`, internal to the proxy. These attributes will be accessible to
any plugin (i.e. front- and backends) in the proxy.

Each internal attribute has a mapping for two different *profiles*, `openid`and `saml`. The mapping between received
attributes (in the proxy backend) <-> internal <-> returned attributes (from the proxy frontend) is defined as:

* Any plugin using the `openid` profile will use the attribute value from
  `email` delivered from the target provider as the value for `mail`.
* Any plugin using the `saml` profile will use the attribute value from `mail`,
  `emailAdress` and `email` depending on which attributes are delivered by the
  target provider as the value for `mail`.
* Any plugin using the `openid` profile will use the attribute value under the
  key `formatted` in the `address` attribute delivered by the target provider.
* Any plugin using the `saml` profile will use the attribute value from `postaladdress`
  delivered from the target provider as the value for `address`.

### user_id_from_attrs

The subject identifier generated by the backend module can be overridden by
specifying a list of internal attribute names under the `user_id_from_attrs` key.
The attribute values of the attributes specified in this list will be
concatenated and used as the subject identifier.

### user_id_to_attr

To store the subject identifier in a specific internal attribute, the internal
attribute name can be specified in `user_id_to_attr`.
When the [ALService](https://github.com/its-dirg/ALservice) is used for account
linking, the `user_id_to_attr` configuration parameter should be set, since that
service will overwrite the subject identifier generated by the proxy.

