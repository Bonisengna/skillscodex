# Como usar o orquestrador de engenharia

## O que foi criado

- Uma skill central, **0 — Orquestração — Líder de Engenharia**, baseada nos três anexos enviados. O pacote `.skill` continha os mesmos dois documentos avulsos.
- As nove skills existentes continuam com seus nomes e responsabilidades.
- Onze configurações de subagentes: os nove papéis, mais triagem e uma variante de programador para mudanças complexas. Não significa onze agentes executando ao mesmo tempo.
- Um acordo `AGENTS.md` para acionar o fluxo em trabalhos de programação após instalação deliberada.
- Três perfis preparáveis offline, sem credenciais, API paga ou instalação automática.

## Modelos e papéis

| Agente TOML | Papel | Perfil equilibrado | Esforço |
| --- | --- | --- | --- |
| Conversa principal (`config.toml`) | Orquestrador | GPT-5.6 Sol | medium |
| `triagem` | Inventário delimitado | GPT-5.6 Luna | low |
| `planejamento` | 1 — Arquiteto de Projetos | GPT-5.6 Sol | high |
| `programador` | 2 — Implementação delimitada | GPT-5.6 Terra | medium |
| `programador_complexo` | 2 — Implementação de maior risco | GPT-5.6 Sol | high |
| `coordenacao` | 3 — Consolidar revisão | GPT-5.6 Sol | medium |
| `qualidade` | 4 — Revisão de código | GPT-5.6 Terra | high |
| `arquitetura` | 5 — Arquitetura e confiabilidade | GPT-5.6 Sol | high |
| `seguranca` | 6 — Segurança | GPT-5.6 Sol | high |
| `testes` | 7 — QA | GPT-5.6 Terra | medium |
| `experiencia` | 8 — UX e acessibilidade | GPT-5.6 Terra | medium |
| `verificacao` | 9 — Confirmar correções | GPT-5.6 Sol | high |

Essa distribuição é uma política inicial do pacote, não prova de que cada modelo seja sempre superior nesse papel. O orquestrador deve ajustar a escolha à tarefa e ao catálogo disponível, preservando preferências explícitas. Não há garantia de acesso a todos os modelos da tabela.

Perfis:

- **equilibrado:** usa a tabela e começa com no máximo dois subagentes simultâneos, dentro do teto configurado de três.
- **compatibilidade-5.5:** prepara GPT-5.5 para a conversa principal e todos os agentes. Não é chamado de perfil econômico: preço e disponibilidade precisam ser conferidos.
- **herdar:** remove escolhas de modelo/esforço dos arquivos preparados. O ambiente ou conversa principal decide; não há promessa de troca por papel.

O agente `coordenacao` serve para consolidar material já recebido. Normalmente o orquestrador aplica essa skill diretamente, evitando mais um agente apenas para organizar os demais.

## O que significa “usar sempre”

Após mesclar o acordo de orquestração em um `AGENTS.md` efetivamente carregado, trabalhos de projeto passam a ter esse ponto de entrada. Isso não exige abrir todos os especialistas em cada pergunta. Exemplo: trocar um texto não precisa de uma banca completa; mudar permissão de acesso exige revisão e testes compatíveis com o risco.

Skill, agente e modelo são coisas distintas:

- A **skill** define o procedimento.
- O **agente** executa uma tarefa, com contexto e permissões.
- O **modelo** é a capacidade usada naquela execução.

