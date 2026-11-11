# JN's Quota Keeper — detalhamento das perguntas

> Feito por Jaber Felippe Neto (JN Softworks). Licença CC BY 4.0, como o guia.

Este arquivo é o detalhe de cada pergunta do `GUIA.md`. O guia mostra o resumo; o Claude lê a seção daqui quando a pessoa pede o detalhe (e os passos do caminho B, Caixa 7, quando a pessoa aceita o token). A pessoa também pode ler direto.

## Caixa 1

Esta caixa não instala nada: guarda quatro respostas que decidem o resto. A mudança vem nos passos dela: uma cópia de segurança de `settings.json` e do `CLAUDE.md` (cada uma ao lado do original, com a data no nome) e uma seção "Quota Keeper" no `CLAUDE.md`.

### Caixa 1 · Onde gravar
- **Por dentro:** só escolhe o `CLAUDE.md` que recebe as linhas de regra: o da pasta de configuração (vale em todo projeto) ou o da pasta aberta agora. Configurações, hooks e scripts são sempre do usuário inteiro, em qualquer das duas respostas.
- **Ganha:** em "todos", as regras valem em qualquer pasta; em "só neste projeto", ficam só onde você quer.
- **Riscos:** "todos" faz cada linha ser lida em toda sessão de qualquer pasta (custo pequeno, mas fixo). "Só neste projeto" num `CLAUDE.md` compartilhado (num repositório) mostra as linhas a outras pessoas; o guia avisa antes de gravar.
- **Se não ligar:** não existe "não": sem esta resposta as regras não têm onde ficar.
- **Desfazer:** apagar a seção "Quota Keeper" do arquivo escolhido, ou pôr a cópia `CLAUDE.md.antes-quota-keeper-<data>` por cima. Vale na próxima sessão.
- **Dúvida de revisor cético:** "Mexe em arquivo meu?" Só no `CLAUDE.md` escolhido (uma seção no fim) e no `settings.json`, e só depois de uma cópia de segurança.

### Caixa 1 · Onde usa
- **Por dentro:** o app desktop tem ferramentas que o terminal não tem (abrir uma sessão nova visível, arquivar a anterior, Remote Control). A resposta decide se a Caixa 7 oferece o caminho do app, o do terminal ou os dois.
- **Ganha:** o guia não oferece o que não funcionaria no seu jeito de usar.
- **Riscos:** nenhum; só guarda a resposta.
- **Se não ligar:** "Terminal" pula as partes do app; a sessão nova passa a depender do token (caminho B) ou da regra em que o Claude só avisa. O resto do pacote funciona igual.
- **Desfazer:** nada a desfazer. Se errou, peça a pergunta de novo.

### Caixa 1 · Plano
- **Por dentro:** só planos de assinatura (Pro, Max, Ultra) têm limite semanal em %. As partes que medem a cota (`Antes/depois`, `Medir plano`) e o token de longa duração só fazem sentido neles.
- **Ganha:** nenhuma parte inútil é oferecida; com "Não sei", o guia fala no geral.
- **Riscos:** nenhum. O guia nunca supõe o plano: nem pelo que uma ferramenta mostrar; só com a sua confirmação.
- **Se não ligar:** com "Chave de API" ficam de fora as partes em % da cota; tudo o mais funciona, e o vigia de gasto avisa só em tokens.
- **Desfazer:** nada a desfazer.

### Caixa 1 · Modo
- **Por dentro:** escolhe como as outras caixas rodam. **Rápido:** uma tela com as tabelas do Grupo 1 (adotar), Grupo 2 (testar acompanhando) e Grupo 3 (avançado, não ligado agora); um ok instala o Grupo 1, uma caixa marca os hooks do Grupo 2. **Caixa por caixa:** uma caixa por tática. **Conferindo:** como o anterior, mas antes de cada gravação o Claude mostra as linhas exatas e você diz `Gravar` ou `Não gravar`.
- **Ganha:** Rápido = menos cliques; "conferindo" = você vê o que entra em cada arquivo.
- **Riscos:** no Rápido, o Grupo 1 entra com um ok: só regras no `CLAUDE.md`, dois modelos de arquivo e ajustes em `"env"` (nada aprova, bloqueia ou muda permissão). O que é sensível (permissão, aprovação automática, sessões abertas sozinhas, Remote Control, token) não é instalado nem perguntado no Rápido: fica na Caixa 7.
- **Se não ligar:** não existe "não". O modo muda só a forma de perguntar; os arquivos gravados são os mesmos para as mesmas respostas. O Rápido deixa a Caixa 7 inteira para depois, e isso é de propósito.
- **Desfazer:** ver "Riscos gerais e como desfazer tudo" no guia: voltar as cópias de segurança, ou apagar a seção do `CLAUDE.md`, as linhas do `settings.json` e os arquivos copiados.
- **Dúvida de revisor cético:** "O Rápido não instala coisa demais sem eu ver?" Ele mostra o pacote antes (tabelas com risco e como desfazer) e só instala depois do seu ok; você pode escolher "Ver caixa por caixa" ou "Cancelar".

## Caixa 2

Três ajustes no `settings.json` (dentro de `"env"`) e uma regra de esforço. Nada aqui aprova ação, muda permissão ou envia dado para fora do computador. Os ajustes valem a partir da próxima sessão.

### Caixa 2 · Agentes
- **Por dentro:** `CLAUDE_CODE_SUBAGENT_MODEL` = `sonnet` faz todo agente nascer em Sonnet. Quando precisar, o Claude pede Opus ou Haiku para um agente específico (em versões antigas do Claude Code o ajuste vencia esse pedido: se o modelo não mudar, rode `claude update`).
- **Ganha:** agente em Sonnet custa menos que em Opus (é o modelo do meio entre o Haiku e o Opus). O guia não promete um percentual de economia: depende de quantos agentes você usa.
- **Riscos:** o Sonnet erra mais que o Opus em tarefa difícil (código delicado, contas, segurança); por isso o Claude pede Opus nesses casos. Não aprova nada e nada sai do PC por causa disso.
- **Se não ligar:** os agentes usam o modelo da conversa. Tudo funciona; se a conversa for em Opus, os agentes custam mais.
- **Desfazer:** apagar a linha `"CLAUDE_CODE_SUBAGENT_MODEL"` em `"env"` do `settings.json` (ou voltar a cópia da Caixa 1). Vale na próxima sessão.
- **Dúvida de revisor cético:** "Pode gastar mais?" Só se você mandar muitos agentes que antes nem existiriam; o modelo mais barato por si não encarece.

### Caixa 2 · Espera longa
- **Por dentro:** `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` = `1h` guarda a conversa dos agentes por 1 hora em vez de 5 minutos. O cache é a conversa guardada para ser relida mais barato; passado o prazo, guardar de novo custa de novo.
- **Ganha:** agente que espera mais de 5 minutos (compilação, teste, download, renderização) não regrava a conversa inteira na volta. No PC do autor essas regravações eram ~26% de todo o gasto em 8 dias (medido set-nov/2026; pode variar no seu uso).
- **Riscos:** gravar no cache de 1 hora custa 2 vezes (em vez de 1,25). Se seus agentes quase nunca esperam mais de 5 minutos, você paga mais, sem ganho. Por isso a pergunta é feita antes e a opção "Sim" só vale para quem usa agentes que esperam.
- **Se não ligar:** fica o cache de 5 minutos. Tudo funciona; esperas longas custam a conversa inteira de novo.
- **Desfazer:** apagar a linha `"CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL"` em `"env"`. Vale na próxima sessão.
- **Dúvida de revisor cético:** "Vale se eu uso pouco agente?" Não: pule (a pergunta só é feita a quem usa agentes).

### Caixa 2 · Compactar
- **Por dentro:** `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` = `50` (ou `25`) diz quando o Claude Code troca a conversa por um resumo automático: ao chegar a essa fração do espaço, em vez de perto do fim. Os números supõem a janela de 1 milhão de tokens; com 200 mil a pergunta nem é feita.
- **Ganha:** passos não ficam caros porque a conversa já está curta quando seria grande demais. Sem número medido aqui: depende de como você trabalha.
- **Riscos:** o resumo automático perde detalhe da conversa (mais em 25% que em 50%). Quem faz produção longa numa sessão só deve pensar nisso.
- **Se não ligar:** fica o padrão, perto do fim do espaço; os passos antes do resumo custam mais; nada quebra.
- **Desfazer:** apagar a linha em `"env"`. Vale na próxima sessão.

### Caixa 2 · Esforço
- **Por dentro:** só grava uma linha de texto no `CLAUDE.md`: recomendar esforço Alto, Máximo só para problema muito difícil (de preferência num agente), e nunca abrir modo de frota de agentes sem você pedir. O esforço em si é seu, no seletor do app ou do terminal.
- **Ganha:** o Claude deixa de sugerir esforços e modos mais caros sem necessidade.
- **Riscos:** quase nenhum; não muda nenhuma configuração.
- **Se não ligar:** o Claude pode sugerir esforço ou modos mais caros; você decide sempre.
- **Desfazer:** apagar a linha no `CLAUDE.md` (seção Quota Keeper).

