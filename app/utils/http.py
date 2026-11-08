"""Cliente HTTP seguro e centralizado.

Padrões obrigatórios:
- TLS SEMPRE verificado. Proibido ``verify=False``; atrás de proxy corporativo,
  use ``REQUESTS_CA_BUNDLE`` ou ``truststore``.
- Timeout em toda requisição.
- Retry com backoff exponencial para 429/5xx.
- User-Agent honesto, identificando o projeto.

TODO:
- [ ] Implementar ``build_session() -> requests.Session``.
"""
