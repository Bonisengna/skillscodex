# Seleção de modelos e recursos

## Princípio

Escolher a menor capacidade que satisfaça o risco e os critérios da tarefa, não simplesmente o menor preço. Tratar esta matriz como ponto de partida configurável, não benchmark ou garantia. Verificar o catálogo real da sessão; disponibilidade na documentação não comprova acesso na conta.

| Classe da tarefa | Preferência inicial | Esforço | Limite |
| --- | --- | --- | --- |
| Inventário, classificação e resumo delimitados | `gpt-5.6-luna` | low | Não decide arquitetura nem aprova segurança |
| Implementação delimitada, QA e UX usuais | `gpt-5.6-terra` | medium | Escalar se surgir risco ou ambiguidade material |
| Revisão de lógica e contratos | `gpt-5.6-terra` | high | Não substitui análise especializada crítica |
| Orquestração e consolidação | `gpt-5.6-sol` | medium | Uma única coordenação, sem duplicar especialistas |
| Arquitetura, segurança, código complexo e correção crítica | `gpt-5.6-sol` | high | Critérios verificáveis e revisão independente |
| Compatibilidade ou escolha explícita do usuário | `gpt-5.5` | medium/high conforme risco | Confirmar disponibilidade; não presumir menor custo |

Manter o modelo explicitamente escolhido pelo usuário. Sugerir outra opção quando houver benefício, mas não substituir uma escolha fixa silenciosamente. Não interpretar “5.6” como identificador universal: o ambiente pode oferecer variantes ou aliases distintos. Usar apenas um identificador confirmado no catálogo local.

## Decisão antes de cada delegação

1. Identificar papel, risco, ambiguidade, tamanho do contexto e resultado verificável.
2. Consultar modelos e esforços realmente expostos, preferência fixa e orçamento autorizado.
3. Escolher papel e configuração adequada; se a tarefa ficar pequena, manter a execução local em vez de abrir uma thread só para trocar modelo.
4. Registrar a escolha com motivo curto. Usar os parâmetros reais de modelo/esforço da ferramenta, se disponíveis; caso contrário, usar um agente configurado compatível.
5. Confirmar o que o ambiente retornar. Modelo configurado/solicitado não comprova execução: quando o retorno não informar, registrar `modelo efetivo: não informado`.

Não alterar configuração global, assinatura, credenciais ou provedor automaticamente. Não prometer troca do modelo da conversa principal por instrução em Markdown. Sugerir o seletor do cliente ou configuração da próxima sessão se necessário.

## Indisponibilidade e degradação

- Se o modelo não estiver disponível, registrar o motivo e escolher alternativa **já permitida e disponível** que atenda ao risco; informar a substituição.
- Para segurança, dados sensíveis e arquitetura, não rebaixar silenciosamente a exigência para o modelo de triagem. Se não houver alternativa suficiente, parar essa etapa como inconclusiva e pedir direção.
- Se houver modelo fixo ou restrição de custo que impeça a alternativa, pedir decisão.
- Falha de permissão ou aprovação não é falha de modelo: parar, sem trocar ferramenta para contornar o bloqueio.
- Sem seleção de modelo por subagente, herdar o atual e declarar a limitação. Sem subagentes, seguir sequencialmente com as skills e sem alegar independência.
- Não ativar Max, Ultra ou modo de maior consumo por padrão. Aumentar esforço apenas quando justificado, dentro do orçamento combinado.

## Adaptação ao ambiente

- **Codex local compatível:** agentes TOML em `.codex/agents/` ou no diretório pessoal do Codex podem fixar modelo e esforço por papel. Os arquivos `codex/` deste repositório são modelos de configuração; não estão ativos só por existirem no GitHub.
- **ChatGPT Work:** usar as ferramentas de delegação e opções de modelo efetivamente anunciadas pela sessão. Copiar arquivos TOML locais não configura automaticamente o ambiente hospedado.
- **Apenas skills instaladas:** os procedimentos funcionam, mas não garantem a disponibilidade de modelos, subagentes ou isolamento de execução.

O perfil `compatibilidade-5.5` do preparador troca o modelo principal e o de **todos** os agentes preparados, preservando os esforços. Mudar apenas `model` no config principal não altera necessariamente modelos explicitamente fixados nos agentes.

## Fontes e manutenção

Conferido em 2026-08-30: [modelos](https://learn.chatgpt.com/docs/models), [subagentes](https://learn.chatgpt.com/docs/agent-configuration/subagents), [referência de configuração](https://learn.chatgpt.com/docs/config-file/config-reference) e [GPT-5.5](https://developers.openai.com/api/docs/models/gpt-5.5).

Revalidar identificadores e compatibilidade antes da instalação e após atualização do cliente. Não fixar preços nesta skill. Avaliar eficiência com tarefas equivalentes, qualidade, latência e consumo realmente medidos; não inventar uma classificação numérica de capacidade.
