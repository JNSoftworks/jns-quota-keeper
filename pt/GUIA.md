# JN's Quota Keeper — economia de tokens para o Claude Code

> **Feito por Jaber Felippe Neto (JN Softworks).** Licença [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt-br): pode copiar, adaptar e repassar, desde que mantenha o nome do autor e o link da licença. Os scripts estão sob a licença MIT, que também pede para manter o crédito. Versão 1.0, novembro de 2026.

Este arquivo é para o Claude. Se você é a pessoa: não precisa ler. O Claude vai mostrar uma caixa de perguntas por tática e só muda o que você aceitar.

## Como conduzir a instalação (Claude, leia antes de tudo)

1. **Nada muda sem um sim.** Mostre a caixa de uma tática, espere a resposta, faça só os passos daquela resposta, confira, e só então vá para a próxima.
2. **Mostre cada caixa com AskUserQuestion**, uma chamada por caixa, com as perguntas, cabeçalhos e opções como estão aqui (a ferramenta acrescenta "Outro" sozinha). Sem ela, faça as mesmas perguntas numa lista numerada curta e espere.
3. **Resumo antes, detalhe só se pedir.** Antes de cada caixa, mostre em texto curto e simples o que a tática faz ("O que isto faz") e o resumo de cada pergunta: a linha `> **Resumo** — ...` logo abaixo da pergunta. Ela NÃO é opção da caixa; é texto para mostrar antes dela. Diga que o detalhe está em `pt/DETALHES.md` (seção da caixa, subtítulo `Caixa N · Cabeçalho`) e que a pessoa pode pedir "detalhe" pela opção "Outro". Só leia e explique o detalhe quando ela pedir, ou em toda pergunta se em `Modo` ela escolheu "Caixa por caixa, conferindo"; nos outros modos não leia por conta própria (custa a cada passo), salvo onde uma caixa mandar ler. A pessoa pode não ser técnica: nada de sigla ou jargão sem tradução na mesma frase. Cada opção mostra sua consequência numa linha; não esconda risco nem exagere.
4. **Siga a ordem das caixas.** Se uma não se aplica (por exemplo, a pessoa não usa agentes), diga em uma linha e passe para a próxima.
5. **Grave as regras com o texto pronto** de cada caixa ("Texto da regra"), sem reescrever nem enfeitar: cada linha a mais no CLAUDE.md é paga em toda sessão. Dos trechos entre `< >`, preencha só os da instalação:
   - número escolhido, como `<200>`: o número da resposta da pessoa;
   - `<pasta de configuração>`: o caminho completo dela (definida logo abaixo), com barras `/`, ex. `C:/Users/fulano/.claude`;
   - `<caminho>`: só nos testes da Caixa 7, o caminho completo da pasta de teste;
   - `<lista>`: as ferramentas escolhidas na Caixa 7;
   - `<data do lembrete>`: só na Caixa 10, hoje + 7 dias, `AAAA-MM-DD`;
   - escolha `<a | b>`: deixe só a opção que bate com a resposta.

   Ficam literais na regra gravada, para a sessão preencher depois: `<arquivo>`, `<passagem>`, `<projeto>`, `<id>`, `<n>`, `<título da sessão>`, `<data>`, `<id da sessão>`.

   **Onde as linhas de regra entram:** na seção `## Quota Keeper ...` do CLAUDE.md escolhido, sob `### Regras`, antes de `### Recusadas`. A Caixa 1 cria a seção e os dois subtítulos (no fim do arquivo, se a seção não existir). Se a seção existir sem `### Regras`, crie esse subtítulo antes de `### Recusadas`. Recusas ficam sob `### Recusadas`. Rótulos entre colchetes (como "[Número]") só dizem qual versão escolher: não são gravados.
6. **Nunca peça token, senha ou chave no chat**, nem rode comando que mostre um deles na tela. A Caixa 7 ensina a pessoa a gravar o token sozinha.
7. **Fale pouco entre um passo e outro.** O resumo completo vem na Caixa final.
8. **Em dúvida, pare e pergunte.** Se algo daqui não bater com o computador da pessoa (ferramenta com outro nome, opção que não existe, erro), diga o que achou e pergunte. Não invente.
9. **Nomes de ferramentas e opções mudam.** Os daqui são de novembro de 2026. Procure pelo nome com ToolSearch; se não achar, diga e siga sem aquela parte.

**Os três modos da pergunta `Modo` (Caixa 1, pergunta 4).** Valem para as Caixas 2 em diante:
- **Rápido:** siga a seção "Pacote recomendado (modo Rápido)", em três grupos. (1) Mostre, numa mensagem só, as três tabelas, resumidas em palavras simples. (2) Uma chamada do AskUserQuestion com duas perguntas: cabeçalho `Pacote`, opções `Instalar o grupo 1` / `Ver caixa por caixa` / `Cancelar` (cada uma com a consequência em uma linha, como na seção), e a pergunta `Espera longa` da Caixa 2, igual, que decide o cache de 1 hora. (3) Com "Instalar o grupo 1": faça os passos das caixas só para as partes do Grupo 1, sem mais perguntas. (4) Uma chamada com as perguntas do Grupo 2 (marcar várias); instale o marcado, o desmarcado vai para "Recusadas". (5) Diga em uma linha que o Grupo 3 existe e se liga depois, pela Caixa 7, caixa por caixa; ele não é instalado, nem perguntado, nem vai para "Recusadas". (6) Faça a Caixa 10 como está e termine na Caixa final. "Ver caixa por caixa" passa para o segundo modo; "Cancelar" encerra sem mudar mais nada (a cópia de segurança da Caixa 1 já existe).
- **Caixa por caixa:** uma caixa de perguntas por tática, na ordem. Grave o que a pessoa aceitar sem perguntar de novo.
- **Caixa por caixa, conferindo:** como o anterior e, antes de cada gravação (linha no `settings.json`, hook, cópia de script, regra no CLAUDE.md), mostre o trecho exato e pergunte, com opções `Gravar` / `Não gravar`. "Não gravar" é recusa daquela parte (vai para "Recusadas").

**O que é "sensível"** (nos dois modos caixa por caixa, sempre perguntado um a um, com o resumo de riscos; no Rápido, nem instalado nem perguntado, porque está todo no Grupo 3): tudo que muda permissão ou o modo padrão de permissão; aprova ações sozinho (hook que aprova, regra de permitir); abre sessões sozinho; liga o Remote Control; ou grava token. Está marcado "(sensível)" nas caixas.

**Dependências entre as perguntas.** Antes de cada caixa (e na caixa do Grupo 2, no Rápido), pule as perguntas cuja condição não vale: a condição vem junto do cabeçalho, como "(só se ...)", e a tabela abaixo reúne as demais. Diga em uma linha o que pulou e por quê (ex.: "pulei os estepes porque você não escolheu a sucessora automática"). Pergunta pulada conta como a resposta que não instala nada e não vai para "Recusadas": se a pessoa mudar de ideia, basta pedir a caixa de novo.

| Se... | Pule | O que a pessoa perde |
|---|---|---|
| Não há Python (Caixa 1, passo 3) | `Freio`, `Trava`, `Lembrete`, `Token`, `Hook estepe`, `Vigia`, `Medir plano`, `Skill uso`, `Relatório` | Scripts e hooks; ficam só as regras de texto |
| `Onde usa` = "Terminal", ou não há `start_session` | Na Caixa 7, tudo menos `Token` e `Permissões` | Sucessora visível no app; fica o caminho B ou a regra "[Eu abro]" |
| `Onde usa` = "App desktop" ou "Os dois" | `Token`, `Permissões` | Nada: no app, o token não faz falta |
| `Plano` = "Chave de API" | `Antes/depois`, `Medir plano`, `Token` | A conta em % da cota (não existe nesse plano) |
| Janela de 200 mil (ou sem saber) | `Compactar`; `Troca` usa ~100 mil | Nada: baixar a compactação só serve na janela de 1 milhão |
| A pessoa não usa agentes | `Espera longa` e a Caixa 5 | Nada agora; se passar a usar, pode pedir |
| `Passagem` = "Não" | `Troca`, `Lembrete` e a Caixa 7 inteira | Sem passagem, troca e sucessora perdem o sentido |
| `Sucessora` não é "O Claude, sozinho" | `Fechar mãe`, `Agendada`, `Recusa`, `Estepes`, `Remote`, `Auto padrão`, `Hook estepe` | A cadeia não segue sozinha; a troca depende de você |
| `Recusa` não é "Sessão de estepe" | `Estepes`, `Hook estepe` | Sem você na tela, a troca espera sua mensagem ou usa a reserva |
| `Agendada` = "Não liberar" | `Auto padrão` | A reserva por tarefa agendada |
| `Token` não é "Sim, me guie" | `Permissões` | As rodadas sem tela |
| Modo Rápido | A Caixa 7 inteira (Grupo 3) | Nada agora: se liga depois |

Combinações que funcionam pela metade (se a pessoa escolher uma, diga em uma linha o que ela perde):
- Troca de sessão sem `Vigia`: depende de o Claude notar o tamanho da conversa; no uso do autor, 14 de 36 trocas passaram do ponto antes do vigia.
- `Espera longa` "Sim" sem agentes que esperam mais de 5 minutos: gravar custa 2 vezes e nada se ganha.
- "Experimental: Opus coordena" sem `Freio`: só a regra de texto impede o Sonnet de abrir agentes.
- `Fechar mãe` "Não": a sessão anterior pode reler a conversa a cada turno da nova, gastando cota, até ser arquivada.
- Estepes sem `Hook estepe`: no modo automático, a troca por estepe pode ser barrada e cair no "Avisar e seguir".
- `Agendada` liberada com `Auto padrão` "Não mudar": a sucessora da tarefa para no primeiro comando, esperando aprovação.
- "Avisar e seguir" com `Remote` "Não usar": o aviso só aparece no computador.
- `Trava` "Não" com "O Claude, sozinho": na troca com agente rodando, a sucessora confere a passagem em vez de a trava garantir.
- `Medir plano` "Não": o vigia avisa só em tokens, não em % da cota.
- `Token` "Sim, me guie" (ou rodadas sem tela) sem `Relatório`: ninguém confere por dia se a conta subiu por outra fonte nem se há sessão escondida. Recomende o `Relatório` (Caixa 8, Grupo 2); só exige Python, mas sem `Medir plano` não dá veredito da conta.

**O que nunca se economiza** (vale sempre): cópia de segurança antes de mudar configuração, confirmação antes de qualquer coisa irreversível, compilar e testar o que mudou, e ler o trecho exato de código que vai ser editado.

**Arquivos deste pacote** (caminhos a partir da pasta onde está o `START_HERE.md`):
- `pt/GUIA.md` (este), `pt/DETALHES.md` (detalhe de cada pergunta, lido só quando a pessoa pede), `pt/PASSAGEM_MODELO.md` e `pt/RESUMOS_MODELO.md` (modelos dos arquivos de passagem e de resumos)
- `scripts/`: `spend_watch.py` (vigia de gasto), `agent_limit.py` (freio de agentes), `session_relay.py` (rodadas sem tela), `measure_point.py` (medir quanto vale 1% do plano), `check_settings.py` (conferir o `settings.json`), `spare_allow.py` (aprova sozinho só as ações nos estepes), `copy_lock.py` (trava de cópia: impede que agentes de duas sessões mexam na mesma cópia de trabalho), `handoff_reminder.py` (lembrete no começo da sessão para ler a passagem), `usage_report.py` (relatório de onde foram os tokens; só lê e imprime), `daily_report.py` (relatório diário de ontem e lembrete uma vez por dia; só lê os registros locais e grava os próprios marcadores)
- `skills/usage-report/SKILL.md` (skill que roda o relatório de uso) e `LICENSE.md`

**Pasta de configuração:** a indicada pela variável de ambiente `CLAUDE_CONFIG_DIR`, se definida (confira: PowerShell `$env:CLAUDE_CONFIG_DIR`; Mac e Linux `echo $CLAUDE_CONFIG_DIR`); senão, a `.claude` dentro da pasta do usuário (Windows: `C:\Users\<nome>\.claude`; Mac: `/Users/<nome>/.claude`; Linux: `/home/<nome>/.claude`). "Pasta de configuração" e `<pasta de configuração>` querem sempre dizer essa pasta. Nos comandos dos hooks e nas regras, use o caminho completo com barras `/`, inclusive no Windows. Antes de copiar o primeiro arquivo para `hooks`, `tools` ou `modelos` dentro dela, crie a subpasta se não existir. `check_settings.py` e `measure_point.py` já leem `CLAUDE_CONFIG_DIR` sozinhos.

**Janela de contexto** (quantos tokens cabem numa conversa: 200 mil ou 1 milhão): no app, o indicador junto da caixa de mensagem; no terminal, o comando `/context` (mostra algo como "x / 200k" ou "x / 1M"). Sem conseguir ver, suponha 200 mil: é o padrão seguro, pois limites pensados para 200 mil também servem na janela de 1 milhão, e o contrário não. Se a pessoa disser que é 1 milhão, refaça só as respostas que dependem disso (Caixas 2, 6 e 8).

**Como mexer no `settings.json` sem quebrar:** leia o arquivo inteiro, acrescente sem apagar o que já existe (dentro de `"env"` e de `"hooks"`, que podem já ter itens), e no fim confira que continua válido:

```text
python <pasta do pacote>/scripts/check_settings.py
```

O script aceita arquivo com BOM, avisa se uma chave aparece repetida (dois `"hooks"` ou dois `"env"`, por exemplo) e imprime `ok` quando está tudo certo. No Mac e no Linux, troque `python` por `python3` aqui e nos comandos dos hooks.

## Por que funciona

Explique isto à pessoa em até 3 frases antes da Caixa 1.

A cada passo (cada vez que o Claude usa uma ferramenta e lê a resposta), ele relê a conversa inteira. Quase todo o gasto vem dessa releitura, não de escrever ou pensar. O que economiza é: conversa curta, menos passos na conversa principal e trabalho pesado fora dela (num agente, com conversa própria, ou num script, que não gasta token).

