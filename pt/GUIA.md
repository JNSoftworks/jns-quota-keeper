# JN's Quota Keeper — economia de tokens para o Claude Code

> **Feito por Jaber Felippe Neto (JN Softworks).** Licença [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt-br): pode copiar, adaptar e repassar, desde que mantenha o nome do autor e o link da licença. Os scripts estão sob a licença MIT, que também pede para manter o crédito. Versão 1.0, novembro de 2026.

Este arquivo é para o Claude. Se você é a pessoa: não precisa ler. O Claude vai mostrar uma caixa de perguntas por tática e só muda o que você aceitar.

## Como conduzir a instalação (Claude, leia antes de tudo)

1. **Nada muda sem um sim.** Cada tática tem uma caixa de perguntas. Mostre a caixa, espere a resposta, faça só os passos daquela resposta, confira, e só então vá para a próxima caixa.
2. **Mostre cada caixa com AskUserQuestion**, uma chamada por caixa, com as perguntas, cabeçalhos e opções como estão aqui. A ferramenta já acrescenta a opção "Outro" sozinha. Sem essa ferramenta, faça as mesmas perguntas numa lista numerada curta e espere.
3. **Antes de cada caixa, diga em palavras simples** o que a tática faz, os riscos reais dela e como desfazer (os blocos "O que isto faz", "Riscos reais" e "Como desfazer" de cada caixa; resuma, sem ler tudo). A pessoa pode não ser técnica: nada de sigla ou jargão sem tradução na mesma frase. Cada opção da pergunta mostra a consequência dela numa linha; não esconda risco nem exagere.
4. **Siga a ordem das caixas.** Se uma caixa não se aplica (por exemplo, a pessoa não usa agentes), diga isso em uma linha e passe para a próxima.
5. **Grave as regras com o texto pronto** de cada caixa ("Texto da regra"). Não reescreva nem enfeite: cada linha a mais no CLAUDE.md é paga em toda sessão. Dos trechos entre `< >`, preencha só os da instalação:
   - número escolhido, como `<200>`: ponha o número da resposta da pessoa;
   - `<pasta de configuração>`: o caminho completo dela (definida logo abaixo), com barras `/`, por exemplo `C:/Users/fulano/.claude`;
   - `<caminho>`: só nos testes da Caixa 7, é o caminho completo da pasta de teste;
   - `<lista>`: as ferramentas escolhidas na Caixa 7;
   - `<data do lembrete>`: só na Caixa 10, a data de hoje + 7 dias, no formato `AAAA-MM-DD`;
   - escolha `<a | b>`: deixe só a opção que bate com a resposta e apague a outra.

   Ficam literais na regra gravada, para a sessão preencher depois: `<arquivo>`, `<passagem>`, `<projeto>`, `<id>`, `<n>`, `<título da sessão>`, `<data>`, `<id da sessão>`.

   **Onde as linhas de regra entram:** dentro da seção `## Quota Keeper ...` do CLAUDE.md escolhido, sob o subtítulo `### Regras`, antes de `### Recusadas`. A Caixa 1 cria a seção e os dois subtítulos (se a seção não existir, no fim do arquivo). Se a seção já existir sem `### Regras`, crie esse subtítulo antes de `### Recusadas`. Linhas de recusa ficam sob `### Recusadas`. Os rótulos entre colchetes (como "[Número]") só dizem qual versão escolher: não são gravados.
6. **Nunca peça token, senha ou chave no chat**, e nunca rode comando que mostre um deles na tela. A Caixa 7 ensina a pessoa a gravar o token sozinha.
7. **Fale pouco entre um passo e outro.** O resumo completo vem na Caixa final.
8. **Em dúvida, pare e pergunte.** Se algo daqui não bater com o que você vê no computador da pessoa (ferramenta com outro nome, opção que não existe, erro), diga o que achou e pergunte. Não invente.
9. **Nomes de ferramentas e opções mudam.** Os citados aqui são de novembro de 2026. Procure pelo nome com ToolSearch; se não achar, diga e siga sem aquela parte.

**Os três modos da pergunta `Modo` (Caixa 1, pergunta 4).** Valem para as Caixas 2 em diante:
- **Rápido:** siga a seção "Pacote recomendado (modo Rápido)", que divide tudo em três grupos. (1) Mostre, numa mensagem só, as três tabelas, resumidas em palavras simples. (2) Uma chamada do AskUserQuestion com duas perguntas: cabeçalho `Pacote`, opções `Instalar o grupo 1` / `Ver caixa por caixa` / `Cancelar` (cada uma com a consequência em uma linha, como na seção), e a pergunta `Espera longa` da Caixa 2, igual, que decide o cache de 1 hora. (3) Com "Instalar o grupo 1": faça os passos das caixas só para as partes do Grupo 1, sem mais perguntas. (4) Uma chamada com as perguntas do Grupo 2 (marcar várias). Instale o que for marcado; o desmarcado vai para "Recusadas". (5) Diga em uma linha que o Grupo 3 existe e se liga depois, pela Caixa 7, caixa por caixa; ele não é instalado, não é perguntado e não vai para "Recusadas". (6) Faça a Caixa 10 como está e termine na Caixa final. "Ver caixa por caixa" passa para o segundo modo; "Cancelar" encerra sem mudar mais nada (a cópia de segurança da Caixa 1 já existe).
- **Caixa por caixa:** uma caixa de perguntas por tática, na ordem, como descrito acima. Grave o que a pessoa aceitar sem perguntar de novo.
- **Caixa por caixa, conferindo:** como o anterior e, antes de cada gravação (linha no `settings.json`, hook, cópia de script, regra no CLAUDE.md), mostre o trecho exato e pergunte, com opções `Gravar` / `Não gravar`. "Não gravar" é recusa daquela parte (vai para "Recusadas").

**O que é "sensível"** (nos dois modos caixa por caixa, sempre perguntado um a um, com o bloco de riscos; no Rápido, não é instalado nem perguntado, porque está todo no Grupo 3): tudo que muda permissão ou o modo padrão de permissão; aprova ações sozinho (hook que aprova, regra de permitir); abre sessões sozinho; liga o Remote Control; ou grava token. O que isso inclui está marcado "(sensível)" nas caixas.

**Dependências entre as perguntas.** Antes de cada caixa (e na caixa do Grupo 2, no modo Rápido), pule as perguntas cuja condição não vale; a condição vem junto do cabeçalho, como "(só se ...)". Diga em uma linha o que pulou e por quê (por exemplo: "pulei os estepes porque você não escolheu a sucessora automática"). Pergunta pulada conta como a resposta que não instala nada e não vai para "Recusadas": se a pessoa mudar de ideia, basta pedir a caixa de novo.

| Se... | Pule | O que a pessoa perde |
|---|---|---|
| Não há Python (Caixa 1, passo 3) | `Freio`, `Trava`, `Lembrete`, `Token`, `Hook estepe`, `Vigia`, `Medir plano`, `Skill uso` | Todos os scripts e hooks; ficam só as regras de texto |
| `Onde usa` = "Terminal", ou não há `start_session` | Na Caixa 7, tudo menos `Token` e `Permissões` | Sucessora visível no app; fica o caminho B ou a regra "[Eu abro]" |
| `Onde usa` = "App desktop" ou "Os dois" | `Token`, `Permissões` | Nada: no app, o token não faz falta |
| `Plano` = "Chave de API" | `Antes/depois`, `Medir plano`, `Token` | A conta em % da cota (não existe nesse plano) |
| Janela de 200 mil (ou sem saber) | `Compactar`; `Troca` usa ~100 mil | Nada: baixar a compactação só serve na janela de 1 milhão |
| A pessoa não usa agentes | `Espera longa` e a Caixa 5 | Nada agora; se passar a usar, pode pedir as duas |
| `Passagem` = "Não" | `Troca`, `Lembrete` e a Caixa 7 inteira | A sessão nova começa do zero, então troca e sucessora automática perdem o sentido |
| `Sucessora` não é "O Claude, sozinho" | `Fechar mãe`, `Agendada`, `Recusa`, `Estepes`, `Remote`, `Auto padrão`, `Hook estepe` | A cadeia não segue sozinha; a troca depende de você |
| `Recusa` não é "Sessão de estepe" | `Estepes`, `Hook estepe` | A troca sem você na tela espera sua próxima mensagem ou usa a reserva |
| `Agendada` = "Não liberar" | `Auto padrão` | A reserva por tarefa agendada |
| `Token` não é "Sim, me guie" | `Permissões` | As rodadas sem tela |
| Modo Rápido | A Caixa 7 inteira (Grupo 3) | Nada agora: ela se liga depois |

Combinações que funcionam pela metade (quando a pessoa escolher uma delas, diga em uma linha o que ela perde):
- Troca de sessão sem `Vigia`: a troca depende de o Claude notar o tamanho da conversa; no uso do autor, 14 de 36 trocas passaram do ponto antes do vigia.
- `Espera longa` "Sim" sem agentes que esperam mais de 5 minutos: cada gravação custa 2 vezes e não se ganha nada.
- "Experimental: Opus coordena" sem `Freio`: só a regra de texto impede o Sonnet de abrir agentes.
- `Fechar mãe` "Não": a sessão anterior pode reler a conversa a cada turno da nova, gastando cota, até ser arquivada.
- Estepes sem `Hook estepe`: no modo automático, a troca por estepe pode ser barrada e cair no "Avisar e seguir".
- `Agendada` liberada com `Auto padrão` "Não mudar": a sucessora aberta por tarefa para no primeiro comando, esperando aprovação.
- "Avisar e seguir" com `Remote` "Não usar": o aviso só aparece no computador.
- `Trava` "Não" com "O Claude, sozinho": na troca com agente rodando, a sucessora confere a passagem em vez de a trava garantir.
- `Medir plano` "Não": o vigia avisa só em tokens, não em % da cota.

**O que nunca se economiza** (vale sempre, sem caixa): cópia de segurança antes de mudar configuração, confirmação antes de qualquer coisa irreversível, compilar e testar o que mudou, e ler o trecho exato de código que vai ser editado.

**Arquivos deste pacote** (caminhos a partir da pasta onde está o `START_HERE.md`):
- `pt/GUIA.md` (este) e `pt/PASSAGEM_MODELO.md` (modelo do arquivo de passagem) e `pt/RESUMOS_MODELO.md` (modelo do arquivo de resumos)
- `scripts/spend_watch.py` (vigia de gasto), `scripts/agent_limit.py` (freio de agentes), `scripts/session_relay.py` (rodadas sem tela), `scripts/measure_point.py` (medir quanto vale 1% do plano), `scripts/check_settings.py` (conferir o `settings.json`), `scripts/spare_allow.py` (aprova sozinho só as ações nos estepes), `scripts/copy_lock.py` (trava de cópia: impede que agentes de duas sessões mexam na mesma cópia de trabalho), `scripts/handoff_reminder.py` (lembrete no começo da sessão para ler a passagem), `scripts/usage_report.py` (relatório de onde foram os tokens, só lê e imprime)
- `skills/usage-report/SKILL.md` (skill que roda o relatório de uso)
- `LICENSE.md`

**Pasta de configuração:** é a pasta indicada pela variável de ambiente `CLAUDE_CONFIG_DIR`, se ela estiver definida (confira: PowerShell `$env:CLAUDE_CONFIG_DIR`; Mac e Linux `echo $CLAUDE_CONFIG_DIR`). Se não estiver, é a pasta `.claude` dentro da pasta do usuário (Windows: `C:\Users\<nome>\.claude`; Mac: `/Users/<nome>/.claude`; Linux: `/home/<nome>/.claude`). Neste guia, "pasta de configuração" e `<pasta de configuração>` sempre querem dizer essa pasta. Nos comandos dos hooks e nas regras, use o caminho completo com barras `/`, inclusive no Windows. Antes de copiar o primeiro arquivo para `hooks`, `tools` ou `modelos` dentro dela, crie a subpasta se não existir. Os scripts `check_settings.py` e `measure_point.py` já leem `CLAUDE_CONFIG_DIR` sozinhos.

**Janela de contexto** (quantos tokens cabem numa conversa: 200 mil ou 1 milhão): no app, o indicador de contexto junto da caixa de mensagem; no terminal, o comando `/context`. Se você não conseguir ver (sem indicador, sem o comando), suponha 200 mil. É o padrão seguro: limites pensados para 200 mil também servem na janela de 1 milhão, e o contrário não. Diga à pessoa como conferir (o indicador ou o `/context` mostra algo como "x / 200k" ou "x / 1M"). Se ela disser que é 1 milhão, refaça só as respostas que dependem disso (Caixas 2, 6 e 8).

**Como mexer no `settings.json` sem quebrar:** leia o arquivo inteiro, acrescente sem apagar o que já existe (dentro de `"env"` e de `"hooks"`, que podem já ter itens), e no fim confira que continua válido:

```text
python <pasta do pacote>/scripts/check_settings.py
```

O script aceita arquivo com BOM, avisa se uma chave aparece repetida (dois `"hooks"` ou dois `"env"`, por exemplo) e imprime `ok` quando está tudo certo.

No Mac e no Linux, troque `python` por `python3` aqui e nos comandos dos hooks.

## Por que funciona

Explique isto à pessoa em até 3 frases antes da Caixa 1.

A cada passo (cada vez que o Claude usa uma ferramenta e lê a resposta), ele relê a conversa inteira. Quase todo o gasto vem dessa releitura, não de escrever ou pensar. O que economiza é: conversa curta, menos passos na conversa principal e trabalho pesado fora dela (num agente, que tem conversa própria, ou num script, que não gasta token).

Números do autor (setembro a novembro de 2026, medidos nos registros das sessões; fonte: medido no PC do autor, pode variar no seu uso):
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

- **Token:** um pedaço de texto, mais ou menos uma palavra. É a unidade em que o Claude lê, escreve e é cobrado.
- **Conversa (ou contexto):** tudo o que já foi dito e lido na sessão. O Claude relê isso a cada passo.
- **Agente:** um ajudante que o Claude abre para uma tarefa. Tem conversa própria, que começa vazia, e devolve só o resumo.
- **Haiku, Sonnet, Opus:** os três modelos do Claude. Haiku é o mais barato e rápido; Sonnet é o do meio; Opus é o mais forte e o mais caro.
- **CLAUDE.md:** arquivo de regras que o Claude lê no começo de toda sessão.
- **Hook:** um pequeno script que o Claude Code roda sozinho num momento fixo (por exemplo, a cada mensagem ou antes de abrir um agente).
- **Cache:** a conversa guardada para ser relida mais barato. Dura 5 minutos por padrão; passado esse tempo, guardar de novo custa de novo.
- **`/clear` e `/compact`:** `/clear` apaga a conversa; `/compact` troca a conversa por um resumo. Só a pessoa pode digitar.

---

## Riscos gerais e como desfazer tudo

Diga isto à pessoa, curto, antes da Caixa 1. Cada caixa traz os riscos dela; aqui está o que vale para o pacote todo.

