# TodoCLI
![GitHub](https://img.shields.io/github/license/sennshi/TodoCLI?color=9966ff&style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/sennshi/TodoCLI?color=6666ff&style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/sennshi/TodoCLI?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/sennshi/TodoCLI?color=ff6699&style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/sennshi/TodoCLI?color=99ccff&style=for-the-badge)


```

sdSS_SSSSSSbs
YSSS~S%SSSSSP
     S&S               __      ________    ____
     S&S    ____  ____/ /___  / ____/ /   /  _/
     S*S   / __ \/ __  / __ \/ /   / /    / /
     S*S  / /_/ / /_/ / /_/ / /___/ /____/ /
     S*S  \____/\____/\____/\____/_____/___/
     S*S
     SP
     Y
     
```

> Uma simples todo list CLI feita utilizando as bibliotecas:
> - [Textual](https://github.com/Textualize/textual)
> - [Rich](https://github.com/Textualize/rich)

## Índice 

* [Início](#todocli)
* [Índice](índice)
* [Instalação](#instalação)
* [Como contribuir?](#como-contribuir)
* [Como usar?](#como-usar)
	* [Criando/Abrindo uma Todo.](#criandoabrindo-uma-todo)
	* [Comandos](#comandos)
		* [Combinações de teclas](#combinações-de-teclas)
		* [Manipulação de task](#manipulação-de-task)
* [Configuração](#configuração)
	* [Alterando banner ASCII](#alterando-banner-ascii)

## Instalação
Para instalar o projeto siga as etapas a seguir:

1. Istalação das bibliotecas/dependências necessárias.
`pip install -r requeriments.txt`

2. Clone o repositório em seu terminal utilizando:
`git clone https://github.com/rodr1goS/TodoCLI`

## Como contribuir?
Caso tenha ideias de melhorias ou adições, faça uma [issue](https://github.com/rodr1goS/TodoCLI/issues/new) ou um [pull request](https://github.com/rodr1goS/TodoCLI/pulls).
Saiba mais [como criar uma solicitação de pull.](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

## Como usar?

### Criando/Abrindo uma Todo.

Para abrir ou criar um todo(os todos sao arquivos json's):

`python3 main.py --todo <nome do todo>.json`

Entretanto se nenhum arquivo for encontrado, será criado uma todo vazia no diretório atual.
Caso apenas execute o arquivo `main.py` sem passar os argumentos necessários, o arquivo `home.py` será executado.
Assim exibindo a tela inicial, que nela contém suas [configurações](#Configurações) e uma [ASCII Art](#Alterando-ASCII-(home.py)).

### Comandos

#### Combinações de teclas
1. `ctrl+q`: sair.
2. `ctrl+o`: abrir painel de informações (informações da todo).
> Eles podem ser alterados para teclas de sua preferência...

#### Manipulação de task

- `add <tarefa>`: é utilizado para adicionar uma tarefa ao todo.
- `rm <tarefa>`: remove tarefa existente.
- `check <tarefa>`: basicamente marca a tarefa como concluída.
- `uncheck <tarefa>`: marca a tarefa como pendente novamente.

As tarefas possuem 2 estados, `<pending>`(pendente) e `<completed>`(completo/concluído)

## Configuração
Após a execução do arquivo `main.py` é gerado um arquivo `config.json`.
Onde podemos definir algumas "Combinações de Teclas" e a cor primária.

```json
{
  "keymapping": {
    "exit": "ctrl+q",
    "panel_toggle": "ctrl+o"
  },
  "pallete": {
    "primary": "blue"
  }
}
```

### Alterando banner ASCII
Para colocar uma ascii art de sua preferência para a home, substitua ascii definida em [ascii_banner](https://github.com/rodr1goS/TodoCLI/blob/main/home.py#L10).

[⬆ Voltar ao top](#todocli)

___
`Made with 💜 by sennshi`