Números do autor (setembro a novembro de 2026, medidos nos registros das sessões; no PC do autor, pode variar no seu uso):
- Reler a conversa foi 73% do gasto; guardar a conversa para reler depois (o cache) foi 19%; escrever e pensar, 8%.
- Com as regras de passagem e troca de sessão (Caixa 6), a conversa principal caiu de ~12,7 para ~3,2 pontos da cota por dia de uso (75% a menos; comparação de antes e depois, não um teste controlado).
- Agentes que passaram de 100 chamadas foram 74% do gasto dos agentes (Caixa 5).
- Agentes esperando compilação ou teste, com o cache padrão de 5 minutos, regravavam a conversa inteira na volta: ~26% de todo o gasto em 8 dias, até ligar o cache de 1 hora (Caixa 2).

A régua usada para comparar (não é preço oficial):

```text
peso = entrada × 1 + gravação no cache × 1,25 (cache de 5 min) ou × 2 (cache de 1 hora) + leitura do cache × 0,1 + saída × 5
```

Quanto vale 1% da cota depende do plano. No plano do autor, 1% da semana foi ~8,5 milhões de peso (medido no PC do autor; pode variar). Não use esse número para outro plano: a Caixa 8 mede o da pessoa.

## Palavras para explicar à pessoa

Use estas explicações curtas quando uma palavra aparecer. Não leia a lista toda para ela.

- **Token:** um pedaço de texto, mais ou menos uma palavra; a unidade em que o Claude lê, escreve e é cobrado.
- **Conversa (ou contexto):** tudo o que já foi dito e lido na sessão. O Claude relê isso a cada passo.
- **Agente:** um ajudante que o Claude abre para uma tarefa, com conversa própria que começa vazia; devolve só o resumo.
- **Haiku, Sonnet, Opus:** os três modelos do Claude: o mais barato e rápido, o do meio e o mais forte e caro.
- **CLAUDE.md:** arquivo de regras que o Claude lê no começo de toda sessão.
- **Hook:** pequeno script que o Claude Code roda sozinho num momento fixo (a cada mensagem, antes de abrir um agente).
- **Cache:** a conversa guardada para ser relida mais barato. Dura 5 minutos por padrão; depois, guardar de novo custa de novo.
- **`/clear` e `/compact`:** `/clear` apaga a conversa; `/compact` a troca por um resumo. Só a pessoa pode digitar.

---

## Riscos gerais e como desfazer tudo

Diga isto à pessoa, curto, antes da Caixa 1. Cada pergunta traz o resumo dos riscos dela; aqui está o que vale para o pacote todo.

- **O que o pacote muda:** o `CLAUDE.md` (uma seção "Quota Keeper"), o `settings.json` (variáveis em `"env"`, hooks e, só na Caixa 7, permissões) e scripts, modelos e uma skill copiados para a pasta de configuração. Mais nada, e só o que a pessoa aceitar.
- **Rede:** nenhum script do pacote faz chamada de rede. O `copy_lock.py` só roda `ps` (Mac e Linux) e a si mesmo. O `session_relay.py` roda o comando `claude` (que, como todo uso do Claude, manda a conversa à Anthropic) e, no Windows, `taskkill` só no processo que ele mesmo abriu. O `daily_report.py` só lê os registros locais e grava os próprios marcadores em `quota_keeper/`.
- **Permissões:** um hook roda com as permissões do usuário, como qualquer programa dele. Nada daqui contorna as aprovações do Claude Code, salvo o que cada caixa marcada "(sensível)" disser com todas as letras.
- **Se o Python faltar ou um hook der erro:** o Claude Code mostra o erro e segue. Um hook só bloqueia uma ação quando termina com código de saída 2 (no começo de sessão, nem isso: só mostra o erro) ou quando responde "negar" de propósito, com mensagem, como o freio e a trava deste pacote. Erro com outro código não bloqueia. Python ausente = a parte com script não funciona, nada mais quebra. (Confira na documentação dos hooks se a versão da pessoa mudou isso.)
- **Pode gastar mais?** Algumas táticas podem gastar MAIS em certos usos: o cache de 1 hora (gravar custa 2 vezes), sessões novas (releem tudo que carregam no começo) e estepes (sessões reservas: um turno curto ao nascer, depois arquivadas). Cada caixa diz quando.
- **Desfazer tudo:** (1) volte as cópias de segurança da Caixa 1 (`settings.json.antes-quota-keeper-<data>` e `CLAUDE.md.antes-quota-keeper-<data>`) por cima dos arquivos atuais, ou (2) apague a seção "Quota Keeper" do `CLAUDE.md`, tire do `settings.json` as linhas de `"env"`, `"hooks"` e `"permissions"` que o pacote pôs, e apague o que foi copiado para a pasta de configuração (scripts em `hooks` e `tools`, modelos em `modelos`, a pasta `skills/usage-report` e, se existirem, `quota_keeper/`, `spares.txt` e `relay_token.txt`). Vale na próxima sessão.

---

## Pacote recomendado (modo Rápido)

O que o modo Rápido mostra antes de instalar, em três grupos. Caminhos são da pasta de configuração; "regra" é uma linha no `CLAUDE.md`. Tudo vale na próxima sessão. Os passos de cada parte são os da caixa dela, com a resposta "(Recomendado)" salvo indicação aqui. Cada linha diz a caixa e o cabeçalho da pergunta; o detalhe, se a pessoa pedir, está em `pt/DETALHES.md` (por exemplo, "Caixa 2 · Agentes").

**Grupo 1 — Adotar (instala com um ok).** Só regras, dois modelos de arquivo e ajustes em `"env"`. Nada aprova, bloqueia nem muda permissão.

| Parte (caixa) | O que instala | Risco | Como desfazer |
|---|---|---|---|
| CLAUDE.md enxuto e memória curta (3: `CLAUDE.md`, `Memória`) | Regras; o Claude propõe cortes e só move com sim | Detalhe movido pode passar despercebido (fica um ponteiro) | Apagar as linhas; devolver o trecho |
| Conversa curta, texto longo em arquivo (3: `Conversa`, `Texto longo`) | Regras | Você vê menos detalhe no caminho | Apagar as linhas |
| Hábitos de leitura (4: os quatro) | Regras | Pode perder o que ficou fora do trecho | Apagar as linhas |
| Agentes em Sonnet (2: `Agentes`) | `CLAUDE_CODE_SUBAGENT_MODEL` | Sonnet erra mais que Opus em tarefa difícil; o Claude pede Opus | Apagar a linha em `"env"` |
| Modelo certo por tarefa, agentes curtos e em lote (5: `Agente curto`, `Modelos` "Por papel", `Lote`) | Regras | Mais agentes por tarefa; Haiku erra mais no que parecia simples | Apagar as linhas |
| Esforço Alto (2: `Esforço`) | Regra | Nenhum relevante | Apagar a linha |
| Cache de 1 hora (2: `Espera longa`), só se os agentes esperam mais de 5 minutos | `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` | Gravar custa 2 vezes; sem esperas longas, gasta mais | Apagar a linha em `"env"` |
| Passagem e resumos, troca de sessão, uma tarefa por sessão (6: `Passagem`, `Troca`, `Uma tarefa`) | Regras e os dois modelos em `modelos/`; troca em ~250 mil (~100 mil na janela de 200 mil) | Arquivos novos nos projetos, sem perguntar; passagem velha leva a sessão nova ao ponto errado | Apagar as linhas e os modelos; arquivos já criados ficam |
| Uso antes e depois de tarefa grande (8: `Antes/depois`), não com "Chave de API" | Regra | Nenhum relevante | Apagar a linha |
| Conferir gastando menos e fim de turno (9: "Prova barata", "Testes por partes", "Não pagar duas vezes" e os três de `Fim do turno`) | Regras | Defeito só visível pode passar; mensagem final um pouco maior | Apagar as linhas |

Ficam fora do Rápido, sem ir para "Recusadas", porque pedem escolha da pessoa: "Duas revisões só no sensível" (Caixa 9) e "Experimental: Opus coordena" (Caixa 5). Ela pode pedir depois.

Opções da pergunta `Pacote`:
- **Instalar o grupo 1** — Instalo o Grupo 1 agora, sem mais perguntas; depois mostro o Grupo 2 numa caixa só.
- **Ver caixa por caixa** — Nada é instalado agora; passo a uma caixa de perguntas por tática, com os riscos de cada uma.
- **Cancelar** — Paro aqui; só a cópia de segurança da Caixa 1 foi feita.

**Grupo 2 — Testar acompanhando (a pessoa marca numa caixa só).** Scripts que rodam sozinhos (hooks) ou mudam a conversa. Nenhum aprova ação; o freio e a trava só podem negar. Vale olhar os primeiros dias. Cada um tem um teste na caixa dele (só com sim).

