from .helper import create_option as option


existing_options = {
    "whoiam": option(title="Qui sommes-nous ?", command="whoiam"),
    "ready": option(title="Commencer", command="start"),
    "start": option(title="Ajouter mon profil", command="start"),
    "stop": option(title="Je reste là.", command="exit", stop=True),
    "confirmexit": option(title="Quitter", command="confirmexit"),
    "cancelexit": option(title="Continuer", command="cancelexit")
}