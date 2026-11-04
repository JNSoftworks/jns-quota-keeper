# JN's Quota Keeper

**Token-saving tactics for Claude Code · Táticas de economia de tokens para o Claude Code**

**Made by / Feito por: Jaber Felippe Neto (JN Softworks)**
License / Licença: guides [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), scripts MIT (free to copy and adapt, keeping the credit / livre para copiar e adaptar, mantendo o crédito; see / ver `LICENSE.md`) · v1.0, November 2026 / novembro de 2026

## For people / Para pessoas

**EN:** Save this whole folder on your computer (for example, in Documents). Open Claude Code and say:
*"Read `<path to this folder>/START_HERE.md` and follow it."*
Claude shows one question box per tactic and changes only what you accept.

**PT:** Salve esta pasta inteira no seu computador (por exemplo, em Documentos). Abra o Claude Code e diga:
*"Leia `<caminho desta pasta>/START_HERE.md` e siga."*
O Claude mostra uma caixa de perguntas por tática e só muda o que você aceitar.

## For Claude

1. Ask the language first. Use AskUserQuestion with exactly this one question:
   - question: `Choose your language / Escolha o idioma`
   - header: `Language`
   - option `English`, description: `Only changes the language of the next setup messages. Nothing else changes.`
   - option `Português`, description: `Só muda o idioma das próximas mensagens desta instalação. Nada mais muda.`

   Without AskUserQuestion, ask the same thing in one line and wait.
2. **English** → read `en/GUIDE.md` only. **Português** → read `pt/GUIA.md` only. Don't read the other one: it has the same content, and reading both wastes tokens.
3. Follow the guide you read from the top. Don't change anything before its question boxes.