| Parte (caixa) | O que instala | Risco | Como desfazer |
|---|---|---|---|
| Vigia de gasto (8: `Vigia`, limites do autor) | `hooks/spend_watch.py` em `"UserPromptSubmit"` e `"PostToolUse"`, e uma regra | Lê os registros locais (só contagens); uma linha de aviso ao cruzar um limite | Tirar as duas entradas; apagar script e regra |
| Freio de agentes (5: `Freio`) | `hooks/agent_limit.py` em `"PreToolUse"` | Pode negar um agente que você queria (a mensagem diz por quê) | Tirar a entrada; apagar o script |
| Trava de cópia (5: `Trava`) | `hooks/copy_lock.py` em `"PreToolUse"` e `"SubagentStop"` | Trava presa impede outra sessão de escrever na pasta por até 2 horas | Tirar as entradas; apagar o script; `copy_lock.py release <pasta>` solta na hora |
| Lembrete da passagem (6: `Lembrete`) | `hooks/handoff_reminder.py` em `"SessionStart"` | Uma linha a mais no começo da sessão em pastas com passagem | Tirar a entrada; apagar o script |
| Compactar em 50% (2: `Compactar`), só na janela de 1 milhão | `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | O resumo automático perde detalhe | Apagar a linha em `"env"` |
| Relatório de uso (8: `Skill uso`) | `skills/usage-report/`, `tools/usage_report.py` e `tools/measure_point.py` | Lê os registros locais (só contagens); nada sai do PC | Apagar a pasta da skill e os dois scripts |
| Medir o plano (8: `Medir plano`), só com limite semanal em % | `tools/measure_point.py`, uma regra e a primeira marca | É estimativa; pede o % em dois dias diferentes | Apagar a linha, o script e `tools/measure_marks.csv` |
| Relatório diário (8: `Relatório`), só se a pessoa quiser | `tools/daily_report.py` e `tools/usage_report.py`; hook em `"SessionStart"` (matcher `startup`) que, uma vez por dia, só lembra o Claude de perguntar "Quer o relatório de ontem?" (Ver agora / Hoje não) | Lê só os registros locais; é indício, não prova (não vê outro computador, claude.ai nem celular); uma linha a mais na primeira sessão do dia | Tirar a entrada; apagar os dois scripts e a pasta `quota_keeper/` |

Como perguntar (uma chamada, `multiSelect: true` nas duas perguntas, cada opção com o risco da tabela em uma linha; o `Relatório diário` só se houver Python):
- **Quais destes hooks testar?** — cabeçalho `Hooks` — opções `Vigia de gasto` / `Freio de agentes` / `Trava de cópia` / `Lembrete da passagem`.
- **E destes?** — cabeçalho `Outros` — opções `Compactar em 50%` (tire com a janela de 200 mil) / `Relatório de uso` / `Medir o plano` (tire com "Chave de API") / `Relatório diário` (quatro opções é o máximo da caixa). Se sobrar uma opção só, pergunte-a sem `multiSelect`, com `Sim` / `Não`.
- Sem Python, tire todas as opções menos `Compactar em 50%` (a pergunta `Hooks` não é feita) e diga isso em uma linha.
- Antes da caixa, mostre o resumo (Ganha / Arrisca / Se não ligar / Desfazer) de cada opção, tirado da tabela (vale o item 3 de "Como conduzir").

**Grupo 3 — Avançado, não ligar no começo (o Rápido não instala nem pergunta).** É tudo da Caixa 7. Diga que existe e que se liga depois, caixa por caixa (basta pedir "rode a Caixa 7 do guia do Quota Keeper"), de preferência depois de uma ou duas semanas com o resto. Quem ligar o token ou as rodadas sem tela deve ligar também o `Relatório diário` (Grupo 2): ele mostra, uma vez por dia, sessões escondidas e conta subindo sem explicação. Detalhe de cada parte: `pt/DETALHES.md`, Caixa 7.

| Parte (Caixa 7) | O que instalaria | Por que fica para depois | Como desfazer, se ligar |
|---|---|---|---|
| Sucessão automática com arquivamento da anterior (`Sucessora`, `Fechar mãe`, `Recusa`, `Estepes`) | Regras que abrem a sessão nova e estepes sozinhos e arquivam a anterior | Abre e arquiva sessões sem você olhar; pode gastar mais. Só compensa com a passagem já funcionando | Apagar as linhas; desarquivar pela lista |
| Token de longa duração em arquivo (`Token`, `Permissões`) | `relay_token.txt` | Chave da conta, válida por um ano, num arquivo: quem a pegar gasta sua cota. Só serve a quem usa só o terminal | Apagar o arquivo; revogar como diz a Caixa 7 |
| Rodadas sem tela (caminho B) | `tools/session_relay.py` e uma regra | Trabalho escondido, sem aprovação: um erro pode editar arquivos sem você ver | Apagar o script e a regra |
| Remote Control automático (`Remote`) | Regra que liga o Remote Control nas sucessoras | Quem entrar na sua conta claude.ai ou pegar o celular desbloqueado manda ordens ao computador | Apagar a linha; desligar em cada sessão e no app |
| Aprovação automática: hook dos estepes, regras de permitir, modo automático como padrão (`Hook estepe`, `Agendada`, `Auto padrão`) | `hooks/spare_allow.py`; linhas em `"permissions"` | Ações passam sem você ver, em todas as sessões e projetos; o filtro do modo automático pode errar | Tirar as linhas; apagar o script |

---

## Caixa 1 — Antes de começar

**O que isto faz:** decidir onde as regras ficam, como a pessoa usa o Claude Code e como a instalação segue. Nada muda ainda: a mudança vem nos passos (cópia de segurança e seção no `CLAUDE.md`).

Perguntas:

1. **Onde gravar as regras que você aceitar?** — cabeçalho `Onde gravar`
   > **Resumo** — **Ganha:** regras em todos os projetos (ou só neste). **Arrisca:** quase nada; "todos" faz cada linha ser lida em toda sessão; "só neste projeto" em arquivo compartilhado mostra as linhas aos outros. **Se não ligar:** não há "não": sem esta resposta não há onde gravar. **Desfazer:** apagar a seção "Quota Keeper" ou voltar a cópia de segurança.
   - **Em todos os projetos (Recomendado)** — Vão para o `CLAUDE.md` da pasta de configuração (em geral `~/.claude/CLAUDE.md`) e valem em qualquer pasta.
   - **Só neste projeto** — Vão para o `CLAUDE.md` da pasta aberta agora; se o arquivo for compartilhado, outras pessoas as verão.

2. **Onde você usa o Claude Code?** — cabeçalho `Onde usa`
   > **Resumo** — **Ganha:** o guia só oferece o que funciona no seu jeito de usar. **Arrisca:** nada, só guarda a resposta. **Se não ligar:** com "Terminal", as partes que dependem do app (sucessora visível, Remote Control) são puladas; o resto funciona igual. **Desfazer:** nada; peça a pergunta de novo.
   - **App desktop** — O app do Claude no computador, na aba Code. Libera as partes que usam as ferramentas do app.
   - **Terminal** — O comando `claude` numa janela de terminal ou no editor de código. As partes só do app são puladas.
   - **Os dois** — Oferece as partes dos dois; nada é instalado sem você aceitar.

3. **Como você paga o Claude?** — cabeçalho `Plano`
   > **Resumo** — **Ganha:** as partes que medem a cota em % só aparecem se o seu plano tem esse limite. **Arrisca:** nada; "Não sei" é seguro. **Se não ligar:** com "Chave de API" ficam de fora `Antes/depois`, `Medir plano` e `Token`; o resto funciona. **Desfazer:** nada.
   - **Pro, Max ou Ultra** — Assinatura pessoal, com limite semanal; as partes que medem a cota em % ficam disponíveis.
   - **Team ou Enterprise** — Plano de empresa; a empresa pode definir os limites, então as partes de medir a cota ficam como sugestão.
   - **Chave de API** — Paga por token, sem limite semanal em %; as partes que medem a cota em % são puladas.
   - **Não sei** — Tudo bem: o guia fica no geral e diz, em cada caixa, o que depende do plano.

4. **Como instalo o que você aceitar?** — cabeçalho `Modo`
   > **Resumo** — **Ganha:** Rápido = poucos cliques; "conferindo" = você vê as linhas exatas antes de gravar. **Arrisca:** no Rápido, um ok instala o Grupo 1 (regras e ajustes sem permissão). **Se não ligar:** não há "não": só muda como pergunto. **Desfazer:** como em "Riscos gerais e como desfazer tudo".
   - **Rápido (Recomendado)** — Uma tela com o pacote recomendado, o risco de cada parte e como desfazer. Um ok instala o básico (regras e ajustes sem permissão); os hooks você marca numa caixa só; o avançado (sessões abertas sozinhas, aprovação automática, token) não é instalado agora.
   - **Caixa por caixa** — Uma caixa de perguntas por tática, com os riscos de cada uma. Gravo o que você aceitar sem perguntar de novo.
   - **Caixa por caixa, conferindo** — Como a anterior e, antes de cada gravação (settings.json, hook, regra), mostro as linhas exatas e espero seu ok. Máximo controle, mais cliques.

Na pergunta 3 não ponha "(Recomendado)" em nenhuma opção: é um fato sobre a pessoa. A pergunta 4 conduz a instalação: ver "Os três modos da pergunta `Modo`" no começo do guia.

Passos:
1. Faça uma cópia de segurança de cada arquivo que existir, ao lado do original, com a data de hoje (relógio do computador) no nome: `<pasta de configuração>/settings.json` → `settings.json.antes-quota-keeper-<AAAA-MM-DD>`, e o CLAUDE.md escolhido → `CLAUDE.md.antes-quota-keeper-<AAAA-MM-DD>`. Diga à pessoa onde ficaram.
2. No fim do CLAUDE.md escolhido (crie se não existir), acrescente a seção abaixo. As caixas seguintes põem as regras sob "Regras" e as recusas sob "Recusadas".

   ```markdown
   ## Quota Keeper (táticas de Jaber Felippe Neto, JN Softworks)

   ### Regras

   ### Recusadas (não oferecer de novo)
   ```

   Se a resposta foi "Só neste projeto" e esse CLAUDE.md é compartilhado (num repositório, por exemplo), avise antes de gravar. Configurações, hooks e scripts são sempre do usuário inteiro (`<pasta de configuração>/settings.json`), mesmo com "Só neste projeto": essa resposta vale só para as linhas de regra. Avise a pessoa disso.

   Se a seção "Quota Keeper" (ou "Economia de tokens", nome antigo) já existir, atualize a que existe, nunca crie outra. O mesmo vale para as configurações e os hooks das caixas seguintes: se já estão no `settings.json`, atualize, nunca duplique.
3. Confira se há Python 3 (`python --version` ou `python3 --version`). Os scripts das Caixas 5, 6, 7 e 8 precisam dele. Se não houver, avise que essas partes precisam do Python (https://www.python.org/downloads/) e siga com o resto.
4. Guarde a resposta de "Onde usa": a Caixa 7 depende dela.
5. Guarde a resposta de "Modo": ela decide como as Caixas 2 em diante seguem (os três modos, no começo do guia). Com "Rápido", depois dos passos desta caixa siga o roteiro do Rápido (tabelas do "Pacote recomendado (modo Rápido)", pergunta `Pacote`, caixa do Grupo 2) em vez de abrir a Caixa 2. Com os outros dois, siga caixa por caixa.
6. Guarde a resposta de "Plano": as Caixas 7 e 8 dependem dela. Nunca suponha o plano, nem pelo que uma ferramenta mostrar. Com "Não sei", fale de forma geral ("se o seu plano tiver limite semanal em %...") e deixe a pessoa decidir. Se ela quiser descobrir, mostre o que a tela de uso diz (no app, a ferramenta `get_usage`; no terminal, `/usage`) e peça que confirme; sem confirmação, fica "Não sei".

**Recusas, em todas as caixas:** cada tática respondida "Não" (ou desmarcada) vira uma linha em "Recusadas", com o nome dela, para nenhuma sessão perguntar de novo.

---

## Caixa 2 — Configurações

**O que isto faz:** três ajustes no `<pasta de configuração>/settings.json` e uma regra de esforço. Nada aprova ação, muda permissão ou envia dado; tudo vale na próxima sessão.
**Atenção:** compactar em 50% supõe a janela de 1 milhão (regra "Janela de contexto", no começo do guia). Na de 200 mil, pule a pergunta 3 e deixe o padrão.

Perguntas:

1. **Os agentes nascem em Sonnet?** — cabeçalho `Agentes`
   > **Resumo** — **Ganha:** agentes mais baratos que o Opus. **Arrisca:** o Sonnet erra mais em tarefa difícil; o Claude pede Opus nesses casos. **Se não ligar:** os agentes usam o modelo da conversa; pode custar mais. **Desfazer:** apagar `CLAUDE_CODE_SUBAGENT_MODEL` em `"env"`.
   - **Sim (Recomendado)** — Todo agente começa no Sonnet. Quando precisar, o Claude pede Opus ou Haiku para um agente específico.
   - **Não** — Os agentes usam o modelo da conversa; podem custar mais se ela for em Opus.

2. **Seus agentes costumam esperar mais de 5 minutos por algo (compilação, testes, download, renderização)?** — cabeçalho `Espera longa` (só se a pessoa usa agentes)
   > **Resumo** — **Ganha:** agente que espera mais de 5 minutos não paga de novo a conversa inteira (no PC do autor, ~26% do gasto; set-nov/2026). **Arrisca:** gravar custa 2 vezes (não 1,25): sem esperas longas, gasta mais. **Se não ligar:** fica o cache de 5 minutos. **Desfazer:** apagar `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` em `"env"`.
   - **Sim, cache de 1 hora** — O agente que espera não paga de novo a conversa inteira na volta. Só compensa com esperas de mais de 5 minutos; sem elas, gasta mais.
   - **Não, deixar como está** — Nada muda: o cache de 5 minutos serve para tarefas rápidas.

3. **Quando resumir a conversa automaticamente?** — cabeçalho `Compactar` (só na janela de 1 milhão)
   > **Resumo** — **Ganha:** a conversa é resumida antes de cada passo ficar caro. **Arrisca:** o resumo automático perde detalhe; em 25%, mais. **Se não ligar:** fica o padrão, perto do fim do espaço; passos mais caros, nada quebra. **Desfazer:** apagar `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` em `"env"`.
   - **Em 50% (Recomendado)** — Resume quando a conversa chega à metade do espaço; perde algum detalhe.
   - **Em 25%** — Para produção longa numa sessão só. Resume mais vezes e perde mais detalhe.
   - **Não mexer** — Nada muda: fica no padrão, perto do fim do espaço.

4. **Virar regra: esforço Alto, sem modo de frota de agentes?** — cabeçalho `Esforço`
   > **Resumo** — **Ganha:** o Claude recomenda esforço Alto e evita modos que abrem muitos agentes de uma vez. **Arrisca:** quase nada: é só uma linha de texto; o seletor de esforço continua com você. **Se não ligar:** o Claude pode sugerir esforço ou modos mais caros. **Desfazer:** apagar a linha da regra no `CLAUDE.md`.
   - **Sim (Recomendado)** — O Claude recomenda esforço Alto; Máximo só para problema muito difícil; nenhum modo que abre muitos agentes sem você pedir. O esforço em si você muda no seletor.
   - **Não** — Nada muda; o Claude pode sugerir esforço ou modos mais caros.

Passos (cada um só se a resposta pediu):
1. No `settings.json`, dentro de `"env"` (crie se não existir), acrescente sem apagar o que já está lá:
   - pergunta 1 "Sim": `"CLAUDE_CODE_SUBAGENT_MODEL": "sonnet"`. Avise: em versões antigas do Claude Code, essa configuração vencia o modelo pedido para um agente específico; se um agente pedido em Opus ou Haiku não mudar de modelo, atualize (`claude update`).
   - pergunta 2 "Sim": `"CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL": "1h"`
   - pergunta 3: `"CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50"` (ou `"25"`)

   Exemplo com os três:

   ```json
   {
     "env": {
       "CLAUDE_CODE_SUBAGENT_MODEL": "sonnet",
       "CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL": "1h",
       "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50"
     }
   }
   ```
2. Pergunta 4 "Sim": grave a regra.
3. Diga à pessoa: os ajustes valem na próxima sessão; para desfazer, apague a linha (ou volte a cópia da Caixa 1). O esforço da conversa só ela muda, no seletor do app ou do terminal.

Texto da regra:
> - Esforço: recomendar Alto; Máximo só para problema muito difícil (de preferência num agente com esforço máximo, não na conversa toda). Nunca abrir modo de frota de agentes sem a pessoa pedir.

Conferir: o `settings.json` continua válido (comando no começo do guia). Mostre à pessoa só as linhas novas.

---

## Caixa 3 — O que o Claude lê toda vez

**O que isto faz:** o CLAUDE.md e o índice da memória entram em toda sessão e são relidos a cada passo; escrever custa 5 vezes mais que ler, e o que se escreve fica na conversa. Aqui só se gravam regras (texto); nenhum script e nenhuma permissão. Vale na próxima sessão.

Perguntas:

1. **Manter o CLAUDE.md curto (regras e ponteiros; o detalhe vai para outros arquivos)?** — cabeçalho `CLAUDE.md`
   > **Resumo** — **Ganha:** menos texto pago em toda sessão. **Arrisca:** o detalhe movido pode passar despercebido (fica um ponteiro); nada move sem o seu sim, e a cópia da Caixa 1 guarda o arquivo. **Se não ligar:** o CLAUDE.md segue crescendo e custando mais. **Desfazer:** apagar a linha da regra; devolver o trecho movido.
   - **Sim, e sugerir cortes (Recomendado)** — Vira regra, e o Claude propõe agora o que mover para outro arquivo. Nada sai sem o seu sim.
   - **Só a regra** — Vale daqui para frente; o arquivo atual fica como está.
   - **Não** — Nada muda; o CLAUDE.md pode seguir crescendo e custando mais.

2. **Memória com índice curto (uma linha por ficha; projeto grande ganha uma ficha-resumo)?** — cabeçalho `Memória`
   > **Resumo** — **Ganha:** só as 200 primeiras linhas do índice entram; linha curta cabe mais. **Arrisca:** encurtar pode apagar detalhe útil (só com sim); a cópia da Caixa 1 NÃO guarda a memória, peça uma. **Se não ligar:** índice longo é cortado na linha 200. **Desfazer:** apagar a regra; devolver o texto da cópia.
   - **Sim (Recomendado)** — Linha curta cabe mais e custa menos; encurtar linhas existentes só com o seu sim.
   - **Não uso memória** — Nada a fazer; esta parte é pulada.
   - **Não** — Nada muda; índice longo é cortado depois da linha 200.

3. **Mensagens curtas no meio do trabalho, tudo junto no fim?** — cabeçalho `Conversa`
   > **Resumo** — **Ganha:** a conversa cresce mais devagar. **Arrisca:** você acompanha menos o que o Claude faz no meio do trabalho; avisos e resultados só vêm juntos no fim. **Se não ligar:** você vê mais detalhe no caminho e a conversa custa mais. **Desfazer:** apagar a linha da regra.
   - **Sim (Recomendado)** — Entre um passo e outro, só uma linha do que está fazendo. Respostas, resultados e avisos vêm juntos na mensagem final.
   - **Não** — Nada muda; você vê mais detalhe, e a conversa cresce mais rápido.

4. **Coisa longa vai para arquivo, não para o chat?** — cabeçalho `Texto longo`
   > **Resumo** — **Ganha:** texto ou log grande não fica na conversa sendo relido em cada passo. **Arrisca:** quase nada: um passo a mais para você (salvar num arquivo da pasta e dizer o nome). **Se não ligar:** colar no chat segue cômodo, e custa em cada passo seguinte. **Desfazer:** apagar a linha da regra.
   - **Sim (Recomendado)** — Para mostrar um texto ou log grande, você salva num arquivo da pasta e diz o nome; o Claude lê só o trecho que precisa.
   - **Não** — Nada muda; colar no chat é mais cômodo, mas custa em cada passo seguinte.

Passos:
1. Pergunta 1 "Sim, e sugerir cortes": meça o CLAUDE.md (linhas e tamanho). Se passar de ~200 linhas ou ~10 KB, proponha uma lista de blocos para mover a um arquivo de referência (por exemplo, `docs/`), cada um com a linha-ponteiro que fica no lugar. Mostre a lista e só mova com sim.
2. Pergunta 2 "Sim": se a pessoa usa a memória automática (pasta `memory` com um `MEMORY.md`), mostre quantas linhas e KB o índice tem. Só as primeiras 200 linhas entram na sessão. Proponha encurtar as linhas longas (mais de ~150 caracteres), só com sim.
3. Grave as regras aceitas.

Texto da regra:
> - CLAUDE.md curto: só regras e ponteiros; explicação e detalhe vão para outro arquivo, citado numa linha.
> - Memória: índice com uma linha curta por ficha (abaixo de 200 linhas); projeto com muitas fichas ganha uma ficha-resumo, e as fichas novas dele entram nela, não no índice.
> - Entre ferramentas, só texto curto do que está sendo feito; respostas, resultados e avisos vão juntos na mensagem final.
> - Texto ou log longo: pedir à pessoa que salve num arquivo da pasta em vez de colar no chat; ler só o trecho necessário.

---

## Caixa 4 — Leitura

**O que isto faz:** tudo o que o Claude lê fica na conversa e é relido em cada passo seguinte. Aqui só se gravam regras (texto) sobre como ler; nenhum script e nenhuma permissão. Vale na próxima sessão.

Pergunta (uma só, com várias respostas: `multiSelect: true`):

1. **Quais destes hábitos de leitura viram regra?** — cabeçalho `Leitura`
   > **Resumo** — **Ganha:** arquivo de 50 mil tokens lido no começo pesa ~560 mil em 100 passos (régua do guia, não é preço oficial). **Arrisca:** perder o que ficou fora do trecho; resumo de agente omitir algo; nota velha; erro sem marca no log não aparecer. **Se não ligar:** tudo lido inteiro, mais caro. **Desfazer:** apagar a linha do hábito.
   - **Buscar em vez de ler** — Procurar o nome ou o título e ler só umas 50 linhas em volta. Nunca ler inteiro documento grande, log ou arquivo gerado.
   - **Leitura grande para agente** — Um agente lê e devolve só o resumo; o volume não entra na conversa. Haiku para achar e filtrar; Sonnet para entender.
   - **Extrair uma vez** — Quando várias tarefas usam a mesma fonte grande, um agente escreve uma nota curta e as próximas leem a nota.
   - **Log filtrado na fonte** — Marcar as linhas do próprio log e buscar só a marca; nunca carregar inteiro um log de compilação ou de teste.
   Se a pessoa não marcar nenhuma: nada muda.

Passos: grave uma linha por item marcado; os não marcados vão para "Recusadas".

Texto da regra:
> - Buscar antes de ler: procurar o nome e ler só o trecho em volta; documento grande, log e arquivo gerado nunca inteiros.
> - Leitura grande (log, vários arquivos, documento longo) vai para agente que devolve só o resumo (Haiku para achar, filtrar e contar; Sonnet para entender). Ler inteiro só o que vou editar.
> - Fonte grande usada por várias tarefas: extrair uma vez numa nota curta no projeto e reaproveitar a nota.
> - Log: marcar as próprias linhas e buscar a marca; nunca carregar inteiro um log de compilação ou de teste.

---

## Caixa 5 — Agentes

**O que isto faz:** limita o tamanho do trabalho de cada agente, escolhe o modelo de cada tipo de trabalho e, com dois scripts opcionais, freia cadeias de agentes e protege uma pasta de duas sessões ao mesmo tempo. No uso do autor, agentes de 100 ou mais chamadas foram 74% do gasto dos agentes (medido no PC do autor, set-nov/2026; pode variar no seu uso).

Perguntas (são 5; a caixa de perguntas aceita 4 por chamada: faça em 2 chamadas, 1 a 3 e depois 4 e 5):

1. **Agente curto: parar em ~100 chamadas e passar o bastão?** — cabeçalho `Agente curto`
   > **Resumo** — **Ganha:** agentes não ficam caros por reler a própria conversa. **Arrisca:** tarefa dividida em mais agentes. **Se não ligar:** agentes sem limite de tamanho; a espera máxima de ~50 min e o "Opus coordena" perdem a base. **Desfazer:** apague a linha do CLAUDE.md.
   - **Sim, em ~100 (Recomendado)** — O agente fecha o item, grava onde parou num arquivo e devolve o resumo; se sobrou trabalho, a conversa principal abre outro a partir do arquivo.
   - **Não** — Nada muda; agentes sem limite de tamanho.
2. **Qual modelo para cada tipo de trabalho?** — cabeçalho `Modelos`
   > **Resumo** — **Ganha:** o trabalho mecânico sai num modelo mais barato. **Arrisca:** o modelo barato erra mais; "Opus coordena" é teste, sem economia comprovada. **Se não ligar:** você escolhe o modelo de cada agente na mão. **Desfazer:** apague a linha do CLAUDE.md.
   - **Por papel (Recomendado)** — Sonnet por padrão; Haiku para o mecânico; Opus só para código delicado (segurança, contas, dinheiro, criptografia).
   - **Experimental: Opus coordena** — Um agente Opus divide o trabalho e revisa; agentes Sonnet, um por vez, executam. Em teste, sem economia comprovada.
   - **Não mudar** — Nada muda; você escolhe o modelo de cada agente na mão.
3. **Agentes em lote e com resposta curta?** — cabeçalho `Lote`
   > **Resumo** — **Ganha:** menos agentes e respostas curtas que a conversa principal relê menos. **Arrisca:** o detalhe fica num arquivo, não na resposta. **Se não ligar:** agentes devolvem respostas longas. **Desfazer:** apague a linha do CLAUDE.md.
   - **Sim (Recomendado)** — Um agente por tarefa; vários na mesma mensagem; cada um grava o detalhe num arquivo e devolve 5 a 10 linhas.
   - **Não** — Nada muda; respostas longas, relidas a cada passo.
4. **Instalar o freio de agentes?** — cabeçalho `Freio` (só com Python)
   > **Resumo** — **Ganha:** impede cadeia sem fim de agentes abrindo agentes. **Arrisca:** pode negar um agente que você queria (a mensagem diz o motivo); só NEGA, nunca aprova. **Se não ligar:** cadeias sem limite continuam possíveis; o "Opus coordena" fica só com a regra de texto. **Desfazer:** apague a entrada de `agent_limit.py` em `"PreToolUse"` do `settings.json`.
   - **Sim (Recomendado)** — Um agente aberto por outro agente não abre mais agentes, e cada agente tem no máximo 6 filhos.
   - **Não** — Nada muda; cadeias sem limite continuam possíveis.
5. **Instalar a trava de cópia?** — cabeçalho `Trava` (só com Python)
   > **Resumo** — **Ganha:** duas sessões não escrevem na mesma pasta ao mesmo tempo. **Arrisca:** uma trava presa bloqueia a outra sessão (some em 2 h, ou com `release`); só NEGA, nunca aprova. **Se não ligar:** duas sessões podem se atrapalhar; a troca com agente rodando (Caixa 7) passa a depender de conferência manual. **Desfazer:** apague as entradas de `copy_lock.py` em `"PreToolUse"` e `"SubagentStop"`.
   - **Sim (Recomendado)** — Quando um agente escreve numa cópia de trabalho (pasta com `.git`, `.p4config` ou `.uproject`), outra sessão não escreve ali nem lança agente nela até esses agentes terminarem. Ler e editar notas `.md` e `.txt` sempre passam.
   - **Não** — Nada muda; duas sessões podem mexer na mesma pasta ao mesmo tempo.

Passos:
1. Perguntas 1 a 3: grave as regras aceitas. Na pergunta 2, grave a regra "Por papel" ou a "Experimental" (não as duas). A linha "[Só com cache de 1 hora]" entra só se a Caixa 2, pergunta 2, foi "Sim, cache de 1 hora".
2. "Experimental": crie `~/Documents/piloto_opus_sonnet.md` (não na pasta de configuração, que é protegida) com uma tabela (data, tarefa, passou de primeira?, o que o Opus teve que refazer). Funciona melhor com o freio (pergunta 4).
3. Pergunta 4 "Sim":
   1. Copie `scripts/agent_limit.py` para `<pasta de configuração>/hooks/agent_limit.py`.
   2. No `settings.json`, dentro de `"hooks"`, acrescente em `"PreToolUse"` (crie a lista se não existir; não apague o que já houver):

      ```json
      "PreToolUse": [
        {
          "matcher": "Agent|Task",
          "hooks": [
            { "type": "command", "command": "python \"<pasta de configuração>/hooks/agent_limit.py\"", "timeout": 10 }
          ]
        }
      ]
      ```

      (O `matcher` tem os dois nomes porque versões antigas do Claude Code chamavam a ferramenta de `Task`.)
   3. Conferir. Algumas versões só leem os hooks ao abrir a sessão: tente nesta sessão; se o bloqueio não vier, peça à pessoa para abrir uma sessão nova na mesma pasta (no terminal, sair e rodar `claude` de novo) e colar o pedido abaixo nela, ou deixe o teste para a Caixa final. Três agentes: a conversa abre o A; o A abre o B; o B tenta abrir o C e deve ser bloqueado. Faça o pedido: *"Teste do freio. Abra um agente Haiku, o A, e peça a ele: 'abra um agente B e peça a B: abra um agente C que responda oi; se B for bloqueado, devolva a mensagem do bloqueio. Depois me devolva a mensagem que B recebeu.' Devolva o que A respondeu."* O esperado é a mensagem "Agent limit: ...". Se o agente A ou o B disser que não tem a ferramenta de abrir agente, o freio não faz falta nessa versão: avise e siga.
4. Pergunta 5 "Sim":
   1. Copie `scripts/copy_lock.py` para `<pasta de configuração>/hooks/copy_lock.py`.
   2. No `settings.json`, dentro de `"hooks"`, acrescente em `"PreToolUse"` e em `"SubagentStop"` (crie as listas que não existirem; não apague o que já houver, como a entrada do freio):

      ```json
      "PreToolUse": [
        {
          "matcher": "Bash|PowerShell|Edit|Write|NotebookEdit|MultiEdit|Agent|Task",
          "hooks": [
            { "type": "command", "command": "python \"<pasta de configuração>/hooks/copy_lock.py\"", "timeout": 10 }
          ]
        }
      ],
      "SubagentStop": [
        {
          "hooks": [
            { "type": "command", "command": "python \"<pasta de configuração>/hooks/copy_lock.py\"", "timeout": 10 }
          ]
        }
      ]
      ```

   3. Diga à pessoa: só agentes pegam a trava, e a trava some sozinha (detalhe: Caixa 5 · Trava). Para ver as travas: `python <pasta de configuração>/hooks/copy_lock.py list`; para soltar uma, só com certeza de que o agente acabou: `python <pasta de configuração>/hooks/copy_lock.py release <pasta>`. Nenhuma regra vai para o CLAUDE.md.
   4. Conferir: `python <pasta de configuração>/hooks/copy_lock.py test` (17 casos simulados, sem mexer nas travas reais); a última linha tem que ser `ALL OK`. Depois confira o `settings.json` com `check_settings.py`.

Texto da regra:
> - Agente que edita ou corrige: o pedido dele diz "ao chegar a ~100 chamadas, feche o item, grave o ponto de retomada em <arquivo> e devolva o resumo". Se sobrou trabalho, a conversa principal abre outro agente a partir desse arquivo. Tarefa grande já nasce dividida em agentes de ~100 chamadas.
> - **[Só com cache de 1 hora]** Agente não fica mais de ~50 minutos numa espera só; espera maior = gravar o ponto de retomada e devolver.
> - Modelos por papel: Sonnet por padrão; Haiku para o mecânico (achar arquivo, filtrar log, contar); Opus só para agente que edita código delicado (segurança, contas, dinheiro, criptografia).
> - (Experimental) Código novo ou correção fora de segurança, contas e criptografia: um agente Opus coordena. Ele escreve o pedido de cada pedaço, abre agentes Sonnet um de cada vez (~80 chamadas cada; o Sonnet não abre agentes), roda os testes por script, revisa só o que mudou, conserta o que estiver ruim e devolve poucas linhas. Pedaço que falhar duas vezes, o Opus faz. Anotar cada caso em `~/Documents/piloto_opus_sonnet.md`; depois de ~6 casos, perguntar à pessoa se vira padrão.
> - Agentes: um por tarefa, não um por pedacinho; vários ao mesmo tempo saem na MESMA mensagem; cada um grava o detalhe num arquivo e devolve 5 a 10 linhas.

---

## Caixa 6 — Passagem e troca de sessão

**O que isto faz:** o Claude mantém em cada projeto um arquivo de passagem (feito, pela metade, próximo passo exato) e um de resumos (uma entrada por sessão); quando a conversa fica grande ou a etapa muda, a sessão nova começa pela passagem. Foi a maior economia do autor: a conversa principal caiu 75% (medido no PC do autor, set-nov/2026; pode variar no seu uso). Avise a pessoa de não escrever senha, token ou dado pessoal nesses arquivos (vão junto se a pasta for publicada).
**Atenção:** os números desta caixa (trocar em ~250 mil) supõem a janela de 1 milhão de tokens. Veja a janela da pessoa (regra "Janela de contexto", no começo do guia; sem conseguir ver, suponha 200 mil). Se for de 200 mil, troque de sessão em ~100 mil (diga isso à pessoa na pergunta 2 e use `<100>` na regra) e não baixe a compactação da Caixa 2.

Perguntas:

1. **Passagem e resumos nos projetos com trabalho em andamento?** — cabeçalho `Passagem`
   > **Resumo** — **Ganha:** a sessão nova começa de onde a anterior parou, e dá para achar quem fez o quê. **Arrisca:** arquivos novos nos projetos sem perguntar a cada vez; passagem velha leva ao ponto errado. **Se não ligar:** a sessão nova começa do zero; `Troca`, `Lembrete` e a Caixa 7 são puladas. **Desfazer:** apague as linhas do CLAUDE.md; os arquivos criados ficam.
   - **Sim, passagem + resumos (Recomendado)** — Na primeira tarefa de várias etapas, crio sozinho `PASSAGEM.md` e `RESUMOS.md` na raiz do projeto (ou uso os que ele já tiver); uma entrada por sessão nos resumos.
   - **Só a passagem** — Só o `PASSAGEM.md`; sem arquivo de resumos, depois não há onde achar em qual sessão algo foi feito.
   - **Não** — Nada muda; a sessão nova perde o que só estava na conversa.
2. **Quando trocar de sessão?** — cabeçalho `Troca` (só se `Passagem` não foi "Não")
   > **Resumo** — **Ganha:** conversa que não incha, então cada passo relê menos. **Arrisca:** cada troca perde o que só estava na conversa; trocar tarde sai mais caro. **Se não ligar ("Só quando eu pedir"):** só um aviso; a sucessora automática (Caixa 7) fica sem gatilho. **Desfazer:** apague a linha do CLAUDE.md.
   - **~200 mil ou etapa nova** — Mais trocas, cada passo relê menos. Etapa nova sempre começa em sessão nova.
   - **~250 mil ou etapa nova (Recomendado)** — Na conta do autor (260 sessões), entre 200 e 300 mil o custo total quase não muda; acima de ~300 mil cada passo relê tanto que sai mais caro.
   - **~300 mil ou etapa nova** — Menos trocas, cada passo mais caro. Vale quando a passagem perde muito do que a conversa sabia.
   - **Só quando eu pedir** — Só aviso em uma linha quando a conversa passar de ~250 mil.
3. **Uma tarefa por sessão?** — cabeçalho `Uma tarefa`
   > **Resumo** — **Ganha:** conversas curtas e focadas, mais baratas. **Arrisca:** mais sessões abertas para você acompanhar. **Se não ligar:** assuntos se acumulam na mesma conversa, que incha. **Desfazer:** apague a linha do CLAUDE.md.
   - **Sim (Recomendado)** — Assunto novo e sem ligação vai para uma sessão nova (ou `/clear`).
   - **Não** — Nada muda; assuntos se acumulam na mesma conversa.
4. **Lembrete de começo de sessão para ler a passagem?** — cabeçalho `Lembrete` (só se `Passagem` não foi "Não"; com Python)
   > **Resumo** — **Ganha:** o Claude lembra de ler a passagem ao abrir a pasta. **Arrisca:** script sem rede que só lista a pasta; não aprova nem bloqueia nada. **Se não ligar:** só a regra do CLAUDE.md manda ler a passagem, e o Claude pode esquecer. **Desfazer:** apague a entrada de `handoff_reminder.py` em `"SessionStart"` do `settings.json`.
   - **Sim (Recomendado)** — Script (`handoff_reminder.py`, começo de sessão) que, se a pasta tiver um `PASSAGEM*.md` ou `HANDOFF*.md`, mostra uma linha mandando ler o arquivo primeiro. Só lista a pasta. Custo: uma linha por sessão nessas pastas.
   - **Não** — Nada muda; sem o lembrete o Claude pode esquecer a passagem.

Passos:
1. Pergunta 1 "Sim, passagem + resumos" ou "Só a passagem": copie `pt/PASSAGEM_MODELO.md` para `<pasta de configuração>/modelos/PASSAGEM_MODELO.md` (crie `modelos` se não existir). Só no "Sim, passagem + resumos": copie também `pt/RESUMOS_MODELO.md` para `<pasta de configuração>/modelos/RESUMOS_MODELO.md`. Grave a regra da versão escolhida.
2. Pergunta 2: grave a regra com o número escolhido, ou a regra "Só quando eu pedir". Diga à pessoa onde ver o tamanho da conversa: no app, o indicador de contexto junto da caixa de mensagem; no terminal, o comando `/context`.
3. Pergunta 3: grave a regra. Lembre a pessoa: só ela pode digitar `/clear` ou `/compact`; o Claude não consegue.
4. Pergunta 4 "Sim":
   1. Copie `scripts/handoff_reminder.py` para `<pasta de configuração>/hooks/handoff_reminder.py`.
   2. No `settings.json`, dentro de `"hooks"`, acrescente em `"SessionStart"` (crie a lista se não existir; se já houver itens nela, acrescente este como mais um item da lista, sem apagar nem trocar os outros; o relatório diário da Caixa 8 entra do mesmo jeito, como item separado):

      ```json
      "SessionStart": [
        {
          "matcher": "startup",
          "hooks": [
            { "type": "command", "command": "python \"<pasta de configuração>/hooks/handoff_reminder.py\"", "timeout": 10 }
          ]
        }
      ]
      ```

   3. Confira com `python <pasta de configuração>/hooks/handoff_reminder.py --test` (a última linha tem que ser `ALL OK`) e depois com `check_settings.py`. O lembrete aparece na próxima sessão aberta numa pasta com passagem.
5. Se houver um projeto com trabalho em andamento agora, ofereça criar o `PASSAGEM.md` dele (e o `RESUMOS.md` ao lado, se a pergunta 1 foi "Sim, passagem + resumos") (só com sim).

Texto da regra (na troca de sessão, grave uma das duas versões):
> - Passagem: todo projeto com trabalho em andamento tem um arquivo de passagem (o que o projeto já tiver, ou `PASSAGEM.md` na raiz, a partir de `<pasta de configuração>/modelos/PASSAGEM_MODELO.md`). No primeiro trabalho de várias etapas num projeto, criar o arquivo sozinho (e o de resumos, abaixo). Reescrever, não acrescentar no fim. Anotar na passagem os passos feitos ao fechar cada parte, antes da troca de sessão e quando o vigia de gasto avisar. Pergunta sem resposta vai na seção "Perguntas à pessoa". Sessão nova começa lendo a passagem e faz o "próximo passo exato" sem perguntar, exceto ações irreversíveis, que pedem confirmação. Nunca escrever senha, token ou dado pessoal na passagem.
> - **[Número]** Troca de sessão: com a conversa em ~<250> mil tokens, ou numa etapa nova, fechar a parte em andamento, atualizar a passagem e trocar de sessão. Se não houver regra de sucessora, dizer à pessoa em uma linha o que colar na sessão nova.
> - **[Só quando eu pedir]** Troca de sessão só quando a pessoa pedir; avisar em uma linha quando a conversa passar de ~<250> mil tokens.
> - Uma tarefa por sessão: assunto novo e sem ligação vai para sessão nova.
> - **[Só com passagem + resumos]** Resumos: todo projeto com arquivo de passagem tem, ao lado dele, um arquivo de resumos (`PASSAGEM.md` → `RESUMOS.md`; `PASSAGEM_X.md` → `RESUMOS_X.md`; criar sozinho a partir de `<pasta de configuração>/modelos/RESUMOS_MODELO.md`). Passo obrigatório de TODA troca de sessão e de todo fim de etapa, sem a pessoa pedir: ao fechar (antes de abrir a sucessora ou de encerrar a etapa), acrescentar no fim UMA entrada `## <n> — <título da sessão> (<data>, <id da sessão>)` com até três linhas curtas: **Fez** (com os nomes que alguém procuraria depois: arquivos, telas, ferramentas), **Decidiu** (o que ficou fechado, e por quem), **Ficou** (o que ficou aberto ou sem resposta, ou "nada"). Não relê o arquivo inteiro, só acrescenta. Serve para achar depois em qual sessão algo foi feito.

