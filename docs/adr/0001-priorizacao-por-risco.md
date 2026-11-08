# ADR-0001 — Priorização por risco (KEV + EPSS + CVSS)

- **Status:** Aceito
- **Data:** 2026-11-07

## Contexto

São publicadas dezenas de milhares de CVEs por ano. Priorizar só pelo CVSS gera fadiga de
alertas: o CVSS mede a **gravidade** caso a falha seja explorada, mas não a **probabilidade**
de exploração, e a maioria das CVEs nunca chega a ser explorada.

## Decisão

Combinar três sinais complementares:

| Sinal | Pergunta | Fonte |
|---|---|---|
| CISA KEV | Já está sendo explorada? | CISA |
| EPSS | Qual a chance de exploração em 30 dias? | FIRST |
| CVSS | Quão grave é se for explorada? | NVD |

Regra v1: **KEV → CRÍTICO**; **CVSS ≥ 9.0 ou EPSS ≥ 0.5 → ALTO**;
**CVSS ≥ 7.0 ou EPSS ≥ 0.1 → MÉDIO**; demais itens da watchlist → **INFO**.
Os limiares ficam configuráveis na watchlist.

## Consequências

- ✅ Alertas refletem risco real, não só severidade teórica.
- ✅ Todas as fontes são públicas, gratuitas e com API documentada.
- ⚠️ O EPSS é recalculado diariamente; um item pode mudar de nível com o tempo
  (avaliar realerta em mudança de nível numa versão futura).
- ⚠️ CVEs recém-publicadas podem ainda não ter CVSS/EPSS; tratar como INFO até o enriquecimento.
