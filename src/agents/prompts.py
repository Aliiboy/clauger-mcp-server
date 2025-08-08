from server import mcp


@mcp.prompt(
    name="Promptologue",
    title="Createur de Prompt",
    description="Permet de créer un prompt optimisé",
)
def create_prompt(
    main_intention: str,
    target_audience: str,
    key_entities: str,
    user_context: str,
    scope_include: str,
    scope_exclude: str,
    output_format: str,
    constraints: str,
) -> str:
    """
    Génère un prompt structuré pour un LLM à partir de plusieurs entrées utilisateur.

    Ce prompt est conçu pour guider un LLM dans la création d'un prompt optimisé
    en suivant une méthodologie structurée en quatre étapes : Déconstruire,
    Diagnostiquer, Développer et Livrer.

    Args:
        main_intention: L'objectif principal ou l'intention du prompt à générer.
        target_audience: Le public cible pour la réponse finale du LLM.
        key_entities: Les entités, concepts ou mots-clés principaux à inclure.
        user_context: Le contexte général fourni par l'utilisateur.
        scope_include: Les éléments ou sujets qui doivent être inclus dans la réponse.
        scope_exclude: Les éléments ou sujets qui doivent être exclus de la réponse.
        output_format: Le format de sortie souhaité pour la réponse du LLM.
        constraints: Les contraintes spécifiques à appliquer au prompt ou à sa sortie.

    Returns:
        Une chaîne de caractères formatée contenant le prompt complet et structuré.
    """
    return f"""
    # Contexte

    Nous allons créer le meilleur prompt jamais écrits. Le meilleur prompt comprenant des détails exhaustifs afin d’informer pleinement le LLM sur :

    - Ses objectifs
    - Les domaines d’expertise requis
    - Le format de la réponse attendus
    - Les références
    - Les exemples
    - La meilleure approche pour attendre l’objectif

    En nous basant sur ces éléments et les informations suivantes, vous serez en mesure d’écrire le meilleur prompt.

    # Rôle

    Vous êtes un expert en prompt engineering pour modèles de langage (LLM). Vous maitrisez le processus de conception et de structuration d’un prompt, de sorte qu’il soit efficacement interprété et compris par un modèle d’intelligence artificielle générative.

    # Etapes

    1. **DÉCONSTRUIRE** 
        1. Extraire l’intention principale, les entités clés et le contexte
        2. Identifier les exigences de sortie et les contraintes
        3. Cartographier ce qui est fourni vs. ce qui manque
    2. **DIAGNOSTIQUER**
        1. Auditer les lacunes de clarté et les ambiguïtés
        2. Vérifier la spécificité et l’exhaustivité
        3. Évaluer les besoins en structure et en complexité
    3. **DÉVELOPPER**
        1. Sélectionner les techniques optimales selon le type de demande :
            - *Créatif* → Approche multi-perspective + mise en avant du ton
            - *Technique* → Basé sur les contraintes + précision accrue
            - *Éducatif* → Quelques exemples (few-shot) + structure claire
            - *Complexe* → Raisonnement en chaîne (chain-of-thought) + cadres systématiques
        2. Assigner le rôle ou l’expertise IA approprié
        3. Renforcer le contexte et implémenter une structure logique
    4. **LIVRER**
        1. Construire un prompt optimisé
        2. Formater en fonction de la complexité
        3. Fournir des consignes de mise en œuvre

    # Entrée utilisateur

    Pour construire le prompt, il est nécessaire que l’utilisateur fournisse :

    - Intention principale : {main_intention}
    - Lecteur visé : {target_audience}
    - Entités clés : {key_entities}
    - Contexte disponible : {user_context}
    - Périmètre à inclure : {scope_include}
    - Périmètre à exclure : {scope_exclude}

    # Format de sortie

    - Format : {output_format}
    - Contraintes : {constraints}
            """
