"""Entrypoint da aplicação.

Responsabilidades:
- Carregar configurações (``app.config.settings``) e falhar cedo se algo obrigatório faltar.
- Configurar o logging com redação de segredos (``app.utils.logger``).
- Executar o pipeline em loop, respeitando ``POLL_INTERVAL_MINUTES``.
- Encerrar de forma limpa em SIGINT/SIGTERM.

TODO:
- [ ] Implementar o loop de agendamento.
- [ ] Modo ``--once`` para rodar uma única vez (útil para cron/CI).
"""


def main() -> None:
    raise NotImplementedError("Pipeline ainda não implementado — veja docs/architecture.md")
