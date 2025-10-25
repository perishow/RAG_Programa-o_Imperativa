# RAG - Introdução à Programação

Este projeto implementa um sistema RAG (Retrieval-Augmented Generation) para responder perguntas sobre introdução à programação, baseado em um material didático em PDF.

## 🛠️ Ferramentas Utilizadas

- **LangChain** - Framework para desenvolvimento de aplicações com LLMs
- **Ollama** - Para execução de modelos de linguagem localmente
- **Chroma** - Banco de dados vetorial para armazenamento e recuperação de embeddings
- **UnstructuredPDFLoader** - Carregador de documentos PDF
- **Gemma3** - Modelo de linguagem para geração de respostas
- **Nomic-embed-text** - Modelo de embeddings para representação vetorial do texto

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Ollama instalado e configurado
- Modelos Gemma3 e nomic-embed-text baixados no Ollama

## 🔧 Instalação e Configuração

### 1. Clonar o repositório e acessar o diretório

```bash
git clone https://github.com/perishow/RAG_Programa-o_Imperativa.git
cd RAG_Programa-o_Imperativa
```

### 2. Criar e ativar um ambiente virtual

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar o Ollama

Certifique-se de que o Ollama está instalado e execute os seguintes comandos para baixar os modelos necessários:

```bash
ollama pull gemma3
ollama pull nomic-embed-text
```

### 5. Preparar os dados

Coloque o arquivo PDF com o material de introdução à programação na pasta `data/` com o nome `introducaoProgramacao.pdf`:

```
RAG_Programa-o_Imperativa/
├── data/
│   └── introducaoProgramacao.pdf
├── venv/
└── main.py
```

## 🚀 Execução

```bash
python seu_script.py
```

O sistema irá:
1. Carregar e processar o PDF
2. Dividir o conteúdo em chunks menores
3. Criar o banco de dados vetorial
4. Iniciar o chat interativo

Digite suas perguntas sobre introdução à programação e pressione 'q' para sair.

## 📁 Estrutura do Projeto

```
RAG_Programa-o_Imperativa/
├── data/
│   └── introducaoProgramacao.pdf
├── venv/
├── requirements.txt
├── README.md
└── main.py
```

## 📝 requirements.txt

As dependências do projeto estão listadas no arquivo `requirements.txt`:

```
langchain-ollama
langchain-chroma
langchain-community
langchain-core
ollama
pandas
unstructured
chromadb
```

## 💡 Funcionalidades

- Processamento de documentos PDF em português
- Divisão inteligente do texto em chunks
- Recuperação semântica usando embeddings
- Geração de respostas contextualizadas
- Interface de chat interativa

## 🎯 Uso

O sistema está preparado para responder perguntas sobre:
- Conceitos básicos de programação
- Sintaxe de linguagens de programação
- Algoritmos fundamentais
- Boas práticas de programação
- E outros tópicos relacionados ao material fornecido
