# How to generate proxy metadata

The proxy metadata is generated based on the front-/backend plugins listed in `proxy_conf.yaml`
using the `satosa-saml-metadata` (installed globally by SATOSA installation).

To produce signed SAML metadata for all SAML front- and backend modules, run the following command:

```bash
satosa-saml-metadata <path to proxy_conf.yaml> <path to key for signing> <path to cert for signing>
```

Detailed usage instructions can be viewed by running `satosa-saml-metadata --help`.