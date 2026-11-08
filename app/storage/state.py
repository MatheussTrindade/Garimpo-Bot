"""Estado persistente em SQLite (``DB_PATH``).

Responsabilidades:
- Registrar alertas enviados (deduplicação por ``cve_id`` + ``source``).
- Guardar o checkpoint (último timestamp processado) de cada coletor.

TODO:
- [ ] Criar o schema na inicialização (incluindo o diretório).
- [ ] Gravações transacionais (nada se perde se o processo cair no meio).
"""
