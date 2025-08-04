# Importez les packages pour vous assurer que les décorateurs @mcp.tool() et @mcp.prompt()
# sont exécutés et que les fonctionnalités sont enregistrées sur l'instance MCP partagée.
from server import mcp
from src import agents, multiply, weather  # noqa: F401


def main():
    """Point d'entrée pour le serveur d'exécution directe."""
    mcp.run()


if __name__ == "__main__":
    main()