## Caixa 3

Só regras de texto no `CLAUDE.md`: nenhum script e nenhuma permissão. O `CLAUDE.md` e o índice da memória entram em toda sessão antes da primeira mensagem e são relidos a cada passo, então cada linha deles é paga muitas vezes por dia.

### Caixa 3 · CLAUDE.md
- **Por dentro:** a regra manda manter o arquivo com regras e ponteiros; explicação e detalhe vão para outro arquivo, citado numa linha. Com "Sim, e sugerir cortes", o Claude mede o arquivo; se passar de ~200 linhas ou ~10 KB, propõe uma lista de blocos para mover (cada um com a linha-ponteiro que fica no lugar) e só move com o seu sim.
- **Ganha:** menos texto pago em toda sessão. Sem percentual prometido: depende do tamanho do seu arquivo.
- **Riscos:** o detalhe movido pode passar despercebido se o Claude não abrir o outro arquivo; por isso fica um ponteiro e nada move sem sim. A cópia da Caixa 1 guarda o `CLAUDE.md` antes de mexer.
- **Se não ligar:** o arquivo continua como está, pode crescer e custar mais em toda sessão. Nada quebra.
- **Desfazer:** apagar a linha da regra; devolver ao `CLAUDE.md` o trecho que foi movido (o ponteiro diz onde está), ou voltar a cópia de segurança. Vale na próxima sessão.

### Caixa 3 · Memória
- **Por dentro:** a memória automática tem um índice (`MEMORY.md`) lido em toda sessão, só até a linha 200. A regra pede uma linha curta por ficha e, em projeto com muitas fichas, uma ficha-resumo onde as novas entram. Com "Sim", o Claude mostra quantas linhas e KB o índice tem e propõe encurtar linhas com mais de ~150 caracteres, só com o seu sim.
- **Ganha:** linha curta cabe mais e custa menos; nada fica cortado depois da linha 200.
- **Riscos:** encurtar uma linha pode apagar um detalhe útil. A cópia de segurança da Caixa 1 NÃO guarda a memória (só `settings.json` e `CLAUDE.md`): se a memória importa, peça uma cópia antes.
- **Se não ligar:** índice longo é cortado depois da linha 200 e custa em toda sessão; nada quebra. Com "Não uso memória" a parte é pulada.
- **Desfazer:** apagar a linha da regra; devolver o texto original (da cópia que você pediu).

### Caixa 3 · Conversa
- **Por dentro:** regra: entre uma ferramenta e outra, só uma linha do que está sendo feito; respostas, resultados e avisos vêm juntos na mensagem final. Escrever custa 5 vezes mais que ler, e tudo que se escreve fica na conversa e é relido depois.
- **Ganha:** a conversa cresce mais devagar.
- **Riscos:** você acompanha menos o que o Claude faz no meio do trabalho, e um aviso só chega no fim. Para trabalho em que você quer ver cada passo, responda "Não".
- **Se não ligar:** mais detalhe no caminho; a conversa custa mais.
- **Desfazer:** apagar a linha da regra.

### Caixa 3 · Texto longo
- **Por dentro:** regra: texto ou log longo vai para um arquivo da pasta (você salva e diz o nome) em vez de colado no chat; o Claude lê só o trecho necessário.
- **Ganha:** texto colado fica na conversa para sempre e é relido a cada passo; no arquivo, só entra o que for lido.
- **Riscos:** um passo a mais para você (salvar o arquivo). Nada sai do computador por causa disso.
- **Se não ligar:** colar no chat segue cômodo, mas custa em cada passo seguinte.
- **Desfazer:** apagar a linha da regra.

## Caixa 4

Só regras de texto no `CLAUDE.md` sobre como ler: nenhum script e nenhuma permissão. Tudo que o Claude lê fica na conversa e é relido em cada passo seguinte. Exemplo (conta pela régua do guia, não é preço oficial): um arquivo de 50 mil tokens lido no começo pesa ~5 mil em cada passo depois; em 100 passos, ~560 mil. Lido por um agente, ele nunca entra na conversa principal.

### Caixa 4 · Leitura
Uma pergunta com quatro hábitos; marque os que quiser (cada um vira uma linha de regra; os não marcados vão para "Recusadas").
- **Buscar em vez de ler:** procurar o nome ou o título e ler só ~50 linhas em volta; nunca ler inteiro documento grande, log ou arquivo gerado. Risco: perder o que ficou fora do trecho.
- **Leitura grande para agente:** um agente lê e devolve só o resumo (Haiku para achar e filtrar; Sonnet para entender). Risco: o resumo omitir algo; o agente em si custa uma conversa nova.
- **Extrair uma vez:** quando várias tarefas usam a mesma fonte grande, um agente escreve uma nota curta e as próximas leem a nota. Risco: a nota ficar velha se a fonte mudar.
- **Log filtrado na fonte:** marcar as linhas do próprio log e buscar só a marca. Risco: erro sem marca não aparece.
- **Ganha:** conversa menor, passos mais baratos. Sem percentual prometido: depende do que você lê.
- **Se não marcar nenhum:** tudo continua lido inteiro e custa mais em cada passo; nada quebra.
- **Desfazer:** apagar a linha do hábito no `CLAUDE.md` (seção Quota Keeper). Vale na próxima sessão.
- **Dúvida de revisor cético:** "O Claude vai deixar de ver coisa importante?" Pode, nos hábitos de buscar e de resumo; por isso a regra manda ler inteiro só o que vai ser editado, e o guia nunca economiza em ler o trecho exato de código antes de mudá-lo.

## Caixa 5

Vale para toda a caixa: as perguntas 1 a 3 só gravam texto no CLAUDE.md (orientam o Claude, não bloqueiam nada). As perguntas 4 e 5 instalam scripts Python que o Claude Code roda antes de cada uso de ferramenta. Esses scripts só podem NEGAR uma ação; nunca aprovam nada e não pulam nenhum pedido de permissão. Se o script falhar por erro dele, deixa tudo passar (a proteção some, nada trava). Se o Python não existir ou o caminho estiver errado, o Claude Code mostra o erro do hook e segue (no Windows, o comando pode ser `py` em vez de `python`; confira no terminal). Nenhum script usa a rede. Os dois leem arquivos internos do Claude Code (a lista de agentes da conversa), que podem mudar numa atualização: nesse caso deixam de proteger, sem bloquear nada por engano.

### Caixa 5 · Agente curto

- **Por dentro:** uma regra no CLAUDE.md manda o pedido de todo agente que edita ou corrige dizer "ao chegar a ~100 chamadas, feche o item, grave o ponto de retomada num arquivo e devolva o resumo". Se sobrar trabalho, a conversa principal abre outro agente a partir desse arquivo.
- **O que ganha:** o agente relê a própria conversa a cada passo, então fica caro se trabalhar muito. No uso do autor, agentes de 100 ou mais chamadas foram 74% do gasto dos agentes, e 71% desse gasto veio de passos com a conversa do agente acima de 200 mil tokens (medido no PC do autor, set-nov/2026; pode variar no seu uso).
- **Riscos:** (1) um agente interrompido pode deixar a tarefa pela metade; (2) abrir o seguinte custa mais uma releitura do arquivo de retomada; (3) o trabalho fica dividido em mais agentes. Tudo pequeno e visível: nada é apagado, o ponto de retomada fica num arquivo.
- **Se não ligar:** agentes seguem sem limite de tamanho. A linha extra "[Só com cache de 1 hora]" (espera máxima de ~50 min) e o "Opus coordena" da pergunta Modelos (pedaços de ~80 chamadas) foram pensados para este limite e perdem a base; o resto do pacote funciona igual.
- **Desfazer:** apague do CLAUDE.md as linhas desta caixa. Vale na próxima sessão.
- **Revisor cético:** "isso muda permissão?" Não, é só texto. "Gasta mais?" Pode gastar um pouco mais em releituras do arquivo de retomada; o objetivo é evitar o agente longo, que é mais caro.

### Caixa 5 · Modelos

