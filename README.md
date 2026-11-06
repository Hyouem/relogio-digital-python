# Relógio Digital do Maurício

Relógio digital desenvolvido em Python e Tkinter, com interface
minimalista, relógio em tempo real e alternância entre temas.

<img width="588" height="341" alt="image" src="https://github.com/user-attachments/assets/d388c36d-f874-4137-8e1e-51054498c4cf" />

## Funcionalidades

- Saudação personalizada: Olá, Maurício!
- Data completa em português brasileiro
- Relógio atualizado a cada segundo
- Modo claro e escuro
- Interface gráfica com Tkinter
- Testes automatizados com unittest
- Integração com GitHub Actions

## Tecnologias

- Python 3.10+
- Tkinter
- unittest
- Git e GitHub
- GitHub Actions

## Execução

Abra o PowerShell na pasta do projeto:

```powershell
py main.py
```

## Testes

```powershell
py -m unittest discover -s tests -v
```

## Personalização

O nome do usuário está definido na constante NOME_USUARIO,
dentro do arquivo main.py.

As cores estão definidas no dicionário TEMAS.

## Observações

O aplicativo utiliza a data e o horário local do computador.

Nenhuma biblioteca externa precisa ser instalada no Windows
quando o Python já possui suporte ao Tkinter.

O GitHub Pages não executa aplicativos Tkinter. O repositório
hospeda o código-fonte e executa os testes automatizados.
