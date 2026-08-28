---
name: remediation-verifier
description: Verificar de forma independente se correções aprovadas resolveram achados de engenharia sem introduzir regressões. Use depois da remediação; não use para aprovar mudanças sem reproduzir o problema original e validar os critérios definidos.
---

# Remediation Verifier

Trabalhe a partir do achado original, plano aprovado, alterações realizadas e critérios de resolução.

## Fluxo

1. Reproduza a condição original quando for seguro.
2. Confirme que a alteração corresponde ao plano aprovado ou explique o desvio.
3. Execute o teste específico do achado.
4. Execute regressões proporcionais à área afetada.
5. Verifique efeitos colaterais em segurança, dados, desempenho e UX.
6. Classifique cada item como resolvido, parcialmente resolvido, não resolvido, regressão introduzida ou inconclusivo.

Não marque um item como resolvido apenas porque o código mudou ou o teste novo passou. Preserve evidências e limitações.

## Saída

Gere o relatório de reverificação com achado original, versão avaliada, testes executados, resultados, regressões, evidências e decisão. Achado crítico ou alto não resolvido mantém o bloqueio.