- **O que o pacote muda:** o `CLAUDE.md` (uma seção "Quota Keeper"), o `settings.json` (variáveis em `"env"`, hooks e, só na Caixa 7, permissões) e scripts, modelos e uma skill copiados para a pasta de configuração. Mais nada, e só o que a pessoa aceitar.
- **Rede:** nenhum script do pacote faz chamada de rede. O `copy_lock.py` só roda `ps` (Mac e Linux) e a si mesmo. O `session_relay.py` roda o comando `claude` (que, como todo uso do Claude, manda a conversa à Anthropic) e, no Windows, `taskkill` só no processo que ele mesmo abriu.
- **Permissões:** um hook roda com as permissões do usuário, como qualquer programa dele. Nada daqui contorna as aprovações do Claude Code, salvo o que cada caixa marcada "(sensível)" disser com todas as letras. Fora isso, o Claude continua pedindo aprovação como antes.
- **Se o Python faltar ou um hook der erro:** o Claude Code mostra o erro e segue. Um hook só bloqueia uma ação quando termina com código de saída 2 (no evento de começo de sessão, nem isso: só mostra o erro) ou quando responde "negar" de propósito, como fazem o freio e a trava deste pacote, com mensagem. Erro com outro código não bloqueia: a ação segue. Python ausente = a parte que usa script não funciona, nada mais quebra. (Confira na documentação dos hooks do Claude Code se a versão da pessoa mudou isso.)
- **Pode gastar mais?** Algumas táticas podem gastar MAIS em certos usos: o cache de 1 hora (gravar custa 2 vezes), sessões novas (releem tudo que carregam no começo) e estepes (sessões reservas, que gastam um turno curto ao nascer e depois ficam arquivadas). Cada caixa diz quando.
- **Desfazer tudo:** (1) volte as cópias de segurança da Caixa 1 (`settings.json.antes-quota-keeper-<data>` e `CLAUDE.md.antes-quota-keeper-<data>`) por cima dos arquivos atuais, ou (2) apague a seção "Quota Keeper" do `CLAUDE.md`, tire do `settings.json` as linhas de `"env"`, `"hooks"` e `"permissions"` que o pacote pôs, e apague o que foi copiado para a pasta de configuração (os scripts em `hooks` e `tools`, os modelos em `modelos`, a pasta `skills/usage-report` e, se existirem, `spares.txt` e `relay_token.txt`). Vale a partir da próxima sessão.

---

## Pacote recomendado (modo Rápido)

O que o modo Rápido mostra antes de instalar, em três grupos. Os caminhos são da pasta de configuração; "regra" é uma linha no `CLAUDE.md`. Tudo vale a partir da próxima sessão. O passo a passo de cada parte é o da caixa dela, com a resposta "(Recomendado)" quando não houver outra indicação aqui.

**Grupo 1 — Adotar (instala com um ok).** Só regras, dois modelos de arquivo e ajustes em `"env"`. Nada aprova, bloqueia nem muda permissão.

