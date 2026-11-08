# Threat Model (STRIDE simplificado)

## Ativos

| Ativo | Impacto se comprometido |
|---|---|
| `TELEGRAM_TOKEN` | Controle total do bot: envio de mensagens falsas/phishing ao canal |
| API keys (NVD, GitHub, abuse.ch) | Abuso de cota em nome do projeto |
| Integridade dos alertas | Time age sobre informação falsa ou deixa de agir sobre CVE crítica |
| Estado (SQLite) | Alertas duplicados ou suprimidos |

## Ameaças e mitigações

| # | Ameaça | STRIDE | Mitigação | Status |
|---|---|---|---|---|
| T1 | Token vazado em commit | Information Disclosure | `.gitignore`, gitleaks no pre-commit e no CI, Push Protection | ✅ |
| T2 | Token vazado em log/exceção (está na URL da API) | Information Disclosure | Logger com redação; nunca logar URL/exceção crua do Telegram | 🚧 |
| T3 | MITM nas chamadas HTTP | Tampering | TLS sempre verificado; `verify=False` proibido (bandit/ruff `S501`) | 🚧 |
| T4 | Injeção de HTML/links via descrição de CVE | Tampering / Spoofing | `html.escape` em todo campo externo | 🚧 |
| T5 | Dependência maliciosa ou vulnerável | Tampering | Versões fixadas, pip-audit no CI, Dependabot | ✅ |
| T6 | Flood/ban pelo rate limit do Telegram | Denial of Service | Throttling + `retry_after` | 🚧 |
| T7 | Fonte fora do ar ou retornando lixo | Denial of Service | Validação por schema (pydantic) e isolamento por coletor | 🚧 |
| T8 | Container comprometido escalando privilégio | Elevation of Privilege | Imagem slim, usuário não-root, sem segredos na imagem | ✅ |

Legenda: ✅ implementado · 🚧 previsto na estrutura, pendente de código.

## Fora do escopo

- Comprometimento da conta Telegram do administrador.
- Dados incorretos publicados pelas próprias fontes oficiais.
