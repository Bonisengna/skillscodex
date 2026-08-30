# Validação do pacote de orquestração

## Escopo

Validar este pacote de instruções e configuração, sem instalar no computador do usuário, acessar produção, usar credenciais de aplicações ou chamar modelos por API.

## Verificações reproduzíveis

Python 3.11+, biblioteca padrão:

```bash
python -m unittest discover -s tests -v
```

Cobertura: sintaxe TOML, nomes únicos dos agentes, papéis de leitura, limite de paralelismo, skills referenciadas, links locais, geração dos três perfis, preservação de instruções/permissões, recusa de sobrescrita e de destinos ativos, ausência de escrita quando o perfil ou a origem são inválidos.

Além desses testes, validar o frontmatter da skill com o validador da skill-creator quando disponível. Essa verificação estrutural não comprova comportamento nem compatibilidade com o cliente instalado.

## Avaliação comportamental

Foi realizada uma avaliação independente somente de leitura: projeto existente em Python/Postgres restrito ao backend, relatórios genéricos sobre RLS e chave pública, ausência de código/testes e ambiente limitado a GPT-5.5 sem subagentes.

Resultado observado: não aprovou a release, não tratou ausência de RLS ou chave pública isoladamente como vulnerabilidade confirmada, pediu evidências, não iniciou correções e declarou as limitações de modelo/independência. Essa avaliação verificou um cenário, não é benchmark estatístico.

## Limites que permanecem

- Não foi executado o Codex CLI neste ambiente; a configuração foi conferida pela documentação atual e pelo parser TOML, não carregada em um cliente real.
- Disponibilidade dos modelos, troca efetiva por papel e consumo precisam ser testados na instalação.
- Não foi validada uma aplicação de produção nem executada auditoria de segurança.
- Os perfis são políticas iniciais; não existe medição de economia ou superioridade por tarefa nesta entrega.
- A revisão independente não garante ausência de falhas; manter avaliação em casos reais e corrigir desvios observados.