| Parte (caixa) | O que instala | Risco | Como desfazer |
|---|---|---|---|
| CLAUDE.md enxuto e memória curta (3: `CLAUDE.md`, `Memória`) | Regras; o Claude propõe cortes e só move com sim | Detalhe movido pode passar despercebido (fica um ponteiro) | Apagar as linhas; devolver o trecho movido |
| Conversa curta, texto longo em arquivo (3: `Conversa`, `Texto longo`) | Regras | Você vê menos detalhe no caminho | Apagar as linhas |
| Hábitos de leitura (4: os quatro) | Regras | Pode perder o que ficou fora do trecho lido | Apagar as linhas |
| Agentes em Sonnet (2: `Agentes`) | `CLAUDE_CODE_SUBAGENT_MODEL` | Sonnet erra mais que Opus em tarefa difícil; o Claude pede Opus nesses casos | Apagar a linha em `"env"` |
| Modelo certo por tarefa, agentes curtos e em lote (5: `Agente curto`, `Modelos` "Por papel", `Lote`) | Regras | Mais agentes por tarefa; Haiku erra mais no que parecia simples | Apagar as linhas |
| Esforço Alto (2: `Esforço`) | Regra | Nenhum relevante: o seletor de esforço continua com você | Apagar a linha |
| Cache de 1 hora (2: `Espera longa`), só se a pessoa responder que os agentes esperam mais de 5 minutos | `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` | Gravar custa 2 vezes; sem esperas longas, gasta mais | Apagar a linha em `"env"` |
| Passagem e resumos, troca de sessão, uma tarefa por sessão (6: `Passagem`, `Troca`, `Uma tarefa`) | Regras e os dois modelos em `modelos/`; troca em ~250 mil (~100 mil na janela de 200 mil) | Arquivos novos nos projetos, criados sem perguntar; passagem velha leva a sessão nova ao ponto errado | Apagar as linhas e os modelos; os arquivos já criados ficam até você apagar |
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
| Vigia de gasto (8: `Vigia`, limites do autor) | `hooks/spend_watch.py` em `"UserPromptSubmit"` e `"PostToolUse"`, e uma regra | Lê os registros locais das conversas (só contagens); uma linha de aviso quando cruza um limite | Tirar as duas entradas do `settings.json`; apagar o script e a regra |
| Freio de agentes (5: `Freio`) | `hooks/agent_limit.py` em `"PreToolUse"` | Pode negar um agente que você queria (a mensagem diz por quê) | Tirar a entrada; apagar o script |
| Trava de cópia (5: `Trava`) | `hooks/copy_lock.py` em `"PreToolUse"` e `"SubagentStop"` | Trava presa impede outra sessão de escrever naquela pasta por até 2 horas | Tirar as entradas; apagar o script; `copy_lock.py release <pasta>` solta na hora |
| Lembrete da passagem (6: `Lembrete`) | `hooks/handoff_reminder.py` em `"SessionStart"` | Uma linha a mais no começo da sessão nas pastas com passagem | Tirar a entrada; apagar o script |
| Compactar em 50% (2: `Compactar`), só na janela de 1 milhão | `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | O resumo automático perde detalhe | Apagar a linha em `"env"` |
| Relatório de uso (8: `Skill uso`) | `skills/usage-report/`, `tools/usage_report.py` e `tools/measure_point.py` | Lê os registros locais (só contagens); nada sai do PC | Apagar a pasta da skill e os dois scripts |
| Medir o plano (8: `Medir plano`), só com limite semanal em % | `tools/measure_point.py`, uma regra e a primeira marca | É uma estimativa; pede o % em dois dias diferentes | Apagar a linha, o script e `tools/measure_marks.csv` |

Como perguntar (uma chamada, `multiSelect: true` nas duas perguntas, cada opção com o risco da tabela em uma linha):
- **Quais destes hooks testar?** — cabeçalho `Hooks` — opções `Vigia de gasto` / `Freio de agentes` / `Trava de cópia` / `Lembrete da passagem`.
- **E destes?** — cabeçalho `Outros` — opções `Compactar em 50%` (tire com a janela de 200 mil) / `Relatório de uso` / `Medir o plano` (tire com "Chave de API"). Se sobrar uma opção só, pergunte-a sem `multiSelect`, com `Sim` / `Não`.
- Sem Python, tire todas as opções menos `Compactar em 50%` (a pergunta `Hooks` não é feita) e diga isso em uma linha.

**Grupo 3 — Avançado, não ligar no começo (o Rápido não instala nem pergunta).** É tudo da Caixa 7. Diga que existe e que se liga depois, pela Caixa 7, caixa por caixa (basta pedir "rode a Caixa 7 do guia do Quota Keeper"), de preferência depois de uma ou duas semanas com o resto.

| Parte (Caixa 7) | O que instalaria | Por que fica para depois | Como desfazer, se ligar |
|---|---|---|---|
| Sucessão automática com arquivamento da anterior (`Sucessora`, `Fechar mãe`, `Recusa`, `Estepes`) | Regras que abrem a sessão nova e estepes sozinhos e arquivam a anterior | Abre sessões sem você olhar e arquiva a anterior; cada sessão nova recarrega instruções e passagem, então pode gastar mais. Só compensa com a passagem já funcionando bem | Apagar as linhas; desarquivar pela lista de arquivadas |
| Token de longa duração em arquivo (`Token`, `Permissões`) | `relay_token.txt` | Chave da sua conta, válida por um ano, num arquivo: quem a pegar (programa, administrador, cópia na nuvem) gasta sua cota, e revogar só ela não é simples. Só serve a quem usa só o terminal | Apagar o arquivo; revogar como diz a Caixa 7 |
| Rodadas sem tela (caminho B) | `tools/session_relay.py` e uma regra | O Claude trabalha escondido e ninguém aprova nada: o que está na lista passa direto, e um erro pode editar arquivos sem você ver | Apagar o script e a regra |
| Remote Control automático (`Remote`) | Regra que liga o Remote Control nas sucessoras | Quem entrar na sua conta claude.ai, ou pegar o celular desbloqueado, manda ordens ao computador | Apagar a linha; desligar em cada sessão e no app |
| Aprovação automática: hook dos estepes, regras de permitir, modo automático como padrão (`Hook estepe`, `Agendada`, `Auto padrão`) | `hooks/spare_allow.py`; linhas em `"permissions"` | Ações passam sem você ver. As regras de permitir e o modo automático valem para todas as sessões e projetos, e o filtro do modo automático pode errar nos dois lados | Tirar as linhas do `settings.json`; apagar o script |

---

## Caixa 1 — Antes de começar

**O que isto faz:** decidir onde as regras ficam, como a pessoa usa o Claude Code e como a instalação segue. Ainda não muda nada.
**Riscos reais:** nenhum nesta caixa: só guarda respostas. A mudança vem nos passos (cópia de segurança e seção no `CLAUDE.md`).
**Como desfazer:** nada a desfazer antes dos passos; depois, ver "Riscos gerais e como desfazer tudo".

Perguntas:

1. **Onde gravar as regras que você aceitar?** — cabeçalho `Onde gravar`
   - **Em todos os projetos (Recomendado)** — Vão para o `CLAUDE.md` da pasta de configuração do Claude Code (em geral `~/.claude/CLAUDE.md`) e valem em qualquer pasta, em toda sessão (cada linha é lida sempre).
   - **Só neste projeto** — Vão para o `CLAUDE.md` da pasta aberta agora. Vale só para as linhas de regra; se o arquivo for compartilhado, outras pessoas as verão.
2. **Onde você usa o Claude Code?** — cabeçalho `Onde usa`
   - **App desktop** — O app do Claude no computador, na aba Code. Libera as partes que usam as ferramentas do app.
   - **Terminal** — O comando `claude` numa janela de terminal ou dentro do editor de código. As partes só do app serão puladas.
   - **Os dois** — Oferece as partes dos dois; nada é instalado sem você aceitar.
3. **Como você paga o Claude?** — cabeçalho `Plano`
   - **Pro, Max ou Ultra** — Assinatura pessoal, com limite de uso por semana; as partes que medem a cota em % ficam disponíveis.
   - **Team ou Enterprise** — Plano de empresa; os limites podem ser definidos pela empresa, então as partes de medir a cota ficam como sugestão.
   - **Chave de API** — Paga por uso (por token), sem limite semanal em %; as partes que medem a cota em % são puladas.
   - **Não sei** — Tudo bem: o guia fica no geral e diz, em cada caixa, o que depende do plano.
4. **Como instalo o que você aceitar?** — cabeçalho `Modo`
   - **Rápido (Recomendado)** — Uma tela com o pacote recomendado, o risco de cada parte e como desfazer. Um ok instala o básico (regras e ajustes que não mexem em permissão); os hooks você marca numa caixa só; o avançado (sessões abertas sozinhas, aprovação automática, token) não é instalado agora.
   - **Caixa por caixa** — Uma caixa de perguntas por tática, com os riscos de cada uma. Gravo o que você aceitar sem perguntar de novo.
   - **Caixa por caixa, conferindo** — Como a anterior e, antes de cada gravação (settings.json, hook, regra), mostro as linhas exatas e espero seu ok. Máximo controle, mais cliques.

Na pergunta 3 não ponha "(Recomendado)" em nenhuma opção: é um fato sobre a pessoa, não uma escolha. A pergunta 4 é a de conduzir a instalação: ver "Os três modos da pergunta `Modo`" no começo do guia.

Passos:
1. Faça uma cópia de segurança, com a data no nome, de cada arquivo que existir: `<pasta de configuração>/settings.json` → `settings.json.antes-quota-keeper-<AAAA-MM-DD>`, e o CLAUDE.md escolhido → `CLAUDE.md.antes-quota-keeper-<AAAA-MM-DD>`. A data é a de hoje, pelo relógio do computador (por exemplo `2026-11-04`). Cada cópia fica na mesma pasta do original, ao lado dele. Diga à pessoa onde ficaram.
2. No fim do CLAUDE.md escolhido (crie se não existir), acrescente a seção abaixo. As caixas seguintes põem as linhas de regra sob "Regras" e as recusas sob "Recusadas".

   ```markdown
   ## Quota Keeper (táticas de Jaber Felippe Neto, JN Softworks)

   ### Regras

   ### Recusadas (não oferecer de novo)
   ```

   Se a resposta foi "Só neste projeto" e esse CLAUDE.md é compartilhado com outras pessoas (num repositório, por exemplo), avise antes de gravar.

   Configurações, hooks e scripts são sempre do usuário inteiro (`<pasta de configuração>/settings.json`), mesmo com "Só neste projeto": essa resposta vale só para as linhas de regra. Avise a pessoa disso.

   Se a seção "Quota Keeper" (ou "Economia de tokens", nome antigo) já existir (o guia foi rodado antes), atualize a que existe, nunca crie outra. O mesmo vale para as configurações e os hooks das caixas seguintes: se já estiverem no `settings.json`, atualize, nunca duplique.
3. Confira se há Python 3 (`python --version` ou `python3 --version`). Os scripts das Caixas 5, 6, 7 e 8 precisam dele. Se não houver, avise que essas partes vão precisar do Python (https://www.python.org/downloads/) e siga com o resto.
4. Guarde a resposta de "Onde usa": a Caixa 7 depende dela.
5. Guarde a resposta de "Modo": ela decide como as Caixas 2 em diante seguem (regras dos três modos, no começo do guia). Com "Rápido", depois dos passos desta caixa siga o roteiro do modo Rápido (tabelas do "Pacote recomendado (modo Rápido)", pergunta `Pacote`, caixa do Grupo 2) em vez de abrir a Caixa 2. Com os outros dois, siga caixa por caixa.
6. Guarde a resposta de "Plano": as Caixas 7 e 8 dependem dela. Nunca suponha o plano, nem pelo que uma ferramenta mostrar. Com "Não sei", fale de forma geral ("se o seu plano tiver limite semanal em %...") e deixe a pessoa decidir. Se ela quiser descobrir, mostre o que a tela de uso diz (no app, a ferramenta `get_usage`; no terminal, `/usage`) e peça que ela confirme; sem a confirmação dela, fica "Não sei".

**Recusas, em todas as caixas:** cada tática respondida "Não" (ou desmarcada) vira uma linha em "Recusadas", com o nome dela, para nenhuma sessão perguntar de novo.

---

## Caixa 2 — Configurações

**O que isto faz:** três ajustes no `<pasta de configuração>/settings.json` e uma regra de esforço.
**Por quê:** agentes num modelo mais barato; agente que espera não paga de novo a conversa inteira; conversa resumida antes de cada passo ficar caro.
**Riscos reais:**
- Sonnet nos agentes: agente pode errar mais em tarefa difícil que o Opus; o Claude pede Opus para os casos delicados.
- Cache de 1 hora: gravar custa 2 vezes (não 1,25); se o agente não esperar mais de 5 minutos, você paga mais, não menos.
- Compactar em 50% ou 25%: o resumo automático perde detalhe da conversa.
- Nada aqui aprova ação nem muda permissão; nenhum dado sai do computador por causa destes ajustes.
**Como desfazer:** apague a linha correspondente em `"env"` do `settings.json` (ou volte a cópia da Caixa 1) e, para a regra de esforço, apague a linha dela do `CLAUDE.md`. Vale a partir da próxima sessão.
**Atenção:** os números desta caixa (compactar em 50%) supõem a janela de 1 milhão de tokens. Veja a janela da pessoa (regra "Janela de contexto", no começo do guia; sem conseguir ver, suponha 200 mil). Se for de 200 mil, não baixe a compactação: pule a pergunta 3 e deixe o padrão.

Perguntas:

1. **Os agentes nascem em Sonnet?** — cabeçalho `Agentes`
   - **Sim (Recomendado)** — Todo agente começa no Sonnet, mais barato que o Opus. Quando precisar, o Claude pede Opus ou Haiku para um agente específico.
   - **Não** — Os agentes usam o mesmo modelo da conversa; nada muda, e agentes podem custar mais se a conversa for em Opus.
2. **Seus agentes costumam esperar mais de 5 minutos por algo (compilação, testes, download, renderização)?** — cabeçalho `Espera longa` (só se a pessoa usa agentes)
   - **Sim, cache de 1 hora** — O agente que espera não paga de novo a conversa inteira na volta. Risco: cada gravação custa 2 vezes (em vez de 1,25), então só compensa com agentes que esperam mais de 5 minutos; no PC do autor, essas esperas eram ~26% do gasto (medido set-nov/2026; pode variar no seu uso). Sem esperas longas, gasta mais.
   - **Não, deixar como está** — Nada muda: o cache padrão de 5 minutos serve para tarefas rápidas.
3. **Quando resumir a conversa automaticamente?** — cabeçalho `Compactar` (só na janela de 1 milhão)
   - **Em 50% (Recomendado)** — A conversa é resumida quando chega à metade do espaço, antes de cada passo ficar caro; o resumo perde algum detalhe.
   - **Em 25%** — Para produção longa numa sessão só. Resume mais vezes e perde mais detalhe.
   - **Não mexer** — Nada muda: fica no padrão, perto do fim do espaço (passos ficam mais caros antes do resumo).
4. **Virar regra: esforço Alto, sem modo de frota de agentes?** — cabeçalho `Esforço`
   - **Sim (Recomendado)** — O Claude recomenda esforço Alto; Máximo só para problema muito difícil; nenhum modo que abre muitos agentes de uma vez sem você pedir. É só uma regra: o esforço em si você muda no seletor.
   - **Não** — Nada muda; o Claude não terá essa orientação e pode sugerir esforço ou modos mais caros.

Passos (cada um só se a resposta pediu):
1. No `settings.json`, dentro de `"env"` (crie se não existir), acrescente sem apagar o que já está lá:
   - pergunta 1 "Sim": `"CLAUDE_CODE_SUBAGENT_MODEL": "sonnet"`. Avise a pessoa: em versões antigas do Claude Code, essa configuração vencia o modelo pedido para um agente específico. Se um agente pedido em Opus ou Haiku não mudar de modelo, atualize o Claude Code (`claude update`).
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
3. Diga à pessoa: os ajustes valem a partir da próxima sessão; para desfazer, apague a linha (ou volte a cópia da Caixa 1). O esforço da conversa só ela muda, no seletor de esforço do app ou do terminal.

Texto da regra:
> - Esforço: recomendar Alto; Máximo só para problema muito difícil (de preferência num agente com esforço máximo, não na conversa toda). Nunca abrir modo de frota de agentes sem a pessoa pedir.

Conferir: o `settings.json` continua válido (comando no começo do guia). Mostre à pessoa só as linhas novas.

---

## Caixa 3 — O que o Claude lê toda vez

**O que isto faz:** o CLAUDE.md e o índice da memória entram em toda sessão antes da primeira mensagem e são relidos a cada passo. Cada linha neles é paga muitas vezes por dia. Junto vem o jeito de conversar: escrever custa 5 vezes mais que ler, e tudo o que é escrito fica na conversa. Aqui só se gravam regras (texto); nenhum script e nenhuma permissão.
**Riscos reais:**
- Mover trechos do CLAUDE.md para outro arquivo: o Claude pode deixar de ver o detalhe se não abrir o arquivo. Por isso nada move sem o seu sim, e fica um ponteiro no lugar.
- Encurtar linhas da memória pode apagar um detalhe útil; só com o seu sim, e a cópia da Caixa 1 guarda o CLAUDE.md (a memória, não: peça uma cópia se importar).
- Mensagens curtas no meio do trabalho: você acompanha menos o que o Claude está fazendo.
**Como desfazer:** apague a linha da regra no `CLAUDE.md` (seção Quota Keeper). Arquivo movido: devolva o trecho do ponteiro. Vale na próxima sessão.

Perguntas:

1. **Manter o CLAUDE.md curto (regras e ponteiros; o detalhe vai para outros arquivos)?** — cabeçalho `CLAUDE.md`
   - **Sim, e sugerir cortes (Recomendado)** — Vira regra, e o Claude propõe agora o que mover para outro arquivo. Nada sai sem o seu sim.
   - **Só a regra** — Vale daqui para frente; o arquivo atual fica como está.
   - **Não** — Nada muda; o CLAUDE.md pode seguir crescendo e custando mais em toda sessão.
2. **Memória com índice curto (uma linha por ficha; projeto grande ganha uma ficha-resumo)?** — cabeçalho `Memória`
   - **Sim (Recomendado)** — O índice é lido em toda sessão, e só até certo tamanho. Linha curta cabe mais e custa menos; encurtar linhas existentes só com o seu sim.
   - **Não uso memória** — Nada a fazer; esta parte é pulada.
   - **Não** — Nada muda; índice longo é cortado depois da linha 200 e custa em toda sessão.
3. **Mensagens curtas no meio do trabalho, tudo junto no fim?** — cabeçalho `Conversa`
   - **Sim (Recomendado)** — Entre um passo e outro, só uma linha do que está fazendo. Respostas, resultados e avisos vêm juntos na mensagem final.
   - **Não** — Nada muda; você vê mais detalhe no caminho, e a conversa cresce mais rápido (custa mais).
4. **Coisa longa vai para arquivo, não para o chat?** — cabeçalho `Texto longo`
   - **Sim (Recomendado)** — Para mostrar um texto ou log grande, você salva num arquivo da pasta e diz o nome; o Claude lê só o trecho que precisa. Dá um passo a mais para você.
   - **Não** — Nada muda; colar texto grande no chat é mais cômodo, mas custa em cada passo seguinte.

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

**O que isto faz:** tudo o que o Claude lê fica na conversa e é relido em cada passo seguinte. Aqui só se gravam regras (texto) sobre como ler; nenhum script e nenhuma permissão.
**Por quê:** um arquivo de 50 mil tokens lido no começo custa ~5 mil de peso em cada passo depois; em 100 passos, ~560 mil (conta feita pela régua do guia, não é preço oficial). Lido por um agente, ele nunca entra na conversa principal.
**Riscos reais:**
- Buscar em vez de ler: o Claude pode perder contexto que estava fora do trecho lido.
- Agente lendo no lugar: o resumo pode omitir um detalhe; o agente em si custa uma conversa nova.
- Nota extraída uma vez pode ficar velha se a fonte mudar.
**Como desfazer:** apague a linha da regra no `CLAUDE.md` (seção Quota Keeper). Vale na próxima sessão.

Pergunta (uma só, com várias respostas: `multiSelect: true`):

1. **Quais destes hábitos de leitura viram regra?** — cabeçalho `Leitura`
   - **Buscar em vez de ler** — Procurar o nome ou o título e ler só umas 50 linhas em volta. Nunca ler inteiro um documento grande, um log ou um arquivo gerado. Risco: pode perder o que ficou fora do trecho.
   - **Leitura grande para agente** — Um agente lê e devolve só o resumo; o volume não entra na conversa. Haiku para achar e filtrar; Sonnet para entender. Risco: o resumo pode omitir algo.
   - **Extrair uma vez** — Quando várias tarefas usam a mesma fonte grande, um agente escreve uma nota curta com o que importa, e as próximas leem a nota. Risco: a nota pode ficar velha.
   - **Log filtrado na fonte** — Marcar as linhas do próprio log e buscar só a marca; nunca carregar inteiro um log de compilação ou de teste. Risco: erro sem marca não aparece.
   Se a pessoa não marcar nenhuma: nada muda; tudo continua sendo lido inteiro, e custa mais em cada passo.

Passos: grave uma linha por item marcado; os não marcados vão para "Recusadas".

Texto da regra:
> - Buscar antes de ler: procurar o nome e ler só o trecho em volta; documento grande, log e arquivo gerado nunca inteiros.
> - Leitura grande (log, vários arquivos, documento longo) vai para agente que devolve só o resumo (Haiku para achar, filtrar e contar; Sonnet para entender). Ler inteiro só o que vou editar.
> - Fonte grande usada por várias tarefas: extrair uma vez numa nota curta no projeto e reaproveitar a nota.
> - Log: marcar as próprias linhas e buscar a marca; nunca carregar inteiro um log de compilação ou de teste.

---

## Caixa 5 — Agentes

**O que isto faz:** um agente nasce com conversa vazia, então cada passo dele é barato no começo. Mas ele também relê a própria conversa a cada passo, e fica caro se trabalhar muito tempo. Esta caixa limita o tamanho do trabalho de cada agente, escolhe o modelo de cada tipo de trabalho e, com dois scripts opcionais, freia cadeias de agentes e protege uma pasta de duas sessões ao mesmo tempo.
**Por quê:** no uso do autor, agentes de 100 ou mais chamadas foram 74% do gasto dos agentes, e 71% desse gasto veio de passos com a conversa do agente acima de 200 mil tokens (medido no PC do autor, set-nov/2026; pode variar no seu uso).
**Riscos reais:**
- Regras de agente (perguntas 1 a 3) são só texto no CLAUDE.md: não bloqueiam nada, só orientam o Claude. Risco pequeno: um agente interrompido em ~100 chamadas pode deixar a tarefa pela metade, e abrir o seguinte custa mais uma releitura do arquivo de retomada.
- O freio (pergunta 4) e a trava (pergunta 5) são scripts Python que o Claude Code roda antes de cada uso de ferramenta. Eles só podem NEGAR uma ação, nunca aprovar nada: não pulam nenhum pedido de permissão. O freio nega abrir agente (nível 2 ou mais de 6 filhos); a trava nega escrever, rodar comando que escreve ou abrir agente numa pasta que o agente de OUTRA sessão está usando.
- Se o script falhar por erro dele, ele deixa tudo passar (a proteção some, nada trava). Se o Python não existir ou o caminho estiver errado, o Claude Code mostra o erro do hook e segue; também não trava o trabalho (mas confira se `python` abre no terminal da pessoa; no Windows pode ser `py`).
- Os dois leem arquivos internos do Claude Code (a lista de agentes da conversa) que podem mudar numa atualização; nesse caso deixam de proteger, sem bloquear nada por engano.
- A trava grava arquivos pequenos em `<pasta de configuração>/locks` e um registro em `<pasta de configuração>/hooks/copy_lock.log`. Uma trava presa por engano bloqueia outra sessão de escrever naquela pasta até soltar (some sozinha em 2 horas, ou quando o Claude dono fecha). Nenhum script usa a rede.
- "Opus coordena" (pergunta 2) gasta mais etapas e mais agentes; não é economia comprovada: no PC do autor ainda está em teste.
**Como desfazer:** apague do CLAUDE.md as linhas desta caixa (vale na próxima sessão). Para o freio e a trava: apague a entrada que chama `agent_limit.py` / `copy_lock.py` em `"PreToolUse"` (e a de `copy_lock.py` em `"SubagentStop"`) no `settings.json`, ou volte a cópia de segurança da Caixa 1; depois apague os arquivos em `hooks/`. Trava presa agora: `python <pasta de configuração>/hooks/copy_lock.py release <pasta>`. Ver as travas: `... copy_lock.py list`.

Perguntas (são 5; a caixa de perguntas aceita 4 por chamada: faça em 2 chamadas, 1 a 3 e depois 4 e 5):

1. **Agente curto: parar em ~100 chamadas e passar o bastão?** — cabeçalho `Agente curto`
   - **Sim, em ~100 (Recomendado)** — O agente fecha o item, grava onde parou num arquivo e devolve o resumo. Se sobrou trabalho, a conversa principal abre outro agente a partir desse arquivo. Risco: pode haver trabalho dividido em mais agentes.
   - **Não** — Nada muda; agentes seguem sem limite de tamanho e podem ficar caros se rodarem muito tempo.
2. **Qual modelo para cada tipo de trabalho?** — cabeçalho `Modelos`
   - **Por papel (Recomendado)** — Sonnet por padrão; Haiku para o mecânico (achar arquivo, filtrar log, contar); Opus só para código delicado (segurança, contas, dinheiro, criptografia). Risco: Haiku erra mais em tarefa que parecia simples.
   - **Experimental: Opus coordena** — Opus coordena, Sonnet executa: um agente forte (Opus) escreve o pedido de cada pedaço e abre agentes Sonnet um por vez; o Sonnet não abre agentes. O Opus roda os testes por script, revisa só o que mudou e conserta; pedaço que falhar duas vezes ele mesmo faz. Risco: mais etapas e mais agentes; não é economia comprovada (em teste no PC do autor).
   - **Não mudar** — Nada muda; você continua escolhendo o modelo de cada agente na mão.
3. **Agentes em lote e com resposta curta?** — cabeçalho `Lote`
   - **Sim (Recomendado)** — Um agente por tarefa (não um por pedacinho); vários lançados na mesma mensagem; cada um grava o detalhe num arquivo e devolve 5 a 10 linhas. Risco: a resposta curta esconde detalhe (está no arquivo).
   - **Não** — Nada muda; agentes devolvem respostas longas, que a conversa principal relê a cada passo.
4. **Instalar o freio de agentes?** — cabeçalho `Freio` (só com Python)
   - **Sim (Recomendado)** — Um script impede que um agente aberto por outro agente abra mais agentes, e limita cada agente a 6 filhos. Evita cadeia sem fim. Risco: pode negar um agente que você queria; a mensagem diz o motivo.
   - **Não** — Nada muda; cadeias de agentes sem limite continuam possíveis.
5. **Instalar a trava de cópia?** — cabeçalho `Trava` (só com Python)
   - **Sim (Recomendado)** — Quando um agente escreve numa cópia de trabalho (uma pasta com `.git`, `.p4config` ou um `.uproject`), a sessão dele fica com essa pasta. Outra sessão não pode escrever ali nem lançar agente nela até esses agentes terminarem. Ler, e editar notas `.md` e `.txt`, sempre passam. Faz diferença quando duas sessões podem trabalhar na mesma pasta, por exemplo depois de uma troca de sessão com um agente ainda rodando. Risco: uma trava presa bloqueia a outra sessão até soltar (2 horas, ou `release`).
   - **Não** — Nada muda; duas sessões podem mexer na mesma pasta ao mesmo tempo e se atrapalhar.

Passos:
1. Perguntas 1 a 3: grave as regras aceitas. Na pergunta 2, grave a regra "Por papel" ou a "Experimental" (não as duas). A linha "[Só com cache de 1 hora]" entra só se a Caixa 2, pergunta 2, foi "Sim, cache de 1 hora".
2. "Experimental": crie `~/Documents/piloto_opus_sonnet.md` (não na pasta de configuração, que é protegida: escrever lá pede permissão) com uma tabela (data, tarefa, passou de primeira?, o que o Opus teve que refazer). A regra manda anotar cada caso e, depois de ~6, perguntar à pessoa se vira padrão. Funciona melhor com o freio (pergunta 4), que impede o agente Sonnet de abrir outros.
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
   3. Diga à pessoa: o freio lê um arquivo interno do Claude Code, que pode mudar numa atualização. Se mudar, o freio para de frear, mas nunca bloqueia nada que não devia.
   4. Conferir. Algumas versões só leem os hooks ao abrir a sessão, e o Claude não consegue abrir sessão nova por conta própria nesta altura. Então: tente nesta sessão; se o bloqueio não vier, peça à pessoa para abrir uma sessão nova (no app, uma sessão nova na mesma pasta; no terminal, sair e rodar `claude` de novo) e colar o pedido abaixo nela. Se ela preferir, deixe o teste para a Caixa final. O teste usa três agentes: a conversa abre o A; o A abre o B; o B tenta abrir o C e deve ser bloqueado; o A devolve a mensagem que o B recebeu. Faça o pedido: *"Teste do freio. Abra um agente Haiku, o A, e peça a ele: 'abra um agente B e peça a B: abra um agente C que responda oi; se B for bloqueado, devolva a mensagem do bloqueio. Depois me devolva a mensagem que B recebeu.' Devolva o que A respondeu."* O esperado é a mensagem "Agent limit: ...". Se o agente A ou o B disser que não tem a ferramenta de abrir agente, o freio não faz falta nessa versão: avise e siga.
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

   3. Diga à pessoa: só agentes pegam a trava (as edições da própria conversa principal não pegam), e agentes da mesma sessão a dividem. Ela some quando o último agente daquela sessão devolve sem nada em segundo plano, quando a sessão dona é fechada ou arquivada (o processo do Claude dela termina), ou depois de 2 horas sem sinal dos agentes dela. Para ver as travas: `python <pasta de configuração>/hooks/copy_lock.py list`; para soltar uma, só com certeza de que o agente acabou: `python <pasta de configuração>/hooks/copy_lock.py release <pasta>`. Ela lê campos que o Claude Code manda para os hooks e arquivos internos do Claude Code, que podem mudar numa atualização; em qualquer erro, deixa tudo passar. Nenhuma regra vai para o CLAUDE.md: a própria mensagem do bloqueio diz o que fazer.
   4. Conferir: `python <pasta de configuração>/hooks/copy_lock.py test` roda 17 casos simulados numa pasta temporária, sem mexer nas travas reais; a última linha tem que ser `ALL OK`. Depois confira o `settings.json` com `check_settings.py`.

Texto da regra:
> - Agente que edita ou corrige: o pedido dele diz "ao chegar a ~100 chamadas, feche o item, grave o ponto de retomada em <arquivo> e devolva o resumo". Se sobrou trabalho, a conversa principal abre outro agente a partir desse arquivo. Tarefa grande já nasce dividida em agentes de ~100 chamadas.
> - **[Só com cache de 1 hora]** Agente não fica mais de ~50 minutos numa espera só; espera maior = gravar o ponto de retomada e devolver.
> - Modelos por papel: Sonnet por padrão; Haiku para o mecânico (achar arquivo, filtrar log, contar); Opus só para agente que edita código delicado (segurança, contas, dinheiro, criptografia).
> - (Experimental) Código novo ou correção fora de segurança, contas e criptografia: um agente Opus coordena. Ele escreve o pedido de cada pedaço, abre agentes Sonnet um de cada vez (~80 chamadas cada; o Sonnet não abre agentes), roda os testes por script, revisa só o que mudou, conserta o que estiver ruim e devolve poucas linhas. Pedaço que falhar duas vezes, o Opus faz. Anotar cada caso em `~/Documents/piloto_opus_sonnet.md`; depois de ~6 casos, perguntar à pessoa se vira padrão.
> - Agentes: um por tarefa, não um por pedacinho; vários ao mesmo tempo saem na MESMA mensagem; cada um grava o detalhe num arquivo e devolve 5 a 10 linhas.

---

## Caixa 6 — Passagem e troca de sessão

**O que isto faz:** o Claude mantém, em cada projeto, um arquivo curto de passagem (o que foi feito, o que está pela metade, o próximo passo exato) e um arquivo de resumos (uma entrada por sessão, para achar depois quem fez o quê). Ele cria os dois sozinho no primeiro trabalho de várias etapas, anota os passos ao fechar cada parte e, quando a conversa fica grande ou a etapa muda, uma sessão nova começa pela passagem, com a conversa vazia.
**Por quê:** foi a maior economia do autor: a conversa principal caiu 75% depois desta regra (medido no PC do autor, set-nov/2026; pode variar no seu uso). O resumo automático (compactação) perde detalhe; o arquivo não.
**Riscos reais:**
- Os arquivos ficam na pasta do projeto, em texto simples: nada sai do computador por causa deles. Mas se a pasta for publicada (repositório, nuvem), a passagem vai junto; não escreva senha, token ou dado pessoal nela. Avise a pessoa disso.
- O Claude passa a criar e reescrever `PASSAGEM.md`/`RESUMOS.md` sozinho, sem perguntar a cada vez: aparecem arquivos novos nos projetos (e num repositório, em `git status`). Se não quiser versionar, ponha-os no `.gitignore`.
- Uma passagem velha ou errada faz a sessão nova partir do ponto errado. O Claude confere o "próximo passo" antes de agir e pede confirmação em ação irreversível, mas a pessoa deve olhar o arquivo se a sessão nova parecer perdida.
- Trocar de sessão custa uma releitura da passagem e perde o que só estava na conversa; é um troco pequeno perto de seguir numa conversa enorme.
- O lembrete de começo de sessão (pergunta 4) é um script Python sem rede: custa uma linha no começo de cada sessão; se falhar, o Claude Code mostra o erro e segue.
**Como desfazer:** apague do CLAUDE.md as linhas desta caixa (vale na próxima sessão); os arquivos `PASSAGEM.md`/`RESUMOS.md` já criados ficam, apague à mão se quiser. Lembrete: apague a entrada de `"SessionStart"` que chama `handoff_reminder.py` no `settings.json` (ou volte a cópia de segurança da Caixa 1) e o arquivo em `hooks/`.
**Atenção:** os números desta caixa (trocar em ~250 mil) supõem a janela de 1 milhão de tokens. Veja a janela da pessoa (regra "Janela de contexto", no começo do guia; sem conseguir ver, suponha 200 mil). Se for de 200 mil, troque de sessão em ~100 mil (diga isso à pessoa na pergunta 2 e use `<100>` na regra) e não baixe a compactação da Caixa 2.

Perguntas:

1. **Passagem e resumos nos projetos com trabalho em andamento?** — cabeçalho `Passagem`
   - **Sim, passagem + resumos (Recomendado)** — Na primeira tarefa de várias etapas de um projeto, crio sozinho `PASSAGEM.md` e `RESUMOS.md` na raiz, a partir dos modelos deste guia (se o projeto já tiver um arquivo assim, uso o dele). Anoto os passos na passagem ao fechar cada parte e, em toda troca de sessão e fim de etapa, acrescento uma entrada no `RESUMOS.md` (Fez / Decidiu / Ficou). Risco: aparecem arquivos novos nos projetos, sem perguntar a cada vez.
   - **Só a passagem** — Crio e mantenho só o `PASSAGEM.md`; sem arquivo de resumos. Menos arquivos, mas depois não há onde achar em qual sessão algo foi feito.
   - **Não** — Nada muda; a sessão nova começa sem arquivo de passagem e perde o que só estava na conversa.
2. **Quando trocar de sessão?** — cabeçalho `Troca` (só se `Passagem` não foi "Não")
   - **~200 mil ou etapa nova** — Mais trocas, cada passo relê menos. Etapa nova sempre começa em sessão nova. Risco: mais trocas, cada uma perde um pouco do que a conversa sabia.
   - **~250 mil ou etapa nova (Recomendado)** — Na conta do autor (260 sessões), entre 200 e 300 mil o custo total quase não muda, e 250 fica no meio. Acima de ~300 mil, cada passo relê tanto que sai mais caro. Etapa nova sempre começa em sessão nova.
   - **~300 mil ou etapa nova** — Menos trocas, cada passo mais caro. Vale quando a passagem perde muito do que a conversa sabia.
   - **Só quando eu pedir** — Nada troca sozinho; só aviso em uma linha quando a conversa passar de ~250 mil. A conversa pode ficar cara se você esquecer.
3. **Uma tarefa por sessão?** — cabeçalho `Uma tarefa`
   - **Sim (Recomendado)** — Assunto novo, sem ligação com o que está aberto, vai para uma sessão nova (ou `/clear`), não para o fim desta conversa. Risco: mais sessões abertas para você acompanhar.
   - **Não** — Nada muda; assuntos diferentes se acumulam na mesma conversa, que fica grande e cara.
4. **Lembrete de começo de sessão para ler a passagem?** — cabeçalho `Lembrete` (só se `Passagem` não foi "Não"; com Python)
   - **Sim (Recomendado)** — Instalo um script (`handoff_reminder.py`, evento de começo de sessão) que, se a pasta aberta tiver um `PASSAGEM*.md` ou `HANDOFF*.md`, mostra ao Claude uma linha mandando ler o arquivo primeiro. Só lista a pasta: não lê arquivo, não escreve, não usa a rede. Custo: uma linha a mais no começo de cada sessão nessas pastas. Se falhar (ou o Python não existir), o Claude Code mostra o erro e a sessão segue normal.
   - **Não** — Nada muda; a regra do CLAUDE.md já manda ler a passagem, mas sem esse lembrete o Claude pode esquecer.

Passos:
1. Pergunta 1 "Sim, passagem + resumos" ou "Só a passagem": copie `pt/PASSAGEM_MODELO.md` para `<pasta de configuração>/modelos/PASSAGEM_MODELO.md` (crie `modelos` se não existir). Só no "Sim, passagem + resumos": copie também `pt/RESUMOS_MODELO.md` para `<pasta de configuração>/modelos/RESUMOS_MODELO.md`. São os modelos: a sessão cria `PASSAGEM.md` (e `RESUMOS.md`) de cada projeto a partir deles. Grave a regra da versão escolhida.
2. Pergunta 2: grave a regra com o número escolhido, ou a regra "Só quando eu pedir". Diga à pessoa onde ver o tamanho da conversa: no app, o indicador de contexto junto da caixa de mensagem; no terminal, o comando `/context`.
3. Pergunta 3: grave a regra. Lembre a pessoa: só ela pode digitar `/clear` ou `/compact`; o Claude não consegue.
4. Pergunta 4 "Sim":
   1. Copie `scripts/handoff_reminder.py` para `<pasta de configuração>/hooks/handoff_reminder.py`.
   2. No `settings.json`, dentro de `"hooks"`, acrescente em `"SessionStart"` (crie a lista se não existir; não apague o que já houver):

      ```json
      "SessionStart": [
        {
          "hooks": [
            { "type": "command", "command": "python \"<pasta de configuração>/hooks/handoff_reminder.py\"", "timeout": 10 }
          ]
        }
      ]
      ```

   3. Diga à pessoa: o script não aprova nem bloqueia nada, só imprime uma linha, e só procura na pasta onde a sessão abriu. Confira com `python <pasta de configuração>/hooks/handoff_reminder.py --test` (a última linha tem que ser `ALL OK`) e depois com `check_settings.py`. O lembrete aparece na próxima sessão aberta numa pasta com passagem.
5. Se houver um projeto com trabalho em andamento agora, ofereça criar o `PASSAGEM.md` dele (e o `RESUMOS.md` ao lado, se a pergunta 1 foi "Sim, passagem + resumos") (só com sim).

Texto da regra (na troca de sessão, grave uma das duas versões):
> - Passagem: todo projeto com trabalho em andamento tem um arquivo de passagem (o que o projeto já tiver, ou `PASSAGEM.md` na raiz, a partir de `<pasta de configuração>/modelos/PASSAGEM_MODELO.md`). No primeiro trabalho de várias etapas num projeto, criar o arquivo sozinho (e o de resumos, abaixo). Reescrever, não acrescentar no fim. Anotar na passagem os passos feitos ao fechar cada parte, antes da troca de sessão e quando o vigia de gasto avisar. Pergunta sem resposta vai na seção "Perguntas à pessoa". Sessão nova começa lendo a passagem e faz o "próximo passo exato" sem perguntar, exceto ações irreversíveis, que pedem confirmação. Nunca escrever senha, token ou dado pessoal na passagem.
> - **[Número]** Troca de sessão: com a conversa em ~<250> mil tokens, ou numa etapa nova, fechar a parte em andamento, atualizar a passagem e trocar de sessão. Se não houver regra de sucessora, dizer à pessoa em uma linha o que colar na sessão nova.
> - **[Só quando eu pedir]** Troca de sessão só quando a pessoa pedir; avisar em uma linha quando a conversa passar de ~<250> mil tokens.
> - Uma tarefa por sessão: assunto novo e sem ligação vai para sessão nova.
> - **[Só com passagem + resumos]** Resumos: todo projeto com arquivo de passagem tem, ao lado dele, um arquivo de resumos (`PASSAGEM.md` → `RESUMOS.md`; `PASSAGEM_X.md` → `RESUMOS_X.md`; criar sozinho a partir de `<pasta de configuração>/modelos/RESUMOS_MODELO.md`). Passo obrigatório de TODA troca de sessão e de todo fim de etapa, sem a pessoa pedir: ao fechar (antes de abrir a sucessora ou de encerrar a etapa), acrescentar no fim UMA entrada `## <n> — <título da sessão> (<data>, <id da sessão>)` com até três linhas curtas: **Fez** (com os nomes que alguém procuraria depois: arquivos, telas, ferramentas), **Decidiu** (o que ficou fechado, e por quem), **Ficou** (o que ficou aberto ou sem resposta, ou "nada"). Não relê o arquivo inteiro, só acrescenta. Serve para achar depois em qual sessão algo foi feito.

