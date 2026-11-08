"""Contrato comum dos coletores.

Todo coletor deve:
- Usar o cliente HTTP seguro de ``app.utils.http`` (TLS verificado, timeout, retry).
- Respeitar rate limits e os termos de uso da fonte.
- Retornar modelos normalizados (``app.models``), nunca JSON cru.

TODO:
- [ ] Definir ``Collector`` (Protocol) com ``name`` e ``collect(since) -> list[Vulnerability]``.
"""
