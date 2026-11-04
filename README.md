# Quota Keeper

**Token-saving tactics for Claude Code · Táticas de economia de tokens para o Claude Code**

By / Por **Jaber Neto (JN Softworks)** · v1.0, November 2026 / novembro de 2026

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
6. A handoff file, so a fresh session can pick up the work with an empty conversation, plus an optional summaries file that makes it easy to find which session did what.
7. An automatic successor session, so Claude opens the next session itself.
8. A spend watch hook, and a script that measures how much 1% of your plan is worth.
9. Checking the work while spending less.

**Why it works.** At every step Claude rereads the whole conversation; in the author's records that rereading was 73% of the cost. Short conversations and heavy work done outside the main one (in an agent or a script) are what save the quota. The guide shows the author's numbers; yours will differ, and Box 8 measures your own.

**Get started.**
1. Download this repository (green **Code** button → **Download ZIP**, then unzip) or `git clone` it.
2. Open Claude Code and say: *"Read `<path to this folder>/START_HERE.md` and follow it."*
3. Answer the question boxes. Python 3 is needed only for the scripts (Boxes 5, 7 and 8).

## Português

**O que é.** Uma instalação guiada que o próprio Claude Code faz. O Claude lê o guia, mostra uma caixa de perguntas por tática e só muda o que você aceitar, depois de fazer uma cópia de segurança. Não tem instalador nem comando para rodar na mão.

**Para quem.** Quem usa o Claude por assinatura e esbarra no limite de uso do Claude Code (app desktop ou terminal), principalmente com sessões longas, muitos agentes ou várias sessões ao mesmo tempo. Não precisa ser técnico.

**O que ele configura** (cada item é opcional):
1. Onde as regras ficam (todos os projetos ou só um) e a cópia de segurança das configurações.
2. Configurações: agentes num modelo mais barato, cache de 1 hora para agente que espera, resumo automático da conversa mais cedo e uma regra de esforço.
3. CLAUDE.md e índice de memória enxutos, porque são relidos a cada passo.
4. Ler menos: log grande e arquivo longo vão para um ajudante que devolve só o resumo.
5. Agentes: modelo mais barato para o trabalho simples e agentes curtos que gravam onde pararam.
6. Arquivo de passagem, para uma sessão nova continuar o trabalho com a conversa vazia, e um arquivo de resumos opcional para achar depois qual sessão fez o quê.
7. Sessão sucessora automática: o próprio Claude abre a sessão seguinte.
8. Vigia de gasto e um script que mede quanto vale 1% do seu plano.
9. Conferir o trabalho gastando menos.

**Por que funciona.** A cada passo o Claude relê a conversa inteira; nos registros do autor, essa releitura foi 73% do gasto. Conversa curta e trabalho pesado fora da conversa principal (num agente ou num script) é o que poupa a cota. O guia mostra os números do autor; os seus vão ser outros, e a Caixa 8 mede os seus.

**Como começar.**
1. Baixe este repositório (botão verde **Code** → **Download ZIP**, depois descompacte) ou use `git clone`.
2. Abra o Claude Code e diga: *"Leia `<caminho desta pasta>/START_HERE.md` e siga."*
3. Responda às caixas. O Python 3 só é preciso para os scripts (Caixas 5, 7 e 8).

## License / Licença

Guides and templates / Guias e modelos: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Scripts: MIT. Details / Detalhes: [`LICENSE.md`](LICENSE.md).

Suggested credit / Crédito sugerido: *Quota Keeper, token-saving tactics by Jaber Neto (JN Softworks), CC BY 4.0.*

Not affiliated with or endorsed by Anthropic. Claude and Claude Code are trademarks of Anthropic. / Sem vínculo com a Anthropic nem aprovação dela. Claude e Claude Code são marcas da Anthropic.