---

## Caixa 7 — Sessão sucessora automática (a mais trabalhosa)

**O que isto faz:** na hora de trocar de sessão (Caixa 6), em vez de pedir à pessoa para abrir uma sessão nova, o próprio Claude abre a sucessora, que começa pela passagem. A sucessora pode abrir a próxima do mesmo jeito: a cadeia segue enquanto houver trabalho. Conforme as respostas, a caixa grava regras no `CLAUDE.md` e pode gravar no `settings.json` regras de permitir e o modo automático como padrão, instalar um hook (programa que o Claude Code roda antes de uma ação) que aprova sozinho certas ações nos "estepes" (sessões reservas, paradas e arquivadas) e guardar um token (chave de acesso) para rodadas sem tela. **Esta caixa inteira é sensível:** no modo Rápido ela não é instalada nem perguntada (Grupo 3 do pacote recomendado); quem quiser roda esta caixa depois, caixa por caixa, e cada parte abaixo vira pergunta, com o risco dela.
**Avançado:** recomendado só depois de uma ou duas semanas usando as outras táticas.
**Por quê:** sem isso, a troca depende da pessoa estar olhando. O autor teve uma etapa parada a noite inteira esperando um clique. E a sessão anterior, se continuar ligada à nova, acorda e relê a conversa inteira cada vez que a nova termina um turno.