---

## Caixa 7 — Sessão sucessora automática (a mais trabalhosa)

**O que isto faz:** na hora de trocar de sessão (Caixa 6), o próprio Claude abre a sucessora, que começa pela passagem e pode abrir a próxima do mesmo jeito. Conforme as respostas, grava regras no `CLAUDE.md` e pode gravar no `settings.json` regras de permitir e o modo automático como padrão, instalar um hook (programa que o Claude Code roda antes de uma ação) que aprova ações nos "estepes" (sessões reservas, paradas e arquivadas) e guardar um token (chave de acesso) para rodadas sem tela. **A caixa toda é sensível:** não entra no modo Rápido (Grupo 3); quem quiser a roda depois, caixa por caixa.
**Avançado:** só depois de uma ou duas semanas com as outras táticas. Por quê, riscos e desfazer: `pt/DETALHES.md`, "Caixa 7".

**Rodadas sem tela (caminho B e reserva do A):** a trava é **avisar a pessoa em uma linha ANTES de abrir qualquer sessão escondida** e lançar com `--reason "<motivo curto>" --notified`; o script anota cada rodada em `<pasta de configuração>/quota_keeper/relay_log.jsonl` (nunca o token).

Pré-requisito: Caixa 6, pergunta 1 (`Passagem`), respondida "Sim, passagem + resumos" ou "Só a passagem"; sem arquivo de passagem, pule a caixa. Se rodada depois, noutra sessão, refaça `Onde usa` e `Plano` da Caixa 1 e veja no `CLAUDE.md` o que as Caixas 5 e 6 gravaram.

