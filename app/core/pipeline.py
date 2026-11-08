"""Orquestra o fluxo principal:

    collect → enrich → filter → score → dedupe → notify → persist

Garantias esperadas:
- Um alerta só é marcado como enviado APÓS confirmação do notifier.
- Falha em um coletor não derruba os demais (isolamento por fonte).

TODO:
- [ ] Implementar ``run_once()``.
"""
