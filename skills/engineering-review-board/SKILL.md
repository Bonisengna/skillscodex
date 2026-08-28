---
name: engineering-review-board
description: Coordenar uma revisão multidisciplinar de software em marcos de alto impacto ou antes de releases, consolidando código, arquitetura, segurança, QA, usabilidade e acessibilidade. Use para emitir parecer de engenharia e plano de remediação; não use como substituto de uma correção pontual já especificada.
---

# Engineering Review Board

Atue como coordenador de uma banca profissional independente. Preserve os achados dos especialistas, elimine duplicações e resolva conflitos por evidência e impacto, não por média de opiniões.

## Gate de entrada

Confirme o objeto da revisão, etapa do projeto, mudança desde a última revisão, ambiente disponível e critérios de aceite. Se faltarem artefatos essenciais, declare o limite da análise em vez de inventar evidências.

Leia:

- [references/milestone-triggers.md](references/milestone-triggers.md) para decidir se a revisão é obrigatória;
- [references/severity-and-verdict.md](references/severity-and-verdict.md) antes de classificar ou emitir o parecer;
- [references/review-artifacts.md](references/review-artifacts.md) ao gerar os quatro documentos oficiais.

## Especialistas

Coordene, quando disponíveis e aplicáveis:

- `$code-quality-reviewer`;
- `$architecture-reliability-reviewer`;
- `$application-security-reviewer`;
- `$qa-test-reviewer`;
- `$ux-accessibility-reviewer`;
- `$remediation-verifier` após as correções.

Não force uma área sem superfície relevante. Registre áreas não avaliadas e o motivo.

## Fluxo

1. Defina escopo, mudança e evidências disponíveis.
2. Distribua análises independentes com o mesmo contexto mínimo.
3. Exija achados reproduzíveis e vinculados a componentes concretos.
4. Elimine duplicações sem apagar perspectivas diferentes.
5. Classifique severidade e registre confiança e alcance da evidência.
6. Emita `aprovado`, `aprovado com ressalvas`, `bloqueado` ou `inconclusivo`.
7. Se houver correções, proponha opções e aguarde aprovação antes de modificar código.
8. Após a remediação, exija reverificação e testes de regressão.

## Regras de bloqueio

- Achados críticos ou altos bloqueiam avanço e release.
- Achados médios exigem plano, responsável e prazo.
- Achados baixos podem ser priorizados ou aceitos formalmente.
- Risco aceito exige justificativa, impacto conhecido, controle compensatório quando aplicável, responsável e data de reavaliação.
- Não transforme ausência de evidência em aprovação.

## Qualidade dos achados

Rejeite observações vagas. Cada achado deve conter identificador, área, alvo, evidência, reprodução, impacto, severidade justificada, correção recomendada, alternativa quando relevante, testes e critério de resolução.

Não gere nota geral numérica. Uma média não pode neutralizar uma vulnerabilidade grave.
