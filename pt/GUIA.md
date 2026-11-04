# JN's Quota Keeper — economia de tokens para o Claude Code

> **Feito por Jaber Neto (JN Softworks).** Licença [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt-br): pode copiar, adaptar e repassar, desde que mantenha o nome do autor e o link da licença. Os scripts estão sob a licença MIT, que também pede para manter o crédito. Versão 1.0, novembro de 2026.

Este arquivo é para o Claude. Se você é a pessoa: não precisa ler. O Claude vai mostrar uma caixa de perguntas por tática e só muda o que você aceitar.

## Como conduzir a instalação (Claude, leia antes de tudo)

1. **Nada muda sem um sim.** Cada tática tem uma caixa de perguntas. Mostre a caixa, espere a resposta, faça só os passos daquela resposta, confira, e só então vá para a próxima caixa.
2. **Mostre cada caixa com AskUserQuestion**, uma chamada por caixa, com as perguntas, cabeçalhos e opções como estão aqui. A ferramenta já acrescenta a opção "Outro" sozinha. Sem essa ferramenta, faça as mesmas perguntas numa lista numerada curta e espere.
3. **Antes de cada caixa, explique em até 3 frases simples** o que a tática faz e por quê. A pessoa pode não ser técnica: nada de sigla ou jargão sem tradução na mesma frase.
4. **Siga a ordem das caixas.** Se uma caixa não se aplica (por exemplo, a pessoa não usa agentes), diga isso em uma linha e passe para a próxima.
5. **Grave as regras com o texto pronto** de cada caixa ("Texto da regra"). Não reescreva nem enfeite: cada linha a mais no CLAUDE.md é paga em toda sessão. Dos trechos entre `< >`, preencha só os da instalação:
   - número escolhido, como `<200>`: ponha o número da resposta da pessoa;
   - `<pasta de configuração>`: o caminho completo dela (definida logo abaixo), com barras `/`, por exemplo `C:/Users/fulano/.claude`;
   - `<caminho>`: só nos testes da Caixa 7, é o caminho completo da pasta de teste;
   - `<lista>`: as ferramentas escolhidas na Caixa 7;
   - escolha `<a | b>`: deixe só a opção que bate com a resposta e apague a outra.

   Ficam literais na regra gravada, para a sessão preencher depois: `<arquivo>`, `<passagem>`, `<projeto>`, `<id>`, `<n>`, `<título da sessão>`, `<data>`, `<id da sessão>`.

   **Onde as linhas de regra entram:** dentro da seção `## Quota Keeper ...` do CLAUDE.md escolhido, sob o subtítulo `### Regras`, antes de `### Recusadas`. A Caixa 1 cria a seção e os dois subtítulos (se a seção não existir, no fim do arquivo). Se a seção já existir sem `### Regras`, crie esse subtítulo antes de `### Recusadas`. Linhas de recusa ficam sob `### Recusadas`. Os rótulos entre colchetes (como "[Número]") só dizem qual versão escolher: não são gravados.
6. **Nunca peça token, senha ou chave no chat**, e nunca rode comando que mostre um deles na tela. A Caixa 7 ensina a pessoa a gravar o token sozinha.
7. **Fale pouco entre um passo e outro.** O resumo completo vem na Caixa final.
8. **Em dúvida, pare e pergunte.** Se algo daqui não bater com o que você vê no computador da pessoa (ferramenta com outro nome, opção que não existe, erro), diga o que achou e pergunte. Não invente.
9. **Nomes de ferramentas e opções mudam.** Os citados aqui são de novembro de 2026. Procure pelo nome com ToolSearch; se não achar, diga e siga sem aquela parte.

**O que nunca se economiza** (vale sempre, sem caixa): cópia de segurança antes de mudar configuração, confirmação antes de qualquer coisa irreversível, compilar e testar o que mudou, e ler o trecho exato de código que vai ser editado.

**Arquivos deste pacote** (caminhos a partir da pasta onde está o `START_HERE.md`):
- `pt/GUIA.md` (este) e `pt/PASSAGEM_MODELO.md` (modelo do arquivo de passagem) e `pt/RESUMOS_MODELO.md` (modelo do arquivo de resumos)
- `scripts/spend_watch.py` (vigia de gasto), `scripts/agent_limit.py` (freio de agentes), `scripts/session_relay.py` (rodadas sem tela), `scripts/measure_point.py` (medir quanto vale 1% do plano), `scripts/check_settings.py` (conferir o `settings.json`)
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

Números do autor (plano Ultra, antes Max 20x, setembro a novembro de 2026, medidos nos registros das sessões):
- Reler a conversa foi 73% do gasto; guardar a conversa para reler depois (o cache) foi 19%; escrever e pensar, 8%.
- Com as regras de passagem e troca de sessão (Caixa 6), a conversa principal caiu de ~12,7 para ~3,2 pontos da cota por dia de uso (75% a menos).
- Agentes que passaram de 100 chamadas foram 74% do gasto dos agentes (Caixa 5).
- Agentes esperando compilação ou teste, com o cache padrão de 5 minutos, regravavam a conversa inteira na volta: ~26% de todo o gasto em 8 dias, até ligar o cache de 1 hora (Caixa 2).

A régua usada para comparar (não é preço oficial):

```text
peso = entrada × 1 + gravação no cache × 1,25 (cache de 5 min) ou × 2 (cache de 1 hora) + leitura do cache × 0,1 + saída × 5
```

Quanto vale 1% da cota depende do plano. No plano Ultra do autor (antes Max 20x), 1% da semana foi ~8,5 milhões de peso. Não use esse número para outro plano: a Caixa 8 mede o da pessoa.

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

## Caixa 1 — Antes de começar

**O que é:** decidir onde as regras ficam e como a pessoa usa o Claude Code. Ainda não muda nada.

Perguntas:

1. **Onde gravar as regras que você aceitar?** — cabeçalho `Onde gravar`
   - **Em todos os projetos (Recomendado)** — Vão para o `CLAUDE.md` da pasta de configuração do Claude Code (em geral `~/.claude/CLAUDE.md`) e valem em qualquer pasta.
   - **Só neste projeto** — Vão para o `CLAUDE.md` da pasta aberta agora. Vale só para as linhas de regra.
2. **Onde você usa o Claude Code?** — cabeçalho `Onde usa`
   - **App desktop** — O app do Claude no computador, na aba Code.
   - **Terminal** — O comando `claude` numa janela de terminal ou dentro do editor de código.
   - **Os dois**
3. **Como você paga o Claude?** — cabeçalho `Plano`
   - **Pro, Max ou Ultra** — Assinatura pessoal, com limite de uso por semana.
   - **Team ou Enterprise** — Plano de empresa; os limites podem ser definidos pela empresa.
   - **Chave de API** — Paga por uso (por token), sem limite semanal em %.
   - **Não sei** — Tudo bem: o guia fica no geral e diz, em cada caixa, o que depende do plano.

Nesta pergunta não ponha "(Recomendado)" em nenhuma opção: é um fato sobre a pessoa, não uma escolha.