- **Por dentro:** "Por papel" grava uma regra: Sonnet por padrão; Haiku para o mecânico (achar arquivo, filtrar log, contar); Opus só para agente que edita código delicado (segurança, contas, dinheiro, criptografia). "Experimental: Opus coordena" acrescenta que, em código novo ou correção fora de segurança, contas e criptografia, um agente Opus escreve o pedido de cada pedaço e abre agentes Sonnet um de cada vez (~80 chamadas cada; o Sonnet não abre agentes), roda os testes por script, revisa só o que mudou e conserta; pedaço que falhar duas vezes, o Opus faz. Cada caso é anotado em `~/Documents/piloto_opus_sonnet.md` e, depois de ~6, o Claude pergunta se vira padrão.
- **O que ganha:** o trabalho mecânico sai num modelo mais barato. Não há número de economia para "Por papel" neste guia; para "Opus coordena" ainda não há economia comprovada: está em teste no PC do autor.
- **Riscos:** (1) o modelo mais barato erra mais em tarefa que parecia simples; (2) "Opus coordena" gasta mais etapas e mais agentes, e pode custar mais que fazer direto; (3) o arquivo do piloto fica em `~/Documents`, fora da pasta de configuração, em texto simples.
- **Se não ligar ("Não mudar"):** você escolhe o modelo de cada agente na mão. Nada mais deixa de funcionar. Sem o freio (pergunta Freio), o "Opus coordena" fica segurado só pela regra de texto de que o Sonnet não abre agentes.
- **Desfazer:** apague a linha do CLAUDE.md; apague `~/Documents/piloto_opus_sonnet.md` se quiser.
- **Revisor cético:** "isso contorna alguma permissão?" Não; só orienta qual modelo usar.

### Caixa 5 · Lote

- **Por dentro:** regra no CLAUDE.md: um agente por tarefa (não um por pedacinho); vários ao mesmo tempo saem na MESMA mensagem; cada um grava o detalhe num arquivo e devolve 5 a 10 linhas.
- **O que ganha:** menos agentes abertos e respostas curtas, que a conversa principal relê a cada passo.
- **Riscos:** a resposta curta esconde detalhe; ele está no arquivo, mas é preciso abri-lo. Vários agentes ao mesmo tempo gastam em paralelo.
- **Se não ligar:** agentes devolvem respostas longas e podem ser abertos em pedaços pequenos. Nada mais deixa de funcionar.
- **Desfazer:** apague a linha do CLAUDE.md.

### Caixa 5 · Freio

- **Por dentro:** copia `agent_limit.py` para a pasta `hooks/` e o registra em `"PreToolUse"` com `matcher` `Agent|Task` (os dois nomes porque versões antigas chamavam a ferramenta de `Task`). Antes de cada abertura de agente, o script nega se quem abre já é um agente de nível 2 ou mais, ou se já tem 6 filhos.
- **O que ganha:** impede cadeia sem fim de agentes abrindo agentes.
- **Riscos:** (1) pode negar um agente que você queria; a mensagem "Agent limit: ..." diz o motivo; (2) se o Claude Code mudar o arquivo interno que o script lê, o freio para de frear; (3) só NEGA, nunca aprova: nenhum pedido de permissão é pulado.
- **Se não ligar:** cadeias sem limite continuam possíveis. O "Opus coordena" fica segurado só pela regra de texto.
- **Desfazer:** apague do `settings.json` a entrada que chama `agent_limit.py` em `"PreToolUse"` (ou volte a cópia de segurança da Caixa 1) e apague o arquivo em `hooks/`. Vale na próxima sessão.
- **Revisor cético:** "e se o Python não existir?" O Claude Code mostra o erro do hook e segue; o trabalho não trava.

### Caixa 5 · Trava

- **Por dentro:** copia `copy_lock.py` para `hooks/` e o registra em `"PreToolUse"` (matcher `Bash|PowerShell|Edit|Write|NotebookEdit|MultiEdit|Agent|Task`) e em `"SubagentStop"`. Quando um agente escreve numa cópia de trabalho (pasta com `.git`, `.p4config` ou um `.uproject`), a sessão dele fica com essa pasta. Outra sessão não pode escrever, rodar comando que escreve nem lançar agente ali até esses agentes terminarem. Ler, e editar notas `.md` e `.txt`, sempre passam. Só agentes pegam a trava (as edições da própria conversa principal não), e agentes da mesma sessão a dividem.
- **O que ganha:** duas sessões não escrevem na mesma pasta ao mesmo tempo, por exemplo depois de uma troca de sessão com um agente ainda rodando.
- **Riscos:** (1) uma trava presa por engano bloqueia a outra sessão de escrever naquela pasta; (2) o script grava arquivos pequenos em `<pasta de configuração>/locks` e um registro em `<pasta de configuração>/hooks/copy_lock.log`; (3) só NEGA, nunca aprova. A trava some quando o último agente daquela sessão devolve sem nada em segundo plano, quando a sessão dona é fechada ou arquivada, ou após 2 horas sem sinal.
- **Se não ligar:** duas sessões podem mexer na mesma pasta e se atrapalhar. A troca de sessão com agente rodando (Caixa 7) passa a conferir a passagem em vez da trava.
- **Desfazer:** apague do `settings.json` as entradas de `copy_lock.py` em `"PreToolUse"` e `"SubagentStop"` (ou volte a cópia de segurança da Caixa 1) e apague o arquivo em `hooks/`. Trava presa agora: `python <pasta de configuração>/hooks/copy_lock.py release <pasta>`. Ver as travas: `... copy_lock.py list`.
- **Revisor cético:** "o que ela bloqueia?" Só escrita, comando que escreve e abrir agente, numa pasta que agente de OUTRA sessão está usando. O resto passa.

## Caixa 6

Vale para toda a caixa: os números (trocar em ~250 mil) supõem a janela de 1 milhão de tokens; com a de 200 mil, a troca é em ~100 mil. Os arquivos de passagem e de resumos ficam na pasta do projeto, em texto simples; nada sai do computador por causa deles.

### Caixa 6 · Passagem

- **Por dentro:** na primeira tarefa de várias etapas de um projeto, o Claude cria sozinho `PASSAGEM.md` (o que foi feito, o que está pela metade, o próximo passo exato) e, no "Sim, passagem + resumos", também `RESUMOS.md` (uma entrada por sessão: Fez / Decidiu / Ficou), a partir de modelos copiados para `<pasta de configuração>/modelos`. Se o projeto já tiver um arquivo assim, usa o dele. Anota os passos ao fechar cada parte e, em toda troca de sessão e fim de etapa, acrescenta uma entrada nos resumos.
- **O que ganha:** foi a maior economia do autor: a conversa principal caiu 75% depois desta regra (medido no PC do autor, set-nov/2026; pode variar no seu uso). O resumo automático (compactação) perde detalhe; o arquivo não. Os resumos servem para achar depois em qual sessão algo foi feito.
- **Riscos:** (1) aparecem arquivos novos nos projetos sem perguntar a cada vez (num repositório, em `git status`; para não versionar, use o `.gitignore`); (2) se a pasta for publicada (repositório, nuvem), a passagem vai junto: não escreva senha, token ou dado pessoal nela; (3) uma passagem velha ou errada faz a sessão nova partir do ponto errado: o Claude confere o "próximo passo" antes de agir e pede confirmação em ação irreversível, mas olhe o arquivo se a sessão nova parecer perdida; (4) trocar de sessão custa uma releitura da passagem e perde o que só estava na conversa.
- **Se não ligar:** a sessão nova começa sem arquivo de passagem e perde o que só estava na conversa. As perguntas Troca e Lembrete e toda a Caixa 7 (sucessora automática) perdem o sentido e são puladas. "Só a passagem" mantém a passagem, mas sem arquivo de resumos.
- **Desfazer:** apague do CLAUDE.md as linhas desta caixa (vale na próxima sessão). Os arquivos já criados ficam; apague à mão se quiser.
- **Revisor cético:** "o Claude escreve em disco sozinho?" Sim, só esses dois arquivos de texto, dentro do projeto. Os pedidos de permissão do Claude Code continuam valendo.

### Caixa 6 · Troca

- **Por dentro:** regra no CLAUDE.md: com a conversa no número escolhido (~200, ~250 ou ~300 mil tokens) ou numa etapa nova, o Claude fecha a parte em andamento, atualiza a passagem e troca de sessão. Sem regra de sucessora, diz à pessoa em uma linha o que colar na sessão nova. "Só quando eu pedir" só avisa em uma linha.
- **O que ganha:** cada passo relê menos. Na conta do autor (260 sessões), entre 200 e 300 mil o custo total quase não muda, e acima de ~300 mil cada passo relê tanto que sai mais caro (medido no PC do autor, set-nov/2026; pode variar no seu uso).
- **Riscos:** (1) cada troca perde um pouco do que a conversa sabia; (2) trocar tarde sai mais caro; (3) a sessão nova relê a passagem (pequeno perto de seguir numa conversa enorme).
- **Se não ligar ("Só quando eu pedir"):** nada troca sozinho; a conversa pode ficar cara se você esquecer. A sucessora automática (Caixa 7) fica sem gatilho.
- **Desfazer:** apague a linha do CLAUDE.md.

### Caixa 6 · Uma tarefa

- **Por dentro:** regra: assunto novo e sem ligação com o que está aberto vai para sessão nova (ou `/clear`, que só a pessoa pode digitar).
- **O que ganha:** conversas curtas e focadas, que custam menos por passo.
- **Riscos:** mais sessões abertas para você acompanhar.
- **Se não ligar:** assuntos diferentes se acumulam na mesma conversa, que fica grande e cara. Nada mais deixa de funcionar.
- **Desfazer:** apague a linha do CLAUDE.md.

