"""Notifier do Telegram (Bot API).

Regras de segurança:
- Nunca logar o token nem a URL da API (o token faz parte da URL).
- Conteúdo externo sempre escapado (``parse_mode=HTML``).
- Validar a resposta (``ok: true``) antes de considerar o envio feito.
- Respeitar o rate limit (~20 msgs/min por grupo) e o ``retry_after`` do HTTP 429.

TODO:
- [ ] Implementar ``TelegramNotifier``.
"""