**Riscos reais:**
- **Abre sessões sozinho**, sem a pessoa na tela, e pode deixar sessões reservas (estepes) paradas na pasta. Cada sessão nova recarrega as instruções e lê a passagem de novo, então pode gastar mais cota do que seguir numa conversa só; o estepe gasta um turno curto ao nascer. O autor não tem número medido para isso.
- **Ações aprovadas sem a pessoa ver (só se ela aceitar cada uma):** o hook dos estepes, as regras de permitir da tarefa agendada e o modo automático como padrão. As regras de permitir e o modo automático valem para TODAS as sessões e projetos desta conta do computador, não só para a sucessora.
- **Arquiva sessões** (a anterior e os estepes usados). Arquivar não apaga: dá para desarquivar.
- **Remote Control** liga a sessão à conta claude.ai da pessoa: quem entrar nela manda ordens ao computador.
- **Token** (só para quem usa terminal): é uma chave da conta guardada num arquivo no computador.
**Como desfazer** (vale na próxima sessão; as sessões já abertas guardam o que leram; tudo isto também pode ser pedido ao Claude):
- `CLAUDE.md`: apague as linhas que começam com "Sucessora:", "Fechar a anterior:", "Avisar e seguir:", "Estepes:", "Troca com agente rodando:", "Remote Control:", "Herança" e "Rodadas sem tela:".
- `settings.json` (ou volte a cópia de segurança da Caixa 1): tire de `"permissions"` → `"allow"` as duas linhas `"mcp__scheduled-tasks__create_scheduled_task"` e `"mcp__scheduled-tasks__run_scheduled_task"`; tire `"defaultMode": "auto"` de `"permissions"` (ou ponha de volta o valor que a cópia de segurança mostra); tire de `"hooks"` → `"PreToolUse"` o bloco cujo `matcher` é `SendMessage|mcp__ccd_session_mgmt__.*`; tire de `"permissions"` → `"deny"` a linha `Read(.../relay_token.txt)` (opcional: ela é inofensiva).
- Arquivos: apague `<pasta de configuração>/hooks/spare_allow.py`, `.../hooks/spare_allow.log`, `.../spares.txt`, `.../tools/session_relay.py`, `.../relay_token.txt` e, em cada projeto, `SUCESSORA.md` e `relay.log`.
- Sessões e tarefa: os estepes são as sessões de título "Estepe <pasta> N" na lista de arquivadas do app; deixe arquivadas (arquivada não gasta nada) ou apague (pedindo ao Claude: `list_sessions` e `delete_session`, se a ferramenta existir, ou pelo menu da sessão). A tarefa agendada é a "sucessora-<pasta>": peça ao Claude `list_scheduled_tasks` e `delete_scheduled_task`, ou apague na seção Rotinas do app. Atenção: apagar uma tarefa arquiva a sessão que ela abriu.
- Remote Control: desligue em cada sessão (`set_remote_control` com false, ou o menu da sessão) e desligue nas configurações do app a opção que liga em toda sessão nova.
- Token: apague o arquivo `relay_token.txt` (a Caixa 7, caminho B, diz como revogar).

**Dúvidas que um revisor cético faria, com resposta direta:**
- **O `spare_allow.py` contorna as permissões?** Ele passa por cima de uma coisa só: o pedido de aprovação (e o filtro do modo automático) para seis ferramentas, e apenas quando o alvo é um id listado em `spares.txt`: `SendMessage` (mensagem para a sessão) e, no app, desarquivar, mudar título, mudar modelo, mudar esforço e ligar ou desligar o Remote Control. Ele não lê o texto da mensagem. Todo o resto segue o fluxo normal e continua pedindo aprovação ou passando pelo filtro: abrir sessão (`start_session`), arquivar, soltar, apagar, parar, mudar o modo de permissão de outra sessão e qualquer ação em sessão que não esteja na lista. Regras de negar, pelo que a documentação do Claude Code diz, continuam valendo (o autor não testou). Duas ressalvas: uma mensagem a um estepe é uma ordem a outra sessão, que depois age com as permissões dela; e, se o id ficar em `spares.txt` depois que o estepe virou sessão de trabalho, aquelas seis ações seguem aprovadas nela (o Claude tira o id depois de usar o estepe; confira o arquivo de vez em quando). Cada decisão vai para `hooks/spare_allow.log` (hora, ferramenta e id, sem o texto das mensagens; o arquivo não é limpo sozinho).
- **O que acontece se o hook falhar (Python ausente, erro, passar dos 10 s)?** Nada é aprovado: pela documentação do Claude Code, um hook que falha não bloqueia nem aprova, e a ação segue o fluxo normal (pede aprovação ou cai no filtro). Perde-se só a comodidade: o estepe pode ser barrado e a troca cai no "Avisar e seguir". O autor não testou apagando o Python.
- **O modo automático (`"defaultMode": "auto"`) deixa o Claude agir sem perguntar em quê?** Em vez de pedir seu ok a cada ação, um filtro julga cada uma: deixa passar o que parece seguro e rotineiro (ler e editar arquivos do projeto, comandos comuns) e barra o que parece arriscado ou fora do que você pediu. Ele pode errar nos dois lados. Não é o modo que ignora todas as permissões (o guia não usa esse), e as regras de negar continuam valendo. Vale para toda sessão nova que a pessoa abrir, em qualquer projeto.
- **Token em arquivo: quem lê, como apagar e revogar?** O arquivo `relay_token.txt` fica na pasta de configuração. No Windows o guia deixa só o usuário da pessoa com acesso; no Mac e no Linux, só o dono (modo 600). Mesmo assim, qualquer programa que rode como a pessoa, administradores do computador e cópias de segurança ou nuvem que levem a pasta conseguem ler. O Claude não lê (regra de negar a leitura, que vale para a ferramenta de leitura, mas não é garantia contra um comando de terminal). Apagar: apague o arquivo. Revogar: a documentação oficial (conferida em novembro de 2026) não mostra como revogar só esse token; olhe a lista de acessos e sessões nas configurações da conta em claude.ai ou fale com o suporte da Anthropic. O token vale por um ano.
- **Isso pode gastar mais?** Pode. Cada sessão nova (sucessora, estepe, tarefa agendada) começa com a conversa vazia, mas recarrega instruções e memória e lê a passagem, e o primeiro uso dela não aproveita o que a anterior já tinha guardado em cache. Em troca, evita o custo de seguir numa conversa muito grande. "Avisar e seguir" e a conversa que passa do limite sem resposta custam o contrário: cada passo numa conversa grande gasta mais. As rodadas sem tela gastam da mesma cota. Sem número do autor para a soma.
- **Dados saem do computador?** Os scripts do pacote não fazem chamada de rede. O que roda no Claude (inclusive as rodadas sem tela, que chamam o comando `claude`) manda a conversa à Anthropic, como todo uso do Claude. O Remote Control mostra a conversa na conta claude.ai da pessoa e nos aparelhos dela.

Pré-requisito: Caixa 6, pergunta 1 (`Passagem`), respondida "Sim, passagem + resumos" ou "Só a passagem". Sem arquivo de passagem, pule esta caixa. Se esta caixa for rodada depois, numa outra sessão, faça antes de novo as perguntas `Onde usa` e `Plano` da Caixa 1 e veja no `CLAUDE.md` o que as Caixas 5 e 6 gravaram.

Há dois caminhos. Explique os dois à pessoa antes da caixa:
- **Caminho A, pelo app (visível, sem token):** no app desktop, o Claude tem uma ferramenta para abrir outra sessão. A sucessora aparece na barra lateral como qualquer sessão. É o recomendado.
- **Caminho B, pelo terminal (sem tela, precisa de token):** um script roda o Claude pelo terminal (`claude -p`) em rodadas, cada uma com conversa vazia, lendo e atualizando a passagem. Não aparece no app; o resultado fica nos arquivos e num log. Precisa de um token de acesso de longa duração. Serve só para quem usa só o terminal: no app, os estepes, o "avisar e seguir" e a tarefa agendada cobrem as recusas sem token, então quem usa o app não instala o token.

**Antes de mostrar qualquer pergunta** (só se a Caixa 1 respondeu "App desktop" ou "Os dois"): ache as ferramentas com ToolSearch, pelo nome (lista no passo 1 do caminho A), e veja o modo de permissão desta sessão (`get_session` com "self", campo `permissionMode`). Depois:
- Se `start_session` existe: siga como abaixo.
- Se `start_session` não existe: o caminho A não está disponível nesta versão. Diga isso à pessoa em uma linha e trate o caso como "Terminal" (próximo item): não faça as perguntas 1, 2, 5, 6, 7, 8, 9 e 10, que dependem dessa ferramenta. Se ela recusar o caminho B ("Agora não"), grave só a regra "[Eu abro]" (a regra mínima: o Claude atualiza a passagem e **avisa a pessoa para abrir a sessão nova**), não grave as regras de fechar a anterior nem a de herança, ponha "Sessão sucessora automática (sem a ferramenta no app)" em "Recusadas" e pule os passos do caminho A.

Como mostrar as perguntas (são dez, divididas em até três chamadas do AskUserQuestion, que aceita no máximo quatro perguntas por vez; as condicionais só vêm depois da resposta que as libera). Antes de cada chamada, mostre em poucas linhas o "Riscos reais" e o "Como desfazer" das perguntas dela:
- Se a Caixa 1 respondeu "Terminal": não faça as perguntas 1, 2, 5, 6, 7, 8, 9 e 10, que dependem do app. Faça só a 3 e, se a resposta for "Sim, me guie", a 4 numa segunda chamada. A sucessora desse caso é a regra do caminho B; com "Agora não", fica a regra "[Eu abro]".
- Se respondeu "App desktop" ou "Os dois": não faça as perguntas 3 e 4 (o token não é preciso no app; trate como "Agora não", sem pôr em "Recusadas"). Primeira chamada: pergunta 1. Segunda chamada, só se a 1 for "O Claude, sozinho": perguntas 2, 5, 6 e 8 (com as outras respostas da 1, o Claude não abre sessão, então não há anterior a fechar, reserva nem Remote Control de sucessora a decidir). Terceira chamada, só com as respostas da segunda e só com as perguntas que elas liberam: a 7 e a 10 (se a 6 for "Sessão de estepe") e a 9 (se a 5 for "Liberar as duas regras"); se nenhuma for liberada, não há terceira chamada. Com "O Claude propõe, eu clico" ou "Eu abro" na 1, só a primeira chamada acontece. Na regra "[O Claude, sozinho]", o "Se isso também falhar" fica "aviso a pessoa em uma linha".

Pergunta 3 e o plano (Caixa 1): com "Chave de API", não faça a pergunta 3 (o token é só das assinaturas) e trate como "Agora não"; se a Caixa 1 também respondeu "Terminal", fica a regra "[Eu abro]". Com "Não sei", faça a pergunta e diga que o token só existe nos planos de assinatura (Pro, Max, Ultra, Team e Enterprise); se o comando do token recusar a conta dela, trate como "Agora não".

Na pergunta 3 (só no caso "Terminal"), ponha "(Recomendado)" em **"Sim, me guie"**.

Na pergunta 9, use o modo de permissão visto antes das perguntas. Se for `auto` (modo automático), ponha "(Recomendado)" em **"Sim, automático"**; se for outro, ou se não deu para ver, em **"Não mudar"**. Nunca ponha o modo automático como padrão sem a pergunta 9 respondida "Sim, automático".

1. **Quem abre a sessão sucessora?** — cabeçalho `Sucessora` (sensível: abre sessões sozinho; só no app, com `start_session`)
   **Riscos reais:** a sessão nova nasce sem você olhar e pode ficar escondida (ver "Rotinas" nas travas); cada sessão nova recarrega as instruções e lê a passagem de novo, o que pode gastar mais cota que seguir numa conversa só; a cadeia só para quando a passagem diz que a etapa acabou ou tem pergunta para você. Com a primeira opção o Claude grava também a regra "Troca com agente rodando".
   **Como desfazer:** apague do `CLAUDE.md` as linhas "Sucessora:", "Troca com agente rodando:" e "Herança"; arquive pela barra lateral as sessões que ele abriu. Vale na próxima sessão.
   - **O Claude, sozinho (Recomendado)** — Na hora da troca, o Claude atualiza a passagem, abre a sucessora e para. Você só vê a nova sessão aparecer; ninguém pede seu ok, e a cadeia segue sozinha até a passagem dizer que acabou.
   - **O Claude propõe, eu clico** — Aparece um cartão para você iniciar. Nada abre sem seu clique; se você não estiver olhando, o trabalho para até o clique.
   - **Eu abro** — O Claude atualiza a passagem e diz o que colar na sessão nova. Nada abre sozinho; é a opção mais segura e dá mais trabalho a você.
2. **A sucessora fecha a anterior?** — cabeçalho `Fechar mãe` (sensível: arquiva sessões; só se `Sucessora` for "O Claude, sozinho")
   **Riscos reais:** arquivar não apaga a conversa (ela some da lista normal e volta pela lista de arquivadas); se o Claude errasse o id, arquivaria a sessão errada, por isso o id vem no pedido ("Sessão anterior: <id>") e a regra não vale para sessão paralela de outra tarefa. A sucessora também desliga o Remote Control da anterior e se solta dela. Na regra "Troca com agente rodando", a sessão anterior se arquiva sozinha quando o último agente dela devolve.
   **Como desfazer:** apague do `CLAUDE.md` a linha "Fechar a anterior:"; para trazer uma sessão de volta, desarquive pela lista de arquivadas.
   - **Sim (Recomendado)** — A sucessora se solta da anterior e a arquiva, para a anterior não acordar e reler tudo a cada turno da nova. O título ganha um número ("Site" → "Site 2" → "Site 3").
   - **Não** — Nada é arquivado sozinho; as duas ficam abertas e a anterior pode reler a conversa inteira a cada turno da nova (gasta cota) até você arquivá-la. Na regra "Troca com agente rodando", tire o trecho em que a sessão anterior se arquiva sozinha.