### Caixa 6 · Lembrete

- **Por dentro:** copia `handoff_reminder.py` para `hooks/` e o registra em `"SessionStart"` (matcher `startup`). Se a pasta aberta tiver um `PASSAGEM*.md` ou `HANDOFF*.md`, o script mostra ao Claude uma linha mandando ler o arquivo primeiro. Só lista a pasta: não lê arquivo, não escreve, não usa a rede, não aprova nem bloqueia nada.
- **O que ganha:** o Claude não esquece de ler a passagem ao abrir a pasta.
- **Riscos:** custa uma linha a mais no começo de cada sessão nessas pastas. Se o script falhar ou o Python não existir, o Claude Code mostra o erro e a sessão segue normal.
- **Se não ligar:** a regra do CLAUDE.md já manda ler a passagem, mas sem o lembrete o Claude pode esquecer. Nada mais deixa de funcionar.
- **Desfazer:** apague do `settings.json` a entrada de `"SessionStart"` que chama `handoff_reminder.py` (ou volte a cópia de segurança da Caixa 1) e o arquivo em `hooks/`. Se houver outro item em `"SessionStart"` (como o relatório diário da Caixa 8), apague só este. Vale na próxima sessão.
- **Revisor cético:** "e se o Python não existir?" O Claude Code mostra o erro e segue. Confira com `handoff_reminder.py --test` (a última linha tem que ser `ALL OK`).

## Caixa 7

(Detalhamento das perguntas da Caixa 7. O resumo de cada uma está no guia; aqui está o que faz por dentro, o que se ganha, cada risco, o que continua funcionando sem ela e como desfazer.)

### Caixa 7 · Visão geral e como desfazer tudo

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

### Caixa 7 · Dúvidas de um revisor cético

**Dúvidas que um revisor cético faria, com resposta direta:**
- **O `spare_allow.py` contorna as permissões?** Ele passa por cima de uma coisa só: o pedido de aprovação (e o filtro do modo automático) para seis ferramentas, e apenas quando o alvo é um id listado em `spares.txt`: `SendMessage` (mensagem para a sessão) e, no app, desarquivar, mudar título, mudar modelo, mudar esforço e ligar ou desligar o Remote Control. Ele não lê o texto da mensagem. Todo o resto segue o fluxo normal e continua pedindo aprovação ou passando pelo filtro: abrir sessão (`start_session`), arquivar, soltar, apagar, parar, mudar o modo de permissão de outra sessão e qualquer ação em sessão que não esteja na lista. Regras de negar, pelo que a documentação do Claude Code diz, continuam valendo (o autor não testou). Duas ressalvas: uma mensagem a um estepe é uma ordem a outra sessão, que depois age com as permissões dela; e, se o id ficar em `spares.txt` depois que o estepe virou sessão de trabalho, aquelas seis ações seguem aprovadas nela (o Claude tira o id depois de usar o estepe; confira o arquivo de vez em quando). Cada decisão vai para `hooks/spare_allow.log` (hora, ferramenta e id, sem o texto das mensagens; o arquivo não é limpo sozinho).
- **O que acontece se o hook falhar (Python ausente, erro, passar dos 10 s)?** Nada é aprovado: pela documentação do Claude Code, um hook que falha não bloqueia nem aprova, e a ação segue o fluxo normal (pede aprovação ou cai no filtro). Perde-se só a comodidade: o estepe pode ser barrado e a troca cai no "Avisar e seguir". O autor não testou apagando o Python.
- **O modo automático (`"defaultMode": "auto"`) deixa o Claude agir sem perguntar em quê?** Em vez de pedir seu ok a cada ação, um filtro julga cada uma: deixa passar o que parece seguro e rotineiro (ler e editar arquivos do projeto, comandos comuns) e barra o que parece arriscado ou fora do que você pediu. Ele pode errar nos dois lados. Não é o modo que ignora todas as permissões (o guia não usa esse), e as regras de negar continuam valendo. Vale para toda sessão nova que a pessoa abrir, em qualquer projeto.
- **Token em arquivo: quem lê, como apagar e revogar?** O arquivo `relay_token.txt` fica na pasta de configuração. No Windows o guia deixa só o usuário da pessoa com acesso; no Mac e no Linux, só o dono (modo 600). Mesmo assim, qualquer programa que rode como a pessoa, administradores do computador e cópias de segurança ou nuvem que levem a pasta conseguem ler. O Claude não lê (regra de negar a leitura, que vale para a ferramenta de leitura, mas não é garantia contra um comando de terminal). Apagar: apague o arquivo. Revogar: a documentação oficial (conferida em novembro de 2026) não mostra como revogar só esse token; olhe a lista de acessos e sessões nas configurações da conta em claude.ai ou fale com o suporte da Anthropic. O token vale por um ano.
- **Isso pode gastar mais?** Pode. Cada sessão nova (sucessora, estepe, tarefa agendada) começa com a conversa vazia, mas recarrega instruções e memória e lê a passagem, e o primeiro uso dela não aproveita o que a anterior já tinha guardado em cache. Em troca, evita o custo de seguir numa conversa muito grande. "Avisar e seguir" e a conversa que passa do limite sem resposta custam o contrário: cada passo numa conversa grande gasta mais. As rodadas sem tela gastam da mesma cota. Sem número do autor para a soma.
- **Dados saem do computador?** Os scripts do pacote não fazem chamada de rede. O que roda no Claude (inclusive as rodadas sem tela, que chamam o comando `claude`) manda a conversa à Anthropic, como todo uso do Claude. O Remote Control mostra a conversa na conta claude.ai da pessoa e nos aparelhos dela.

### Caixa 7 · Travas do app

O que o autor encontrou ao testar (novembro de 2026). As regras do guia já tratam cada uma; isto explica o porquê.

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

### Caixa 7 · Sucessora

**O que faz por dentro:** Na hora da troca (regra da Caixa 6), o Claude grava a passagem e chama `start_session` com o pedido "Leia e siga <passagem>. Sessão anterior: <id>" mais as regras desta seção (herança); a sessão nova lê a passagem e faz o "próximo passo exato". Com a primeira opção o Claude grava também a regra "Troca com agente rodando".

**O que se ganha:** A etapa não para esperando você: o autor teve uma etapa parada a noite inteira esperando um clique (relato do autor, sem número).

**Riscos reais:** a sessão nova nasce sem você olhar e pode ficar escondida (ver "Rotinas" nas travas); cada sessão nova recarrega as instruções e lê a passagem de novo, o que pode gastar mais cota que seguir numa conversa só; a cadeia só para quando a passagem diz que a etapa acabou ou tem pergunta para você. Com a primeira opção o Claude grava também a regra "Troca com agente rodando".

**Se não ligar (o que funciona e o que não):** "O Claude propõe, eu clico" e "Eu abro" funcionam: nada abre sozinho, o trabalho espera por você. Em ambos as perguntas 2 e 5 a 10 não fazem sentido e são puladas. Passagem, resumos, troca de sessão e vigia continuam como estão.

**O que protege o contexto na sucessão:** a passagem e os resumos (Caixa 6) guardam o que foi feito e o próximo passo; o pedido inicial da sucessora manda ler a passagem e repete as regras; a passagem é atualizada antes de abrir a nova. **O risco que sobra:** passagem mal feita (a nova parte do ponto errado; o que só estava na conversa se perde) e arquivar algo ainda vivo, que a regra já não força quando há agente ou tarefa em segundo plano.

**Como desfazer:** apague do `CLAUDE.md` as linhas "Sucessora:", "Troca com agente rodando:" e "Herança"; arquive pela barra lateral as sessões que ele abriu. Vale na próxima sessão.

### Caixa 7 · Fechar mãe

**O que faz por dentro:** A sucessora, logo no começo, se solta da sessão que a abriu, desliga o Remote Control dela e a arquiva pelo id que vem no pedido. O título ganha um número ("Site" → "Site 2").

**O que se ganha:** Cada fim de turno da nova acordaria a anterior, que releria a conversa inteira; arquivada, ela não gasta nada.

**Riscos reais:** arquivar não apaga a conversa (ela some da lista normal e volta pela lista de arquivadas); se o Claude errasse o id, arquivaria a sessão errada, por isso o id vem no pedido ("Sessão anterior: <id>") e a regra não vale para sessão paralela de outra tarefa. A sucessora também desliga o Remote Control da anterior e se solta dela. Na regra "Troca com agente rodando", a sessão anterior se arquiva sozinha quando o último agente dela devolve.

**Se não ligar (o que funciona e o que não):** As duas sessões ficam abertas e a anterior pode reler a conversa inteira a cada turno da nova (gasta cota) até você arquivá-la. O resto da caixa funciona. Na regra "Troca com agente rodando", tire o trecho em que a anterior se arquiva sozinha.

