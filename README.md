# Python Executer (Terminal + Browser)

Ein kleines Python-Tool, das sich wie ein Terminal verhält. Du kannst Python-Code eingeben und bekommst sofort die Ausgabe.

## Browser-Version (einfach öffnen)

Öffne `index.html` direkt im Browser oder hoste den Ordner über einen kleinen Webserver:

```bash
python3 -m http.server 8000
```

Dann im Browser aufrufen: `http://localhost:8000`

## Terminal-Version

```bash
python3 python_executer.py
```

## Befehle

- `:help` Hilfe anzeigen
- `:exit` Beenden (im Browser: Eingabe leeren)
- `:reset` Umgebung zurücksetzen
- `:vars` Aktuelle Variablen anzeigen

## Beispiele

```text
py> x = 5
py> x * 2
10
py> :vars
x = 5
```
