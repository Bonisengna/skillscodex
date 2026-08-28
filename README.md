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

## Como instalar

### Opção 1 — Clonar o repositório

```bash
git clone https://github.com/Bonisengna/skillscodex.git
```

Copie as pastas que estão dentro de `skillscodex/skills/` para a pasta de skills do Codex:

**Linux ou macOS**

```bash
mkdir -p ~/.codex/skills
cp -R skillscodex/skills/* ~/.codex/skills/
```

**Windows PowerShell**

```powershell
New-Item -ItemType Directory -Force "$HOME\.codex\skills"
Copy-Item -Recurse -Force ".\skillscodex\skills\*" "$HOME\.codex\skills\"
```

Depois, abra uma nova conversa ou reinicie o Codex para que as skills instaladas sejam descobertas.

### Opção 2 — Instalar somente uma skill

Copie apenas a pasta desejada, preservando toda a sua estrutura. Exemplo:

```text
~/.codex/skills/project-discovery-architect/
├── SKILL.md
├── agents/
└── references/
```

Não copie somente o `SKILL.md`, pois algumas skills dependem dos arquivos em `references/`.

## Como acionar uma skill

Use o nome da skill com o prefixo `$` no início ou no corpo do pedido.

```text
Use $project-discovery-architect para planejar um sistema de busca e candidatura a vagas.
```

Também é possível descrever a necessidade naturalmente. Quando a skill estiver instalada e a descrição corresponder ao pedido, o Codex poderá selecioná-la automaticamente. Para ter controle explícito, prefira mencionar `$nome-da-skill`.

## Fluxo recomendado

### 1. Começar ou retomar um projeto

```text
Use $project-discovery-architect para analisar este projeto. Antes de tomar decisões, descubra se ele é novo ou existente, faça as perguntas necessárias, compare alternativas e pare no próximo gate de aprovação.
```

A skill começará identificando uma das duas rotas:

- **Projeto novo:** descoberta do problema, usuários, resultados, regras, restrições e critérios de sucesso.
- **Projeto existente:** inventário do estado atual, falhas, riscos, dívida técnica e partes que devem ser preservadas.

Ela não deverá escolher stack, arquitetura ou escopo definitivo sem apresentar opções e receber aprovação.

### 2. Desenvolver até um marco relevante

Depois que descoberta, escopo, arquitetura e plano forem aprovados, a implementação pode avançar até o próximo gate. Exemplos de marcos:

- conclusão de uma funcionalidade central;
- mudança em autenticação ou permissões;
- criação ou migração de banco de dados;
- nova API, webhook, upload ou integração;
- preparação para publicação.

### 3. Executar a banca de revisão

```text
Use $engineering-review-board para revisar este marco antes do release. Consolide código, arquitetura, segurança, QA, usabilidade e acessibilidade. Não altere o código antes de apresentar o plano de correção e receber minha aprovação.
```

A coordenadora poderá usar os especialistas aplicáveis e produzir:

1. `ENGINEERING_REVIEW_REPORT.md` — achados, evidências, severidade e veredito.
2. `REMEDIATION_PLAN.md` — ordem e estratégia das correções.
3. `ACCEPTED_RISKS.md` — riscos adiados com justificativa, responsável e prazo.
4. `REVERIFICATION_REPORT.md` — confirmação das correções e regressões.

Achados críticos ou altos bloqueiam o avanço. Achados médios exigem plano, responsável e prazo.

### 4. Aprovar e corrigir

Após ler o relatório, aprove a estratégia desejada de forma explícita:

```text
Aprovo o plano de correção proposto para os achados SEC-001 e CODE-002. Aplique somente essas correções, execute os testes definidos e não faça mudanças adicionais sem me consultar.
```

### 5. Reverificar

```text
Use $remediation-verifier para confirmar se SEC-001 e CODE-002 foram resolvidos e se as mudanças introduziram alguma regressão.
```

O verificador deverá reproduzir o problema original, testar a correção e classificar cada achado como resolvido, parcialmente resolvido, não resolvido, regressão introduzida ou inconclusivo.

## Quando usar cada skill diretamente

| Skill | Exemplo de uso |
| --- | --- |
| `$project-discovery-architect` | Planejar um projeto novo ou diagnosticar um existente |
| `$engineering-review-board` | Fazer uma revisão completa de um marco ou release |
| `$code-quality-reviewer` | Revisar lógica, complexidade e manutenção de uma mudança |
| `$architecture-reliability-reviewer` | Avaliar arquitetura, desempenho, dados e recuperação |
| `$application-security-reviewer` | Revisar autenticação, permissões, APIs, dados e integrações |
| `$qa-test-reviewer` | Avaliar testes, critérios de aceite e riscos de regressão |
| `$ux-accessibility-reviewer` | Testar jornadas, responsividade e acessibilidade |
| `$remediation-verifier` | Confirmar de forma independente as correções realizadas |

## Exemplo completo

```text
Use $project-discovery-architect.

Quero criar uma plataforma que pesquise vagas e ajude o usuário a se candidatar. Antes de propor arquitetura ou programar, determine se o projeto é novo ou existente, investigue objetivo, usuários, regras de negócio, integrações, custos, segurança e critérios de sucesso. Apresente alternativas com vantagens e riscos, recomende a opção mais viável e aguarde minha aprovação em cada gate.
```

Quando o projeto atingir um marco:

```text
Use $engineering-review-board para revisar a funcionalidade de cadastro e autenticação. Considere o código, arquitetura, segurança, testes, interface em desktop e celular e acessibilidade. Achados críticos e altos devem bloquear o release. Gere o relatório e o plano, mas não corrija nada antes da minha aprovação.
```
