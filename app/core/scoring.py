"""Priorização dos alertas.

Regra inicial (ajustável):
- 🔴 CRÍTICO → está no CISA KEV (exploração ativa confirmada)
- 🟠 ALTO    → CVSS >= 9.0  OU  EPSS >= 0.5
- 🟡 MÉDIO   → CVSS >= 7.0  OU  EPSS >= 0.1
- ⚪ INFO    → demais itens da watchlist

TODO:
- [ ] Implementar ``score(vuln) -> Severity``.
"""
