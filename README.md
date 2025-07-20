# RPG_X_TEMP - Ambiente de Desenvolvimento Temporário

Este é um ambiente de desenvolvimento temporário para projetos RPG.

## Estrutura do Projeto

```
RPG_X_TEMP/
├── README.md
├── package.json
├── src/
│   ├── index.js
│   ├── index.test.js
│   ├── game.test.js
│   └── utils/
├── public/
│   ├── index.html
│   ├── game.js
└── docs/
    └── API.md
```

## Instalação

```bash
npm install
```

## Uso

```bash
npm start
```

## Testes

Para executar os testes automatizados, utilize o comando:

```bash
npm test
```

### Testes Backend

- Localizados em `src/index.test.js`
- Testam os endpoints da API para obter o estado do jogador e realizar ações (ataque, cura, erros)

### Testes Frontend

- Localizados em `src/game.test.js`
- Testam a interface do usuário simulando a exibição do estado do jogador e interações básicas

Certifique-se de que o servidor esteja parado antes de executar os testes para evitar conflitos de porta.

    └── API.md