3. **Instalar o token para as rodadas sem tela (caminho B)?** — cabeçalho `Token` (sensível: grava uma chave da conta em arquivo; só no terminal, fora de "Chave de API", com Python)
   **Riscos reais:** o token é uma chave de acesso à conta Claude da pessoa, válida por um ano: quem o tiver gasta a cota dela. Fica em `<pasta de configuração>/relay_token.txt`; o guia restringe o arquivo ao usuário dela, mas qualquer programa que rode como ela, administradores e cópias de segurança ou nuvem que levem a pasta podem lê-lo. O Claude nunca vê o token. As rodadas rodam sem ninguém olhar e gastam a mesma cota.
   **Como desfazer:** apague `relay_token.txt`, `tools/session_relay.py` e a regra "Rodadas sem tela:"; tire do `settings.json` a linha `Read(.../relay_token.txt)` (opcional). Para revogar, ver "Token em arquivo" acima e o fim do caminho B.
   - **Sim, me guie** — Você roda um comando, faz login no navegador e grava o token num arquivo. O Claude nunca vê o token. Leva uns 10 minutos.
   - **Agora não** — Nada é gravado; fica só o caminho A, que precisa do app desktop.
4. **O que as rodadas sem tela podem usar?** — cabeçalho `Permissões` (só se `Token` for "Sim, me guie")
   **Riscos reais:** nenhuma rodada pede aprovação: o que está na lista passa direto e o resto é recusado. Mesmo só com arquivos, uma rodada errada pode editar ou sobrescrever arquivos do projeto sem você ver (use git ou uma cópia).
   - **Só arquivos (Recomendado)** — Ler, buscar, criar e editar arquivos. Nenhum comando.
   - **Arquivos + terminal** — Também roda comandos (testes, compilação). Mais útil e mais arriscado: ninguém está olhando, e o terminal da rodada também enxerga o token.
   - **Decidir por projeto** — O Claude pergunta na primeira vez em cada projeto, e nada roda sem esse sim.
5. **Liberar a reserva por tarefa agendada?** — cabeçalho `Agendada` (sensível: grava regras de permitir; só se `Sucessora` for "O Claude, sozinho")
   **Riscos reais:** acrescenta duas regras em `"permissions"` → `"allow"` do `settings.json`: criar e rodar tarefa agendada sem pedir aprovação. Elas valem para TODAS as sessões e projetos, não só para a sucessora; uma sessão induzida por texto malicioso (numa página ou arquivo) poderia agendar algo que roda depois, sem ninguém olhando, no modo de permissão padrão e sob as regras de negar. A tarefa só é criada na primeira troca em que estepe e "Avisar e seguir" não bastarem.
   **Como desfazer:** tire de `"allow"` as linhas `"mcp__scheduled-tasks__create_scheduled_task"` e `"mcp__scheduled-tasks__run_scheduled_task"`; apague a tarefa `sucessora-<pasta>` (ver "Como desfazer" no topo da caixa). Vale na próxima sessão.
   - **Liberar as duas regras (Recomendado)** — O Claude cria e roda a tarefa agendada sem pedir aprovação, mas só como reserva. Sem as regras, o modo automático costuma barrar a tarefa.
   - **Não liberar** — Nada é gravado; quando o app recusar abrir a sessão, e estepe e "Avisar e seguir" não bastarem, a reserva é o caminho B (se instalado) ou um aviso a você.
6. **Quando o app recusar abrir a sucessora?** — cabeçalho `Recusa` (sensível: pode criar e reativar sessões sozinho; só se `Sucessora` for "O Claude, sozinho")
   **Riscos reais:** "Sessão de estepe" cria sessões reservas sem você ver (ver a pergunta 7) e depois as arquiva e reativa; "Avisar e seguir" deixa a conversa crescer até sua próxima mensagem, e cada passo numa conversa grande gasta mais cota; "Reserva na hora" pode deixar a sucessora escondida em Rotinas.
   **Como desfazer:** apague do `CLAUDE.md` as linhas "Estepes:" e "Avisar e seguir:"; apague os estepes (ver "Como desfazer" no topo da caixa).
   - **Sessão de estepe (Recomendado)** — A cada mensagem sua, o Claude confere e repõe algumas sessões paradas e arquivadas na pasta do projeto (os "estepes"; quantos, a pergunta 7 diz). Na troca, ele desarquiva um, dá o título novo e manda a tarefa por mensagem: a sucessora sai na hora, na lista normal, mesmo sem você na tela. Sem estepe na pasta, cai no "Avisar e seguir".
   - **Avisar e seguir** — O Claude grava a passagem, manda um aviso (no computador e, com Remote Control ligado, no celular) e continua trabalhando nesta sessão. Na sua próxima mensagem, qualquer uma, ele abre a sucessora na lista normal antes de tudo. A reserva (tarefa agendada, rodadas sem tela) fica só para quando a conversa passar muito do limite sem resposta sua. Não cria sessão nenhuma antes da sua mensagem.
   - **Reserva na hora** — O Claude usa logo a reserva. A sucessora sai mais cedo, mas, se for por tarefa agendada, fica escondida na seção Rotinas e não consegue abrir a próxima sozinha.
7. **Quantos estepes por pasta?** — cabeçalho `Estepes` (só se a pergunta 6 for "Sessão de estepe"; a opção "Outro" da caixa deixa a pessoa digitar outro número)
   **Riscos reais:** o Claude cria até esse número de sessões vazias na pasta, sem você ver, e repõe as usadas a cada mensagem sua. Cada uma gasta um turno curto ao nascer (recarrega as instruções e responde "pronta"); arquivada, não gasta nada. Elas ocupam a lista de arquivadas. O autor não tem número medido para o gasto total.
   - **10 (Recomendado)** — Cobre uma noite com várias trocas, mesmo com várias sessões na mesma pasta dividindo os estepes. Cria até 10 sessões de uma vez na primeira mensagem sua depois da instalação.
   - **6** — O mínimo: basta para quem tem uma ou duas sessões por pasta; cria menos sessões de uma vez.
   - **16** — Para quem deixa muitas sessões trabalhando na mesma pasta por muito tempo sem voltar ao computador; é o que cria mais sessões e gasta mais turnos curtos.
8. **Ligar o Remote Control?** — cabeçalho `Remote` (sensível: só no app desktop, caminho A, e se `Sucessora` for "O Claude, sozinho"). Mostre os riscos abaixo antes de perguntar.
   **O que isto faz:** liga a sessão à conta da pessoa no claude.ai, para ela acompanhar e mandar mensagens pelo celular ou pelo navegador; é o que faz o aviso de "Avisar e seguir" chegar no celular.
   **Riscos reais:** quem entrar na conta dela no claude.ai, ou pegar o celular desbloqueado, pode mandar ordens para a sessão, que roda no computador dela com as permissões da sessão (arquivos e comandos); por isso, conta com verificação em duas etapas e celular com bloqueio. A conversa também passa a aparecer nesses outros aparelhos. E uma sessão aberta pelo Remote Control conta como "trabalho vivo": o app não deixa arquivá-la, por isso a sucessora desliga o da anterior antes de arquivar.
   **Como desfazer:** apague a linha "Remote Control:" do `CLAUDE.md`; desligue em cada sessão (`set_remote_control` com false, ou o menu da sessão) e desligue nas configurações do app a opção que liga em toda sessão nova. Se suspeitar de acesso indevido à conta, troque a senha e saia dos aparelhos conectados, nas configurações da conta.
   - **Só nas sucessoras (Recomendado)** — O Claude liga o Remote Control em cada sucessora que ele abre (lista normal, estepe ou tarefa agendada), para você seguir a cadeia de longe. As outras sessões ficam como você deixar.
   - **Ligar já** — O mesmo, e o Claude também liga agora o desta sessão; para ligar em toda sessão nova, você liga a opção do app que faz isso (em novembro de 2026, "Connect new sessions to Remote Control", nas configurações do app).
   - **Não usar** — Nada é ligado: o Claude nunca liga o Remote Control. Ele ainda desliga o da sessão anterior antes de arquivá-la, se estiver ligado. Sem ele, o aviso de "Avisar e seguir" só aparece no computador.
9. **Começar toda sessão no modo automático?** — cabeçalho `Auto padrão` (sensível: muda o modo padrão de permissão; só se a pergunta 5 for "Liberar as duas regras")
   **O que isto faz:** grava `"defaultMode": "auto"` em `"permissions"` do `settings.json` do usuário. Motivo: a tarefa agendada não herda o modo de quem a criou; sem isso, a sucessora aberta por ela para no primeiro comando, esperando aprovação.
   **Riscos reais:** vale para TODA sessão nova, em todo projeto, não só para a sucessora: em vez de você aprovar cada ação, um filtro decide (deixa passar o que parece seguro e rotineiro, barra o que parece arriscado) e pode errar nos dois lados. Não ignora as permissões, e as regras de negar valem. Exige versão recente do Claude Code e um plano com esse modo; sem isso a sessão começa no modo normal.
   **Como desfazer:** tire `"defaultMode": "auto"` de `"permissions"` (ou ponha o valor que a cópia de segurança da Caixa 1 mostra). Vale na próxima sessão.
   - **Sim, automático** — Toda sessão nova começa no modo automático, inclusive a sucessora que a tarefa abre. Para quem já trabalha no modo automático.
   - **Não mudar** — O modo padrão fica como está. A sucessora aberta pela tarefa começa no modo normal e para no primeiro comando ou edição, esperando você aprovar. (O app diz que cada rotina guarda as aprovações dadas durante uma execução e que elas valem nas próximas; não testado.)
10. **Instalar o hook que aprova ações nos estepes?** — cabeçalho `Hook estepe` (sensível: aprova ações sozinho; só se a pergunta 6 for "Sessão de estepe"; com Python)
   **O que isto faz:** copia `scripts/spare_allow.py` para `<pasta de configuração>/hooks/`, cria `spares.txt` vazio e acrescenta um bloco em `"hooks"` → `"PreToolUse"`.
   **Riscos reais:** aprova sozinho só seis ações (mensagem, desarquivar, título, modelo, esforço e Remote Control) e só em sessão cujo id esteja em `spares.txt`; não lê o texto da mensagem; se falhar, não aprova nada. Detalhes na resposta "O `spare_allow.py` contorna as permissões?" no topo da caixa. Registra tudo em `hooks/spare_allow.log`, no seu computador.
   **Como desfazer:** tire de `"hooks"` → `"PreToolUse"` o bloco com `matcher` `SendMessage|mcp__ccd_session_mgmt__.*` e apague `hooks/spare_allow.py`, `hooks/spare_allow.log` e `spares.txt`. Vale na próxima sessão.
   - **Instalar o hook (Recomendado)** — As trocas por estepe passam sem caixa de aprovação; as seis ações ficam aprovadas só nos estepes listados.
   - **Sem o hook** — Nada é aprovado sozinho; o modo automático pode barrar mexer num estepe que outra sessão criou, ou a mensagem com a tarefa, e então a troca cai no "Avisar e seguir" ou você aprova na caixa.

### Passos do caminho A (app desktop)

Só se a Caixa 1 respondeu "App desktop" ou "Os dois" e `start_session` existe. Se respondeu "Terminal", ou se a ferramenta não existe, vá direto para o caminho B (ou, sem ele, para a regra mínima acima).

1. **Ferramentas** (achadas antes das perguntas, com ToolSearch, pelo nome): `start_session` (abrir sessão), `create_scheduled_task` e `list_scheduled_tasks` (criar e listar tarefa agendada), `run_scheduled_task` (rodar uma tarefa agora), `set_session_title` (trocar o título de uma sessão), `detach_session`, `archive_session` e `unarchive_session` (soltar, arquivar e desarquivar), `list_sessions` e `get_session` (listar e ver sessões), `set_remote_control` (ligar e desligar o Remote Control), `set_session_effort` e `set_session_model` (esforço e modelo de outra sessão), `list_task_runs` (sessões abertas por uma tarefa), `list_sections` (seções da barra lateral), `PushNotification` (aviso no computador e, com Remote Control, no celular) e `SendMessage` (mensagem para outra sessão). Em novembro de 2026 elas existiam com esses nomes no app desktop. Antes de qualquer `set_remote_control`, veja `remoteControlState` com `get_session` e só chame se o estado for outro: chamar à toa pode abrir uma caixa de aprovação ou desligar o Remote Control sem querer. Chame `start_session` com initiation "user_asked" (os valores "offer" e "own_initiative" viram um cartão esperando clique) e contexto "fresh" (conversa vazia).
2. **Grave as regras** da pergunta 1 (uma das três versões abaixo) e, se a pergunta 2 for "Sim", a de fechar a anterior; se a pergunta 6 for "Avisar e seguir", a de avisar e seguir; se for "Sessão de estepe", a dos estepes (com o número da pergunta 7) e também a de avisar e seguir, para quando não houver estepe (com "Reserva na hora", nada a mais: a regra da pergunta 1 já usa a reserva). Com "O Claude, sozinho" (pergunta 1), grave também a regra de troca com agente rodando. Se a pergunta 8 não for "Não usar", grave a regra do Remote Control; se for "Ligar já", ligue agora o Remote Control desta sessão (veja antes `remoteControlState` com `get_session` e só chame `set_remote_control` com "self" e true se estiver desligado) e diga à pessoa onde fica a opção do app para as sessões novas. Grave sempre a regra de herança. Com a pergunta 2 "Não", não grave a regra de fechar a anterior e, na regra de troca com agente rodando, tire o trecho em que a sessão anterior se arquiva sozinha. Explique à pessoa que o pedido da sucessora leva o id da sessão atual ("Sessão anterior: <id>"), achado com `list_sessions` ou `get_session`, para a sucessora saber quem arquivar; com a tarefa só manual (passo 4), o pedido inteiro vai no arquivo `SUCESSORA.md`.
3. **Grave só o que a pessoa aceitou**, no `<pasta de configuração>/settings.json` (não no do projeto: lá o modo automático como padrão não vale). Cada item abaixo é sensível: grave só com a resposta da pergunta dele e, no modo "Caixa por caixa, conferindo", mostre o trecho e espere o "Gravar". Nunca grave `"defaultMode"`, regra de permitir nem hook por conta própria:
   - Pergunta 5 "Liberar as duas regras": em `"permissions"` → `"allow"`, acrescente os nomes exatos das ferramentas de criar e de rodar tarefa agendada como o ToolSearch mostrou (em novembro de 2026: `"mcp__scheduled-tasks__create_scheduled_task"` e `"mcp__scheduled-tasks__run_scheduled_task"`). Crie o que faltar e não apague o que já existir.
   - Pergunta 9 "Sim, automático": em `"permissions"` ponha `"defaultMode": "auto"`. Com "Não mudar", não mexa nesse campo.
   - Pergunta 5 "Não liberar": nada no `settings.json`; na regra da pergunta 1, apague o trecho que vai de "uso uma tarefa agendada" até "Se isso também falhar:", inclusive.
   - Pergunta 10 "Instalar o hook": copie `scripts/spare_allow.py` para `<pasta de configuração>/hooks/spare_allow.py`, crie `<pasta de configuração>/spares.txt` vazio e, em `"hooks"` → `"PreToolUse"`, acrescente `{ "matcher": "SendMessage|mcp__ccd_session_mgmt__.*", "hooks": [ { "type": "command", "command": "python \"<pasta de configuração>/hooks/spare_allow.py\"", "timeout": 10 } ] }` (troque `mcp__ccd_session_mgmt__` pelo começo do nome que o ToolSearch mostrou). O hook aprova sozinho as ações da troca (desarquivar, título, modelo, esforço, Remote Control e mensagem) só quando o alvo é um estepe listado em `spares.txt`; o resto segue o filtro normal. Sem ele, o modo automático barra mexer num estepe que outra sessão criou e às vezes barra a mensagem com a tarefa, achando que contorna a trava do `start_session` (visto em 04/11/2026). Com ele, uma sessão fez tudo isso num estepe que não criou, sem nenhuma caixa (testado no mesmo dia). Não use regra de permitir para essas ferramentas: ela valeria para todas as sessões. Com "Sem o hook": não copie nem registre nada, não crie `spares.txt` e, na regra "Estepes", apague os trechos sobre `spares.txt`.

   Confira com `check_settings.py`. Diga à pessoa que o modo automático como padrão exige uma versão recente do Claude Code e um plano que tenha esse modo; sem isso, a sessão começa no modo normal.