Um `SKILL.md` não troca sozinho o modelo principal. Os TOML são configurações para clientes locais compatíveis. O Work usa os recursos hospedados anunciados na sessão; não lê automaticamente configurações do seu Windows. [Subagentes](https://learn.chatgpt.com/docs/agent-configuration/subagents)

## Preparação e instalação posterior

Nesta entrega, criar o commit não ativa nada. Não substituir seu `config.toml`, `AGENTS.md` ou suas skills existentes sem conferir o conteúdo e fazer backup.

### 1. Atualizar a cópia em Documentos/Projetos

Se o repositório já existe, não clonar por cima. No PowerShell:

```powershell
$documentos = [Environment]::GetFolderPath("MyDocuments")
$repositorio = Join-Path $documentos "Projetos\skillscodex"
git -C $repositorio status --short
git -C $repositorio branch --show-current
```

Se estiver na `main` e não houver alterações locais pendentes, atualizar:

```powershell
git -C $repositorio pull --ff-only origin main
```

Se houver mudanças locais, branch diferente ou erro, parar e revisar; não usar reset forçado, apagar nem renomear a pasta inteira.

### 2. Preparar um perfil sem instalar

Conferir Python 3.11+ e, na raiz do repositório, executar **apenas um** dos exemplos:

```powershell
Set-Location $repositorio
python --version
python .\scripts\prepare_codex.py --profile equilibrado --output .\prepared\equilibrado
```

Ou, se a opção escolhida for GPT-5.5:

```powershell
python .\scripts\prepare_codex.py --profile compatibilidade-5.5 --output .\prepared\gpt55
```

Ou para herdar a configuração do ambiente:

```powershell
python .\scripts\prepare_codex.py --profile herdar --output .\prepared\herdar
```

O preparador cria `codex/config.toml`, `codex/AGENTS.md` e `codex/agents/*.toml` dentro da pasta escolhida. Recusa destino existente ou situado em diretórios ativos `.codex`/`.agents`. Não copia skills, não instala, não chama modelos e não sobrescreve configurações. Se quiser repetir, use outro nome de pasta; não apague a anterior automaticamente.

### 3. Ativar somente na etapa combinada

Antes de copiar qualquer coisa:

1. Identificar o cliente: Codex CLI/IDE/local ou ChatGPT Work.
2. Conferir versão, modelos disponíveis e suporte a agentes TOML independentes. Versões antigas podem usar outra estrutura; não misturar formatos sem verificar.
3. Escolher instalação por projeto ou pessoal/global. Por projeto reduz o alcance da mudança inicial.
4. Fazer backup dos destinos existentes e revisar diferenças.
5. Instalar as dez pastas de skills completas no local reconhecido pelo cliente. Na documentação local atual: `.agents/skills` no projeto ou no usuário. Conferir a instalação anterior em `.codex/skills` antes de migrar, sem apagar dados nem criar duplicatas.
6. Mesclar o config preparado e o acordo `AGENTS.md`; copiar agentes para o local compatível. Em instalação por projeto: config/agentes sob `.codex/`, acordo na raiz do projeto. Em instalação pessoal: respeitar o diretório configurado do Codex.
7. Confirmar a descoberta das skills e papéis em uma nova sessão, e só então testar uma tarefa pequena, sem publicação e sem dados reais.

Não há instalador automático nesta versão. A etapa de ativação exige escolher escopo e verificar sua máquina. [Skills](https://learn.chatgpt.com/docs/build-skills), [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) e [configuração](https://learn.chatgpt.com/docs/config-file/config-reference).

## Exemplos de uso após instalação

Projeto novo:

```text
Use $stack-engineering-orchestrator. Quero criar um sistema de candidaturas.
Antes de escolher tecnologias ou programar, faça as perguntas essenciais,
compare alternativas viáveis e aguarde minha aprovação.
```

Projeto existente:

```text
Use $stack-engineering-orchestrator. O projeto já tem login e API em Python.
Revise o módulo de documentos, sem alterar código nem acessar produção.
Delegue segurança e QA se houver tarefas independentes que justifiquem isso.
Informe o modelo solicitado e as evidências de cada análise.
```

Implementação autorizada:

```text
Aprovo a abordagem descrita no plano para SEC-001 e QA-002.
Use $stack-engineering-orchestrator para distribuir somente essas correções,
respeitar os arquivos atribuídos e verificar regressões. Não faça deploy.
```

No ChatGPT, selecionar a skill com `@` quando estiver instalada; no Codex CLI/IDE, usar `$`. Não confundir uma skill mencionada em texto com uma skill realmente disponível.

## Ajustes em relação aos anexos

O fluxo foi ampliado de revisão para planejamento/desenvolvimento/revisão. O checklist foi contextualizado: RLS não é requisito universal de todo Postgres; chave pública não equivale a segredo; BFF não é obrigatório para toda API; falta de scanner/evidência essencial é uma limitação que impede aprovação, não automaticamente uma falha alta.

As aprovações continuam obrigatórias para decisões estruturais, correções ainda não autorizadas e publicação. Testes e controles do repositório são necessários para fiscalização técnica: os documentos não substituem CI nem proteção de branch.