**Como desfazer:** apague do `CLAUDE.md` a linha "Fechar a anterior:"; para trazer uma sessão de volta, desarquive pela lista de arquivadas.

### Caixa 7 · Token

**O que faz por dentro:** Você gera o token com `claude setup-token` numa janela de terminal do sistema e o grava num arquivo (passos no caminho B); o script `session_relay.py` lê o arquivo e o entrega só às rodadas do `claude -p`. O Claude nunca vê o token.

**O que se ganha:** A cadeia anda sozinha no terminal, sem tela e sem app, com conversa vazia a cada rodada.

**Riscos reais:** o token é uma chave de acesso à conta Claude da pessoa, válida por um ano: quem o tiver gasta a cota dela. Fica em `<pasta de configuração>/relay_token.txt`; o guia restringe o arquivo ao usuário dela, mas qualquer programa que rode como ela, administradores e cópias de segurança ou nuvem que levem a pasta podem lê-lo. O Claude nunca vê o token. As rodadas rodam sem ninguém olhar e gastam a mesma cota.

**Se não ligar (o que funciona e o que não):** **Funciona sem ele:** o caminho A no app (se houver `start_session`), a regra "[Eu abro]" (o Claude atualiza a passagem e avisa você), estepes, "Avisar e seguir" e a tarefa agendada. **Deixa de funcionar:** no terminal, a cadeia de sessões não anda sozinha; e a reserva "rodadas sem tela" some do caminho A (ela cai em um aviso a você). Passagem, resumos, troca, vigia e o resto do pacote não dependem do token.

**Por que arquivo, e não variável do sistema** (`setx` no Windows, `export` no perfil do terminal): o token passaria a valer para todo `claude` aberto nessa conta do computador, e o login normal (`/login`) deixaria de valer até a variável ser removida. No arquivo, ele é lido só pelo script e entregue só às rodadas.

**Como desfazer:** apague `relay_token.txt`, `tools/session_relay.py` e a regra "Rodadas sem tela:"; tire do `settings.json` a linha `Read(.../relay_token.txt)` (opcional). Para revogar, ver "Token em arquivo" acima e o fim do caminho B.

### Caixa 7 · Permissões

**O que faz por dentro:** Define o `--tools` do script: a lista de ferramentas que uma rodada escondida pode usar. Nada fora da lista roda; ninguém é perguntado.

**O que se ganha:** Limita o estrago possível de uma rodada que ninguém está vendo.

**Riscos reais:** nenhuma rodada pede aprovação: o que está na lista passa direto e o resto é recusado. Mesmo só com arquivos, uma rodada errada pode editar ou sobrescrever arquivos do projeto sem você ver (use git ou uma cópia).

**Se não ligar (o que funciona e o que não):** Sem o token a pergunta nem existe. Com o token, a lista é obrigatória; "Só arquivos" é a menor.

**Como desfazer:** 

### Caixa 7 · Agendada

**O que faz por dentro:** Acrescenta duas regras de permitir em `settings.json`: criar e rodar tarefa agendada. A tarefa é a reserva visível para quando o app recusa abrir a sessão; ela é criada só na primeira troca em que estepe e "Avisar e seguir" não bastarem.

**O que se ganha:** Uma sucessora aberta com um comando só, em poucos segundos, mesmo num turno automático (testado em 04/11/2026 no PC do autor).

**Riscos reais:** acrescenta duas regras em `"permissions"` → `"allow"` do `settings.json`: criar e rodar tarefa agendada sem pedir aprovação. Elas valem para TODAS as sessões e projetos, não só para a sucessora; uma sessão induzida por texto malicioso (numa página ou arquivo) poderia agendar algo que roda depois, sem ninguém olhando, no modo de permissão padrão e sob as regras de negar. A tarefa só é criada na primeira troca em que estepe e "Avisar e seguir" não bastarem.

**Se não ligar (o que funciona e o que não):** A reserva passa a ser as rodadas sem tela (se instaladas) ou um aviso a você; a pergunta 9 (modo automático padrão) é pulada, porque só serve à tarefa. As regras de permitir valem para todas as sessões da conta.

**Como desfazer:** tire de `"allow"` as linhas `"mcp__scheduled-tasks__create_scheduled_task"` e `"mcp__scheduled-tasks__run_scheduled_task"`; apague a tarefa `sucessora-<pasta>` (ver "Como desfazer" no topo da caixa). Vale na próxima sessão.

### Caixa 7 · Recusa

**O que faz por dentro:** Escolhe o que o Claude faz quando o app recusa abrir a sessão nova (turno que não veio de mensagem sua): usar estepes, avisar e seguir ou ir direto à reserva.

**O que se ganha:** A troca não fica presa quando o app recusa.

**Riscos reais:** "Sessão de estepe" cria sessões reservas sem você ver (ver a pergunta 7) e depois as arquiva e reativa; "Avisar e seguir" deixa a conversa crescer até sua próxima mensagem, e cada passo numa conversa grande gasta mais cota; "Reserva na hora" pode deixar a sucessora escondida em Rotinas.

**Se não ligar (o que funciona e o que não):** Não existe "não" aqui: a mínima é "Avisar e seguir", que não cria sessão nenhuma antes da sua mensagem. Sem "Sessão de estepe", as perguntas 7 e 10 são puladas.

**Como desfazer:** apague do `CLAUDE.md` as linhas "Estepes:" e "Avisar e seguir:"; apague os estepes (ver "Como desfazer" no topo da caixa).

### Caixa 7 · Estepes

**O que faz por dentro:** Estepes são sessões vazias, arquivadas, que o Claude desarquiva, renomeia e usa na troca. A regra confere a pasta a cada mensagem sua e repõe os usados até o número escolhido.

**O que se ganha:** Troca sem você na tela, na lista normal de sessões (a tarefa agendada fica escondida em Rotinas).

**Riscos reais:** o Claude cria até esse número de sessões vazias na pasta, sem você ver, e repõe as usadas a cada mensagem sua. Cada uma gasta um turno curto ao nascer (recarrega as instruções e responde "pronta"); arquivada, não gasta nada. Elas ocupam a lista de arquivadas. O autor não tem número medido para o gasto total.

**Se não ligar (o que funciona e o que não):** Com menos estepes (6), uma noite com muitas trocas na mesma pasta pode acabá-los; aí cai em "Avisar e seguir". O gasto: um turno curto por estepe ao nascer.

**Como desfazer:** 

### Caixa 7 · Remote

**O que faz por dentro:** Liga o Remote Control: a sessão fica acessível pela conta claude.ai da pessoa, no celular ou no navegador. A regra liga nas sucessoras; "Ligar já" liga também nesta sessão. Antes de ligar ou desligar, o Claude vê o estado com `get_session` (chamar à toa pode abrir caixa de aprovação ou desligar o que você queria ligado).

**O que se ganha:** Acompanhar e mandar mensagem de longe; é o que faz o aviso chegar no celular.

**Riscos reais:** quem entrar na conta dela no claude.ai, ou pegar o celular desbloqueado, pode mandar ordens para a sessão, que roda no computador dela com as permissões da sessão (arquivos e comandos); por isso, conta com verificação em duas etapas e celular com bloqueio. A conversa também passa a aparecer nesses outros aparelhos. E uma sessão aberta pelo Remote Control conta como "trabalho vivo": o app não deixa arquivá-la, por isso a sucessora desliga o da anterior antes de arquivar.

**Se não ligar (o que funciona e o que não):** Tudo funciona sem ele; o aviso de "Avisar e seguir" só aparece no computador. O Claude ainda desliga o Remote Control da anterior antes de arquivá-la, se estiver ligado. Se suspeitar de acesso indevido à conta: troque a senha e saia dos aparelhos conectados.

**Como desfazer:** apague a linha "Remote Control:" do `CLAUDE.md`; desligue em cada sessão (`set_remote_control` com false, ou o menu da sessão) e desligue nas configurações do app a opção que liga em toda sessão nova. Se suspeitar de acesso indevido à conta, troque a senha e saia dos aparelhos conectados, nas configurações da conta.

### Caixa 7 · Auto padrão

**O que faz por dentro:** Grava `"defaultMode": "auto"` em `"permissions"` do `settings.json` do usuário. Motivo: a tarefa agendada não herda o modo de quem a criou; sem isso a sucessora para no primeiro comando. Exige versão recente do Claude Code e um plano com o modo automático; sem isso a sessão começa no modo normal.

**O que se ganha:** A sucessora da tarefa trabalha sozinha, sem esperar você.

**Riscos reais:** vale para TODA sessão nova, em todo projeto, não só para a sucessora: em vez de você aprovar cada ação, um filtro decide (deixa passar o que parece seguro e rotineiro, barra o que parece arriscado) e pode errar nos dois lados. Não ignora as permissões, e as regras de negar valem. Exige versão recente do Claude Code e um plano com esse modo; sem isso a sessão começa no modo normal.

