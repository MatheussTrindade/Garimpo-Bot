# ADR-0002 — Estado persistente em SQLite

- **Status:** Aceito
- **Data:** 2026-11-07

## Contexto

O bot precisa lembrar o que já foi alertado (deduplicação) e até onde cada fonte foi lida
(checkpoint incremental), sobrevivendo a reinícios e quedas no meio da execução.

## Opções avaliadas

| Opção | Prós | Contras |
|---|---|---|
| Arquivo JSON | Trivial | Escrita não atômica, corrompe em queda, não escala |
| **SQLite** | Transacional, zero infraestrutura, embutido no Python | Um único escritor |
| PostgreSQL / Redis | Escala, acesso concorrente | Infraestrutura extra, desnecessária no MVP |

## Decisão

Usar **SQLite** (módulo `sqlite3` da stdlib) em `DB_PATH`, com gravações transacionais.
Um alerta só é registrado como enviado após a confirmação do Telegram.

## Consequências

- ✅ Sem dependências nem serviços extras; funciona igual local e em container (volume).
- ✅ Nada se perde ou duplica se o processo cair no meio do envio.
- ⚠️ Se o bot passar a rodar em várias réplicas, migrar para PostgreSQL.
