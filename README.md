# JN's Quota Keeper

**Token-saving tactics for Claude Code · Táticas de economia de tokens para o Claude Code**

A guide and hooks that make Claude Code spend less of your quota. Not a usage monitor: it changes how Claude works, and it runs fine next to any usage tracker. · Um guia e hooks que fazem o Claude Code gastar menos da sua cota. Não é um monitor de uso: ele muda o jeito de o Claude trabalhar e convive com qualquer medidor de consumo.

By / Por **Jaber Felippe Neto (JN Softworks)** · v1.0, November 2026 / novembro de 2026

[English](#english) · [Português](#português)

## English

**What it is.** A guided setup that Claude Code runs for you. Claude reads the guide, shows one question box per tactic and changes only what you accept, after making a backup. No installer, nothing to run by hand.

**Who it's for.** Anyone on a Claude subscription who hits the usage limits in Claude Code (desktop app or terminal), especially with long sessions, many agents or several sessions at once. You don't need to be technical.

**What it sets up** (each one is optional):
1. Where the rules go (all projects or just one) and a backup of your settings.
2. Settings: agents on a cheaper model, a 1-hour cache for agents that wait, earlier compaction, and an effort rule.
3. A lean CLAUDE.md and memory index, since they are reread at every step.
4. Reading less: big logs and long files go to a helper that returns only a summary.
5. Agents: cheaper models for simple work, and short agents that save a resume point.
6. A handoff file, so a fresh session can pick up the work with an empty conversation, plus an optional summaries file that makes it easy to find which session did what, and an optional session-start reminder to read the handoff.
7. An automatic successor session, so Claude opens the next session itself.
8. A spend watch hook, a script that measures how much 1% of your plan is worth, and a usage-report skill ("where did my quota go?" by session and by model).
9. Checking the work while spending less, plus end-of-turn habits (pending questions, a final message with the answer first).

**Why it works.** At every step Claude rereads the whole conversation; in the author's records that rereading was 73% of the cost. Short conversations and heavy work done outside the main one (in an agent or a script) are what save the quota. The guide shows the author's numbers; yours will differ, and Box 8 measures your own.

**Get started.**
1. Download this repository (green **Code** button → **Download ZIP**, then unzip) or `git clone` it.
2. Open Claude Code and say: *"Read `<path to this folder>/START_HERE.md` and follow it."*
3. Answer the question boxes. Box 1 asks how to install: **Quick** (one screen with the recommended bundle, the risk of each part and how to undo it: one OK installs the basics, you tick the hooks you want to try in one box, and the advanced part waits), **Box by box**, or **Box by box, double-checking** (shows the exact lines before each write). Python 3 is needed only for the scripts (Boxes 5, 6, 7 and 8).

**Risks and limits.** Each box lists its real risks and how to undo it before you answer.
- What changes on your PC: lines in your CLAUDE.md and `settings.json`, and some small scripts copied into your Claude config folder. A backup is made first.
- No script in this package uses the network. Some read your local session records (they contain your conversations) to count tokens; nothing is copied out. The relay script (`session_relay.py`) runs `claude` itself, which, like any use of Claude, sends the conversation to Anthropic.
- Sensitive things (permission changes, anything that approves actions by itself, opening sessions by itself, Remote Control, saving a token) all live in Box 7. Quick mode neither installs nor asks about them; box by box, each one is asked separately with its risks. Nothing here bypasses Claude Code's approvals except what you accept there.
- To undo: the final box lists how to undo each thing in one line; to undo everything, restore the Box 1 backup and delete the copied files.

## Português

**O que é.** Uma instalação guiada que o próprio Claude Code faz. O Claude lê o guia, mostra uma caixa de perguntas por tática e só muda o que você aceitar, depois de fazer uma cópia de segurança. Não tem instalador nem comando para rodar na mão.

**Para quem.** Quem usa o Claude por assinatura e esbarra no limite de uso do Claude Code (app desktop ou terminal), principalmente com sessões longas, muitos agentes ou várias sessões ao mesmo tempo. Não precisa ser técnico.

**O que ele configura** (cada item é opcional):
1. Onde as regras ficam (todos os projetos ou só um) e a cópia de segurança das configurações.
2. Configurações: agentes num modelo mais barato, cache de 1 hora para agente que espera, resumo automático da conversa mais cedo e uma regra de esforço.
3. CLAUDE.md e índice de memória enxutos, porque são relidos a cada passo.
4. Ler menos: log grande e arquivo longo vão para um ajudante que devolve só o resumo.
5. Agentes: modelo mais barato para o trabalho simples e agentes curtos que gravam onde pararam.
6. Arquivo de passagem, para uma sessão nova continuar o trabalho com a conversa vazia, um arquivo de resumos opcional para achar depois qual sessão fez o quê e um lembrete opcional, no começo da sessão, para ler a passagem.
7. Sessão sucessora automática: o próprio Claude abre a sessão seguinte.
8. Vigia de gasto, um script que mede quanto vale 1% do seu plano e uma skill de relatório de uso ("onde foi minha cota?" por sessão e por modelo).
9. Conferir o trabalho gastando menos, mais hábitos de fim de turno (perguntas pendentes, mensagem final com a resposta na primeira linha).

**Por que funciona.** A cada passo o Claude relê a conversa inteira; nos registros do autor, essa releitura foi 73% do gasto. Conversa curta e trabalho pesado fora da conversa principal (num agente ou num script) é o que poupa a cota. O guia mostra os números do autor; os seus vão ser outros, e a Caixa 8 mede os seus.

**Como começar.**
1. Baixe este repositório (botão verde **Code** → **Download ZIP**, depois descompacte) ou use `git clone`.
2. Abra o Claude Code e diga: *"Leia `<caminho desta pasta>/START_HERE.md` e siga."*
3. Responda às caixas. A Caixa 1 pergunta como instalar: **Rápido** (uma tela com o pacote recomendado, o risco de cada parte e como desfazer: um ok instala o básico, você marca numa caixa só os hooks que quer testar, e o avançado fica para depois), **Caixa por caixa** ou **Caixa por caixa, conferindo** (mostra as linhas exatas antes de cada gravação). O Python 3 só é preciso para os scripts (Caixas 5, 6, 7 e 8).

**Riscos e limites.** Cada caixa lista os riscos reais e como desfazer antes de você responder.
- O que muda no PC: linhas no seu CLAUDE.md e no `settings.json`, e alguns scripts pequenos copiados para a pasta de configuração do Claude. Uma cópia de segurança é feita antes.
- Nenhum script deste pacote usa rede. Alguns leem os registros locais das sessões (que contêm suas conversas) para contar tokens; nada é copiado para fora. O script de revezamento (`session_relay.py`) roda o próprio `claude`, que, como todo uso do Claude, manda a conversa à Anthropic.
- O que é sensível (mudança de permissão, qualquer coisa que aprove ações sozinha, abrir sessões sozinho, Remote Control, gravar um token) fica todo na Caixa 7. O modo Rápido não instala nem pergunta nada disso; no caixa por caixa, cada um é perguntado à parte, com os riscos. Nada aqui contorna as aprovações do Claude Code, salvo o que você aceitar ali.
- Para desfazer: a caixa final traz como desfazer cada coisa em uma linha; para desfazer tudo, volte a cópia de segurança da Caixa 1 e apague os arquivos copiados.

## License / Licença

Guides and templates / Guias e modelos: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Scripts: MIT. Details / Detalhes: [`LICENSE.md`](LICENSE.md).

Suggested credit / Crédito sugerido: *JN's Quota Keeper, token-saving tactics by Jaber Felippe Neto (JN Softworks), CC BY 4.0.*

Not affiliated with or endorsed by Anthropic. Claude and Claude Code are trademarks of Anthropic. / Sem vínculo com a Anthropic nem aprovação dela. Claude e Claude Code são marcas da Anthropic.