**Se não ligar (o que funciona e o que não):** O modo padrão fica como está. A sucessora aberta pela tarefa começa no modo normal e para no primeiro comando ou edição, esperando você aprovar. (O app diz que cada rotina guarda as aprovações dadas e as reusa nas próximas execuções; o autor não testou.)

**Como desfazer:** tire `"defaultMode": "auto"` de `"permissions"` (ou ponha o valor que a cópia de segurança da Caixa 1 mostra). Vale na próxima sessão.

### Caixa 7 · Hook estepe

**O que faz por dentro:** Copia `scripts/spare_allow.py` para `<pasta de configuração>/hooks/`, cria `spares.txt` vazio e registra um bloco em `"hooks"` → `"PreToolUse"`. O hook aprova só quando o alvo é um id listado em `spares.txt`. Registra cada decisão em `hooks/spare_allow.log` (hora, ferramenta, id; sem o texto das mensagens).

**O que se ganha:** As trocas por estepe passam sem caixa; sem ele o modo automático barrou mexer num estepe criado por outra sessão e às vezes a mensagem com a tarefa, achando que contornava a trava do `start_session` (visto em 04/11/2026). Com o hook, uma sessão fez tudo isso num estepe que não criou, sem nenhuma caixa (testado no mesmo dia). Não use regra de permitir para essas ferramentas: ela valeria para todas as sessões.

**Riscos reais:** aprova sozinho só seis ações (mensagem, desarquivar, título, modelo, esforço e Remote Control) e só em sessão cujo id esteja em `spares.txt`; não lê o texto da mensagem; se falhar, não aprova nada. Detalhes na resposta "O `spare_allow.py` contorna as permissões?" no topo da caixa. Registra tudo em `hooks/spare_allow.log`, no seu computador.

**Se não ligar (o que funciona e o que não):** Nada é aprovado sozinho. O modo automático pode barrar mexer num estepe ou a mensagem com a tarefa; a troca cai em "Avisar e seguir" ou você aprova na caixa.

**Como desfazer:** tire de `"hooks"` → `"PreToolUse"` o bloco com `matcher` `SendMessage|mcp__ccd_session_mgmt__.*` e apague `hooks/spare_allow.py`, `hooks/spare_allow.log` e `spares.txt`. Vale na próxima sessão.

### Caixa 7 · Rodadas sem tela e aviso prévio

**O que faz por dentro:** `session_relay.py` roda o `claude -p` em rodadas (cada uma com conversa vazia, lendo e atualizando a passagem) e para quando a passagem diz ETAPA CONCLUIDA, no limite de rodadas ou no tempo limite. Não aparece no app. Cada rodada é anotada em `<pasta de configuração>/quota_keeper/relay_log.jsonl` (linhas `start`, `round`, `end`, com hora, pasta, modelo, motivo e se houve aviso; o token nunca entra). Erro ao gravar esse registro é ignorado e nunca para o revezamento.

**A regra de aviso:** antes de abrir qualquer sessão escondida, o Claude avisa a pessoa em uma linha (o que vai rodar, por quê, quantas rodadas, que gasta a cota dela) e lança com `--reason "<motivo>" --notified`. Sem `--notified`, o relatório diário (Caixa 8) marca a rodada como "sem aviso registrado".

**O que se ganha:** nenhuma sessão escondida gasta cota sem você saber; e o relatório diário consegue separar rodada anunciada de sessão sem tela que ninguém anunciou.

**Se recusar as rodadas sem tela (pergunta 3, "Agora não"):** no terminal a cadeia de sessões não anda sozinha (o Claude atualiza a passagem e avisa você para abrir a nova); no app, o caminho A cobre. O resto do pacote funciona. Sem token, `session_relay.py` nem é copiado.

**Limites do script:** rodada que passa do tempo limite (`--timeout`, padrão 1 hora) é cortada e o revezamento para (tarefa longa precisa de `--timeout` maior); o script também para no limite de rodadas, mesmo que a última diga CONTINUE. Nada é aprovado sozinho: a rodada só usa as ferramentas da lista escolhida na pergunta 4; o resto é recusado, sem pergunta.

**Riscos que continuam:** a rodada gasta a mesma cota; uma rodada errada pode editar arquivos do projeto (use git); o registro só vê rodadas lançadas pelo script, não outro programa que use `claude -p` no mesmo PC.

**Como desfazer:** apague `tools/session_relay.py`, `relay_token.txt`, a regra "Rodadas sem tela:" e, em cada projeto, `relay.log`; `quota_keeper/relay_log.jsonl` pode ser apagado a qualquer hora (volta a ser criado na próxima rodada).

**Relatório diário:** quem escolher o token ou as rodadas sem tela deve ganhar a oferta do relatório diário; a pergunta é da Caixa 8. Ele mostra, entre outras coisas, sessões sem tela abertas sem aviso registrado e sessões sem tela rodando há muito tempo. Limite honesto: só vê este computador.

### Caixa 7 · Token (revogar e desligar)

- **Revogar:** a documentação oficial (conferida em novembro de 2026) não mostra como revogar só esse token. Olhe a lista de acessos e sessões nas configurações da conta em claude.ai ou fale com o suporte da Anthropic. Apagar o arquivo não revoga; o token vale por um ano. Se vazou, trate como senha vazada.
- **Desligar o caminho B:** apague `<pasta de configuração>/relay_token.txt` (sem ele o script não roda), `<pasta de configuração>/tools/session_relay.py` e, em cada projeto, `relay.log`; tire do `CLAUDE.md` a regra "Rodadas sem tela:" e, do `settings.json`, a linha `Read(.../relay_token.txt)` em `"deny"` (opcional).

### Caixa 7 · Passos do caminho B

Só se a pergunta 3 foi "Sim, me guie". Um passo por vez, esperando a pessoa dizer que fez.

**O que é o token** (diga assim): uma chave de acesso à conta Claude dela, válida por um ano, feita para scripts. Quem a tem usa a cota dela; é como uma senha.

