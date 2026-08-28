# Skills Codex — Engenharia Profissional

Pacote de skills para planejar, revisar e evoluir projetos de software com responsabilidades separadas, gates de aprovação e rastreabilidade.

## Skills incluídas

- `project-discovery-architect`: descoberta, diagnóstico e planejamento antes da implementação.
- `engineering-review-board`: coordenação da banca multidisciplinar.
- `code-quality-reviewer`: qualidade e manutenibilidade do código.
- `architecture-reliability-reviewer`: arquitetura, desempenho e confiabilidade.
- `application-security-reviewer`: segurança proporcional ao risco do projeto.
- `qa-test-reviewer`: testes, regressões e critérios de aceite.
- `ux-accessibility-reviewer`: usabilidade e acessibilidade em desktop e celular.
- `remediation-verifier`: reverificação independente das correções.

## Princípios

- Projetos começam pela identificação de projeto novo ou existente.
- Decisões estruturais exigem alternativas, recomendação e aprovação explícita.
- A equipe avança somente até o próximo gate aprovado.
- Achados críticos e altos bloqueiam releases.
- Correções são planejadas e aprovadas antes de alterar o código.
- Riscos aceitos exigem justificativa, responsável e prazo de reavaliação.

Cada skill está em `skills/<nome-da-skill>/` com seu `SKILL.md`, metadados de interface e referências necessárias.
