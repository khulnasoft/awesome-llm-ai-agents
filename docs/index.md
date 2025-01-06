# Documentation Index

Welcome to the documentation for the **RAG System**. This system integrates various **Retrieval-Augmented Generation (RAG)** agents to enhance the generation of text using external knowledge retrieval methods. Below, you’ll find all the necessary information about the system's architecture, individual components, setup, usage, and contribution guidelines.

## Table of Contents

1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Individual Agents](#individual-agents)
   - [Autonomous RAG](agents/rag/autonomous_rag/README.md)
   - [Corrective RAG](agents/rag/corrective_rag/README.md)
   - [Hybrid Search RAG](agents/rag/hybrid_search_rag/README.md)
   - [Llama3.1 Local RAG](agents/rag/llama3.1_local_rag/README.md)
   - [Local Hybrid Search RAG](agents/rag/local_hybrid_search_rag/README.md)
   - [RAG as a Service](agents/rag/rag-as-a-service/README.md)
   - [RAG Database Routing](agents/rag/rag_database_routing/README.md)
4. [Installation and Setup](#installation-and-setup)
   - [Installing Dependencies](#installing-dependencies)
   - [Setting Up the Environment](#setting-up-the-environment)
   - [Running the System](#running-the-system)
5. [Configuration](#configuration)
6. [Troubleshooting](#troubleshooting)
7. [Contributing](#contributing)
8. [License](#license)

## Project Overview

The **RAG System** provides a set of agents that leverage external knowledge sources to enhance the output of AI text generation models. Each agent is designed to handle a specific retrieval and generation strategy, allowing for fine-grained control over how external data is integrated into the generative process.

Key features of the system:
- Support for hybrid search and autonomous retrieval methods.
- Multiple agents specialized for different use cases, such as corrective text generation and hybrid search.
- Full integration with external databases and services for efficient retrieval.
- Easy extensibility for additional agents or integration points.

## System Architecture

The system is composed of various **RAG Agents**, each responsible for a different aspect of the process. All agents rely on an external knowledge source (e.g., databases, Redis, APIs) to retrieve relevant information that augments the AI model's responses. The system is designed to be modular, allowing developers to swap out or customize agents as needed.

Here’s an overview of the system architecture:
- **RAG Agents**: Modular components responsible for text retrieval and augmentation.
- **API Layer**: Exposes functionality for interacting with the agents, allowing them to be used through simple RESTful interfaces.
- **Cache Layer**: Redis is commonly used to store retrieved information for faster future access.

## Individual Agents

Each agent within the system has its own specific functionality. You can read more about each agent by visiting the links below:

- [Autonomous RAG](agents/rag/autonomous_rag/README.md): An autonomous RAG agent designed to generate text based on external knowledge retrieval.
- [Corrective RAG](agents/rag/corrective_rag/README.md): A RAG agent that corrects and improves the quality of generated text by integrating external validation.
- [Hybrid Search RAG](agents/rag/hybrid_search_rag/README.md): A RAG agent that combines multiple search strategies for more accurate results.
- [Llama3.1 Local RAG](agents/rag/llama3.1_local_rag/README.md): A RAG agent that uses a locally hosted version of Llama3.1 for generating augmented responses.
- [Local Hybrid Search RAG](agents/rag/local_hybrid_search_rag/README.md): A locally run agent utilizing hybrid search techniques for retrieval and generation.
- [RAG as a Service](agents/rag/rag-as-a-service/README.md): A service-oriented RAG agent that exposes an API for external integration.
- [RAG Database Routing](agents/rag/rag_database_routing/README.md): A RAG agent that intelligently routes requests to different databases based on the context of the query.

## Installation and Setup

To get started with the **RAG System**, follow the steps below.

### Installing Dependencies

Each agent has its own set of dependencies, which are listed in the `requirements.txt` file within its directory. Make sure to install the dependencies for the specific agents you plan to work with.

```bash
pip install -r requirements.txt