4. **Explique à pessoa as travas** que o autor encontrou (testadas em novembro de 2026):
   - **O app recusa abrir a sessão** quando o turno não veio de uma mensagem da pessoa: aviso de agente, mensagem de outra sessão, tarefa agendada, e até o primeiro turno de uma sessão aberta por outra. A recusa é do próprio app, e nenhuma configuração muda isso. Uma mensagem nova da pessoa no meio de um turno desses já destrava: num teste de 04/11/2026, o turno começou por aviso automático, a pessoa respondeu caixas de pergunta e mandou mensagens no meio, e a sucessora abriu. Resposta numa caixa de pergunta, sozinha, não destrava (outro teste do mesmo dia: a pessoa respondeu "abra agora" na caixa e o app recusou de novo), então a regra pede mensagem nova. Por isso a regra deixa a troca, quando der, para um turno que veio de mensagem da pessoa ("avisar e seguir", pergunta 6), e tem reservas: primeiro uma tarefa agendada (a só manual do projeto, rodada na hora, ou uma de uma vez só para ~2 minutos depois, com o mesmo pedido; ela aparece no app como sessão); depois o caminho B, se instalado; por último, avisar a pessoa.
   - **No modo automático, o classificador** (o filtro que aprova ou barra cada ação) **pode barrar a tarefa agendada**, porque ela roda sozinha mais tarde. A regra de permitir da pergunta 5 resolve: ação com regra própria não passa pelo classificador (está na documentação do modo automático). Com as regras, criar e rodar a tarefa passaram num turno automático; sem a regra de rodar, o classificador barrou `run_scheduled_task` até num turno da pessoa (04/11/2026).
   - **A tarefa agendada não guarda o modo da sessão que a criou**, nem quando criada num turno da pessoa: ela roda no modo padrão das configurações. Se esse modo for o normal, a sucessora para no primeiro comando esperando aprovação. Daí a pergunta 9 ("Começar toda sessão no modo automático?").
   - **O app recusa arquivar a anterior enquanto ela tem "trabalho vivo"**: turno em andamento (ela ainda está escrevendo a última mensagem quando a sucessora começa), agente ou tarefa em segundo plano, mensagem na fila, ou alguém olhando por Remote Control (pelo celular, por exemplo). Por isso a regra desliga o Remote Control da anterior antes, tenta de novo nos turnos seguintes e, se for agente em segundo plano, não força. Arquivar também pode pedir aprovação num cartão, conforme o modo de permissão.
   - Uma autorização dada antes não destrava a abertura da sessão: o app olha se veio mensagem da pessoa, não o que ela já aprovou. O que ajuda é trocar de sessão num turno da pessoa quando a conversa já estiver perto do limite, sem esperar.
   - **Por que estepe e "avisar e seguir" vêm antes da tarefa agendada:** a sucessora aberta por tarefa agendada fica só na seção Rotinas e não tem `start_session`, então a cadeia fica presa lá. O estepe fica na lista normal. Avisando e continuando, a troca acontece na próxima mensagem da pessoa, na lista normal. O aviso (`PushNotification`) chega no celular só com o Remote Control ligado, e o app não mostra o aviso se a pessoa já estiver olhando a sessão.
   - **Sessão de estepe** (pergunta 6; testado em 04/11/2026, tudo num turno automático): uma sessão criada antes com o pedido "não faça nada, responda só 'pronta'", depois solta e arquivada, pode ser desarquivada, renomeada e receber a tarefa por mensagem sem a pessoa. Ela trabalhou no modo padrão das configurações (no teste, o automático), sem pedir aprovação, e fica na lista normal de sessões, não em Rotinas. Modelo e esforço não pedem um estepe de cada tipo: a sessão que usa o estepe troca os dois nele (`set_session_model`, `set_session_effort`) antes de mandar a mensagem; o app não deixa uma sessão trocar o próprio modelo, só o de outra. Travas: o Remote Control do estepe só liga depois que ele recebe a mensagem (antes, o app responde "requires an active session"); cada estepe nasce na pasta da sessão que o criou, então os estepes são por pasta; criar estepe usa `start_session`, que só passa num turno que veio de mensagem da pessoa, então a reposição fica para esse turno; a sucessora que veio de estepe já está solta e não faz `detach_session`. O nome "Estepe <pasta> N" é de propósito uma palavra que quase não aparece em título de sessão, para a busca não confundir.
   - Tarefa de uma vez só fica na lista de tarefas agendadas, desligada, depois de rodar. Apagar a tarefa arquiva a sessão que ela abriu: só apague quando a cadeia já tiver passado dela.
   - **A tarefa só manual (sem horário) é a melhor reserva** numa sessão comum. Criada antes, ela continua ligada depois de rodar (não se desliga como a de uma vez), roda de novo a cada troca e abre a sessão em poucos segundos com `run_scheduled_task`, também num turno automático (com as regras da pergunta 5; testado em 04/11/2026). Limites: o app recusa rodar tarefa de dentro de uma sessão aberta por tarefa ("from a scheduled-task run session"), e essa sessão também não tem `start_session`; recusa rodar enquanto outra execução da mesma tarefa estiver em andamento; e a tarefa roda na pasta da sessão que a criou (a ferramenta não tem campo de pasta). Como o pedido da tarefa é fixo, o que muda a cada troca vai num arquivo `SUCESSORA.md` na pasta, que a sessão anterior reescreve logo antes de rodar a tarefa: o pedido inteiro (passagem, "Sessão anterior: <id>", título da sucessora). Assim uma pasta com várias passagens usa uma tarefa só. A sessão nova nasce com o título da tarefa; a anterior o troca com `set_session_title` (passou em 04/11/2026). Crie a tarefa com `notifyOnCompletion` false: sem isso, a sessão que a criou recebe um aviso a cada execução e acorda para reler a conversa.
   - **A sessão aberta por tarefa agendada nasce sem Remote Control e com esforço médio.** A sessão que criou a tarefa, se ainda estiver no turno, confere em `list_task_runs` que ela abriu e ajusta os dois (`set_remote_control` e `set_session_effort`). A própria sessão da tarefa não consegue: enquanto ninguém a abre na tela, toda ação que pede aprovação é recusada ("nobody has opened this scheduled run"). Isso incluiu ligar o próprio Remote Control e criar outra tarefa agendada, mesmo com a regra de permitir (testado em 04/11/2026). Por isso uma sucessora aberta por tarefa só abre a próxima num turno que veio de mensagem da pessoa, ou depois que a pessoa a abrir na tela; se não der, avisa a pessoa.
   - **Rotinas:** no app, cada tarefa agendada vira uma "rotina". A sessão que ela abre aparece só dentro da seção Rotinas da barra lateral, debaixo da rotina, e não junto das outras sessões. Se essa seção estiver desligada, a sucessora existe, mas a pessoa não a vê. Confira com `list_sections` (seção `routines`, campo `shown`). Se estiver desligada, peça à pessoa que a ligue no menu de filtro da barra lateral: o Claude não consegue (nenhuma ferramenta liga a seção nem tira a sessão de lá). E a tarefa de uma vez se desliga sozinha depois de rodar; desligada, ela e a sessão dela somem da seção Rotinas quando a sessão termina o turno (a sessão não é arquivada, só fica escondida; visto em 04/11/2026). Por isso a mensagem final da sessão que criou a tarefa sempre traz o link da sessão nova.
5. **Teste** (com sim da pessoa; abre uma sessão de verdade e gasta um pouco de cota):
   1. Crie uma pasta de teste, `~/Documents/teste_sucessora/` (não na pasta de configuração, que é protegida), com um `PASSAGEM.md` cujo próximo passo exato é: *"Crie `ok.txt` com a palavra ok e escreva ETAPA CONCLUIDA na primeira linha desta passagem."*
   2. Abra uma sessão chamada "Teste de sucessora" com o pedido: *"Teste de instalação: não arquive nem solte nenhuma sessão. Leia e siga `<caminho>/PASSAGEM.md`."* (Sem essa frase, a regra de fechar a anterior poderia soltar ou arquivar esta sessão de instalação.)
   3. Confira com `list_sessions` que ela apareceu. Quando ela terminar, confira que `ok.txt` existe. Diga à pessoa que pode arquivar a sessão de teste e apagar a pasta.

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

Só se a pergunta 3 foi "Sim, me guie". Vá devagar: um passo por vez, esperando a pessoa dizer que fez antes de seguir.

**O que é o token** (explique assim à pessoa): uma chave de acesso à conta Claude dela, válida por um ano, feita para scripts. Quem tem o token usa a cota dela. É como uma senha.