**Roteiro (Claude):**
- Explique à pessoa os dois caminhos. **A, pelo app** (visível, sem token, recomendado): uma ferramenta do app desktop abre outra sessão, que aparece na barra lateral. **B, pelo terminal** (sem tela, precisa de token): um script roda `claude -p` em rodadas de conversa vazia, lendo e atualizando a passagem; não aparece no app. Só para quem usa só o terminal: no app, estepes, "avisar e seguir" e tarefa agendada cobrem as recusas.
- Antes de qualquer pergunta (Caixa 1 = "App desktop" ou "Os dois"): ache as ferramentas com ToolSearch (lista no passo 1 do caminho A) e veja o modo de permissão (`get_session` "self", campo `permissionMode`).
- Sem `start_session`: o caminho A não existe nesta versão; diga em uma linha e trate como "Terminal" (sem as perguntas 1, 2, 5 a 10). Com "Agora não" na 3, grave só "[Eu abro]" (o Claude atualiza a passagem e **avisa a pessoa para abrir a sessão nova**), sem as regras de fechar a anterior e de herança; ponha "Sessão sucessora automática (sem a ferramenta no app)" em "Recusadas" e pule os passos do caminho A.
- "Terminal": sem as perguntas 1, 2, 5 a 10. Faça só a 3 e, com "Sim, me guie", a 4 numa segunda chamada; "(Recomendado)" em **"Sim, me guie"**. A sucessora é a regra do caminho B; com "Agora não", "[Eu abro]".
- "App desktop" ou "Os dois": sem a 3 e a 4 (trate como "Agora não", sem pôr em "Recusadas"). Máximo de quatro perguntas por chamada do AskUserQuestion; as condicionais só depois da resposta que as libera. 1ª chamada: só a 1. 2ª, só se a 1 for "O Claude, sozinho": 2, 5, 6 e 8 (com as outras respostas da 1 não há anterior a fechar, reserva nem Remote Control de sucessora a decidir). 3ª, só com o que a 2ª liberou: 7 e 10 (se a 6 for "Sessão de estepe") e 9 (se a 5 for "Liberar as duas regras"); sem nada liberado, não há 3ª. Com "O Claude propõe, eu clico" ou "Eu abro" na 1, só a 1ª. Na regra "[O Claude, sozinho]", o "Se isso também falhar" fica "aviso a pessoa em uma linha".
- Antes de cada chamada, mostre os Resumos das perguntas dela (regra 3 de "Como conduzir"; detalhe em `pt/DETALHES.md`, "Caixa 7").
- "Chave de API" (Caixa 1): sem a 3 (como "Agora não"; com "Terminal" também, fica "[Eu abro]"). "Não sei": faça a 3, dizendo que o token só existe nas assinaturas (Pro, Max, Ultra, Team e Enterprise); se o comando recusar a conta, "Agora não".
- Pergunta 9: "(Recomendado)" em **"Sim, automático"** só se `permissionMode` for `auto`; se for outro, ou não deu para ver, em **"Não mudar"**. Nunca ponha o modo automático como padrão sem a 9 = "Sim, automático".

1. **Quem abre a sessão sucessora?** — cabeçalho `Sucessora` (sensível: abre sessões sozinho; só no app, com `start_session`)
   > **Resumo** — **Ganha:** a troca acontece sem esperar clique seu. **Arrisca:** abre sessões sozinho e cada uma relê as instruções (mais cota); passagem mal feita faz a nova partir do ponto errado. **Se não ligar:** "propõe" e "Eu abro" funcionam; 2 e 5 a 10 puladas. **Desfazer:** apague "Sucessora:", "Troca com agente rodando:" e "Herança" do `CLAUDE.md`; arquive as sessões abertas.
   - **O Claude, sozinho (Recomendado)** — Atualiza a passagem, abre a sucessora e para; ninguém pede seu ok e a cadeia segue até a passagem dizer que acabou.
   - **O Claude propõe, eu clico** — Aparece um cartão; nada abre sem seu clique, e se você não olhar o trabalho para.
   - **Eu abro** — O Claude atualiza a passagem e diz o que colar na sessão nova; a mais segura e a que dá mais trabalho.
2. **A sucessora fecha a anterior?** — cabeçalho `Fechar mãe` (sensível: arquiva sessões; só se `Sucessora` for "O Claude, sozinho")
   > **Resumo** — **Ganha:** a anterior não relê tudo a cada turno da nova. **Arrisca:** arquivar algo vivo (a regra não força; arquivar não apaga). **Se não ligar:** as duas ficam abertas e a anterior gasta cota. **Desfazer:** apague "Fechar a anterior:"; desarquive.
   - **Sim (Recomendado)** — A sucessora se solta da anterior e a arquiva. O título ganha um número ("Site" → "Site 2" → "Site 3").
   - **Não** — Nada é arquivado sozinho; a anterior pode reler a conversa a cada turno da nova até você arquivá-la.
3. **Instalar o token para as rodadas sem tela (caminho B)?** — cabeçalho `Token` (sensível: grava uma chave da conta em arquivo; só no terminal, fora de "Chave de API", com Python)
   > **Resumo** — **Ganha:** no terminal a cadeia anda sozinha (rodadas sem tela). **Arrisca:** chave da conta num arquivo, válida por um ano; rodadas escondidas gastam cota (por isso o aviso antes). **Se não ligar:** no terminal você abre a nova sessão; no app o caminho A cobre. **Desfazer:** apague `relay_token.txt`, `tools/session_relay.py` e a regra "Rodadas sem tela:".
   - **Sim, me guie** — Você roda um comando, faz login no navegador e grava o token num arquivo; o Claude nunca o vê. Uns 10 minutos.
   - **Agora não** — Nada é gravado; o resto do pacote funciona.
   Depois de "Sim, me guie", diga em uma linha que o **relatório diário é recomendado** para quem usa rodadas sem tela e que a Caixa 8 pergunta.
