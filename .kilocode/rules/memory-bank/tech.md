# Pile Technologique

## Technologies Principales

*   **Langage de programmation** : Python (version >= 3.13)
*   **Gestionnaire de paquets et d'environnement** : `uv`. Il est utilisé pour initialiser le projet, gérer les dépendances et exécuter des scripts dans un environnement virtuel.
*   **Framework MCP** : La bibliothèque `mcp[cli]` (version >= 1.11.0) est la dépendance principale pour construire le serveur MCP.

## Dépendances Anticipées

*   **Manipulation de Word** : La bibliothèque `python-docx` sera probablement nécessaire pour créer, lire et modifier des documents `.docx`. Elle n'est pas encore listée dans `pyproject.toml` et devra être ajoutée.

## Environnement de Développement

L'environnement de développement documenté dans le `README.md` est basé sur Windows et utilise `winget` et `PowerShell` pour l'installation des prérequis comme `NodeJS`, `uv` et `claude-code`.

Le projet lui-même est multiplateforme grâce à Python et `uv`.