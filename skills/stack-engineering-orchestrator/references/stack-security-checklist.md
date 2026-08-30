# Checklist de segurança da stack

Aplicar somente às superfícies presentes na mudança. Esta é uma base de revisão, não auditoria completa nem certificação. Usar dados sintéticos e ambientes autorizados; não executar carga, exploração, escrita remota ou varredura ativa sem escopo e autorização específicos.

Para cada item: estado (`verificado`, `falhou`, `não verificado`, `não aplicável`), alvo, evidência segura, teste e limitação. Somente `não aplicável` justificado dispensa o controle. Falta de acesso não significa aprovação nem vulnerabilidade confirmada.

## 1. Supabase, PostgreSQL e autorização de dados

- Mapear Data API, schemas expostos, privilégios de tabela/função e caminhos via backend. Não presumir exposição automática só porque a tabela está em `public`; verificar a configuração efetiva.
- Nas tabelas de schemas expostos do Supabase, exigir RLS e políticas compatíveis com os acessos necessários. Uma operação deliberadamente proibida não precisa de policy permissiva.
- Verificar `SELECT`, `INSERT`, `UPDATE` e `DELETE` conforme o produto; testar usuários diferentes, tenants e fluxos legítimos. Habilitar RLS sem policies pode bloquear também usuários autenticados.
- Examinar `USING` e `WITH CHECK`, inclusive a semântica efetiva quando a expressão é omitida. No PostgreSQL, em casos definidos, `USING` também é usado como `WITH CHECK`; não declarar falha só pela ausência textual da cláusula. Tentar alteração indevida de proprietário/tenant em teste autorizado.
- Revisar views, RPC, `SECURITY DEFINER`, `search_path`, `EXECUTE` e papéis privilegiados. Não testar isolamento somente com chave administrativa.
- No PostgreSQL restrito ao backend, avaliar privilégios, autorização do serviço e isolamento real. Ausência de RLS, isoladamente, não prova vulnerabilidade em toda arquitetura.
- Em Firestore/Realtime Database, revisar Firebase Security Rules, não aplicar SQL de PostgreSQL.

Fontes: [Data API](https://supabase.com/docs/guides/api/securing-your-api), [RLS](https://supabase.com/docs/guides/database/postgres/row-level-security), [CREATE POLICY](https://www.postgresql.org/docs/current/sql-createpolicy.html) e [Firebase Rules](https://firebase.google.com/docs/rules).

## 2. Identidade, permissões e isolamento

- Validar identidade e autorização por ação/recurso em backend, função ou política do banco; ocultar botão não é controle de acesso.
- Não confiar em `role`, `user_id` ou `tenant_id` enviados pelo cliente como autorização. Usar fontes verificadas; considerar revogação e validade das claims.
- Testar BOLA/IDOR nos caminhos por ID, listagem, busca, exportação, download e operações em lote. UUID não substitui permissão.
- Verificar compartilhamento legítimo, membros de equipe e limites de administradores, sem reduzir toda autorização a “é o dono”.
- Em IA com ferramentas, separar instrução de conteúdo externo; limitar ferramentas/credenciais ao escopo e exigir aprovação para efeitos externos relevantes.

Fonte: [OWASP BOLA](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/).

## 3. Segredos, frontend e integrações

- Procurar segredos em arquivos atuais, histórico Git, logs e bundle distribuído. Não revelar valores no relatório.
- Chaves Supabase `publishable`/legado `anon` são públicas por desenho; sua presença sozinha não é vazamento. Chaves `secret`/`service_role` e credenciais de terceiros/banco/Redis devem ficar protegidas no servidor.
- Conferir variáveis que o framework expõe ao cliente. `.gitignore` não remove segredos já versionados e não impede exposição pelo build.
- Usar backend/edge para integrações que exigem segredo. APIs públicas, OAuth com fluxo apropriado e acessos diretos autorizados por políticas não exigem obrigatoriamente um BFF.
- Se houver segredo exposto, bloquear a entrega e propor revogação/rotação e investigação. A execução dessas ações externas precisa da autorização e do acesso correspondentes.

Fontes: [chaves Supabase](https://supabase.com/docs/guides/getting-started/api-keys), [variáveis no Vite](https://vite.dev/guide/env-and-mode), [Gitleaks](https://github.com/gitleaks/gitleaks).

## 4. Entradas, arquivos, webhooks e abuso

- Validar esquema, tipo, tamanho e formato na camada confiável. Usar consultas parametrizadas; não concatenar entrada em SQL/comandos.
- Tratar saída segundo o contexto de renderização. Validação genérica não substitui defesa contra XSS; sanitizar HTML quando o produto realmente permitir HTML.
- Validar uploads por política de tipos, tamanho, conteúdo e armazenamento; não confiar só na extensão ou no MIME informado pelo cliente. Conferir autorização de leitura e substituição.
- Verificar assinatura, janela de tempo, replay e idempotência de webhooks conforme o provedor.
- Aplicar limites de abuso nas ações sensíveis, contemplando tentativas distribuídas, usuário e origem confiável. Se usar Redis, verificar atomicidade do contador/TTL e comportamento em indisponibilidade.
- Revisar autenticação/ACL, exposição de rede e chaves por tenant no Redis; não tratar cache como fonte definitiva de permissão ou de transação financeira.

Fontes: [validação de entradas](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) e [upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html).

## 5. Verificações complementares

Definir o conjunto necessário conforme a alteração, não “qualquer scanner basta”:

| Camada | Evidência esperada |
| --- | --- |
| Segredos | Gitleaks ou equivalente; escopo de arquivos/histórico declarado |
| Python | Bandit ou equivalente, regras e exclusões informadas |
| Python/Node/TypeScript | Análise estática pertinente e dependências/lockfiles avaliados |
| API e autorização | Testes com diferentes identidades e recursos |
| Aplicação em execução | ZAP ou avaliação dinâmica quando pertinente e autorizada |
| Dados | Policies, privilégios e testes da configuração efetiva |

Descobrir comandos pela versão instalada e `--help`. Não instalar ferramentas globalmente nem conectar serviços pagos por conta própria. Falta de ferramenta deve gerar proposta de alternativa ou limitação explícita. Não considerar saída vazia de scanner uma garantia de segurança.

Para cada execução, registrar ferramenta/versão, regras, escopo, ambiente, resultado e exclusões. Se um teste essencial não puder ocorrer, o parecer é inconclusivo e a release não é liberada. Se houver vulnerabilidade alta/crítica confirmada, bloquear. Reavaliar os mesmos controles após correção.

Fontes: [Bandit](https://bandit.readthedocs.io/en/latest/), [Opengrep](https://github.com/opengrep/opengrep) e [ZAP](https://www.zaproxy.org/getting-started/).
