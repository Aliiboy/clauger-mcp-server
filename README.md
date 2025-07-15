




# clauger-mcp-server
Clauger MCP Server avec Claude-code

## Processus d'installation sur le poste

### Installer Git

```powershell
winget install --id Git.Git -e --source winget
```

### Installer NodeJS

```powershell
winget install --scope user -e --id OpenJS.NodeJS.LTS
```

### Pour exécuter les commandes NodeJS (optionnel ?)

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### Installer claude-code

```powershell
npm install -g @anthropic-ai/claude-code
```

### Installer uv (gestionnaire de package python)

```powershell
winget install --id=astral-sh.uv -e
```

### Initialiser un projet

```powershell
uv init
```

### Créer l'environnement de developpement

```powershell
uv venv .venv
```

### Activer l'environnement de developpement

```powershell
.\.venv\Scripts\activate
```

### Installer MCP Server
```powershell
uv add "mcp[cli]"
```