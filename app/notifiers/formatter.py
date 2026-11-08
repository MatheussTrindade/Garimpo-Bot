"""Formatação das mensagens de alerta (HTML seguro para o Telegram).

Saída esperada (exemplo):

    🔴 CRÍTICO · Explorada ativamente (CISA KEV)
    CVE-2026-12345 — Fortinet FortiOS
    CVSS 9.8 · EPSS 0.94

TODO:
- [ ] Implementar ``format_alert(alert) -> str`` com ``html.escape`` em todo campo externo.
"""
