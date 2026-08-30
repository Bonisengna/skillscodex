#!/usr/bin/env python3
"""Preparar configurações em uma pasta NOVA, sem instalar nem chamar modelos.

Python 3.11+. Somente biblioteca padrão. Os perfis preservam instruções/permissões.
"""

import argparse
import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILES = ("equilibrado", "compatibilidade-5.5", "herdar")
MODEL_KEYS = {"model", "default_subagent_model"}
EFFORT_KEYS = {"model_reasoning_effort", "default_subagent_reasoning_effort"}


def transform(text: str, profile: str) -> str:
    """Transformar apenas atribuições de modelo antes das instruções multiline."""
    if profile not in PROFILES:
        raise ValueError(f"Perfil desconhecido: {profile}")
    head, separator, instructions = text.partition('developer_instructions = """')
    lines = []
    for line in head.splitlines():
        match = re.match(r"^([a-z_]+)\s*=", line)
        key = match.group(1) if match else None
        if profile == "herdar" and key in MODEL_KEYS | EFFORT_KEYS:
            continue
        if profile == "compatibilidade-5.5" and key in MODEL_KEYS:
            line = f'{key} = "gpt-5.5"'
        lines.append(line)
    result = "\n".join(lines) + "\n" + separator + instructions
    tomllib.loads(result)
    return result


def prepare(output: Path, profile: str, source: Path = ROOT / "codex") -> Path:
    if profile not in PROFILES:
        raise ValueError(f"Perfil desconhecido: {profile}")
    output = output.expanduser().absolute()
    if output.exists() or output.is_symlink():
        raise FileExistsError(f"Destino já existe; nada foi alterado: {output}")
    if any(part.lower() in {".codex", ".agents"} for part in output.resolve().parts):
        raise ValueError("Use uma pasta de preparação, fora dos diretórios ativos do Codex.")
    # Validar todas as fontes antes de criar o destino.
    files = {Path("config.toml"): transform((source / "config.toml").read_text(encoding="utf-8"), profile)}
    agents = sorted((source / "agents").glob("*.toml"))
    if not agents:
        raise ValueError("Nenhum agente encontrado na origem.")
    for path in agents:
        files[Path("agents") / path.name] = transform(path.read_text(encoding="utf-8"), profile)
    instructions = (source / "AGENTS.md").read_text(encoding="utf-8")
    # mkdir sem exist_ok protege também contra corrida com outro preparador.
    output.mkdir(parents=True, exist_ok=False)
    target = output / "codex"
    (target / "agents").mkdir(parents=True)
    for relative, content in files.items():
        (target / relative).write_text(content, encoding="utf-8")
    (target / "AGENTS.md").write_text(instructions, encoding="utf-8")
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", choices=PROFILES, default="equilibrado")
    parser.add_argument("--output", required=True, type=Path, help="Pasta nova e não ativa para preparação")
    args = parser.parse_args()
    try:
        target = prepare(args.output, args.profile)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Falha na preparação: {exc}\n")
    print(f"Preparado em {target}. Nada foi instalado e nenhum modelo foi chamado.")


if __name__ == "__main__":
    main()
