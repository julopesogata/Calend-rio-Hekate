from datetime import datetime

# Dados das fases da lua (exemplo simplificado)
MOON_PHASES = [
    {"date": "2025-01-06", "phase": "🌑 Lua Nova", "deipnon": True},
    {"date": "2025-01-13", "phase": "🌓 Quarto Crescente"},
    # Adicione todos os eventos aqui...
]

def generate_html():
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Calendário de Hekate</title>
    <style>
        body {{ font-family: Arial; background: #0d001a; color: #d6b3ff; }}
        .event {{ margin: 10px; padding: 10px; border-left: 3px solid #9933ff; }}
        .deipnon {{ border-color: #ec4899; }}
    </style>
</head>
<body>
    <h1>Calendário Devocionário de Hekate 2025</h1>
    <div class="events">
        {"".join(
            f'<div class="event{" deipnon" if e.get("deipnon") else ""}">'
            f'<strong>{e["phase"]}</strong>: {e["date"]}'
            '</div>'
            for e in MOON_PHASES
        )}
    </div>
    <p>Atualizado em: {datetime.now().strftime("%d/%m/%Y %H:%M")}</p>
</body>
</html>
    """
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    generate_html()
