# 📝 Resumo

### Git e Github:
Durante o trajeto do curso de Git & GitHub pude relembrar os conceitos e comandos, aos quais já havia aprendido grande parte na universidade durante as aulas.
- **Git**:
  - Além dos comandos básicos que já conhecia, como o Commit, Push, Pull, Restore e etc, o que de fato eu aprendi que desconhecia foi sobre o Alias e a diferença entre o Reset Soft, Mixed e Hard, no qual o Soft faz o reset retornando para a versão anterior e coloca o último commit no estado de *staged*, o Mixed coloca o último commit em *unstaged*, já o Hard remove qualquer coisa feita depois do ponto que você retornou. A diferença principal entre o Hard para os outros dois é essa, o Mixed e o Soft formam uma "corrente", onde você pode percorrer pelos pontos anteriores sem que haja perca dos mais recentes, é como se fosse uma fila encadeada.<br>
  O Alias em especial achei muito útil e devo utilizar bastante a partir de agora.
  <br>` -git --global alias.nome-do-seu-novo-arquivo "comando" `
- **GitHub**:
  - Com o Github não foi diferente, por estar acostumado à mexê-lo na universidade, poucas foram as coisas das quais desconhecia. Uma delas eram as releases, já que nos meus projetos pequenos não via necessidade de utilizá-las, então acabei por não aprender antes, mas achei útil. A mesma coisa para as Issues. Além disso, aprendi como usar o VSCode para simplificar os comandos do Git e fazê-los apenas ao clicar um botão.

- **Conventional Commits**:
  - Para a padronização e clareza dos commits, podemos utilizar de uma estratégia chamada Conventional Commits, onde há essa estrutura: `<tipo>(escopo opcional): descrição curta`  
  - Os tipos mais comuns são:
    - feat → funcionalidade nova
    - fix → correção de bug
    - refactor → refatoração
    - docs → documentação
    - test → testes
    - chore → config, build, infra
    - perf → performance

    Exemplos:
    - feat(worker): add task execution with retry logic
    - fix(manager): prevent duplicate task dispatch
    - refactor(scheduler): extract queue handling logic
    - docs(readme): document swarm deployment
    - test(worker): add unit tests for task runner
  - Prefira vários vários commits pequenos e claros do que um commit gigante confuso.
>As demais coisas que não foram citadas, foi porque eu já as conhecia, mas o curso foi de muito proveito.

## Demais pastas:
**Certificados**: Não houve cursos externos, apenas dentro da Compass Udemy.

**Desafio**: Não houve desafio nesta sprint.

**Evidências**: Não houve necessidade de prints ou demais evidências para a realização dessa sprint.

**Exercícios**: O único exercício proposto foi de fato criar o repositório que usaremos durante o estágio e adicionarmos os READMEs.

> Foi nos orientado para que caso não houvessem conteúdos nas pastas, que fosse adicionado um arquivo `.gitkeep`.