4. **O que as rodadas sem tela podem usar?** — cabeçalho `Permissões` (só se `Token` for "Sim, me guie")
   > **Resumo** — **Ganha:** você decide o que uma rodada escondida toca. **Arrisca:** ninguém aprova nada na rodada; ela pode sobrescrever arquivos (use git) e, com terminal, rodar comandos. **Se não ligar:** só existe com o token. **Desfazer:** troque `--tools` na regra "Rodadas sem tela:".
   - **Só arquivos (Recomendado)** — Ler, buscar, criar e editar arquivos; nenhum comando.
   - **Arquivos + terminal** — Também roda comandos (testes, compilação); o terminal da rodada também enxerga o token.
   - **Decidir por projeto** — O Claude pergunta na primeira vez em cada projeto; nada roda sem esse sim.
5. **Liberar a reserva por tarefa agendada?** — cabeçalho `Agendada` (sensível: grava regras de permitir; só se `Sucessora` for "O Claude, sozinho")
   > **Resumo** — **Ganha:** reserva quando o app recusa abrir a sessão. **Arrisca:** duas regras de permitir valem para TODAS as sessões da conta; texto malicioso poderia induzir a agendar algo sem ninguém olhando. **Se não ligar:** a reserva vira rodadas sem tela ou aviso; a 9 é pulada. **Desfazer:** tire as duas linhas de `"allow"` e apague a tarefa `sucessora-<pasta>`.
   - **Liberar as duas regras (Recomendado)** — O Claude cria e roda a tarefa agendada sem pedir aprovação, só como reserva; sem as regras, o modo automático costuma barrá-la.
   - **Não liberar** — Nada é gravado; a reserva é o caminho B (se instalado) ou um aviso a você.
6. **Quando o app recusar abrir a sucessora?** — cabeçalho `Recusa` (sensível: pode criar e reativar sessões sozinho; só se `Sucessora` for "O Claude, sozinho")
   > **Resumo** — **Ganha:** a troca funciona quando o app recusa abrir sessão. **Arrisca:** estepes são sessões criadas sem você ver; "Avisar e seguir" deixa a conversa crescer (passos mais caros); "Reserva na hora" pode esconder a sucessora em Rotinas. **Se não ligar:** use "Avisar e seguir"; 7 e 10 puladas. **Desfazer:** apague "Estepes:" e "Avisar e seguir:"; arquive os estepes.
   - **Sessão de estepe (Recomendado)** — A cada mensagem sua, o Claude repõe sessões paradas e arquivadas na pasta (os "estepes"; quantos, a 7 diz). Na troca, desarquiva um, dá o título novo e manda a tarefa por mensagem: a sucessora sai na hora, na lista normal. Sem estepe na pasta, cai no "Avisar e seguir".
   - **Avisar e seguir** — Grava a passagem, manda um aviso (no computador e, com Remote Control, no celular) e continua nesta sessão; na sua próxima mensagem abre a sucessora na lista normal. A reserva (tarefa agendada, rodadas sem tela) fica para quando a conversa passar muito do limite sem resposta sua. Não cria sessão antes da sua mensagem.
   - **Reserva na hora** — Usa logo a reserva; se for tarefa agendada, a sucessora fica escondida em Rotinas e não abre a próxima sozinha.
7. **Quantos estepes por pasta?** — cabeçalho `Estepes` (só se a pergunta 6 for "Sessão de estepe"; a opção "Outro" da caixa deixa a pessoa digitar outro número)
   > **Resumo** — **Ganha:** mais trocas cobertas sem você na tela. **Arrisca:** até esse número de sessões vazias criadas sem você ver, cada uma com um turno curto ao nascer; sem número medido. **Se não ligar:** 6 é o mínimo; sem estepe cai em "Avisar e seguir". **Desfazer:** mude o número em "Estepes:" e arquive os que sobrarem.
   - **10 (Recomendado)** — Cobre uma noite com várias trocas, mesmo com várias sessões na mesma pasta; cria até 10 sessões na primeira mensagem sua depois da instalação.
   - **6** — O mínimo: basta para uma ou duas sessões por pasta.
   - **16** — Para muitas sessões na mesma pasta por muito tempo sem você voltar; cria mais sessões e gasta mais turnos curtos.
8. **Ligar o Remote Control?** — cabeçalho `Remote` (sensível: só no app desktop, caminho A, e se `Sucessora` for "O Claude, sozinho").
   > **Resumo** — **Ganha:** seguir a cadeia de longe e receber o aviso no celular. **Arrisca:** quem entrar na sua conta claude.ai ou pegar o celular desbloqueado manda ordens ao computador, com as permissões da sessão. **Se não ligar:** tudo funciona; o aviso só aparece no computador. **Desfazer:** apague "Remote Control:"; desligue em cada sessão e a opção do app.
   - **Só nas sucessoras (Recomendado)** — Liga o Remote Control em cada sucessora que abre (lista normal, estepe ou tarefa agendada); as outras sessões ficam como você deixar.
   - **Ligar já** — O mesmo, e liga agora o desta sessão; para toda sessão nova, ligue a opção do app (em novembro de 2026, "Connect new sessions to Remote Control", nas configurações).
   - **Não usar** — O Claude nunca liga o Remote Control; ainda desliga o da sessão anterior antes de arquivá-la, se estiver ligado.
9. **Começar toda sessão no modo automático?** — cabeçalho `Auto padrão` (sensível: muda o modo padrão de permissão; só se a pergunta 5 for "Liberar as duas regras")
   > **Resumo** — **Ganha:** a sucessora da tarefa agendada não para no primeiro comando. **Arrisca:** TODA sessão nova passa a ser julgada por um filtro automático, que erra nos dois lados (regras de negar valem). **Se não ligar:** essa sucessora espera sua aprovação no primeiro comando. **Desfazer:** tire `"defaultMode": "auto"` (ou volte o valor da cópia da Caixa 1).
   - **Sim, automático** — Toda sessão nova começa no modo automático, inclusive a sucessora da tarefa; para quem já trabalha nele.
   - **Não mudar** — O modo padrão fica como está; a sucessora da tarefa para no primeiro comando ou edição, esperando você aprovar.
10. **Instalar o hook que aprova ações nos estepes?** — cabeçalho `Hook estepe` (sensível: aprova ações sozinho; só se a pergunta 6 for "Sessão de estepe"; com Python)
   > **Resumo** — **Ganha:** a troca por estepe passa sem caixa de aprovação. **Arrisca:** aprova sozinho seis ações (mensagem, desarquivar, título, modelo, esforço, Remote Control), só em ids de `spares.txt`; se falhar, não aprova nada. **Se não ligar:** nada é aprovado sozinho; cai em "Avisar e seguir". **Desfazer:** tire o bloco `PreToolUse` e apague `spare_allow.py`, o log e `spares.txt`.
   - **Instalar o hook (Recomendado)** — As seis ações ficam aprovadas só nos estepes listados.
   - **Sem o hook** — Nada é aprovado sozinho; a troca pode cair no "Avisar e seguir" ou você aprova na caixa.

### Passos do caminho A (app desktop)

Só se a Caixa 1 respondeu "App desktop" ou "Os dois" e `start_session` existe. Se respondeu "Terminal", ou se a ferramenta não existe, vá direto para o caminho B (ou, sem ele, para a regra mínima acima).

1. **Ferramentas** (ache com ToolSearch, pelo nome): `start_session` (abrir sessão), `create_scheduled_task`, `list_scheduled_tasks` e `run_scheduled_task` (criar, listar e rodar tarefa agendada), `set_session_title`, `detach_session`, `archive_session` e `unarchive_session` (título; soltar, arquivar e desarquivar), `list_sessions` e `get_session`, `set_remote_control`, `set_session_effort` e `set_session_model` (esforço e modelo de outra sessão), `list_task_runs` (sessões abertas por uma tarefa), `list_sections` (seções da barra lateral), `PushNotification` (aviso no computador e, com Remote Control, no celular) e `SendMessage` (mensagem para outra sessão). Em novembro de 2026 existiam com esses nomes. Antes de qualquer `set_remote_control`, veja `remoteControlState` com `get_session` e só chame se o estado for outro (chamar à toa pode abrir caixa de aprovação ou desligar o que se queria ligado). Chame `start_session` com initiation "user_asked" ("offer" e "own_initiative" viram cartão esperando clique) e contexto "fresh".
2. **Grave as regras** abaixo: a da pergunta 1 (uma das três); a de fechar a anterior se a 2 for "Sim"; pela 6, "Avisar e seguir" = a de avisar e seguir, "Sessão de estepe" = a dos estepes (com o número da 7) e também a de avisar e seguir, "Reserva na hora" = nada a mais; a de troca com agente rodando se a 1 for "O Claude, sozinho"; a do Remote Control se a 8 não for "Não usar" (com "Ligar já", ligue agora o desta sessão: veja `remoteControlState` e só chame `set_remote_control` com "self" e true se estiver desligado; diga onde fica a opção do app para sessões novas); sempre a de herança. Com a 2 "Não", não grave a de fechar a anterior e, na de troca com agente rodando, tire o trecho em que a anterior se arquiva sozinha. Diga à pessoa que o pedido da sucessora leva o id da sessão atual ("Sessão anterior: <id>", de `list_sessions` ou `get_session`), para ela saber quem arquivar; com a tarefa só manual (passo 4), o pedido vai no `SUCESSORA.md`.
3. **Grave só o que a pessoa aceitou**, no `<pasta de configuração>/settings.json` (não no do projeto: lá o modo automático como padrão não vale). Cada item é sensível: só com a resposta da pergunta dele e, no modo "Caixa por caixa, conferindo", mostre o trecho e espere o "Gravar". Nunca grave `"defaultMode"`, regra de permitir nem hook por conta própria:
   - Pergunta 5 "Liberar as duas regras": em `"permissions"` → `"allow"`, os nomes exatos das ferramentas de criar e de rodar tarefa agendada como o ToolSearch mostrou (em novembro de 2026: `"mcp__scheduled-tasks__create_scheduled_task"` e `"mcp__scheduled-tasks__run_scheduled_task"`). Crie o que faltar e não apague o que existe.
   - Pergunta 9 "Sim, automático": em `"permissions"` ponha `"defaultMode": "auto"`. Com "Não mudar", não mexa nesse campo.
   - Pergunta 5 "Não liberar": nada no `settings.json`; na regra da pergunta 1, apague o trecho de "uso uma tarefa agendada" até "Se isso também falhar:", inclusive.
   - Pergunta 10 "Instalar o hook": copie `scripts/spare_allow.py` para `<pasta de configuração>/hooks/spare_allow.py`, crie `<pasta de configuração>/spares.txt` vazio e, em `"hooks"` → `"PreToolUse"`, acrescente `{ "matcher": "SendMessage|mcp__ccd_session_mgmt__.*", "hooks": [ { "type": "command", "command": "python \"<pasta de configuração>/hooks/spare_allow.py\"", "timeout": 10 } ] }` (troque `mcp__ccd_session_mgmt__` pelo começo do nome que o ToolSearch mostrou). O hook aprova sozinho as ações da troca só quando o alvo é um estepe listado em `spares.txt` (por que ele existe e o teste: `pt/DETALHES.md`, "Caixa 7 · Hook estepe"). Não use regra de permitir para essas ferramentas: valeria para todas as sessões. Com "Sem o hook": não copie nem registre nada, não crie `spares.txt` e, na regra "Estepes", apague os trechos sobre `spares.txt`.

   Confira com `check_settings.py`. Diga que o modo automático como padrão exige uma versão recente do Claude Code e um plano com esse modo; sem isso, a sessão começa no modo normal.
4. **Travas do app** (detalhe só se a pessoa perguntar: `pt/DETALHES.md`, "Caixa 7 · Travas do app"): o app recusa abrir sessão em turno que não veio de mensagem da pessoa (resposta numa caixa de pergunta não destrava); recusa arquivar sessão com trabalho vivo; a tarefa agendada não herda o modo de permissão e fica na seção Rotinas, sem `start_session` (confira com `list_sections` que a seção está ligada e ponha sempre o link da sessão nova na mensagem final).
5. **Teste** (com sim da pessoa; abre uma sessão de verdade e gasta um pouco de cota):
   1. Crie `~/Documents/teste_sucessora/` (não na pasta de configuração, que é protegida) com um `PASSAGEM.md` cujo próximo passo exato é: *"Crie `ok.txt` com a palavra ok e escreva ETAPA CONCLUIDA na primeira linha desta passagem."*
   2. Abra uma sessão "Teste de sucessora" com o pedido: *"Teste de instalação: não arquive nem solte nenhuma sessão. Leia e siga `<caminho>/PASSAGEM.md`."* (Sem essa frase, a regra de fechar a anterior poderia soltar ou arquivar a sessão de instalação.)
   3. Confira com `list_sessions` que ela apareceu e, ao terminar, que `ok.txt` existe. Diga que a pessoa pode arquivar a sessão de teste e apagar a pasta.

Texto da regra (pergunta 1, uma das três):
> - **[O Claude, sozinho]** Sucessora: na hora de trocar de sessão, eu mesmo abro a sucessora, sem a pessoa pedir (`start_session`, initiation "user_asked", contexto "fresh", pedido "Leia e siga <passagem>. Sessão anterior: <id>" + as regras de sucessora desta seção; o <id> é o desta sessão, achado com `list_sessions` ou `get_session`), aviso em uma linha com o link e paro. Não abro sucessora se a passagem diz ETAPA CONCLUIDA ou tem pergunta à pessoa que impede o próximo passo. Título = título atual + número ("Site" → "Site 2"). Nunca termino com "abra uma sessão nova", nem deixo cartão esperando clique. Se o app recusar ou virar cartão: uso uma tarefa agendada. Se esta sessão não foi aberta por tarefa e existe a tarefa só manual `sucessora-<pasta do projeto>` (`list_scheduled_tasks`), reescrevo `SUCESSORA.md` na pasta com o mesmo pedido e logo rodo a tarefa (`run_scheduled_task`); senão (ou se o app recusar rodar), crio na hora uma tarefa de uma vez para ~2 minutos depois, com o mesmo pedido. Confiro em `list_task_runs` que ela abriu; ajusto nela o título, o Remote Control (só com a regra do Remote Control) e o esforço (`set_session_title`, `set_remote_control`, `set_session_effort`), se der; e confiro com `list_sections` se a seção Rotinas da barra lateral está ligada (só lá a sessão aparece): se não estiver, aviso a pessoa em uma linha de onde ligar. Ponho sempre o link da sessão nova na mensagem final (a tarefa de uma vez some da barra lateral depois de rodar). Numa sessão comum (não aberta por tarefa) na pasta de um projeto com passagem, se a tarefa só manual da pasta não existe, eu a crio: sem horário, `notifyOnCompletion` false, título "Sucessora <pasta>", pedido "Leia `SUCESSORA.md` nesta pasta e siga o que ele diz." Se isso também falhar: <rodadas sem tela, regra abaixo | aviso a pessoa em uma linha>. Quando der, deixo a troca para um turno que veio de mensagem da pessoa.
> - **[O Claude propõe]** Sucessora: na hora da troca, atualizo a passagem e proponho a sessão nova (cartão), com o pedido "Leia e siga <passagem>".
> - **[Eu abro]** Sucessora: na hora da troca, atualizo a passagem e digo em uma linha o que colar na sessão nova: "Leia e siga <passagem>".

