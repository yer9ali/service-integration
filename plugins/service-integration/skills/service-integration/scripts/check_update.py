"""Сообщает, если на GitHub вышла версия плагина новее установленной.

    python3 check_update.py

Печатает одну строку с командами обновления, если версия в main новее
установленной; иначе ничего. Без сети или при странной версии молчит:
интеграция важнее напоминания. Код выхода всегда 0.
"""

from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

PLUGIN_JSON = Path(__file__).resolve().parents[3] / ".claude-plugin" / "plugin.json"
LATEST_URL = (
    "https://raw.githubusercontent.com/yer9ali/service-integration/main/"
    "plugins/service-integration/.claude-plugin/plugin.json"
)


def _version(text: str) -> tuple[int, ...]:
    return tuple(int(part) for part in json.loads(text)["version"].split("."))


def _render(version: tuple[int, ...]) -> str:
    return ".".join(map(str, version))


def check(mine_text: str, latest_text: str) -> str | None:
    mine, latest = _version(mine_text), _version(latest_text)
    if latest <= mine:
        return None
    return (
        f"доступна версия service-integration {_render(latest)} (установлена {_render(mine)}). "
        "Обновить: claude plugin marketplace update service-integration && "
        "claude plugin update service-integration@service-integration, затем перезапуск Claude Code"
    )


def main() -> int:
    try:
        mine_text = PLUGIN_JSON.read_text(encoding="utf-8")
        with urllib.request.urlopen(LATEST_URL, timeout=3) as resp:  # noqa: S310 — фиксированный https-URL
            latest_text = resp.read().decode("utf-8")
        message = check(mine_text, latest_text)
    except (OSError, ValueError, KeyError):
        return 0
    if message:
        print(message)
    return 0


if __name__ == "__main__":
    sys.exit(main())
