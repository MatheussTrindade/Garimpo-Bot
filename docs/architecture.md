# Arquitetura

## Fluxo

```mermaid
flowchart LR
    subgraph Coleta
        KEV[CISA KEV]
        NVD[NVD CVE 2.0]
        GHSA[GitHub Advisories]
    end
    KEV & NVD & GHSA --> N[Normalização<br/>models.Vulnerability]
    N --> E[Enriquecimento<br/>EPSS]
    E --> F[Filtro<br/>watchlist + thresholds]
    F --> S[Score<br/>KEV · CVSS · EPSS]
    S --> D{Já enviado?<br/>SQLite}
    D -- não --> T[Telegram]
    T -- ok: true --> P[(Persistir estado)]
    D -- sim --> X[Descarta]
```

## Camadas

| Camada | Pasta | Responsabilidade |
|---|---|---|
| Coleta | `app/collectors/` | Um módulo por fonte; retorna modelos normalizados |
| Enriquecimento | `app/enrichers/` | Agrega contexto (EPSS) a itens já coletados |
| Domínio | `app/models/` | `Vulnerability`, `Alert`, `Severity` |
| Regras | `app/core/` | Pipeline, filtros e priorização |
| Saída | `app/notifiers/` | Formatação segura e envio (Telegram) |
| Estado | `app/storage/` | Deduplicação e checkpoints em SQLite |
| Transversal | `app/utils/` | HTTP seguro e logging com redação |

## Princípios

1. **Fontes isoladas:** a falha de um coletor não derruba o pipeline.
2. **Envio confirmado:** só se marca como enviado após `ok: true` do Telegram.
3. **Seguro por padrão:** TLS verificado, timeouts, segredos só por ambiente.
4. **Extensível:** nova fonte = novo módulo em `collectors/`; novo canal = novo `notifier`.