Passos:
1. Faça uma cópia de segurança, com a data no nome, de cada arquivo que existir: `<pasta de configuração>/settings.json` → `settings.json.antes-quota-keeper-<AAAA-MM-DD>`, e o CLAUDE.md escolhido → `CLAUDE.md.antes-quota-keeper-<AAAA-MM-DD>`. A data é a de hoje, pelo relógio do computador (por exemplo `2026-11-04`). Cada cópia fica na mesma pasta do original, ao lado dele. Diga à pessoa onde ficaram.
2. No fim do CLAUDE.md escolhido (crie se não existir), acrescente a seção abaixo. As caixas seguintes põem as linhas de regra sob "Regras" e as recusas sob "Recusadas".

   ```markdown
   ## Quota Keeper (táticas de Jaber Neto, JN Softworks)

   ### Regras

   ### Recusadas (não oferecer de novo)
   ```

   Se a resposta foi "Só neste projeto" e esse CLAUDE.md é compartilhado com outras pessoas (num repositório, por exemplo), avise antes de gravar.

   Configurações, hooks e scripts são sempre do usuário inteiro (`<pasta de configuração>/settings.json`), mesmo com "Só neste projeto": essa resposta vale só para as linhas de regra. Avise a pessoa disso.

   Se a seção "Quota Keeper" (ou "Economia de tokens", nome antigo) já existir (o guia foi rodado antes), atualize a que existe, nunca crie outra. O mesmo vale para as configurações e os hooks das caixas seguintes: se já estiverem no `settings.json`, atualize, nunca duplique.
