# Contributing

Backends and Frontends act like adapters, while micro-services act like plugins
and all of them can be developed by anyone and shared with everyone.

Other people that have been working with the SaToSa proxy, have built
extentions mainly in the form of additional micro-services that are shared to
be used by anyone.

- SUNET maintains a small collection of extentions that focus around the SWAMID
  policies.
  The extentions are licensed under the Apache2.0 license.
  You can find the code using the following URL:

  - https://github.com/SUNET/swamid-satosa/

- A new OIDC frontend, based on the oidc-op library has been build for
  Università della Calabria, by Giuseppe De Marco (@peppelinux); a long-time
  contributor to the IdPy projects.
  The frontend is licensed under the AGPL-3.0 license.
  You can find the code using the following URL:

  - https://github.com/UniversitaDellaCalabria/SATOSA-oidcop

- A spin-off of SATOSA that adds compatibility with the Italian Digital
  Identity System (SPID) is maintained by Giuseppe De Marco.
  You can find the code using the following URL:

  - https://github.com/italia/Satosa-Saml2Spid

- DAASI International have been a long-time user of this software and have made
  their extentions available.
  The extentions are licensed under the Apache2.0 license.
  You can find the code using the following URL:

  - https://gitlab.daasi.de/didmos2/didmos2-auth/-/tree/master/src/didmos_oidc/satosa/micro_services

  The extentions include:

  - SCIM attribute store to fetch attributes via SCIM API (instead of LDAP)
  - Authoritzation module for blocking services if necessary group memberships or
    attributes are missing in the identity (for service providers that do not
    evaluate attributes themselves)
  - Backend chooser with Django UI for letting the user choose between any
    existing SATOSA backend
  - Integration of MFA via PrivacyIDEA, and more.