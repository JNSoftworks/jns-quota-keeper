# JN's Quota Keeper

**Token-saving tactics for Claude Code · Táticas de economia de tokens para o Claude Code**

**Made by / Feito por: Jaber Felippe Neto (JN Softworks)**
License / Licença: guides [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), scripts MIT (free to copy and adapt, keeping the credit / livre para copiar e adaptar, mantendo o crédito; see / ver `LICENSE.md`) · v1.0, November 2026 / novembro de 2026

## For people / Para pessoas

**EN:** Save this whole folder on your computer (for example, in Documents). Open Claude Code and say:
*"Read `<path to this folder>/START_HERE.md` and follow it."*
Claude shows one question box per tactic and changes only what you accept. You can choose **Quick** mode (one screen, one OK) or go box by box.

**Risks and limits:** every box lists its real risks and how to undo them. No script here uses the network. Some read your local session records to count tokens (nothing is copied out). Sensitive things (permissions, auto-approvals, auto-opened sessions, Remote Control, tokens) are left out of Quick mode and, box by box, asked one by one; nothing bypasses Claude Code's approvals except what you accept there. To undo: restore the backup made in Box 1 and delete the copied files; the final box explains each one. There is also a usage-report skill and an optional daily report (Box 8, `scripts/daily_report.py`). Each question has a summary, and the full detail is in `en/DETAILS.md` (ask Claude for "detail").

**PT:** Salve esta pasta inteira no seu computador (por exemplo, em Documentos). Abra o Claude Code e diga:
*"Leia `<caminho desta pasta>/START_HERE.md` e siga."*
O Claude mostra uma caixa de perguntas por tática e só muda o que você aceitar. Você pode escolher o modo **Rápido** (uma tela, um ok) ou ir caixa por caixa.

**Riscos e limites:** cada caixa lista os riscos reais e como desfazer. Nenhum script daqui usa rede. Alguns leem os registros locais das sessões para contar tokens (nada é copiado para fora). O que é sensível (permissões, aprovação automática, sessões abertas sozinhas, Remote Control, tokens) fica fora do modo Rápido e, no caixa por caixa, é perguntado um a um; nada contorna as aprovações do Claude Code, salvo o que você aceitar ali. Para desfazer: volte a cópia de segurança feita na Caixa 1 e apague os arquivos copiados; a caixa final explica cada um. Há também uma skill de relatório de uso e um relatório diário opcional (Caixa 8, `scripts/daily_report.py`). Cada pergunta tem um resumo, e o detalhe completo está em `pt/DETALHES.md` (peça "detalhe" ao Claude).

## For Claude

1. Ask the language first. Use AskUserQuestion with exactly this one question:
   - question: `Choose your language / Escolha o idioma`
   - header: `Language`
   - option `English`, description: `Only changes the language of the next setup messages. Nothing else changes.`
   - option `Português`, description: `Só muda o idioma das próximas mensagens desta instalação. Nada mais muda.`

   Without AskUserQuestion, ask the same thing in one line and wait.
2. **English** → read `en/GUIDE.md` only. **Português** → read `pt/GUIA.md` only. Don't read the other one: it has the same content, and reading both wastes tokens.
3. Follow the guide you read from the top. Don't change anything before its question boxes.
