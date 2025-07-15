# Architecture

## Architecture Système

Ce projet implémente un **Serveur MCP** (Model Context Protocol) qui suit l'architecture client-serveur définie par le protocole.

- **Hôte (Host)** : Une application cliente MCP comme Claude Desktop, qui gère le cycle de vie du serveur.
- **Client MCP** : Le composant au sein de l'hôte qui établit une connexion 1-à-1 avec notre serveur.
- **Serveur MCP (ce projet)** : Un processus local qui expose des fonctionnalités spécifiques pour la manipulation de documents Word.
- **Transport** : La communication se fera via le transport **stdio** (standard input/output), où le client lance le serveur comme un sous-processus et communique via des messages JSON-RPC délimités par des nouvelles lignes.

Le diagramme de flux général est le suivant :

```mermaid
flowchart LR
    subgraph "Application Hôte (ex: Claude Desktop)"
        Client[Client MCP]
    end
    subgraph "Processus Serveur (ce projet)"
        Serveur[Serveur MCP Word]
    end
    subgraph "Système de fichiers local"
        Fichiers[("Documents .docx")]
    end

    Client <-->|Transport stdio (JSON-RPC)| Serveur
    Serveur <-->|Bibliothèque Python| Fichiers
```

## Structure du Code Source

Le code source principal du projet sera situé dans un répertoire `src/clauger_mcp_server/`.

- `src/clauger_mcp_server/server.py` (ou `main.py`): Le point d'entrée du serveur. Il initialisera le serveur MCP, définira les outils et gérera le cycle de vie de la connexion.
- `src/clauger_mcp_server/tools.py`: Ce module contiendra la logique métier pour chaque outil exposé (créer, écrire, modifier des documents Word).
- `src/clauger_mcp_server/word_handler.py`: Une couche d'abstraction pour interagir avec la bibliothèque de manipulation de documents Word (par exemple, `python-docx`).

## Primitives MCP utilisées

Le serveur se concentrera principalement sur l'exposition de **Tools** (Outils), qui sont des fonctions contrôlées par le modèle d'IA pour effectuer des actions.

Les outils prévus sont :
- `creer_document`
- `ecrire_paragraphe`
- `modifier_document`
- `generer_depuis_modele`

Chaque outil sera défini avec un `inputSchema` (schéma JSON) clair pour ses paramètres.

## Cycle de vie de la connexion

1.  **Initialisation** : Le client enverra une requête `initialize` pour négocier la version du protocole et les capacités. Notre serveur répondra en déclarant sa capacité à fournir des `tools`.
2.  **Opération** : Le client enverra des requêtes `tools/call` pour invoquer les fonctionnalités de manipulation de Word. Le serveur exécutera ces actions et renverra les résultats.
3.  **Arrêt** : La connexion sera terminée lorsque le client fermera le flux d'entrée du serveur.