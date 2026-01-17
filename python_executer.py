#!/usr/bin/env python3
"""Simple Python executor with a terminal-like prompt."""

import sys
import textwrap
import traceback

BANNER = """\
Python Executer (Terminal)
Tippe Python-Code ein und drücke Enter.
Spezialbefehle:
  :help   Hilfe anzeigen
  :exit   Beenden
  :reset  Umgebung zurücksetzen
  :vars   Aktuelle Variablen anzeigen
"""


def print_help() -> None:
    print(textwrap.dedent(BANNER))


def format_vars(namespace: dict) -> str:
    items = sorted(
        (key, value)
        for key, value in namespace.items()
        if not key.startswith("__")
    )
    if not items:
        return "(keine Variablen)"
    return "\n".join(f"{key} = {value!r}" for key, value in items)


def main() -> int:
    namespace: dict[str, object] = {}
    print_help()

    while True:
        try:
            line = input("py> ")
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print("\n(Abbruch)\n")
            continue

        stripped = line.strip()
        if not stripped:
            continue

        if stripped == ":exit":
            break
        if stripped == ":help":
            print_help()
            continue
        if stripped == ":reset":
            namespace = {}
            print("Umgebung zurückgesetzt.")
            continue
        if stripped == ":vars":
            print(format_vars(namespace))
            continue

        try:
            compiled = compile(stripped, "<input>", "eval")
            is_eval = True
        except SyntaxError:
            compiled = compile(stripped, "<input>", "exec")
            is_eval = False

        try:
            if is_eval:
                result = eval(compiled, namespace)
                if result is not None:
                    print(result)
            else:
                exec(compiled, namespace)
        except Exception:
            traceback.print_exc()

    return 0


if __name__ == "__main__":
    sys.exit(main())