3. Confira se há Python 3 (`python --version` ou `python3 --version`). Os scripts das Caixas 5, 7 e 8 precisam dele. Se não houver, avise que essas partes vão precisar do Python (https://www.python.org/downloads/) e siga com o resto.
4. Guarde a resposta de "Onde usa": a Caixa 7 depende dela.
5. Guarde a resposta de "Plano": as Caixas 7 e 8 dependem dela. Nunca suponha o plano, nem pelo que uma ferramenta mostrar. Com "Não sei", fale de forma geral ("se o seu plano tiver limite semanal em %...") e deixe a pessoa decidir. Se ela quiser descobrir, mostre o que a tela de uso diz (no app, a ferramenta `get_usage`; no terminal, `/usage`) e peça que ela confirme; sem a confirmação dela, fica "Não sei".

**Recusas, em todas as caixas:** cada tática respondida "Não" (ou desmarcada) vira uma linha em "Recusadas", com o nome dela, para nenhuma sessão perguntar de novo.

---

## Caixa 2 — Configurações

**O que é:** três ajustes no `<pasta de configuração>/settings.json` e uma regra de esforço.
**Por quê:** agentes num modelo mais barato; agente que espera não paga de novo a conversa inteira; conversa resumida antes de cada passo ficar caro.
**Atenção:** os números desta caixa (compactar em 50%) supõem a janela de 1 milhão de tokens. Veja a janela da pessoa (regra "Janela de contexto", no começo do guia; sem conseguir ver, suponha 200 mil). Se for de 200 mil, não baixe a compactação: pule a pergunta 3 e deixe o padrão.

Perguntas:

1. **Os agentes nascem em Sonnet?** — cabeçalho `Agentes`
   - **Sim (Recomendado)** — Todo agente começa no Sonnet, mais barato que o Opus. Quando precisar, o Claude pede Opus ou Haiku para um agente específico.
   - **Não** — Os agentes usam o mesmo modelo da conversa.
2. **Seus agentes costumam esperar mais de 5 minutos por algo (compilação, testes, download, renderização)?** — cabeçalho `Espera longa`
   - **Sim, cache de 1 hora** — O agente que espera não paga de novo a conversa inteira na volta. Cada gravação custa mais (2 vezes em vez de 1,25), então só compensa com esperas longas.
   - **Não, deixar como está** — Tarefas rápidas: o cache padrão de 5 minutos já serve.
3. **Quando resumir a conversa automaticamente?** — cabeçalho `Compactar`
   - **Em 50% (Recomendado)** — A conversa é resumida quando chega à metade do espaço, antes de cada passo ficar caro.
   - **Em 25%** — Para produção longa numa sessão só. Resume mais vezes e perde mais detalhe.
   - **Não mexer** — Fica no padrão, perto do fim do espaço.
4. **Virar regra: esforço Alto, sem modo de frota de agentes?** — cabeçalho `Esforço`
   - **Sim (Recomendado)** — O Claude recomenda esforço Alto; Máximo só para problema muito difícil; nenhum modo que abre muitos agentes de uma vez sem você pedir.
   - **Não**

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

**O que é:** o CLAUDE.md e o índice da memória entram em toda sessão antes da primeira mensagem e são relidos a cada passo. Cada linha neles é paga muitas vezes por dia. Junto vem o jeito de conversar: escrever custa 5 vezes mais que ler, e tudo o que é escrito fica na conversa.

Perguntas:

1. **Manter o CLAUDE.md curto (regras e ponteiros; o detalhe vai para outros arquivos)?** — cabeçalho `CLAUDE.md`
   - **Sim, e sugerir cortes (Recomendado)** — Vira regra, e o Claude propõe agora o que mover para outro arquivo. Nada sai sem o seu sim.
   - **Só a regra** — Vale daqui para frente; o arquivo atual fica como está.
   - **Não**
2. **Memória com índice curto (uma linha por ficha; projeto grande ganha uma ficha-resumo)?** — cabeçalho `Memória`
   - **Sim (Recomendado)** — O índice é lido em toda sessão, e só até certo tamanho. Linha curta cabe mais e custa menos.
   - **Não uso memória**
   - **Não**
3. **Mensagens curtas no meio do trabalho, tudo junto no fim?** — cabeçalho `Conversa`
   - **Sim (Recomendado)** — Entre um passo e outro, só uma linha do que está fazendo. Respostas, resultados e avisos vêm juntos na mensagem final.
   - **Não** — Prefiro acompanhar com mais detalhe.
4. **Coisa longa vai para arquivo, não para o chat?** — cabeçalho `Texto longo`
   - **Sim (Recomendado)** — Para mostrar um texto ou log grande, você salva num arquivo da pasta e diz o nome; o Claude lê só o trecho que precisa.
   - **Não**

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

**O que é:** tudo o que o Claude lê fica na conversa e é relido em cada passo seguinte.
**Por quê:** um arquivo de 50 mil tokens lido no começo custa ~5 mil de peso em cada passo depois; em 100 passos, ~560 mil. Lido por um agente, ele nunca entra na conversa principal.

Pergunta (uma só, com várias respostas: `multiSelect: true`):

1. **Quais destes hábitos de leitura viram regra?** — cabeçalho `Leitura`
   - **Buscar em vez de ler** — Procurar o nome ou o título e ler só umas 50 linhas em volta. Nunca ler inteiro um documento grande, um log ou um arquivo gerado.
   - **Leitura grande para agente** — Um agente lê e devolve só o resumo; o volume não entra na conversa. Haiku para achar e filtrar; Sonnet para entender.
   - **Extrair uma vez** — Quando várias tarefas usam a mesma fonte grande, um agente escreve uma nota curta com o que importa, e as próximas leem a nota.
   - **Log filtrado na fonte** — Marcar as linhas do próprio log e buscar só a marca; nunca carregar inteiro um log de compilação ou de teste.

Passos: grave uma linha por item marcado; os não marcados vão para "Recusadas".

Texto da regra:
> - Buscar antes de ler: procurar o nome e ler só o trecho em volta; documento grande, log e arquivo gerado nunca inteiros.
> - Leitura grande (log, vários arquivos, documento longo) vai para agente que devolve só o resumo (Haiku para achar, filtrar e contar; Sonnet para entender). Ler inteiro só o que vou editar.
> - Fonte grande usada por várias tarefas: extrair uma vez numa nota curta no projeto e reaproveitar a nota.
> - Log: marcar as próprias linhas e buscar a marca; nunca carregar inteiro um log de compilação ou de teste.

---

## Caixa 5 — Agentes

**O que é:** um agente nasce com conversa vazia, então cada passo dele é barato no começo. Mas ele também relê a própria conversa a cada passo, e fica caro se trabalhar muito tempo.
**Por quê:** no uso do autor, agentes de 100 ou mais chamadas foram 74% do gasto dos agentes, e 71% desse gasto veio de passos com a conversa do agente acima de 200 mil tokens.

Perguntas:

1. **Agente curto: parar em ~100 chamadas e passar o bastão?** — cabeçalho `Agente curto`
   - **Sim, em ~100 (Recomendado)** — O agente fecha o item, grava onde parou num arquivo e devolve o resumo. Se sobrou trabalho, a conversa principal abre outro agente a partir desse arquivo.
   - **Não**
2. **Qual modelo para cada tipo de trabalho?** — cabeçalho `Modelos`
   - **Por papel (Recomendado)** — Sonnet por padrão; Haiku para o mecânico (achar arquivo, filtrar log, contar); Opus só para código delicado (segurança, contas, dinheiro, criptografia).
   - **Experimental: Opus coordena** — Um agente Opus divide a tarefa, abre agentes Sonnet um de cada vez, roda os testes e revisa só o que mudou. Ainda em teste pelo autor.
   - **Não mudar**
3. **Agentes em lote e com resposta curta?** — cabeçalho `Lote`
   - **Sim (Recomendado)** — Um agente por tarefa (não um por pedacinho); vários lançados na mesma mensagem; cada um grava o detalhe num arquivo e devolve 5 a 10 linhas.
   - **Não**
4. **Instalar o freio de agentes?** — cabeçalho `Freio`
   - **Sim (Recomendado)** — Um script impede que um agente aberto por outro agente abra mais agentes, e limita cada agente a 6 filhos. Evita cadeia sem fim.
   - **Não**

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

Texto da regra:
> - Agente que edita ou corrige: o pedido dele diz "ao chegar a ~100 chamadas, feche o item, grave o ponto de retomada em <arquivo> e devolva o resumo". Se sobrou trabalho, a conversa principal abre outro agente a partir desse arquivo. Tarefa grande já nasce dividida em agentes de ~100 chamadas.
> - **[Só com cache de 1 hora]** Agente não fica mais de ~50 minutos numa espera só; espera maior = gravar o ponto de retomada e devolver.
> - Modelos por papel: Sonnet por padrão; Haiku para o mecânico (achar arquivo, filtrar log, contar); Opus só para agente que edita código delicado (segurança, contas, dinheiro, criptografia).
> - (Experimental) Código novo ou correção fora de segurança, contas e criptografia: um agente Opus coordena. Ele escreve o pedido de cada pedaço, abre agentes Sonnet um de cada vez (~80 chamadas cada), roda os testes por script, revisa só o que mudou, conserta o que estiver ruim e devolve poucas linhas. Pedaço que falhar duas vezes, o Opus faz. Anotar cada caso em `~/Documents/piloto_opus_sonnet.md`; depois de ~6 casos, perguntar à pessoa se vira padrão.
> - Agentes: um por tarefa, não um por pedacinho; vários ao mesmo tempo saem na MESMA mensagem; cada um grava o detalhe num arquivo e devolve 5 a 10 linhas.

---

## Caixa 6 — Passagem e troca de sessão

**O que é:** um arquivo curto em cada projeto com o que foi feito, o que está pela metade e o próximo passo exato. Quando a conversa fica grande ou a etapa muda, o Claude atualiza esse arquivo, e uma sessão nova começa por ele, com a conversa vazia.
**Por quê:** foi a maior economia do autor: a conversa principal caiu 75% depois desta regra. O resumo automático (compactação) perde detalhe; o arquivo não.
**Atenção:** os números desta caixa (trocar em ~250 mil) supõem a janela de 1 milhão de tokens. Veja a janela da pessoa (regra "Janela de contexto", no começo do guia; sem conseguir ver, suponha 200 mil). Se for de 200 mil, troque de sessão em ~100 mil (diga isso à pessoa na pergunta 2 e use `<100>` na regra) e não baixe a compactação da Caixa 2.

Perguntas:

1. **Usar arquivo de passagem nos projetos com trabalho em andamento?** — cabeçalho `Passagem`
   - **Sim, com o modelo (Recomendado)** — Um `PASSAGEM.md` na raiz do projeto, feito a partir do modelo deste guia. Se o projeto já tiver um arquivo assim, usa o dele.
   - **Não**
2. **Quando trocar de sessão?** — cabeçalho `Troca`
   - **~200 mil ou etapa nova** — Mais trocas, cada passo relê menos. Etapa nova sempre começa em sessão nova.
   - **~250 mil ou etapa nova (Recomendado)** — Na conta do autor (260 sessões), entre 200 e 300 mil o custo total quase não muda, e 250 fica no meio. Acima de ~300 mil, cada passo relê tanto que sai mais caro. Etapa nova sempre começa em sessão nova.
   - **~300 mil ou etapa nova** — Menos trocas, cada passo mais caro. Vale quando a passagem perde muito do que a conversa sabia.
   - **Só quando eu pedir**
3. **Uma tarefa por sessão?** — cabeçalho `Uma tarefa`
   - **Sim (Recomendado)** — Assunto novo, sem ligação com o que está aberto, vai para uma sessão nova (ou `/clear`), não para o fim desta conversa.
   - **Não**
4. **Arquivo de resumos ao lado da passagem?** — cabeçalho `Resumos` (só se a pergunta 1 foi "Sim")
   - **Sim (Recomendado)** — Cada sessão deixa uma entrada curta no fim de um `RESUMOS.md`: o que fez, o que decidiu, o que ficou aberto. Serve só para achar depois em qual sessão algo foi feito.
   - **Não**

Passos:
1. Pergunta 1 "Sim": copie `pt/PASSAGEM_MODELO.md` para `<pasta de configuração>/modelos/PASSAGEM_MODELO.md` (crie `modelos` se não existir). É o modelo: a sessão cria o `PASSAGEM.md` de cada projeto a partir dele quando houver trabalho em andamento. Grave a regra.
2. Pergunta 2: grave a regra com o número escolhido, ou a regra "Só quando eu pedir". Diga à pessoa onde ver o tamanho da conversa: no app, o indicador de contexto junto da caixa de mensagem; no terminal, o comando `/context`.
3. Pergunta 3: grave a regra. Lembre a pessoa: só ela pode digitar `/clear` ou `/compact`; o Claude não consegue.
4. Pergunta 4 "Sim": copie `pt/RESUMOS_MODELO.md` para `<pasta de configuração>/modelos/RESUMOS_MODELO.md` e grave a regra.
5. Se houver um projeto com trabalho em andamento agora, ofereça criar o `PASSAGEM.md` dele e o `RESUMOS.md` ao lado (só com sim).

Texto da regra (na troca de sessão, grave uma das duas versões):
> - Passagem: todo projeto com trabalho em andamento tem um arquivo de passagem (o que o projeto já tiver, ou `PASSAGEM.md` na raiz, a partir de `<pasta de configuração>/modelos/PASSAGEM_MODELO.md`). Reescrever, não acrescentar no fim. Atualizar ao fechar cada parte, antes da troca de sessão e quando o vigia de gasto avisar. Sessão nova começa lendo a passagem e faz o "próximo passo exato" sem perguntar, exceto ações irreversíveis, que pedem confirmação.
> - **[Número]** Troca de sessão: com a conversa em ~<250> mil tokens, ou numa etapa nova, fechar a parte em andamento, atualizar a passagem e trocar de sessão. Se não houver regra de sucessora, dizer à pessoa em uma linha o que colar na sessão nova.
> - **[Só quando eu pedir]** Troca de sessão só quando a pessoa pedir; avisar em uma linha quando a conversa passar de ~<250> mil tokens.
> - Uma tarefa por sessão: assunto novo e sem ligação vai para sessão nova.
> - Resumos: todo projeto com arquivo de passagem tem, ao lado dele, um arquivo de resumos (`PASSAGEM.md` → `RESUMOS.md`; `PASSAGEM_X.md` → `RESUMOS_X.md`; criar a partir de `<pasta de configuração>/modelos/RESUMOS_MODELO.md`). Toda sessão, ao fechar (antes de abrir a sucessora ou de encerrar a etapa), acrescenta no fim UMA entrada `## <n> — <título da sessão> (<data>, <id da sessão>)` com até três linhas curtas: **Fez** (com os nomes que alguém procuraria depois: arquivos, telas, ferramentas), **Decidiu** (o que ficou fechado, e por quem), **Ficou** (o que ficou aberto ou sem resposta, ou "nada"). Não relê o arquivo inteiro, só acrescenta. Serve para achar depois em qual sessão algo foi feito.

---

## Caixa 7 — Sessão sucessora automática (a mais trabalhosa)

**O que é:** na hora de trocar de sessão (Caixa 6), em vez de pedir à pessoa para abrir uma sessão nova, o próprio Claude abre a sucessora, que começa pela passagem. A sucessora pode abrir a próxima do mesmo jeito: a cadeia segue enquanto houver trabalho.
**Por quê:** sem isso, a troca depende da pessoa estar olhando. O autor teve uma etapa parada a noite inteira esperando um clique. E a sessão anterior, se continuar ligada à nova, acorda e relê a conversa inteira cada vez que a nova termina um turno.

Pré-requisito: Caixa 6, pergunta 1, respondida "Sim". Sem arquivo de passagem, pule esta caixa.

Há dois caminhos. Explique os dois à pessoa antes da caixa:
- **Caminho A, pelo app (visível, sem token):** no app desktop, o Claude tem uma ferramenta para abrir outra sessão. A sucessora aparece na barra lateral como qualquer sessão. É o recomendado.
- **Caminho B, pelo terminal (sem tela, precisa de token):** um script roda o Claude pelo terminal (`claude -p`) em rodadas, cada uma com conversa vazia, lendo e atualizando a passagem. Não aparece no app; o resultado fica nos arquivos e num log. Precisa de um token de acesso de longa duração. Serve só para quem usa só o terminal: no app, os estepes, o "avisar e seguir" e a tarefa agendada cobrem as recusas sem token, então quem usa o app não instala o token.

**Antes de mostrar qualquer pergunta** (só se a Caixa 1 respondeu "App desktop" ou "Os dois"): ache as ferramentas com ToolSearch, pelo nome (lista no passo 1 do caminho A), e veja o modo de permissão desta sessão (`get_session` com "self", campo `permissionMode`). Depois:
- Se `start_session` existe: siga como abaixo.
- Se `start_session` não existe: o caminho A não está disponível nesta versão. Diga isso à pessoa em uma linha e trate o caso como "Terminal" (próximo item): não faça as perguntas 1, 2, 5 e 6, que dependem dessa ferramenta. Se ela recusar o caminho B ("Agora não"), grave só a regra "[Eu abro]" (a regra mínima: o Claude atualiza a passagem e **avisa a pessoa para abrir a sessão nova**), não grave as regras de fechar a anterior nem a de herança, ponha "Sessão sucessora automática (sem a ferramenta no app)" em "Recusadas" e pule os passos do caminho A.

Como mostrar as perguntas (são sete, mas não todas de uma vez):
- Se a Caixa 1 respondeu "Terminal": não faça as perguntas 1, 2, 5, 6 e 7, que dependem do app. Faça só a 3 e, se a resposta for "Sim, me guie", a 4 numa segunda chamada. A sucessora desse caso é a regra do caminho B; com "Agora não", fica a regra "[Eu abro]".
- Se respondeu "App desktop" ou "Os dois": não faça as perguntas 3 e 4 (o token não é preciso no app; trate como "Agora não", sem pôr em "Recusadas"). Primeira chamada com as perguntas 1 e 2. Segunda chamada, se a 1 for "O Claude, sozinho": a 5, a 6 e a 7. Na regra "[O Claude, sozinho]", o "Se isso também falhar" fica "aviso a pessoa em uma linha".

Pergunta 3 e o plano (Caixa 1): com "Chave de API", não faça a pergunta 3 (o token é só das assinaturas) e trate como "Agora não"; se a Caixa 1 também respondeu "Terminal", fica a regra "[Eu abro]". Com "Não sei", faça a pergunta e diga que o token só existe nos planos de assinatura (Pro, Max, Ultra, Team e Enterprise); se o comando do token recusar a conta dela, trate como "Agora não".

Na pergunta 3 (só no caso "Terminal"), ponha "(Recomendado)" em **"Sim, me guie"**.

Na pergunta 5, use o modo de permissão visto antes das perguntas. Se for `auto` (modo automático), ponha "(Recomendado)" em **"Liberar e começar no automático"**; se for outro, ou se não deu para ver, em **"Só liberar a tarefa"**.

1. **Quem abre a sessão sucessora?** — cabeçalho `Sucessora`
   - **O Claude, sozinho (Recomendado)** — Na hora da troca, o Claude atualiza a passagem, abre a sucessora e para. Você só vê a nova sessão aparecer.
   - **O Claude propõe, eu clico** — Aparece um cartão para você iniciar. Se você não estiver olhando, o trabalho para até o clique.
   - **Eu abro** — O Claude atualiza a passagem e diz o que colar na sessão nova.
2. **A sucessora fecha a anterior?** — cabeçalho `Fechar mãe`
   - **Sim (Recomendado)** — A sucessora se solta da anterior e a arquiva, para a anterior não acordar e reler tudo a cada turno da nova. O título ganha um número ("Site" → "Site 2" → "Site 3").
   - **Não** — As duas ficam abertas; você arquiva quando quiser.
3. **Instalar o token para as rodadas sem tela (caminho B)?** — cabeçalho `Token`
   - **Sim, me guie** — Você roda um comando, faz login no navegador e grava o token num arquivo. O Claude nunca vê o token. Leva uns 10 minutos.
   - **Agora não** — Fica só o caminho A, que precisa do app desktop.
4. **O que as rodadas sem tela podem usar?** — cabeçalho `Permissões`
   - **Só arquivos (Recomendado)** — Ler, buscar, criar e editar arquivos. Nenhum comando.
   - **Arquivos + terminal** — Também roda comandos (testes, compilação). Mais útil e mais arriscado: ninguém está olhando, e o terminal da rodada também enxerga o token.
   - **Decidir por projeto** — O Claude pergunta na primeira vez em cada projeto.
5. **Liberar a reserva por tarefa agendada?** — cabeçalho `Agendada`
   - **Liberar e começar no automático** — Duas regras que deixam o Claude criar e rodar tarefa agendada sem pedir aprovação, e toda sessão nova (no app e no terminal) passa a começar no modo automático, inclusive a sucessora que a tarefa abre. Para quem já trabalha no modo automático.
   - **Só liberar a tarefa** — Só as regras. A sucessora aberta pela tarefa começa no modo normal e para no primeiro comando ou edição, esperando você aprovar. (O app diz que cada rotina guarda as aprovações dadas durante uma execução e que elas valem nas próximas; não testado.)
   - **Não liberar** — Quando o app recusar abrir a sessão, a reserva é o caminho B (se instalado) ou um aviso a você.
6. **Quando o app recusar abrir a sucessora?** — cabeçalho `Recusa`
   - **Sessão de estepe (Recomendado)** — Num turno seu, o Claude deixa algumas sessões paradas e arquivadas na pasta do projeto (os "estepes"; quantos, a pergunta 7 diz). Na troca, ele desarquiva um, dá o título novo e manda a tarefa por mensagem: a sucessora sai na hora, na lista normal, mesmo sem você na tela. Sem estepe na pasta, cai no "Avisar e seguir".
   - **Avisar e seguir** — O Claude grava a passagem, manda um aviso (no computador e, com Remote Control ligado, no celular) e continua trabalhando nesta sessão. Na sua próxima mensagem, qualquer uma, ele abre a sucessora na lista normal antes de tudo. A reserva (tarefa agendada, rodadas sem tela) fica só para quando a conversa passar muito do limite sem resposta sua.
   - **Reserva na hora** — O Claude usa logo a reserva. A sucessora sai mais cedo, mas, se for por tarefa agendada, fica escondida na seção Rotinas e não consegue abrir a próxima sozinha.
7. **Quantos estepes por pasta?** — cabeçalho `Estepes` (só se a pergunta 6 for "Sessão de estepe"; a opção "Outro" da caixa deixa a pessoa digitar outro número)
   - **2** — Cobre duas trocas seguidas sem você; a terceira cai no "Avisar e seguir".
   - **4 (Recomendado)** — Cobre uma noite com várias trocas. Cada estepe parado custa pouco (só a resposta "pronta"), mas aparece na lista de arquivadas.
   - **6** — Para trabalhos longos que trocam muitas vezes sozinhos.

### Passos do caminho A (app desktop)

Só se a Caixa 1 respondeu "App desktop" ou "Os dois" e `start_session` existe. Se respondeu "Terminal", ou se a ferramenta não existe, vá direto para o caminho B (ou, sem ele, para a regra mínima acima).

1. **Ferramentas** (achadas antes das perguntas, com ToolSearch, pelo nome): `start_session` (abrir sessão), `create_scheduled_task` e `list_scheduled_tasks` (criar e listar tarefa agendada), `run_scheduled_task` (rodar uma tarefa agora), `set_session_title` (trocar o título de uma sessão), `detach_session`, `archive_session` e `unarchive_session` (soltar, arquivar e desarquivar), `list_sessions` e `get_session` (listar e ver sessões), `set_remote_control` (ligar e desligar o Remote Control), `set_session_effort` e `set_session_model` (esforço e modelo de outra sessão), `list_task_runs` (sessões abertas por uma tarefa), `list_sections` (seções da barra lateral), `PushNotification` (aviso no computador e, com Remote Control, no celular) e `SendMessage` (mensagem para outra sessão). Em novembro de 2026 elas existiam com esses nomes no app desktop. Chame `start_session` com initiation "user_asked" (os valores "offer" e "own_initiative" viram um cartão esperando clique) e contexto "fresh" (conversa vazia).
2. **Grave as regras** da pergunta 1 (uma das três versões abaixo) e, se a pergunta 2 for "Sim", a de fechar a anterior; se a pergunta 6 for "Avisar e seguir", a de avisar e seguir; se for "Sessão de estepe", a dos estepes (com o número da pergunta 7) e também a de avisar e seguir, para quando não houver estepe (com "Reserva na hora", nada a mais: a regra da pergunta 1 já usa a reserva). Grave sempre a regra de herança. Explique à pessoa que o pedido da sucessora leva o id da sessão atual ("Sessão anterior: <id>"), achado com `list_sessions` ou `get_session`, para a sucessora saber quem arquivar; com a tarefa só manual (passo 4), o pedido inteiro vai no arquivo `SUCESSORA.md`.
3. **Faça o que a pergunta 5 pediu**, no `<pasta de configuração>/settings.json` (não no do projeto: lá o modo automático como padrão não vale):
   - "Liberar e começar no automático": em `"permissions"` → `"allow"`, acrescente os nomes exatos das ferramentas de criar e de rodar tarefa agendada como o ToolSearch mostrou (em novembro de 2026: `"mcp__scheduled-tasks__create_scheduled_task"` e `"mcp__scheduled-tasks__run_scheduled_task"`); e em `"permissions"` ponha `"defaultMode": "auto"`. Crie o que faltar e não apague o que já existir.
   - "Só liberar a tarefa": só as duas regras em `"allow"`.
   - "Não liberar": nada no `settings.json`; na regra da pergunta 1, apague o trecho que vai de "uso uma tarefa agendada" até "Se isso também falhar:", inclusive.

   Confira com `check_settings.py`. Diga à pessoa que o modo automático como padrão exige uma versão recente do Claude Code e um plano que tenha esse modo; sem isso, a sessão começa no modo normal.
4. **Explique à pessoa as travas** que o autor encontrou (testadas em novembro de 2026):
   - **O app recusa abrir a sessão** quando o turno não veio de uma mensagem da pessoa: aviso de agente, mensagem de outra sessão, tarefa agendada, e até o primeiro turno de uma sessão aberta por outra. A recusa é do próprio app, e nenhuma configuração muda isso. Uma mensagem nova da pessoa no meio de um turno desses já destrava: num teste de 04/11/2026, o turno começou por aviso automático, a pessoa respondeu caixas de pergunta e mandou mensagens no meio, e a sucessora abriu. Resposta numa caixa de pergunta, sozinha, não destrava (outro teste do mesmo dia: a pessoa respondeu "abra agora" na caixa e o app recusou de novo), então a regra pede mensagem nova. Por isso a regra deixa a troca, quando der, para um turno que veio de mensagem da pessoa ("avisar e seguir", pergunta 6), e tem reservas: primeiro uma tarefa agendada (a só manual do projeto, rodada na hora, ou uma de uma vez só para ~2 minutos depois, com o mesmo pedido; ela aparece no app como sessão); depois o caminho B, se instalado; por último, avisar a pessoa.
   - **No modo automático, o classificador** (o filtro que aprova ou barra cada ação) **pode barrar a tarefa agendada**, porque ela roda sozinha mais tarde. A regra de permitir da pergunta 5 resolve: ação com regra própria não passa pelo classificador (está na documentação do modo automático). Com as regras, criar e rodar a tarefa passaram num turno automático; sem a regra de rodar, o classificador barrou `run_scheduled_task` até num turno da pessoa (04/11/2026).
   - **A tarefa agendada não guarda o modo da sessão que a criou**, nem quando criada num turno da pessoa: ela roda no modo padrão das configurações. Se esse modo for o normal, a sucessora para no primeiro comando esperando aprovação. Daí a opção "começar no automático".
   - **O app recusa arquivar a anterior enquanto ela tem "trabalho vivo"**: turno em andamento (ela ainda está escrevendo a última mensagem quando a sucessora começa), agente ou tarefa em segundo plano, mensagem na fila, ou alguém olhando por Remote Control (pelo celular, por exemplo). Por isso a regra desliga o Remote Control da anterior antes, tenta de novo nos turnos seguintes e, se for agente em segundo plano, não força. Arquivar também pode pedir aprovação num cartão, conforme o modo de permissão.
   - Uma autorização dada antes não destrava a abertura da sessão: o app olha se veio mensagem da pessoa, não o que ela já aprovou. O que ajuda é trocar de sessão num turno da pessoa quando a conversa já estiver perto do limite, sem esperar.
   - **Por que estepe e "avisar e seguir" vêm antes da tarefa agendada:** a sucessora aberta por tarefa agendada fica só na seção Rotinas e não tem `start_session`, então a cadeia fica presa lá. O estepe fica na lista normal. Avisando e continuando, a troca acontece na próxima mensagem da pessoa, na lista normal. O aviso (`PushNotification`) chega no celular só com o Remote Control ligado, e o app não mostra o aviso se a pessoa já estiver olhando a sessão.
   - **Sessão de estepe** (pergunta 6; testado em 04/11/2026, tudo num turno automático): uma sessão criada antes com o pedido "não faça nada, responda só 'pronta'", depois solta e arquivada, pode ser desarquivada, renomeada e receber a tarefa por mensagem sem a pessoa. Ela trabalhou no modo padrão das configurações (no teste, o automático), sem pedir aprovação, e fica na lista normal de sessões, não em Rotinas. Modelo e esforço não pedem um estepe de cada tipo: a sessão que usa o estepe troca os dois nele (`set_session_model`, `set_session_effort`) antes de mandar a mensagem; o app não deixa uma sessão trocar o próprio modelo, só o de outra. Travas: o Remote Control do estepe só liga depois que ele recebe a mensagem (antes, o app responde "requires an active session"); cada estepe nasce na pasta da sessão que o criou, então os estepes são por pasta; criar estepe usa `start_session`, que só passa num turno que veio de mensagem da pessoa, então a reposição fica para esse turno; a sucessora que veio de estepe já está solta e não faz `detach_session`. O nome "Estepe <pasta> N" é de propósito uma palavra que quase não aparece em título de sessão, para a busca não confundir.
   - Tarefa de uma vez só fica na lista de tarefas agendadas, desligada, depois de rodar. Apagar a tarefa arquiva a sessão que ela abriu: só apague quando a cadeia já tiver passado dela.
   - **A tarefa só manual (sem horário) é a melhor reserva** numa sessão comum. Criada antes, ela continua ligada depois de rodar (não se desliga como a de uma vez), roda de novo a cada troca e abre a sessão em poucos segundos com `run_scheduled_task`, também num turno automático (com as regras da pergunta 5; testado em 04/11/2026). Limites: o app recusa rodar tarefa de dentro de uma sessão aberta por tarefa ("from a scheduled-task run session"), e essa sessão também não tem `start_session`; recusa rodar enquanto outra execução da mesma tarefa estiver em andamento; e a tarefa roda na pasta da sessão que a criou (a ferramenta não tem campo de pasta). Como o pedido da tarefa é fixo, o que muda a cada troca vai num arquivo `SUCESSORA.md` na pasta, que a sessão anterior reescreve logo antes de rodar a tarefa: o pedido inteiro (passagem, "Sessão anterior: <id>", título da sucessora). Assim uma pasta com várias passagens usa uma tarefa só. A sessão nova nasce com o título da tarefa; a anterior o troca com `set_session_title` (passou em 04/11/2026). Crie a tarefa com `notifyOnCompletion` false: sem isso, a sessão que a criou recebe um aviso a cada execução e acorda para reler a conversa.
   - **A sessão aberta por tarefa agendada nasce sem Remote Control e com esforço médio.** A sessão que criou a tarefa, se ainda estiver no turno, confere em `list_task_runs` que ela abriu e ajusta os dois (`set_remote_control` e `set_session_effort`). A própria sessão da tarefa não consegue: enquanto ninguém a abre na tela, toda ação que pede aprovação é recusada ("nobody has opened this scheduled run"). Isso incluiu ligar o próprio Remote Control e criar outra tarefa agendada, mesmo com a regra de permitir (testado em 04/11/2026). Por isso uma sucessora aberta por tarefa só abre a próxima num turno que veio de mensagem da pessoa, ou depois que a pessoa a abrir na tela; se não der, avisa a pessoa.
   - **Rotinas:** no app, cada tarefa agendada vira uma "rotina". A sessão que ela abre aparece só dentro da seção Rotinas da barra lateral, debaixo da rotina, e não junto das outras sessões. Se essa seção estiver desligada, a sucessora existe, mas a pessoa não a vê. Confira com `list_sections` (seção `routines`, campo `shown`). Se estiver desligada, peça à pessoa que a ligue no menu de filtro da barra lateral: o Claude não consegue (nenhuma ferramenta liga a seção nem tira a sessão de lá). E a tarefa de uma vez se desliga sozinha depois de rodar; desligada, ela e a sessão dela somem da seção Rotinas quando a sessão termina o turno (a sessão não é arquivada, só fica escondida; visto em 04/11/2026). Por isso a mensagem final da sessão que criou a tarefa sempre traz o link da sessão nova.
5. **Teste** (com sim da pessoa):
   1. Crie uma pasta de teste, `~/Documents/teste_sucessora/` (não na pasta de configuração, que é protegida), com um `PASSAGEM.md` cujo próximo passo exato é: *"Crie `ok.txt` com a palavra ok e escreva ETAPA CONCLUIDA na primeira linha desta passagem."*
   2. Abra uma sessão chamada "Teste de sucessora" com o pedido: *"Teste de instalação: não arquive nem solte nenhuma sessão. Leia e siga `<caminho>/PASSAGEM.md`."* (Sem essa frase, a regra de fechar a anterior poderia soltar ou arquivar esta sessão de instalação.)
   3. Confira com `list_sessions` que ela apareceu. Quando ela terminar, confira que `ok.txt` existe. Diga à pessoa que pode arquivar a sessão de teste e apagar a pasta.

Texto da regra (pergunta 1, uma das três):
> - **[O Claude, sozinho]** Sucessora: na hora de trocar de sessão, eu mesmo abro a sucessora, sem a pessoa pedir (`start_session`, initiation "user_asked", contexto "fresh", pedido "Leia e siga <passagem>. Sessão anterior: <id>" + as regras de sucessora desta seção; o <id> é o desta sessão, achado com `list_sessions` ou `get_session`), aviso em uma linha com o link e paro. Não abro sucessora se a passagem diz ETAPA CONCLUIDA ou tem pergunta à pessoa que impede o próximo passo. Título = título atual + número ("Site" → "Site 2"). Nunca termino com "abra uma sessão nova", nem deixo cartão esperando clique. Se o app recusar ou virar cartão: uso uma tarefa agendada. Se esta sessão não foi aberta por tarefa e existe a tarefa só manual `sucessora-<pasta do projeto>` (`list_scheduled_tasks`), reescrevo `SUCESSORA.md` na pasta com o mesmo pedido e logo rodo a tarefa (`run_scheduled_task`); senão (ou se o app recusar rodar), crio na hora uma tarefa de uma vez para ~2 minutos depois, com o mesmo pedido. Confiro em `list_task_runs` que ela abriu; ajusto nela o título, o Remote Control e o esforço (`set_session_title`, `set_remote_control`, `set_session_effort`), se der; e confiro com `list_sections` se a seção Rotinas da barra lateral está ligada (só lá a sessão aparece): se não estiver, aviso a pessoa em uma linha de onde ligar. Ponho sempre o link da sessão nova na mensagem final (a tarefa de uma vez some da barra lateral depois de rodar). Numa sessão comum (não aberta por tarefa) na pasta de um projeto com passagem, se a tarefa só manual da pasta não existe, eu a crio: sem horário, `notifyOnCompletion` false, título "Sucessora <pasta>", pedido "Leia `SUCESSORA.md` nesta pasta e siga o que ele diz." Se isso também falhar: <rodadas sem tela, regra abaixo | aviso a pessoa em uma linha>. Quando der, deixo a troca para um turno que veio de mensagem da pessoa.
> - **[O Claude propõe]** Sucessora: na hora da troca, atualizo a passagem e proponho a sessão nova (cartão), com o pedido "Leia e siga <passagem>".
> - **[Eu abro]** Sucessora: na hora da troca, atualizo a passagem e digo em uma linha o que colar na sessão nova: "Leia e siga <passagem>".

Texto da regra (pergunta 2 "Sim"):
> - Fechar a anterior: a sucessora, logo no começo, se solta da sessão que a abriu (`detach_session`), desliga o Remote Control da anterior (`set_remote_control` com o id dela e false) e arquiva a sessão cujo id vem em "Sessão anterior: <id>" no pedido (`archive_session`). Se recusar, tenta de novo no fim do primeiro turno e no começo de cada turno que vier de mensagem da pessoa, até conseguir; se a recusa falar de agente ou tarefa em segundo plano, não força: avisa em uma linha que a pessoa pode arquivar pela barra lateral. Antes de abrir a sucessora, a sessão encerra os agentes e tarefas em segundo plano que já entregaram. Não vale para sessão paralela de outra tarefa (essa não arquiva ninguém).

Texto da regra (pergunta 6 "Avisar e seguir"; troque `<400>` pelo limite da Caixa 6 + 150 mil):
> - Avisar e seguir: se o app recusar abrir a sucessora (turno que não veio de mensagem da pessoa) ou virar cartão, ainda não troco: gravo a passagem, mando `PushNotification` ("<título>: hora de trocar de sessão, responda qualquer coisa aqui") e continuo o trabalho nesta sessão. Quando chegar mensagem nova da pessoa, antes de qualquer outra coisa atualizo a passagem e abro a sucessora com `start_session`; o pedido dela diz quais agentes ainda rodam aqui e onde cada um grava o ponto de retomada. Depois, aqui, peço a cada agente em andamento que feche o item e grave o ponto de retomada (`SendMessage`), junto os resumos na passagem e aviso a sucessora (`SendMessage` com o id dela). A reserva da regra da sucessora (tarefa agendada, rodadas sem tela, aviso) fica só para o teto: a conversa passar de ~<400> mil tokens sem mensagem da pessoa.

Texto da regra (pergunta 6 "Sessão de estepe"; troque `<4>` pelo número da pergunta 7; grave também a de avisar e seguir):
> - Estepes: a cada mensagem nova da pessoa (o único turno em que `start_session` passa), confiro os estepes da pasta do projeto (`list_sessions` com as arquivadas, título "Estepe <pasta> N"). Para cada número de 1 a <4> sem estepe (usado numa troca ou nunca criado), crio um com esse número, sem passar de <4>: `start_session` "user_asked", contexto "fresh", `use_worktree` false, título "Estepe <pasta> N", pedido "Sessão ESTEPE: não faça nada, não leia arquivos, não chame ferramentas, não siga as regras de começo de sessão; responda só 'pronta' e pare. Mais tarde outra sessão vai mandar a tarefa por mensagem; aí siga a mensagem.", e ponho esforço baixo nela (`set_session_effort`). Quando cada uma responder "pronta", solto (`detach_session`) e arquivo (`archive_session`). Na troca, se o app recusar abrir a sucessora ou virar cartão, e a pasta tiver estepe: desarquivo o de menor número (`unarchive_session`), troco o título dele para o título atual + número (`set_session_title`), ponho nele o modelo e o esforço que a tarefa pede (`set_session_model`, `set_session_effort`; valem a partir do próximo turno, por isso antes da mensagem), mando por `SendMessage` o pedido da sucessora (com "Sessão anterior: <id>", "esqueça o pedido de não fazer nada: agora siga todas as regras" e "não faça `detach_session`: você já está solta"), depois ligo o Remote Control dele (`set_remote_control`), aviso em uma linha com o link e paro. Sem estepe na pasta: avisar e seguir.

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
5. **Proíba a leitura do arquivo.** No `settings.json`, em `"permissions"` → `"deny"` (crie o que faltar e não apague o que já existir), acrescente a regra `"Read(<pasta de configuração>/relay_token.txt)"`, com o caminho completo já preenchido (sem `~`). Assim nenhuma sessão lê o arquivo. Diga à pessoa que o script de revezamento já passa a mesma proibição às rodadas.
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
   - Para desligar o caminho B: apagar `<pasta de configuração>/relay_token.txt`.

Texto da regra (caminho B):
> - Rodadas sem tela: `python <pasta de configuração>/tools/session_relay.py --folder <projeto> --handoff <passagem> --model sonnet --rounds 3 --tools "<lista>"`, lançado solto em segundo plano (Windows: `Start-Process ... -WindowStyle Hidden -PassThru`; Mac e Linux: `nohup ... &`), guardando o número do processo. Uso: <quando estou no terminal | só como reserva, quando o app recusar abrir sessão>. Roda escondido: aviso a pessoa em uma linha; na próxima mensagem dela, confiro o `relay.log` do projeto e, se a passagem não diz ETAPA CONCLUIDA e nada está rodando, lanço de novo ou abro a sucessora. Tarefa longa: `--timeout` maior. Nunca leio, mostro nem copio `relay_token.txt`.

---

## Caixa 8 — Vigia de gasto e medição

**O que é:** um script que roda sozinho a cada mensagem e a cada ferramenta usada, e avisa o Claude quando a sessão passa de certos limites. O Claude conta à pessoa em uma linha e propõe o que fazer (atualizar a passagem, abrir a sucessora, usar agente mais barato).
**Por quê:** ninguém percebe a conversa crescendo. No uso do autor, 14 de 36 trocas de sessão só aconteceram depois de 250 mil tokens, até o vigia passar a avisar no meio do turno.

Plano (Caixa 1): com "Chave de API", não faça as perguntas 2 e 3 (não há % semanal; o gasto aparece em dinheiro, no painel da API) e não as ponha em "Recusadas"; o vigia (pergunta 1) serve do mesmo jeito, porque avisa em tokens. Com "Team ou Enterprise" ou "Não sei", faça as duas, mas diga que só funcionam se a tela de uso mostrar um % de limite semanal; se, na hora de ler, não houver nenhum %, pare e avise a pessoa.

Perguntas:

1. **Instalar o vigia de gasto?** — cabeçalho `Vigia`
   - **Sim, limites do autor (Recomendado)** — Avisa com a conversa em 200 mil tokens (e a cada 100 mil a mais), aos 40, 80 e 150 prompts, e quando um agente chega a 100 e a 150 chamadas.
   - **Sim, avisar mais cedo** — Conversa em 150 mil; agente em 60 e 100 chamadas.
   - **Não**
2. **Conferir o uso antes e depois de tarefa grande?** — cabeçalho `Antes/depois`
   - **Sim (Recomendado)** — O Claude anota o % de uso do plano antes de uma tarefa grande e diz a diferença no fim, em uma linha.
   - **Não**
3. **Medir quanto vale 1% da cota no seu plano?** — cabeçalho `Medir plano`
   - **Sim** — Você anota o % de uso em dois momentos, com um ou dois dias entre eles, e um script faz a conta. Depois disso o vigia também avisa em % da cota.
   - **Não** — O vigia avisa só em tokens.

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

Texto da regra:
> - Vigia de gasto: quando aparecer um aviso "SPEND WATCH", contar à pessoa em uma linha, com o número, e propor o que fazer (passagem, sucessora, agente mais barato).
> - Antes e depois de tarefa grande: anotar o % de uso do plano e dizer a diferença no fim, em uma linha.
> - Medição do plano: no começo de uma sessão, se a última marca em `<pasta de configuração>/tools/measure_marks.csv` tiver mais de um dia, ler o % semanal e rodar `measure_point.py` com ele. Quando a estimativa ficar estável em duas ou três contas, propor pôr o número em `POINT` no `spend_watch.py`.

---

## Caixa 9 — Conferir o trabalho

**O que é:** conferir é obrigatório, mas dá para conferir gastando menos.

Pergunta (uma só, com várias respostas: `multiSelect: true`):

1. **Quais destes hábitos viram regra?** — cabeçalho `Conferência`
   - **Prova barata** — Quando um texto prova (linha de log, valor, saída de teste), usar o texto. Imagem só recortada no que importa e em escala menor; medidas tiradas por script.
   - **Testes por partes** — Depois de cada mudança, os testes do que mudou e uma regressão curta; a bateria inteira antes de publicar.
   - **Duas revisões só no sensível** — Segurança, contas, pagamento e criptografia ganham duas revisões independentes; o resto, uma.
   - **Não pagar duas vezes** — Depois de uma interrupção, conferir se agentes e tarefas em segundo plano ainda rodam e retomar, em vez de recomeçar. Processo só se encerra pelo número (PID) que a própria sessão iniciou, nunca pelo nome.

Passos: grave uma linha por item marcado; os não marcados vão para "Recusadas".

Texto da regra:
> - Prova barata: texto quando texto prova; imagem recortada e em escala menor; medidas por script.
> - Testes: o que mudou + regressão curta a cada mudança; bateria inteira antes de publicar. Testes e conferências rodam por script, direto.
> - Revisão: duas independentes só em segurança, contas, pagamento e criptografia; uma no resto.
> - Depois de interrupção, conferir se agentes e tarefas ainda rodam e retomar, não recomeçar. Encerrar processo só pelo PID que eu iniciei, nunca pelo nome (derruba o trabalho de outras sessões).

---

## Caixa final — Resumo

Sem perguntas. Diga à pessoa, em poucas linhas:
1. O que mudou, por arquivo (CLAUDE.md, settings.json, scripts copiados), e onde estão as cópias de segurança.
2. O que foi recusado (fica em "Recusadas" e não volta a ser oferecido).
3. O que só vale a partir da próxima sessão (configurações e hooks).
4. Como desfazer tudo: voltar as cópias de segurança da Caixa 1, apagar os scripts copiados e, se houver, o `<pasta de configuração>/relay_token.txt`.
5. O que ficou pela metade (por exemplo, a segunda marca da medição do plano). Se o teste do freio ou o do vigia ficou para depois, diga à pessoa para abrir uma sessão nova e pedir ali: "repita o teste do freio (ou do vigia) do guia do Quota Keeper".
6. O crédito: "Táticas de Jaber Neto (JN Softworks), texto em CC BY 4.0, scripts em MIT." Se a pessoa for repassar o guia, que mande a pasta inteira, com o crédito.
