"""Smoke test: garante que o pacote importa (mantém o CI verde enquanto o código nasce)."""

import app


def test_package_imports() -> None:
    assert app.__version__
