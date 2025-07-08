# Sistema Financeiro Simples

Um sistema web simples para controle de finanças pessoais, desenvolvido com Flask (backend) e HTML/CSS/JavaScript (frontend).

## 🚀 Funcionalidades

- ✅ Adicionar receitas e despesas
- ✅ Visualizar saldo atual em tempo real
- ✅ Histórico completo de transações
- ✅ Categorização de transações
- ✅ Interface responsiva e moderna
- ✅ Exclusão de transações
- ✅ Cálculo automático de totais

## 🛠️ Tecnologias Utilizadas

### Backend
- **Flask** - Framework web Python
- **SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados
- **Flask-CORS** - Suporte a CORS

### Frontend
- **HTML5** - Estrutura
- **CSS3** - Estilização moderna com gradientes
- **JavaScript** - Interatividade e comunicação com API

## 📋 Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação e Execução

### 1. Clone ou baixe o projeto
```bash
# Se usando git
git clone <url-do-repositorio>
cd sistema_financeiro

# Ou extraia o arquivo ZIP baixado
```

### 2. Ative o ambiente virtual
```bash
# No Linux/Mac
source venv/bin/activate

# No Windows
venv\\Scripts\\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o servidor
```bash
python src/main.py
```

### 5. Acesse o sistema
Abra seu navegador e acesse: `http://localhost:5000`

## 📖 Como Usar

### Adicionando Receitas
1. Preencha o formulário "Nova Receita" no lado esquerdo
2. Informe a descrição (ex: "Salário")
3. Digite o valor em reais
4. Especifique a categoria (ex: "Trabalho")
5. Clique em "Adicionar Receita"

### Adicionando Despesas
1. Preencha o formulário "Nova Despesa" no lado direito
2. Informe a descrição (ex: "Supermercado")
3. Digite o valor em reais
4. Especifique a categoria (ex: "Alimentação")
5. Clique em "Adicionar Despesa"

### Visualizando Informações
- **Saldo Atual**: Mostra a diferença entre receitas e despesas
- **Total de Receitas**: Soma de todas as receitas
- **Total de Despesas**: Soma de todas as despesas
- **Histórico**: Lista todas as transações com data e hora

### Excluindo Transações
- Clique no botão 🗑️ ao lado de qualquer transação no histórico
- Confirme a exclusão quando solicitado

## 🏗️ Estrutura do Projeto

```
sistema_financeiro/
├── src/
│   ├── models/
│   │   └── transacao.py          # Modelo de dados das transações
│   ├── routes/
│   │   └── transacao.py          # Rotas da API REST
│   ├── static/
│   │   └── index.html            # Interface do usuário
│   ├── database/
│   │   └── app.db               # Banco de dados SQLite
│   └── main.py                  # Arquivo principal do Flask
├── venv/                        # Ambiente virtual Python
├── requirements.txt             # Dependências do projeto
└── README.md                   # Este arquivo
```

## 🔌 API Endpoints

### Transações
- `GET /api/transacoes` - Lista todas as transações
- `POST /api/transacoes` - Adiciona nova transação
- `DELETE /api/transacoes/{id}` - Remove transação específica

### Saldo
- `GET /api/saldo` - Retorna saldo atual e totais

### Categorias
- `GET /api/categorias` - Lista categorias únicas

## 💾 Banco de Dados

O sistema utiliza SQLite com a seguinte estrutura:

### Tabela: transacoes
- `id` (INTEGER) - Chave primária
- `descricao` (VARCHAR) - Descrição da transação
- `valor` (FLOAT) - Valor da transação
- `tipo` (VARCHAR) - "receita" ou "despesa"
- `categoria` (VARCHAR) - Categoria da transação
- `data` (DATETIME) - Data e hora da transação

## 🎨 Interface

A interface foi desenvolvida com design moderno, incluindo:
- Gradientes coloridos para melhor experiência visual
- Cards responsivos para diferentes tamanhos de tela
- Animações suaves em hover
- Formatação automática de valores em reais
- Feedback visual para ações do usuário

## 🔒 Segurança

- Validação de dados no backend
- Sanitização de entradas
- CORS configurado adequadamente
- Tratamento de erros

## 🚀 Possíveis Melhorias Futuras

- Autenticação de usuários
- Relatórios gráficos
- Exportação de dados
- Filtros por período
- Metas financeiras
- Backup automático
- Notificações

## 📝 Licença

Este projeto é de uso livre para fins educacionais e pessoais.

## 👨‍💻 Desenvolvimento

Desenvolvido como um sistema financeiro simples e funcional, ideal para controle básico de finanças pessoais.

---

**Nota**: Este é um sistema de demonstração. Para uso em produção, considere implementar recursos adicionais de segurança e autenticação.