1. **Confira o Claude Code de terminal.** Rode `claude --version`. Se o comando não existir, a pessoa precisa instalar o Claude Code de terminal (instruções oficiais em https://code.claude.com/docs). O token funciona nos planos Pro, Max, Ultra, Team e Enterprise.
2. **A pessoa gera o token.** Você, Claude, não roda este comando: ele abre o navegador e mostra o token na tela. Peça que ela rode, numa janela de terminal do sistema, separada, aberta por ela fora desta conversa:

   ```text
   claude setup-token
   ```

   **Nunca** no painel de terminal do app do Claude, nem no terminal do editor de código: o Claude consegue ler esses painéis, e o token iria parar na conversa.

   Ela faz login no navegador, e o terminal mostra o token (um texto longo). Ela copia o token e **não cola em lugar nenhum ainda, nem no chat**.
3. **A pessoa grava o token num arquivo**, na mesma janela de terminal, com o token ainda copiado. Os comandos abaixo supõem a pasta padrão (`.claude` na pasta do usuário); se a pasta de configuração for outra, troque o caminho do arquivo neles (e use `--token-file` no script, se ele não achar o arquivo):
   - Windows (PowerShell):

     ```powershell
     Get-Clipboard | Out-File -NoNewline -Encoding ascii "$HOME\.claude\relay_token.txt"
     icacls "$HOME\.claude\relay_token.txt" /inheritance:r /grant:r "$($env:USERDOMAIN)\$($env:USERNAME):F"
     icacls "$HOME\.claude\relay_token.txt"
     ```

     (A segunda linha deixa só o usuário dela ler o arquivo; a terceira mostra as permissões, e só o usuário dela deve aparecer.)
   - Mac e Linux: ela roda o comando abaixo, cola o token (ele não aparece na tela) e aperta Enter:

     ```bash
     umask 077; read -rs T; printf %s "$T" > <pasta de configuração>/relay_token.txt; unset T
     ```

   Depois ela limpa a área de transferência de verdade e fecha essa janela de terminal:
   - Windows: copia qualquer outra coisa e, se o histórico da área de transferência (Win+V) estiver ligado, apaga o item do token lá também.
   - Mac: copia outra coisa. Lembre que a área de transferência universal leva o que foi copiado para outros aparelhos Apple dela.
   - Linux: copia outra coisa.

   **Por que arquivo, e não variável do sistema** (`setx` no Windows, `export` no perfil do terminal): o token passaria a valer para todo `claude` aberto nessa conta do computador, e o login normal (`/login`) deixaria de valer até a variável ser removida. No arquivo, ele é lido só pelo script e entregue só às rodadas.
4. **Você confere sem ver o token**; o comando imprime só sim ou não:

   ```text
   python -c "import os, pathlib; t = (pathlib.Path(os.environ.get('CLAUDE_CONFIG_DIR') or pathlib.Path.home() / '.claude') / 'relay_token.txt').read_text(encoding='utf-8-sig').strip(); print('ok' if t.startswith('sk-ant-') and not any(c.isspace() for c in t) else 'confira o arquivo: deve ter só o token, uma linha')"
   ```

   Nunca rode `cat`, `type` ou `Get-Content` nesse arquivo, nem o abra com Read. Se a pasta de configuração estiver num repositório git ou numa pasta sincronizada com a nuvem, avise: o token não pode ir junto (põe `relay_token.txt` no `.gitignore` ou tira da sincronização).
5. **Proíba a leitura do arquivo.** No `settings.json`, em `"permissions"` → `"deny"` (crie o que faltar e não apague o que já existir), acrescente a regra `"Read(<pasta de configuração>/relay_token.txt)"`, com o caminho completo já preenchido (sem `~`). Assim a ferramenta de leitura das sessões não abre o arquivo (um comando de terminal não fica coberto com certeza; por isso o guia manda nunca rodar `cat` nele). Diga à pessoa que o script de revezamento já passa a mesma proibição às rodadas.
6. **Copie o script:** `scripts/session_relay.py` → `<pasta de configuração>/tools/session_relay.py`.
7. **Teste num projeto de brinquedo** (com sim da pessoa; gasta um pouco da cota: duas ou três rodadas rápidas em Haiku). A pasta do teste fica em `~/Documents`, não na pasta de configuração: lá as rodadas não conseguem escrever, porque a pasta é protegida e as rodadas não podem pedir permissão.
   1. Crie `~/Documents/relay_test/PASSAGEM.md` com:

      ```markdown
      # Passagem — teste do revezamento

      ## Próximo passo exato
      Se `contagem.txt` não existe, crie com a linha "um". Se já existe com "um", acrescente a linha "dois" e escreva ETAPA CONCLUIDA na primeira linha desta passagem.
      ```
   2. Rode (sempre com o caminho completo de `tools/session_relay.py` na pasta de configuração; no Windows, com barras `/`):

      ```text
      python <pasta de configuração>/tools/session_relay.py --folder ~/Documents/relay_test --handoff PASSAGEM.md --model haiku --rounds 3
      ```
   3. Esperado: a rodada 1 cria "um" (STATUS: CONTINUE); a rodada 2 acrescenta "dois" e marca ETAPA CONCLUIDA; o script para sozinho. O registro fica em `~/Documents/relay_test/relay.log`, uma linha por rodada.
   4. Se der erro de opção desconhecida, a pessoa atualiza o Claude Code (`claude update`) e vocês tentam de novo. No Windows, se o erro falar de argumentos estranhos, passe `--claude "<caminho do claude.exe>"`: o `claude.cmd` estraga argumentos com parênteses e asteriscos.
8. **Grave a regra** do caminho B com as ferramentas da pergunta 4:
   - "Só arquivos": `--tools "Read,Glob,Grep,Edit,Write"` (o padrão do script).
   - "Arquivos + terminal": acrescente o nome da ferramenta de terminal que aparece na lista de ferramentas da pessoa (no Windows pode ser `Bash`, que é o Git Bash, ou `PowerShell`); não presuma pelo sistema. Por exemplo `--tools "Read,Glob,Grep,Edit,Write,PowerShell"`.
   - "Decidir por projeto": a regra manda perguntar na primeira vez em cada projeto e anotar a resposta no CLAUDE.md daquele projeto.
9. **Explique à pessoa os furos** que o autor encontrou (a regra já cobre os três primeiros):
   - Roda escondido: não aparece no app. Quem lança avisa em uma linha, e a próxima conversa confere o `relay.log`.
   - Rodada que passa do tempo limite (`--timeout`, padrão 1 hora) é cortada, e o revezamento para. Tarefa longa precisa de um `--timeout` maior.
   - O script para no limite de rodadas mesmo que a última diga CONTINUE, e ninguém abre a próxima.
   - Gasta da mesma cota da pessoa.
   - Se o token vazar, trate como senha vazada. A documentação oficial (conferida em novembro de 2026) não mostra como revogar só esse token: procure, nas configurações da conta em claude.ai, a lista de acessos e sessões, ou fale com o suporte da Anthropic.
   - Para desligar o caminho B: apague `<pasta de configuração>/relay_token.txt` (sem o token, o script não roda), `<pasta de configuração>/tools/session_relay.py` e, em cada projeto, o `relay.log`; tire do `CLAUDE.md` a regra "Rodadas sem tela:" e, do `settings.json`, a linha `Read(.../relay_token.txt)` em `"deny"` (opcional). Se o token pode ter vazado, apagar o arquivo não o revoga: veja o item acima. O token vale por um ano.
   - Nada disto é aprovado sozinho: a rodada só usa as ferramentas da lista que a pessoa escolheu (pergunta 4); o resto é recusado, sem pergunta.

Texto da regra (caminho B):
> - Rodadas sem tela: `python <pasta de configuração>/tools/session_relay.py --folder <projeto> --handoff <passagem> --model sonnet --rounds 3 --tools "<lista>"`, lançado solto em segundo plano (Windows: `Start-Process ... -WindowStyle Hidden -PassThru`; Mac e Linux: `nohup ... &`), guardando o número do processo. Uso: <quando estou no terminal | só como reserva, quando o app recusar abrir sessão>. Roda escondido: aviso a pessoa em uma linha; na próxima mensagem dela, confiro o `relay.log` do projeto e, se a passagem não diz ETAPA CONCLUIDA e nada está rodando, lanço de novo ou abro a sucessora. Tarefa longa: `--timeout` maior. Nunca leio, mostro nem copio `relay_token.txt`.

---

## Caixa 8 — Vigia de gasto e medição

**O que isto faz:** um script que roda sozinho a cada mensagem e a cada ferramenta usada, e avisa o Claude quando a sessão passa de certos limites. O Claude conta à pessoa em uma linha e propõe o que fazer (atualizar a passagem, abrir a sucessora, usar agente mais barato).
**Por quê:** ninguém percebe a conversa crescendo. No uso do autor, 14 de 36 trocas de sessão só aconteceram depois de 250 mil tokens, até o vigia passar a avisar no meio do turno.
**Riscos reais:**
- Os scripts leem os registros locais das sessões (`<pasta de configuração>/projects`), que contêm as conversas inteiras. Só contam tokens, modelo e hora; não copiam o conteúdo. Nada sai do computador: nenhum script usa rede.
- Gravam só arquivos pequenos ao lado do script (`hooks/spend_watch_state/` e `tools/measure_marks.csv`).
- Se o vigia falhar (sem Python, formato dos registros mudou): fica mudo ou o Claude Code mostra um erro do hook; ele não bloqueia nem aprova nada, e o trabalho segue.
- Custo: o aviso é uma linha no contexto, só quando um limite é cruzado (poucas vezes por sessão). O vigia roda a cada mensagem e a cada ferramenta, mas lê só o que é novo.
- A medição do plano é uma estimativa; vale só para o seu uso e pode variar.
**Como desfazer:** apague `hooks/spend_watch.py` e as duas linhas do vigia em `"UserPromptSubmit"` e `"PostToolUse"` no `settings.json` (ou volte a cópia de segurança da Caixa 1), e as linhas da Caixa 8 no CLAUDE.md. Se quiser, apague também `hooks/spend_watch_state/`, `tools/measure_point.py`, `tools/measure_marks.csv`, `tools/usage_report.py` e a pasta `skills/usage-report/`. Vale na próxima sessão.

Plano (Caixa 1): com "Chave de API", não faça as perguntas 2 e 3 (não há % semanal; o gasto aparece em dinheiro, no painel da API) e não as ponha em "Recusadas"; o vigia (pergunta 1) serve do mesmo jeito, porque avisa em tokens. Com "Team ou Enterprise" ou "Não sei", faça as duas, mas diga que só funcionam se a tela de uso mostrar um % de limite semanal; se, na hora de ler, não houver nenhum %, pare e avise a pessoa.

Perguntas:

1. **Instalar o vigia de gasto?** — cabeçalho `Vigia` (só com Python)
   - **Sim, limites do autor (Recomendado)** — Avisa com a conversa em 200 mil tokens (e a cada 100 mil a mais), aos 40, 80 e 150 prompts, e quando um agente chega a 100 e a 150 chamadas. Lê os registros locais; nada sai do PC.
   - **Sim, avisar mais cedo** — Conversa em 150 mil; agente em 60 e 100 chamadas. Mais avisos no contexto, em troca de trocar de sessão antes.
   - **Não** — Nada é instalado; você continua sem aviso de conversa grande.
2. **Conferir o uso antes e depois de tarefa grande?** — cabeçalho `Antes/depois` (fora de "Chave de API")
   - **Sim (Recomendado)** — O Claude anota o % de uso do plano antes de uma tarefa grande e diz a diferença no fim, em uma linha. Só uma regra no CLAUDE.md; nenhum script.
   - **Não** — Nada muda; você confere o uso quando quiser.
3. **Medir quanto vale 1% da cota no seu plano?** — cabeçalho `Medir plano` (fora de "Chave de API"; com Python)
   - **Sim** — Você anota o % de uso em dois momentos, com um ou dois dias entre eles, e um script faz a conta. Depois disso o vigia também avisa em % da cota. O script lê os registros locais e grava um .csv pequeno.
   - **Não** — O vigia avisa só em tokens.
4. **Instalar a skill de relatório de uso?** — cabeçalho `Skill uso` (só com Python)
   - **Sim** — Copio uma skill para `<pasta de configuração>/skills/usage-report/`: quando você perguntar "quanto gastei" ou "onde foi minha cota", o Claude roda um script que soma o gasto por sessão e por modelo. Lê as conversas locais (só contagens); nada sai do PC.
   - **Não** — Nada é instalado; o Claude responde a essas perguntas sem o relatório pronto.

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
   5. Diga à pessoa: o vigia lê os registros internos das sessões, que podem mudar numa atualização do Claude Code. Se mudar, ele fica mudo, sem atrapalhar nada.
   6. Conferir: abra um agente Haiku com o pedido *"SPEND-WATCH-TEST. Liste 6 arquivos desta pasta, um por chamada de ferramenta, e devolva qualquer aviso 'SPEND WATCH' que aparecer."* Com essa marca no começo do pedido, o vigia usa limites de teste (3 e 5 chamadas). Se o aviso não vier, a pessoa abre uma sessão nova (no app, uma sessão nova na mesma pasta; no terminal, sair e rodar `claude` de novo) e você repete o pedido nela; algumas versões só leem os hooks ao abrir a sessão. Se ela preferir, deixe o teste para a Caixa final.
2. Pergunta 2 "Sim": grave a regra. Para ler o % de uso: no app, a ferramenta `get_usage` (procure com ToolSearch); sem ela, peça o número à pessoa (tela de uso do app ou de claude.ai, ou `/usage` no terminal).
3. Pergunta 3 "Sim":
   1. Copie `scripts/measure_point.py` para `<pasta de configuração>/tools/measure_point.py`.
   2. Leia o % semanal agora (como na pergunta 2) e rode `python <pasta de configuração>/tools/measure_point.py <%>`. Isso grava a primeira marca.
   3. Grave a regra. A partir da segunda marca, o script mostra quantos tokens de peso valem 1% da cota. Quando o resultado estiver estável (duas ou três contas parecidas), ponha esse número em `POINT`, no topo do `spend_watch.py`: o vigia passa a avisar também em % da cota.
   4. Diga à pessoa: entre duas marcas não pode ter virada da semana da cota, e conversas fora do Claude Code (no chat comum do claude.ai ou do app) não entram nos registros; se ela usar muito o chat comum nesse intervalo, o número sai baixo. Marcas com menos de 3 pontos de diferença não se perdem: o script soma com as próximas até dar 3.
4. Pergunta 4 "Sim": copie a pasta `skills/usage-report/` do pacote para `<pasta de configuração>/skills/usage-report/` e `scripts/usage_report.py` para `<pasta de configuração>/tools/usage_report.py`. Se a pergunta 3 foi "Não", copie também `scripts/measure_point.py` para `tools/` (a skill o usa para "quanto vale 1%"), sem rodá-lo. Diga: vale na próxima sessão; para desfazer, apague a pasta da skill. Não precisa de regra no CLAUDE.md.

Texto da regra:
> - Vigia de gasto: quando aparecer um aviso "SPEND WATCH", contar à pessoa em uma linha, com o número, e propor o que fazer (passagem, sucessora, agente mais barato).
> - Antes e depois de tarefa grande: anotar o % de uso do plano e dizer a diferença no fim, em uma linha.
> - Medição do plano: no começo de uma sessão, se a última marca em `<pasta de configuração>/tools/measure_marks.csv` tiver mais de um dia, ler o % semanal e rodar `measure_point.py` com ele. Quando a estimativa ficar estável em duas ou três contas, propor pôr o número em `POINT` no `spend_watch.py`.

---

## Caixa 9 — Conferir o trabalho

**O que isto faz:** conferir é obrigatório, mas dá para conferir gastando menos. Esta caixa só grava regras de comportamento no CLAUDE.md; nenhum script, hook nem permissão muda.
**Riscos reais:**
- "Duas revisões só no sensível" pode deixar passar um erro numa área que você não considera sensível; se tiver dúvida, deixe desmarcado.
- "Prova barata" usa menos imagens: em caso raro o texto não mostra um defeito visual. Peça uma imagem quando quiser.
- Os hábitos de fim de turno deixam as mensagens finais um pouco mais longas; nenhum outro risco.
- São só instruções: o Claude pode esquecer uma em conversa muito longa.
**Como desfazer:** apague a linha da regra no CLAUDE.md (ou volte a cópia de segurança da Caixa 1). Vale na próxima sessão.

Perguntas (duas, as duas com várias respostas: `multiSelect: true`):

1. **Quais destes hábitos viram regra?** — cabeçalho `Conferência`
   - **Prova barata** — Quando um texto prova (linha de log, valor, saída de teste), usar o texto. Imagem só recortada no que importa e em escala menor; medidas tiradas por script. Um defeito só visível pode passar; peça imagem se quiser.
   - **Testes por partes** — Depois de cada mudança, os testes do que mudou e uma regressão curta; a bateria inteira antes de publicar. Um erro fora do trecho testado só aparece na bateria final.
   - **Duas revisões só no sensível** — Segurança, contas, pagamento e criptografia ganham duas revisões independentes; o resto, uma. Gasta mais nessas áreas e menos no resto.
   - **Não pagar duas vezes** — Depois de uma interrupção, conferir se agentes e tarefas em segundo plano ainda rodam e retomar, em vez de recomeçar. Processo só se encerra pelo número (PID) que a própria sessão iniciou, nunca pelo nome. Evita derrubar o trabalho de outras sessões.
2. **Quais hábitos de fim de turno viram regra?** — cabeçalho `Fim do turno`
   - **Perguntas pendentes** — Perguntas que surgirem no trabalho vão para um arquivo de perguntas do projeto e se repetem no fim de toda mensagem final. A mensagem final fica um pouco maior.
   - **Posso encerrar?** — Antes de encerrar, o Claude se pergunta "deveria estar fazendo algo antes de encerrar?"; se sim, faz; se não, diz o que espera e o que vai acordar a sessão. Evita sessão parada à toa; custa uma checagem curta.
   - **Mensagem final completa** — A resposta vem na primeira linha, seguida das pendências e do que não saiu tão bem ou poderia ter saído melhor. Mais honesto; um pouco mais longa.

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

**O que isto faz:** se o guia ajudar, uma estrela no repositório ajuda outras pessoas a achá-lo. Em vez de pedir agora, antes de a pessoa ver o resultado, o Claude pode lembrar daqui a uma semana. Explique isso em até 2 frases. Não insista e não ponha "(Recomendado)" em nenhuma opção.
**Riscos reais:** praticamente nenhum. Grava uma linha no CLAUDE.md, que custa poucas palavras de contexto até ser usada. Nenhum dado sai do computador; o link só é mostrado, e o Claude nunca dá a estrela por você.
**Como desfazer:** apague a linha "Lembrete único (estrela)" do CLAUDE.md. Ela também se apaga sozinha depois de usada.

Pergunta:

1. **Quer que eu te lembre daqui a uma semana de decidir se dá uma estrela no repositório?** — cabeçalho `Estrela`
   - **Sim, me lembre** — Daqui a 7 dias, na primeira conversa, o Claude pergunta uma vez só se as táticas ajudaram e mostra o link. Quem decide é você; o Claude nunca dá a estrela por você.
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
4. Como desfazer, uma linha para cada coisa instalada: cada regra (apagar a linha no CLAUDE.md); cada configuração (apagar a chave em `"env"` ou em `"permissions"` do `settings.json`); cada hook (apagar a entrada dele em `"hooks"` e o arquivo copiado: `spend_watch.py` em `"UserPromptSubmit"` e `"PostToolUse"`, `agent_limit.py` em `"PreToolUse"`, `copy_lock.py` em `"PreToolUse"` e `"SubagentStop"`, `handoff_reminder.py` em `"SessionStart"`, `spare_allow.py` em `"PreToolUse"`, mais `spares.txt`); cada script em `tools/`; os modelos em `modelos/`; a skill de uso (apagar a pasta `skills/usage-report/`); e, se houver, o `<pasta de configuração>/relay_token.txt` (apagar o arquivo e, se um token foi criado, revogá-lo onde foi criado). Para tudo de uma vez: voltar as cópias de segurança da Caixa 1 e apagar os arquivos copiados. Diga também quando cada coisa passa a valer (a próxima sessão, para configurações, hooks e a skill).
5. O que ficou pela metade (por exemplo, a segunda marca da medição do plano). Se o teste do freio ou o do vigia ficou para depois, diga à pessoa para abrir uma sessão nova e pedir ali: "repita o teste do freio (ou do vigia) do guia do Quota Keeper".
6. Se a Caixa 10 gravou o lembrete, a data em que ele vai aparecer.
7. Se o modo foi Rápido: o Grupo 3 (Caixa 7) não foi instalado. Para ligar depois, de preferência após uma ou duas semanas, basta pedir "rode a Caixa 7 do guia do Quota Keeper".
8. O crédito: "Táticas de Jaber Felippe Neto (JN Softworks), texto em CC BY 4.0, scripts em MIT." Se a pessoa for repassar o guia, que mande a pasta inteira, com o crédito.
