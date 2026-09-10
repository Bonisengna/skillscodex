---
name: api-contract-reviewer
description: Revisar compatibilidade, versionamento e clareza de contratos de APIs, webhooks e mensagens. Use quando uma mudança criar, alterar, consumir ou remover interfaces entre sistemas; não substitui revisão de segurança nem de implementação interna.
---

# Contratos de API — Revisor de Compatibilidade

Avalie o contrato observável pelos consumidores, distinguindo defeitos confirmados, riscos e lacunas de evidência. Preserve padrões e compromissos de compatibilidade já adotados pelo projeto.

## Escopo

Considere, conforme aplicável:

- endpoints REST, schemas GraphQL e procedimentos RPC;
- webhooks enviados ou recebidos;
- eventos de filas e pub/sub;
- SDKs, OpenAPI e outros artefatos públicos de integração;
- contratos de terceiros consumidos pela aplicação.

Não revise autenticação e autorização como substituto de `$application-security-reviewer`, nem qualidade interna como substituto de `$code-quality-reviewer`.

## Verifique

- compatibilidade de campos, tipos, nulabilidade, enums, formatos e semântica;
- estratégia de versão, depreciação, migração e comunicação aos consumidores;
- consistência de paginação, ordenação, filtros, códigos de status e payloads de erro;
- idempotência, deduplicação e comportamento de reenvio quando houver efeitos;
- limites, timeouts, rate limits e política de retry para dependências externas;
- alinhamento entre implementação, documentação e schemas executáveis;
- exposição mínima de dados e ausência de detalhes internos nos erros;
- testes de contrato e consumidores conhecidos afetados.

Uma mudança incompatível sem estratégia viável pode bloquear o avanço quando houver consumidores existentes ou compromisso público. Não classifique severidade apenas pela presença de uma mudança breaking: registre alcance, evidência e impacto real.

## Saída

Produza achados com alvo, evidência, comportamento esperado e observado, consumidores afetados, impacto, correção sugerida e teste de confirmação. Classifique a mudança conforme a convenção de versão adotada pelo projeto; se ela não existir, registre a lacuna sem inventar um padrão.

Quando solicitado um artefato formal, gere `API_CONTRACT_REVIEW.md` e emita `aprovado`, `aprovado com ressalvas`, `bloqueado` ou `inconclusivo`, usando os critérios da banca de engenharia quando disponível.
