"""Coletor da NVD (National Vulnerability Database) — API CVE 2.0.

Fonte: https://nvd.nist.gov/developers/vulnerabilities
Auth:  API key opcional (``NVD_API_KEY``) — aumenta o rate limit.

TODO:
- [ ] Consultar CVEs por janela ``lastModStartDate``/``lastModEndDate``.
- [ ] Respeitar o rate limit (com e sem API key).
"""
