# Fontes de dados

Todas as fontes são públicas e acessadas por **API oficial**, dentro dos termos de uso.

| Fonte | O que fornece | Auth | Fase | Docs |
|---|---|---|---|---|
| **CISA KEV** | CVEs com exploração ativa confirmada + prazo de correção | Não | 1 | [link](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) |
| **NVD CVE API 2.0** | Detalhes de CVE, CVSS, CPE | API key opcional | 1 | [link](https://nvd.nist.gov/developers/vulnerabilities) |
| **FIRST EPSS** | Probabilidade de exploração em 30 dias | Não | 1 | [link](https://www.first.org/epss/api) |
| **GitHub Advisories** | Vulnerabilidades em pacotes (pip, npm, maven...) | Token opcional | 2 | [link](https://docs.github.com/rest/security-advisories/global-advisories) |
| **abuse.ch ThreatFox** | IOCs de malware | Auth-Key gratuita | 3 | [link](https://threatfox.abuse.ch/api/) |

## Boas práticas de consumo

- Respeitar os rate limits documentados (a NVD é bem restritiva sem API key).
- Usar checkpoint incremental (só buscar o que mudou desde a última execução).
- Identificar o projeto no `User-Agent`.
- Citar a fonte em cada alerta.