Texto da regra (pergunta 2 "Sim"):
> - Fechar a anterior: a sucessora, logo no começo, se solta da sessão que a abriu (`detach_session`), desliga o Remote Control da anterior (`set_remote_control` com o id dela e false) e arquiva a sessão cujo id vem em "Sessão anterior: <id>" no pedido (`archive_session`). Se a seção "Rodando na mãe" da passagem citar a própria sessão anterior, ela não a arquiva: essa se arquiva sozinha quando os agentes dela devolverem (regra de troca com agente rodando). Se recusar porque a anterior ainda está trabalhando ("still working" ou "in use": ela ainda escreve a última mensagem; nos testes de 04/11/2026 a recusa sumiu assim que ela terminou o turno), tenta de novo a cada ~30 segundos por até ~2 minutos (espera com um comando em segundo plano, como `sleep 30`, e confere `isRunning` com `get_session`). Se ainda recusar, tenta de novo no fim do primeiro turno e no começo de cada turno que vier de mensagem da pessoa, até conseguir; se a recusa falar de agente ou tarefa em segundo plano, não força: avisa em uma linha que a pessoa pode arquivar pela barra lateral. Antes de abrir a sucessora, a sessão encerra os agentes e tarefas em segundo plano que já entregaram. Não vale para sessão paralela de outra tarefa (essa não arquiva ninguém).

Texto da regra (pergunta 6 "Avisar e seguir"; troque `<400>` pelo limite da Caixa 6 + 150 mil):
> - Avisar e seguir: se o app recusar abrir a sucessora (turno que não veio de mensagem da pessoa) ou virar cartão, ainda não troco: gravo a passagem, mando `PushNotification` ("<título>: hora de trocar de sessão, responda qualquer coisa aqui") e continuo o trabalho nesta sessão. Quando chegar mensagem nova da pessoa, antes de qualquer outra coisa atualizo a passagem e abro a sucessora com `start_session`; agentes ainda rodando aqui seguem a regra de troca com agente rodando. A reserva da regra da sucessora (tarefa agendada, rodadas sem tela, aviso) fica só para o teto: a conversa passar de ~<400> mil tokens sem mensagem da pessoa.

Texto da regra (pergunta 6 "Sessão de estepe"; troque `<10>` pelo número da pergunta 7; grave também a de avisar e seguir):
> - Estepes: a cada mensagem nova da pessoa (o único turno em que `start_session` passa), confiro os estepes da pasta do projeto (`list_sessions` com as arquivadas, título "Estepe <pasta> N"). Para cada número de 1 a <10> sem estepe (usado numa troca ou nunca criado), crio um com esse número, sem passar de <10>: `start_session` "user_asked", contexto "fresh", `use_worktree` false, título "Estepe <pasta> N" (e ponho o id dele em `spares.txt`), pedido "Sessão ESTEPE: não faça nada, não leia arquivos, não chame ferramentas, não siga as regras de começo de sessão; responda só 'pronta' e pare. Mais tarde outra sessão vai mandar a tarefa por mensagem; aí siga a mensagem.", no meu esforço (alto: é o que a maioria das trocas pede, e a resposta "pronta" custa quase o mesmo). Quando cada uma responder "pronta", solto (`detach_session`) e arquivo (`archive_session`; se recusar, mesma espera de ~30 s por até ~2 min da regra de fechar a anterior). Na troca, se o app recusar abrir a sucessora ou virar cartão, e a pasta tiver estepe: desarquivo o de menor número (`unarchive_session`), troco o título dele para o título atual + número + " · <modelo> <esforço>" (ex.: "Site 3 · Opus 5.5 Alto"; ao somar o número, ignoro esse final), porque o rodapé da caixa de texto pode mostrar outro modelo e esforço (`set_session_title`), ponho nele o modelo e o esforço que a tarefa pede (`set_session_model`, `set_session_effort`; valem a partir do próximo turno, por isso antes da mensagem), mando por `SendMessage` o pedido da sucessora (com "Sessão anterior: <id>", "esqueça o pedido de não fazer nada: agora siga todas as regras" e "não faça `detach_session`: você já está solta"), depois, com a regra do Remote Control, ligo o dele (`set_remote_control`), tiro o id dele de `spares.txt` (já não é estepe), aviso em uma linha com o link e paro. Sem estepe na pasta: avisar e seguir.

Texto da regra (pergunta 1 "O Claude, sozinho"; troque `<180>` por cerca de 0,7 × o limite da Caixa 6, arredondado para a dezena mais próxima: 250 → 180, 200 → 140, 300 → 210, 100 → 70; na escolha, deixe a primeira opção se a Caixa 5, pergunta 5, instalou a trava de cópia):
> - Troca com agente rodando: (1) Antes de lançar um agente que deve passar de ~20 minutos, olho o tamanho da conversa; a partir de ~<180> mil, troco primeiro e a sucessora o lança. (2) Na hora de trocar, com um agente meu rodando, troco como de costume e o agente continua aqui, na sessão anterior (a "mãe"). A passagem ganha uma seção "Rodando na mãe": o título desta sessão e cada agente vivo, com a pasta dele, o que faz e quando deve acabar; a sucessora não relança esse trabalho. Divido o que sobrou: tarefa que mexe na mesma pasta e cabe no tempo que os agentes da mãe ainda precisam (ou passa um pouco dele, até ~1/4 a mais), a mãe lança agora, num agente; o resto vai para a sucessora, que começa pelo que NÃO mexe nessa pasta e só pega o trabalho da pasta depois que a mãe a liberar (<a trava de cópia garante | antes de mexer nessa pasta, ela confere que a seção "Rodando na mãe" diz que foi liberada>). Pode ser que isso só caiba à sucessora da sucessora: a passagem leva a seção adiante até a pasta ser liberada. A mãe não pega outra tarefa. Quando o último agente dela devolve, a mãe grava o resultado na passagem, avisa por `SendMessage` a sessão mais nova da cadeia (a de título com o maior número, vista em `list_sessions`) que a pasta foi liberada e onde está o resultado, e se arquiva (`archive_session` com "self"); se recusar, a sucessora a arquiva. (3) Agente com espera longa (compilação, render, testes demorados) espera em pedaços de no máximo ~10 minutos, para a mensagem de parar chegar logo.

Texto da regra (pergunta 8 "Só nas sucessoras" ou "Ligar já"):
> - Remote Control: toda sucessora que eu abro (lista normal, estepe ou tarefa agendada) fica com o Remote Control ligado, para a pessoa acompanhar de longe. Logo depois de abrir, vejo `remoteControlState` com `get_session` e, se estiver desligado, ligo (`set_remote_control` com o id dela e true); no estepe, só depois da mensagem com a tarefa. A sucessora, no começo, faz o mesmo com a própria ("self"). Nunca chamo `set_remote_control` sem ver o estado antes.

Texto da regra (sempre que esta caixa for aceita):
> - Herança (não com a regra "[Eu abro]" sozinha): o pedido de toda sessão sucessora repete as regras de sucessora desta seção, para ela abrir a próxima do mesmo jeito.

### Passos do caminho B (token e rodadas sem tela)

Só se a pergunta 3 foi "Sim, me guie". Leia e siga `pt/DETALHES.md`, "Caixa 7 · Passos do caminho B", um passo por vez, esperando a pessoa dizer que fez: conferir o Claude Code de terminal, a pessoa gerar e gravar o token sem que você o veja, conferir sem ver, proibir a leitura do arquivo, copiar `session_relay.py`, teste num projeto de brinquedo, a lista `--tools` da pergunta 4 e os furos a explicar. Depois grave a regra abaixo.

Texto da regra (caminho B):
> - Rodadas sem tela: antes de lançar, aviso a pessoa em uma linha (o que vai rodar, por quê, quantas rodadas, que gasta a cota dela) e só então lanço: `python <pasta de configuração>/tools/session_relay.py --folder <projeto> --handoff <passagem> --model sonnet --rounds 3 --tools "<lista>" --reason "<motivo curto>" --notified`, solto em segundo plano (Windows: `Start-Process ... -WindowStyle Hidden -PassThru`; Mac e Linux: `nohup ... &`), guardando o número do processo. Nunca lanço sem avisar antes. Uso: <quando estou no terminal | só como reserva, quando o app recusar abrir sessão>. Na próxima mensagem da pessoa, confiro o `relay.log` do projeto e, se a passagem não diz ETAPA CONCLUIDA e nada está rodando, aviso de novo e lanço de novo, ou abro a sucessora. Tarefa longa: `--timeout` maior. Nunca leio, mostro nem copio `relay_token.txt`.

---

## Caixa 8 — Vigia de gasto e medição

**O que isto faz:** scripts que avisam o Claude quando a sessão passa de certos limites e medem o gasto; o Claude conta à pessoa em uma linha e propõe o que fazer (passagem, sucessora, agente mais barato). No uso do autor, 14 de 36 trocas de sessão só aconteceram depois de 250 mil tokens, até o vigia avisar no meio do turno. Nenhum script usa rede nem bloqueia ou aprova nada.

Plano (Caixa 1): com "Chave de API", não faça as perguntas 2 e 3 (não há % semanal) e não as ponha em "Recusadas"; o vigia (pergunta 1) serve do mesmo jeito, porque avisa em tokens. Com "Team ou Enterprise" ou "Não sei", faça as duas, mas diga que só funcionam se a tela de uso mostrar um % de limite semanal; se, na hora de ler, não houver nenhum %, pare e avise a pessoa.

Perguntas (são 5; a caixa de perguntas aceita 4 por chamada: faça em 2 chamadas, as perguntas 1 a 4 e depois a 5; pule as que não se aplicam):

1. **Instalar o vigia de gasto?** — cabeçalho `Vigia` (só com Python)
   > **Resumo** — **Ganha:** aviso antes de a conversa ou um agente ficar caro demais. **Arrisca:** lê os registros locais só para contar; não bloqueia nem aprova nada; se falhar, fica mudo. **Se não ligar:** sem aviso de conversa grande; a troca de sessão (Caixa 6) depende de o Claude notar sozinho. **Desfazer:** apague `hooks/spend_watch.py` e as duas linhas dele em `"UserPromptSubmit"` e `"PostToolUse"`.
   - **Sim, limites do autor (Recomendado)** — Avisa com a conversa em 200 mil tokens (e a cada 100 mil a mais), aos 40, 80 e 150 prompts, e quando um agente chega a 100 e a 150 chamadas.
   - **Sim, avisar mais cedo** — Conversa em 150 mil; agente em 60 e 100 chamadas. Mais avisos, em troca de trocar de sessão antes.
   - **Não** — Nada é instalado; sem aviso de conversa grande.
2. **Conferir o uso antes e depois de tarefa grande?** — cabeçalho `Antes/depois` (fora de "Chave de API")
   > **Resumo** — **Ganha:** você vê quanto da cota uma tarefa grande custou. **Arrisca:** uma regra de texto e uma linha a mais na mensagem final. **Se não ligar:** você confere o uso na tela quando quiser. **Desfazer:** apague a linha do CLAUDE.md.
   - **Sim (Recomendado)** — O Claude anota o % de uso do plano antes de uma tarefa grande e diz a diferença no fim. Só uma regra; nenhum script.
   - **Não** — Nada muda.
3. **Medir quanto vale 1% da cota no seu plano?** — cabeçalho `Medir plano` (fora de "Chave de API"; com Python)
   > **Resumo** — **Ganha:** o vigia passa a avisar em % da cota, não só em tokens; base para o relatório diário. **Arrisca:** o número é estimativa (sai baixo se você usa muito o chat comum); grava um .csv pequeno. **Se não ligar:** o vigia avisa só em tokens; o relatório diário não compara com a conta. **Desfazer:** apague `tools/measure_point.py` e `tools/measure_marks.csv`.
   - **Sim** — Você anota o % de uso em dois momentos, com um ou dois dias entre eles, e um script faz a conta; depois o vigia também avisa em % da cota.
   - **Não** — O vigia avisa só em tokens.
4. **Instalar a skill de relatório de uso?** — cabeçalho `Skill uso` (só com Python)
   > **Resumo** — **Ganha:** responde "onde foi minha cota?" com a soma por sessão e por modelo. **Arrisca:** lê as conversas locais só para contar; nada sai do PC. **Se não ligar:** o Claude responde sem o relatório pronto, mais lento e menos exato. **Desfazer:** apague `skills/usage-report/` e `tools/usage_report.py`.
   - **Sim** — Copio a skill para `<pasta de configuração>/skills/usage-report/`: ao perguntar "quanto gastei" ou "onde foi minha cota", o Claude roda um script que soma o gasto por sessão e por modelo.
   - **Não** — Nada é instalado.
5. **Quer um relatório diário de uso?** — cabeçalho `Relatório` (só com Python; chamada própria, depois das 4 primeiras)
   > **Resumo** — **Ganha:** uma vez por dia o Claude pergunta se você quer o relatório de ontem (gasto deste PC por sessão e modelo; sessões sem tela sem aviso ou rodando há muito tempo; se a conta subiu mais do que este PC explica). **Arrisca:** uma linha de lembrete no começo de cada sessão nova; o script grava 3 arquivos pequenos. **Limite:** só vê este PC; a diferença com a conta é indício, não prova. **Se não ligar:** nenhum aviso de uso estranho. **Desfazer:** tire a entrada do `daily_report.py` em `"SessionStart"` e apague o script e a pasta `quota_keeper/`.
   - **Sim** — Copio o script e ponho um aviso no começo da sessão; na primeira mensagem do dia o Claude pergunta numa caixa "Quer o relatório de uso de ontem?" e só roda se você aceitar.
   - **Não** — Nada é instalado.