1. **Confira o Claude Code de terminal:** `claude --version`. Se não existir, a pessoa o instala (https://code.claude.com/docs). O token funciona nos planos Pro, Max, Ultra, Team e Enterprise.
2. **A pessoa gera o token.** Você não roda este comando (ele abre o navegador e mostra o token). Ela roda, numa janela de terminal do sistema, aberta por ela fora desta conversa:

   ```text
   claude setup-token
   ```

   **Nunca** no painel de terminal do app do Claude nem no terminal do editor de código: o Claude lê esses painéis, e o token iria parar na conversa.

   Ela faz login no navegador, o terminal mostra o token, e ela o copia sem colar em lugar nenhum ainda, nem no chat.
3. **A pessoa grava o token num arquivo**, na mesma janela, com o token ainda copiado. Os comandos supõem a pasta padrão (`.claude` na pasta do usuário); se a de configuração for outra, troque o caminho (e use `--token-file` no script, se ele não achar o arquivo):
   - Windows (PowerShell):

     ```powershell
     Get-Clipboard | Out-File -NoNewline -Encoding ascii "$HOME\.claude\relay_token.txt"
     icacls "$HOME\.claude\relay_token.txt" /inheritance:r /grant:r "$($env:USERDOMAIN)\$($env:USERNAME):F"
     icacls "$HOME\.claude\relay_token.txt"
     ```

     (A segunda linha deixa só o usuário dela ler o arquivo; a terceira mostra as permissões: só o usuário dela deve aparecer.)
   - Mac e Linux: ela roda o comando, cola o token (não aparece na tela) e aperta Enter:

     ```bash
     umask 077; read -rs T; printf %s "$T" > <pasta de configuração>/relay_token.txt; unset T
     ```

   Depois ela limpa a área de transferência e fecha a janela: copia outra coisa (Windows: e apaga o item do token no histórico, Win+V, se ligado; Mac: a área de transferência universal leva o copiado a outros aparelhos Apple dela).

   Grave em arquivo, nunca em variável do sistema (`setx`, `export`); motivo: `pt/DETALHES.md`, "Caixa 7 · Token".
4. **Confira sem ver o token** (imprime só sim ou não):

   ```text
   python -c "import os, pathlib; t = (pathlib.Path(os.environ.get('CLAUDE_CONFIG_DIR') or pathlib.Path.home() / '.claude') / 'relay_token.txt').read_text(encoding='utf-8-sig').strip(); print('ok' if t.startswith('sk-ant-') and not any(c.isspace() for c in t) else 'confira o arquivo: deve ter só o token, uma linha')"
   ```

   Nunca rode `cat`, `type` ou `Get-Content` nesse arquivo, nem o abra com Read. Se a pasta de configuração estiver num repositório git ou pasta sincronizada com a nuvem, avise: o token não pode ir junto (`relay_token.txt` no `.gitignore` ou fora da sincronização).
5. **Proíba a leitura do arquivo.** No `settings.json`, em `"permissions"` → `"deny"` (crie o que faltar, não apague o que existe), acrescente `"Read(<pasta de configuração>/relay_token.txt)"`, com o caminho completo (sem `~`). Isso cobre a ferramenta de leitura, não um comando de terminal (por isso nunca `cat`). Diga que o script já passa a mesma proibição às rodadas.
6. **Copie o script:** `scripts/session_relay.py` → `<pasta de configuração>/tools/session_relay.py`.
7. **Teste num projeto de brinquedo** (com sim da pessoa; duas ou três rodadas rápidas em Haiku, um pouco de cota). A pasta fica em `~/Documents`, não na de configuração: lá as rodadas não escrevem (protegida, e rodada não pede permissão).
   1. Crie `~/Documents/relay_test/PASSAGEM.md` com:

      ```markdown
      # Passagem — teste do revezamento

      ## Próximo passo exato
      Se `contagem.txt` não existe, crie com a linha "um". Se já existe com "um", acrescente a linha "dois" e escreva ETAPA CONCLUIDA na primeira linha desta passagem.
      ```
   2. Rode (caminho completo de `tools/session_relay.py`; no Windows, barras `/`):

      ```text
      python <pasta de configuração>/tools/session_relay.py --folder ~/Documents/relay_test --handoff PASSAGEM.md --model haiku --rounds 3 --reason "teste de instalação" --notified
      ```
   3. Esperado: a rodada 1 cria "um" (STATUS: CONTINUE); a 2 acrescenta "dois" e marca ETAPA CONCLUIDA; o script para sozinho. O registro fica em `~/Documents/relay_test/relay.log`, uma linha por rodada.
   4. Erro de opção desconhecida: a pessoa atualiza o Claude Code (`claude update`) e tentam de novo. No Windows, erro de argumentos estranhos: passe `--claude "<caminho do claude.exe>"` (o `claude.cmd` estraga argumentos com parênteses e asteriscos).
8. **Grave a regra** do caminho B com as ferramentas da pergunta 4:
   - "Só arquivos": `--tools "Read,Glob,Grep,Edit,Write"` (o padrão do script).
   - "Arquivos + terminal": acrescente o nome da ferramenta de terminal da lista da pessoa (`Bash` ou `PowerShell`; não presuma pelo sistema), p. ex. `--tools "Read,Glob,Grep,Edit,Write,PowerShell"`.
   - "Decidir por projeto": a regra manda perguntar na primeira vez em cada projeto e anotar a resposta no CLAUDE.md dele.
9. **Diga à pessoa os furos** (a regra já cobre o aviso, o `relay.log` e a cota): rodada que passa do `--timeout` (padrão 1 hora) é cortada e o revezamento para (tarefa longa pede `--timeout` maior); o script para no limite de rodadas mesmo que a última diga CONTINUE; a rodada só usa as ferramentas da lista da pergunta 4. Token vazado é senha vazada: revogar e desligar o caminho B estão em `pt/DETALHES.md`, "Caixa 7 · Token (revogar e desligar)"; limites e riscos, em "Caixa 7 · Rodadas sem tela e aviso prévio".

## Caixa 8

Vale para as cinco perguntas: nenhum script desta caixa usa rede; nenhum bloqueia ou aprova ação do Claude Code (hooks que só imprimem um aviso); todos usam só a biblioteca padrão do Python. Se o Python não existir, o hook dá erro de comando não encontrado, o Claude Code mostra isso e segue o trabalho.

### Caixa 8 · Vigia

**Por dentro:** `spend_watch.py` roda a cada mensagem (`UserPromptSubmit`) e a cada ferramenta (`PostToolUse`). Lê só o que é novo no registro da sessão (`<pasta de configuração>/projects/.../*.jsonl`), soma tokens, e quando um limite é cruzado (conversa em 200 mil e a cada 100 mil a mais; 40, 80 e 150 prompts; agente em 100 e 150 chamadas) imprime uma linha "SPEND WATCH" que entra no contexto. O Claude conta à pessoa e propõe passagem, sucessora ou agente mais barato. Grava só `hooks/spend_watch_state/` (um arquivo pequeno por sessão, com o que já avisou).

**Ganha:** o aviso chega no meio do turno, não só no fim. No uso do autor, 14 de 36 trocas de sessão só aconteceram depois de 250 mil tokens, antes do vigia avisar assim (medido no PC do autor, set-nov/2026; pode variar no seu uso). Conversa grande é o que mais encarece, porque cada passo relê tudo.

**Riscos:**
- Lê os registros locais, que contêm as conversas inteiras. Só conta tokens, modelo e hora; não copia conteúdo e nada sai do computador.
- Se o formato dos registros mudar numa atualização do Claude Code, ele fica mudo ou o hook mostra erro. Não bloqueia nem aprova nada.
- Custo: uma linha no contexto, poucas vezes por sessão. Ele mesmo roda a cada mensagem e ferramenta (uma partida do Python, dezenas de milissegundos num PC folgado; mais num PC carregado).
- "Avisar mais cedo" gera mais avisos (mais linhas no contexto), em troca de trocar de sessão antes.

**Se não ligar:** não há aviso de conversa grande. Continua funcionando tudo, mas a troca de sessão (Caixa 6) depende de o Claude notar o tamanho sozinho, o que falha com frequência. As perguntas 2 a 4 continuam possíveis (a 3 só avisa em % se o vigia existir).

**Desfazer:** apague `hooks/spend_watch.py`; tire as duas entradas dele (`"UserPromptSubmit"` e `"PostToolUse"`) do `settings.json`; apague a linha da regra no CLAUDE.md e, se quiser, `hooks/spend_watch_state/`. Ou volte a cópia de segurança da Caixa 1. Vale na próxima sessão.

**Dúvidas de um revisor cético:** "contorna as permissões?" Não: só imprime texto. "Lê minhas conversas?" Lê os arquivos, mas só extrai contagens; o código é curto e está no pacote para conferir. "Pode custar mais do que economiza?" O aviso é uma linha; o custo real é o de atrasar uma troca de sessão, que é o que ele evita.

### Caixa 8 · Antes/depois

**Por dentro:** só uma regra no CLAUDE.md. Antes de uma tarefa grande o Claude lê o % de uso do plano (ferramenta de uso no app; no terminal, a pessoa digita `/usage`), e no fim diz a diferença em uma linha.

**Ganha:** você vê o custo real de cada tarefa grande, em % da cota, e aprende o que pesa. Não há número de economia prometido.

**Riscos:** quase nada. O % da conta é inteiro e inclui outros usos (outro computador, celular, chat comum), então a diferença é aproximada. No terminal o Claude não vê o `/usage`; pede o número à pessoa.

**Se não ligar:** nada deixa de funcionar; você só confere o uso na tela quando quiser.

**Desfazer:** apague a linha "Antes e depois de tarefa grande" do CLAUDE.md. Vale na próxima sessão.

### Caixa 8 · Medir plano

**Por dentro:** `measure_point.py <%>` grava uma marca (hora, % semanal, tokens ponderados somados dos registros locais) em `tools/measure_marks.csv`. Entre duas marcas ele divide os tokens ponderados pela subida em pontos e estima quantos valem 1%. Marcas com menos de 3 pontos de diferença são somadas com as próximas. Com o número estável, a pessoa o põe em `POINT` no `spend_watch.py` e o vigia avisa também em %.

**Ganha:** o aviso em % da cota, que é o que a pessoa sente, e a base para o relatório diário comparar com a conta. A estimativa é só sua: no PC do autor, 1 ponto valeu algo na casa de 8,5 milhões de tokens ponderados, mas isso muda por plano e por uso (medido no PC do autor, set-nov/2026; não use o número dele).

**Riscos:**
- É estimativa. Entre duas marcas não pode haver virada da semana da cota. Conversas fora do Claude Code (chat comum do claude.ai ou do app) não entram nos registros; se você as usa muito, o número sai baixo.
- Lê os registros locais (só contagens) e grava um .csv pequeno; nada sai do PC.
- A regra manda o Claude ler o % no começo da sessão se a última marca tiver mais de um dia: uma leitura a mais de vez em quando.

**Se não ligar:** o vigia avisa só em tokens; o relatório diário (pergunta 5) funciona, mas sem o veredito da conta. Nada mais é afetado.

**Desfazer:** apague `tools/measure_point.py` e `tools/measure_marks.csv`, a linha "Medição do plano" do CLAUDE.md e, se tinha posto, volte `POINT` ao valor original no `spend_watch.py`.

### Caixa 8 · Skill uso

**Por dentro:** copia `skills/usage-report/` e `tools/usage_report.py`. Quando você pergunta "quanto gastei" ou "onde foi minha cota", o Claude roda o script, que soma tokens ponderados por sessão e por modelo a partir dos registros locais.

**Ganha:** resposta exata e rápida, em vez de o Claude tentar adivinhar. Sem número de economia: só informa.

**Riscos:** quase nada. Lê as conversas locais só para contar; nada sai do PC. A skill só é carregada quando a pergunta combina. O formato dos registros é interno do Claude Code e pode mudar; se mudar, o relatório sai incompleto.

**Se não ligar:** o Claude responde essas perguntas sem o relatório pronto (menos exato). O relatório diário precisa do `usage_report.py`, mas a pergunta 5 o copia sozinha.

**Desfazer:** apague `skills/usage-report/` e `tools/usage_report.py`. Vale na próxima sessão.

### Caixa 8 · Relatório

**Por dentro:** `daily_report.py` faz o relatório do dia anterior. O hook fica em `"SessionStart"` com `matcher: startup` (roda uma vez por sessão nova, não a cada mensagem: o autor mediu de 0,7 a 8 s por partida num PC com muitas sessões abertas, e por isso não vai em `UserPromptSubmit`). Com `--once-a-day`, se ainda não avisou hoje, ele grava a data em `quota_keeper/daily_asked.txt` e põe no contexto uma linha pedindo ao Claude que, antes do pedido da pessoa, pergunte numa caixa "Quer o relatório de uso de ontem?" (Ver agora / Hoje não). O relatório só roda se ela aceitar. Fica calado dentro de rodadas sem tela e se a sessão não tem pessoa. Um cheque barato (cabeçalho e data dos arquivos de sessão desde ontem) pode acrescentar uma linha: "achei N sessões sem tela sem aviso registrado ou rodando há mais de 8 h".

O relatório mostra: tokens ponderados do dia neste PC (por modelo e as sessões mais pesadas); sessões sem tela (campo `entrypoint` do registro começando com `sdk`), cada uma marcada como "registrada e avisada", "fora do registro" ou "rodou X h"; e, se houver duas marcas do % da conta em volta do dia, a comparação: soma o que este PC registrou entre elas, divide pelo valor de 1% e, se a conta subiu mais de 1,5 vez o explicado + 2 pontos, avisa. A regra do CLAUDE.md manda o Claude gravar o % da conta (`--record-account <%>`) uma vez por dia quando consegue ver o uso (ferramenta de uso no app; `/usage` no terminal, que só a pessoa digita).

**Ganha:** flagrar gasto que você não viu: sessão sem tela esquecida rodando, rodadas abertas sem aviso, e indício de uso da conta fora deste PC. Recomendado a quem ligou o token ou as rodadas sem tela (Caixa 7), porque são as formas de gastar sem ninguém olhando. Sem número de economia prometido.

**Riscos:**
- Um lembrete de uma linha no contexto no começo da primeira sessão do dia (e uma caixa de pergunta). Pode incomodar quem não quer isso; "Hoje não" encerra por aquele dia.
- Grava três arquivos pequenos em `<pasta de configuração>/quota_keeper/`: `daily_asked.txt`, `account_marks.csv` (só se o Claude gravar o %), `relay_log.jsonl` (escrito pelo `session_relay.py`, sem o token). Lê os registros locais só para contar.
- Falso alarme: qualquer outro programa que use `claude -p` neste PC aparece como "fora do registro", e sessões sem tela de antes da instalação também.
- O % da conta é inteiro, daí a folga na comparação; virada semanal entre duas marcas anula a comparação (o script diz).

**Limites honestos:** o script só vê este PC. Outro computador, claude.ai, celular ou alguém usando o seu token não aparecem nos registros: a diferença com a conta é indício, não prova. Sem o valor de 1% medido (pergunta 3), não há veredito, só os números. Sessão aberta de um dia para o outro só pergunta de novo se a pessoa pedir "relatório de ontem". Casar sessão e rodada pela pasta pode falhar com caminho escrito de outro jeito. O formato dos registros é interno do Claude Code e pode mudar; linhas ilegíveis são puladas.

**Se não ligar:** nenhum relatório nem aviso de gasto estranho; o vigia, a medição e a skill funcionam igual. Se a pergunta 3 (Medir plano) foi "Não", o relatório existe mas sem a comparação com a conta.

**Desfazer:** tire a entrada do `daily_report.py` em `"SessionStart"` do `settings.json`; apague `tools/daily_report.py`, a regra do CLAUDE.md e a pasta `<pasta de configuração>/quota_keeper/`. Vale na próxima sessão. O `relay_log.jsonl` pode ser apagado a qualquer hora (volta na próxima rodada).

**Dúvidas de um revisor cético:** "vigia minha atividade?" Só conta uso da sua conta neste PC, no seu computador; nada é enviado. "Prova que alguém roubou meu token?" Não: é indício; confira o painel da conta e, na dúvida, revogue o token. "Hook em Python em toda sessão?" Uma partida por sessão nova, e sai cedo se já avisou hoje.

## Caixa 9

Esta caixa só grava regras de comportamento no CLAUDE.md. Nenhum script, hook nem permissão muda, e nada sai do computador.

### Caixa 9 · Conferência

**Por dentro:** uma linha de regra por hábito marcado. Prova barata: usar o texto (linha de log, valor, saída de teste) quando ele prova, e imagem só recortada e em escala menor. Testes por partes: o que mudou mais uma regressão curta a cada mudança, a bateria inteira só antes de publicar. Duas revisões só no sensível: segurança, contas, pagamento e criptografia ganham duas revisões independentes, o resto uma. Não pagar duas vezes: depois de uma interrupção, conferir o que ainda roda e retomar; encerrar processo só pelo número (PID) que a própria sessão iniciou, nunca pelo nome.

**Ganha:** conferir continua obrigatório, mas gasta menos (imagens e testes grandes custam). Evita também recomeçar trabalho que ainda estava rodando e derrubar processo de outra sessão. Sem número de economia prometido.

**Riscos:**
- Prova barata: em caso raro o texto não mostra um defeito só visível (layout, cor). Peça uma imagem quando quiser.
- Testes por partes: um erro fora do trecho testado só aparece na bateria final.
- Duas revisões só no sensível: uma área que você não considera sensível ganha uma revisão só; se tiver dúvida, deixe desmarcado.
- São instruções, não travas: o Claude pode esquecer uma em conversa muito longa.

**Se não marcar:** o Claude confere do jeito padrão dele (em geral mais imagens e revisões em tudo, mais caro) e não tem a regra do PID; nada deixa de funcionar.

**Desfazer:** apague a linha da regra no CLAUDE.md (ou volte a cópia de segurança da Caixa 1). Vale na próxima sessão.

**Dúvidas de um revisor cético:** "isso afrouxa a qualidade?" Só troca o formato da prova e concentra a dupla revisão onde o erro custa mais; a bateria final continua obrigatória. "Mata processo?" Ao contrário: a regra proíbe matar por nome.

### Caixa 9 · Fim do turno

**Por dentro:** regras de como terminar uma mensagem. Perguntas pendentes: o que surgir no trabalho vai para `PERGUNTAS_PENDENTES.md` do projeto (criado só na primeira pergunta) e se repete no fim da mensagem final. Posso encerrar?: antes de encerrar, o Claude se pergunta "deveria estar fazendo algo antes de encerrar?" e, se sim, faz; se não, diz o que espera e o que vai acordá-lo. Mensagem final completa: resposta na primeira linha, depois pendências e o que não saiu tão bem.

**Ganha:** nada se perde entre sessões, e a sessão não fica parada esperando sem dizer. A resposta vem logo, sem rolar a tela.

**Riscos:** quase nada. Mensagens finais um pouco mais longas, uma checagem curta ao encerrar, e um arquivo novo no projeto (`PERGUNTAS_PENDENTES.md`, só se marcado). Como toda regra, o Claude pode esquecer em conversa muito longa.

**Se não marcar:** perguntas pendentes podem se perder no meio do texto, a sessão pode parar sem aviso e a mensagem final fica no formato padrão; o resto funciona igual.

**Desfazer:** apague a linha da regra no CLAUDE.md e, se quiser, o `PERGUNTAS_PENDENTES.md`. Vale na próxima sessão.

## Caixa 10

### Caixa 10 · Estrela

**Por dentro:** se a pessoa escolher "Sim, me lembre", o Claude grava uma linha no CLAUDE.md com a data de hoje + 7 dias. A partir dela, na primeira resposta de uma sessão, o Claude pergunta uma vez se as táticas ajudaram e, se a pessoa quiser, mostra o link do repositório. Depois de perguntar, apaga a própria linha. Em "Já dei ou dou agora", só mostra o link; em "Não, obrigado", nada é gravado.

**Ganha:** nada para você; ajuda outras pessoas a acharem o guia. Por isso o lembrete vem depois de uma semana de uso, não antes de você ver o resultado.

**Riscos:** praticamente nenhum. Uma linha no CLAUDE.md custa poucas palavras de contexto até ser usada. Nenhum dado sai do computador: o link só é mostrado, e o Claude nunca dá a estrela por você nem abre o navegador.

**Se não ligar:** nada muda; não há lembrete e o resto do pacote funciona igual.

**Desfazer:** apague a linha "Lembrete único (estrela)" do CLAUDE.md (ela também se apaga sozinha depois de usada). Vale na próxima sessão.
