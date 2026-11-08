"""Configurações tipadas via variáveis de ambiente (pydantic-settings).

Regras de segurança:
- Segredos (tokens, API keys) chegam SOMENTE por variável de ambiente / ``.env``.
- Segredos usam ``SecretStr`` para nunca aparecerem em ``repr``/logs.
- Nenhum valor sensível tem default no código.

TODO:
- [ ] Classe ``Settings`` com os campos do ``.env.example``.
- [ ] Carregar a watchlist de ``WATCHLIST_PATH`` (YAML).
"""