Na pergunta 5, ponha "(Recomendado)" em **Sim** só se `Token` foi "Sim, me guie" ou se a pessoa usa rodadas sem tela (Caixa 7).

Passos:
1. Pergunta 1 "Sim":
   1. Copie `scripts/spend_watch.py` para `<pasta de configuração>/hooks/spend_watch.py`.
   2. "Avisar mais cedo": no topo do script, troque para `CONTEXT_START = 150_000` e `AGENT_CALLS = [60, 100]`. Se a janela da pessoa for de 200 mil tokens (regra "Janela de contexto", no começo do guia; sem saber, vale 200 mil), use `CONTEXT_START = 100_000` e `CONTEXT_STEP = 50_000` em qualquer das duas opções.
   3. No `settings.json`, dentro de `"hooks"`, acrescente o mesmo comando em dois eventos (sem apagar o que já houver neles):

      ```json
      "UserPromptSubmit": [
        { "hooks": [ { "type": "command", "command": "python \"<pasta de configuração>/hooks/spend_watch.py\"", "timeout": 20 } ] }
      ],
      "PostToolUse": [
        { "hooks": [ { "type": "command", "command": "python \"<pasta de configuração>/hooks/spend_watch.py\"", "timeout": 20 } ] }
      ]
      ```
   4. Grave a regra.
   5. Conferir: abra um agente Haiku com o pedido *"SPEND-WATCH-TEST. Liste 6 arquivos desta pasta, um por chamada de ferramenta, e devolva qualquer aviso 'SPEND WATCH' que aparecer."* (essa marca faz o vigia usar limites de teste: 3 e 5 chamadas). Se o aviso não vier, a pessoa abre uma sessão nova na mesma pasta (no terminal, sair e rodar `claude` de novo) e você repete o pedido nela, ou deixe o teste para a Caixa final.
2. Pergunta 2 "Sim": grave a regra. Para ler o % de uso: no app, a ferramenta `get_usage` (procure com ToolSearch); sem ela, peça o número à pessoa (tela de uso do app ou de claude.ai, ou `/usage` no terminal).
3. Pergunta 3 "Sim":
   1. Copie `scripts/measure_point.py` para `<pasta de configuração>/tools/measure_point.py`.
   2. Leia o % semanal agora (como na pergunta 2) e rode `python <pasta de configuração>/tools/measure_point.py <%>`. Isso grava a primeira marca.
   3. Grave a regra. A partir da segunda marca, o script mostra quantos tokens de peso valem 1% da cota. Quando o resultado estiver estável (duas ou três contas parecidas), ponha esse número em `POINT`, no topo do `spend_watch.py`: o vigia passa a avisar também em % da cota.
   4. Diga à pessoa: entre duas marcas não pode ter virada da semana da cota, e o chat comum (fora do Claude Code) não entra nos registros, então o número sai baixo se ela o usa muito (detalhe: Caixa 8 · Medir plano).
4. Pergunta 4 "Sim": copie a pasta `skills/usage-report/` do pacote para `<pasta de configuração>/skills/usage-report/` e `scripts/usage_report.py` para `<pasta de configuração>/tools/usage_report.py`. Se a pergunta 3 foi "Não", copie também `scripts/measure_point.py` para `tools/` (a skill o usa para "quanto vale 1%"), sem rodá-lo. Vale na próxima sessão. Não precisa de regra no CLAUDE.md.
5. Pergunta 5 "Sim":
   1. Copie `scripts/daily_report.py` e `scripts/usage_report.py` para `<pasta de configuração>/tools/` (o relatório importa os pesos do `usage_report.py`; se `measure_point.py` também estiver em `tools/`, o `measure_marks.csv` dele é achado sozinho).
   2. No `settings.json`, em `"hooks"`, acrescente uma entrada em `"SessionStart"` (sem apagar as que existirem; se a Caixa 6 já pôs o `handoff_reminder.py` ali, é um segundo item, separado, para ser fácil de desfazer):

      ```json
      "SessionStart": [
        { "matcher": "startup", "hooks": [ { "type": "command", "command": "python -S \"<pasta de configuração>/tools/daily_report.py\" --once-a-day", "timeout": 30 } ] }
      ]
      ```
      O hook fica em `"SessionStart"` com `matcher` `startup` (uma vez por sessão nova), nunca em `"UserPromptSubmit"`.
   3. Grave a regra. Rode `python <pasta de configuração>/tools/daily_report.py --test` (a última linha deve ser `ALL OK`).
   4. Diga à pessoa que o relatório só vê este PC e vale na próxima sessão (detalhe: Caixa 8 · Relatório). Comandos úteis: `daily_report.py --date AAAA-MM-DD` (outro dia), `--max-hours H` (alerta de sessão longa; padrão 8), `--record-account <%>` (grava o % semanal da conta).

Texto da regra:
> - Vigia de gasto: quando aparecer um aviso "SPEND WATCH", contar à pessoa em uma linha, com o número, e propor o que fazer (passagem, sucessora, agente mais barato).
> - Antes e depois de tarefa grande: anotar o % de uso do plano e dizer a diferença no fim, em uma linha.
> - Medição do plano: no começo de uma sessão, se a última marca em `<pasta de configuração>/tools/measure_marks.csv` tiver mais de um dia, ler o % semanal e rodar `measure_point.py` com ele. Quando a estimativa ficar estável em duas ou três contas, propor pôr o número em `POINT` no `spend_watch.py`.
> - **[Só se a pergunta 5 foi "Sim"]** Relatório diário: se, no começo da sessão, aparecer o lembrete "Quota Keeper (once a day)", antes do pedido da pessoa pergunte numa caixa, no idioma dela, "Quer o relatório de uso de ontem?" (Ver agora / Hoje não); só se aceitar, rode `python "<pasta de configuração>/tools/daily_report.py"`, mostre a saída e siga com o pedido. Se o lembrete trouxer o aviso de "cheque barato", mencione-o. Uma vez por dia, quando conseguir ver o % semanal da conta (ferramenta de uso no app; `/usage` só a pessoa digita), rode `daily_report.py --record-account <%>`.

---

## Caixa 9 — Conferir o trabalho

**O que isto faz:** conferir é obrigatório, mas dá para conferir gastando menos. Esta caixa só grava regras de comportamento no CLAUDE.md (instruções que o Claude pode esquecer em conversa muito longa); nenhum script, hook nem permissão muda. Vale na próxima sessão.

Perguntas (duas, as duas com várias respostas: `multiSelect: true`):

1. **Quais destes hábitos viram regra?** — cabeçalho `Conferência`
   > **Resumo** — **Ganha:** conferir gastando menos (menos imagens, testes só do que mudou, revisão dupla só onde importa). **Arrisca:** um erro fora do trecho testado, ou numa área que você não considera sensível, pode passar até a bateria final; imagem só quando você pedir. **Se não marcar:** o Claude confere do jeito padrão, em geral mais caro. **Desfazer:** apague a linha da regra no CLAUDE.md.
   - **Prova barata** — Usar o texto quando ele prova; imagem recortada e menor; medidas por script. Um defeito só visível pode passar.
   - **Testes por partes** — Depois de cada mudança, os testes do que mudou e uma regressão curta; a bateria inteira antes de publicar.
   - **Duas revisões só no sensível** — Segurança, contas, pagamento e criptografia ganham duas revisões independentes; o resto, uma.
   - **Não pagar duas vezes** — Depois de uma interrupção, conferir o que ainda roda e retomar. Processo só se encerra pelo PID que a própria sessão iniciou, nunca pelo nome.
2. **Quais hábitos de fim de turno viram regra?** — cabeçalho `Fim do turno`
   > **Resumo** — **Ganha:** nada fica esquecido: pendências à vista, sessão não fica parada à toa, a resposta vem primeiro. **Arrisca:** mensagens finais um pouco mais longas e uma checagem curta ao encerrar. **Se não marcar:** perguntas pendentes podem se perder e a sessão pode parar sem aviso. **Desfazer:** apague a linha da regra no CLAUDE.md.
   - **Perguntas pendentes** — Perguntas que surgirem vão para um arquivo de perguntas do projeto e se repetem no fim de toda mensagem final.
   - **Posso encerrar?** — Antes de encerrar, o Claude se pergunta "deveria estar fazendo algo antes de encerrar?"; se não, diz o que espera e o que vai acordar a sessão.
   - **Mensagem final completa** — A resposta na primeira linha, depois as pendências e o que não saiu tão bem.

Passos: grave uma linha por item marcado; os não marcados vão para "Recusadas". Se "Perguntas pendentes" foi marcado, crie `PERGUNTAS_PENDENTES.md` na raiz do projeto só quando surgir a primeira pergunta.

Texto da regra:
> - Prova barata: texto quando texto prova; imagem recortada e em escala menor; medidas por script.
> - Testes: o que mudou + regressão curta a cada mudança; bateria inteira antes de publicar. Testes e conferências rodam por script, direto.
> - Revisão: duas independentes só em segurança, contas, pagamento e criptografia; uma no resto.
> - Depois de interrupção, conferir se agentes e tarefas ainda rodam e retomar, não recomeçar. Encerrar processo só pelo PID que eu iniciei, nunca pelo nome (derruba o trabalho de outras sessões).
> - Perguntas pendentes: o que surgir no meio do trabalho vai para o arquivo de perguntas do projeto e é repetido no fim da mensagem final.
> - Antes de encerrar, perguntar de verdade "deveria estar fazendo algo antes de encerrar?". Se sim, fazer. Se não, dizer o que estou esperando e o que vai acordar a sessão. Nunca anunciar "sigo agora" sem a ferramenta já rodando na mesma vez.
> - Mensagem final: a resposta na primeira linha, depois as pendências e o que não saiu tão bem ou poderia ter saído melhor.

---

## Caixa 10 — Lembrete da estrela

**O que isto faz:** se o guia ajudar, uma estrela no repositório ajuda outras pessoas a achá-lo. Em vez de pedir agora, o Claude pode lembrar daqui a uma semana. Explique isso em até 2 frases. Não insista e não ponha "(Recomendado)" em nenhuma opção.

Pergunta:

1. **Quer que eu te lembre daqui a uma semana de decidir se dá uma estrela no repositório?** — cabeçalho `Estrela`
   > **Resumo** — **Ganha:** um lembrete único, para você decidir com calma. **Arrisca:** uma linha no CLAUDE.md; nenhum dado sai do computador; o Claude nunca dá a estrela por você. **Se não ligar:** nada muda. **Desfazer:** apague a linha "Lembrete único (estrela)" (ela se apaga sozinha depois de usada).
   - **Sim, me lembre** — Daqui a 7 dias, na primeira conversa, o Claude pergunta uma vez só se as táticas ajudaram e mostra o link.
   - **Já dei ou dou agora** — O Claude mostra o link agora e não lembra depois; nada é gravado.
   - **Não, obrigado** — Sem lembrete; nada é gravado.

Passos:
1. **Sim, me lembre:** grave a regra abaixo (troque `<data do lembrete>` pela data de hoje + 7 dias). É uma linha só e se apaga sozinha depois de usada.
2. **Já dei ou dou agora:** mostre o link https://github.com/JNSoftworks/jns-quota-keeper e não grave nada.
3. **Não, obrigado:** não grave nada, nem em "Recusadas".

Texto da regra:
> - Lembrete único (estrela): a partir de <data do lembrete>, na primeira resposta de uma sessão, pergunte em uma linha se as táticas do Quota Keeper ajudaram e, se a pessoa quiser dar uma estrela, mostre o link https://github.com/JNSoftworks/jns-quota-keeper. Nunca dê a estrela por ela. Depois de perguntar, qualquer que seja a resposta, apague esta linha.

---

## Caixa final — Resumo

Sem perguntas. Diga à pessoa, em poucas linhas:
1. O que mudou, por arquivo (CLAUDE.md, settings.json, scripts copiados), e onde estão as cópias de segurança.
2. O que foi recusado (fica em "Recusadas" e não volta a ser oferecido).
3. O que só vale a partir da próxima sessão (configurações e hooks).
4. Como desfazer, uma linha para cada coisa instalada: cada regra (apagar a linha no CLAUDE.md); cada configuração (apagar a chave em `"env"` ou em `"permissions"` do `settings.json`); cada hook (apagar a entrada dele em `"hooks"` e o arquivo copiado: `spend_watch.py` em `"UserPromptSubmit"` e `"PostToolUse"`, `agent_limit.py` em `"PreToolUse"`, `copy_lock.py` em `"PreToolUse"` e `"SubagentStop"`, `handoff_reminder.py` e `daily_report.py` em `"SessionStart"`, `spare_allow.py` em `"PreToolUse"` mais `spares.txt`); cada script em `tools/` (no relatório diário, também a regra do CLAUDE.md e a pasta `<pasta de configuração>/quota_keeper/`); os modelos em `modelos/`; a skill de uso (apagar a pasta `skills/usage-report/`); e, se houver, o `<pasta de configuração>/relay_token.txt` (apagar o arquivo e, se um token foi criado, revogá-lo onde foi criado). Para tudo de uma vez: voltar as cópias de segurança da Caixa 1 e apagar os arquivos copiados. Diga também quando cada coisa passa a valer (a próxima sessão, para configurações, hooks e a skill).
5. O que ficou pela metade (por exemplo, a segunda marca da medição do plano). Se o teste do freio ou o do vigia ficou para depois, diga à pessoa para abrir uma sessão nova e pedir ali: "repita o teste do freio (ou do vigia) do guia do Quota Keeper".
6. Se a Caixa 10 gravou o lembrete, a data em que ele vai aparecer.
7. Se o modo foi Rápido: o Grupo 3 (Caixa 7) não foi instalado. Para ligar depois, de preferência após uma ou duas semanas, basta pedir "rode a Caixa 7 do guia do Quota Keeper".
8. O crédito: "Táticas de Jaber Felippe Neto (JN Softworks), texto em CC BY 4.0, scripts em MIT." Se a pessoa for repassar o guia, que mande a pasta inteira, com o crédito.
