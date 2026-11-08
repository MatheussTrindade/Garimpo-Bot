# Changelog

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e [SemVer](https://semver.org/lang/pt-BR/).

## [Unreleased]

### Added
- Estrutura modular: `collectors`, `enrichers`, `core`, `models`, `notifiers`, `storage`, `utils`.
- Pipeline de CI com gitleaks, ruff, bandit, pip-audit e pytest.
- Dependabot, pre-commit, `SECURITY.md`, threat model e Dockerfile sem root.
- Documentação: arquitetura, fontes de dados e ADRs
  ([priorização por risco](docs/adr/0001-priorizacao-por-risco.md),
  [estado em SQLite](docs/adr/0002-estado-em-sqlite.md)).
