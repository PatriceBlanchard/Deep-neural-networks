from django import forms


# un pattern Django form simplifie la génération et le traitement des formulaires HTML

# Chaque attribut correspond à un input attendu dans un formulaire et dont le type déterminera le rendu
# Une foi que la classe est définir il suffit d'injecter une instance de ce form dans un template
# et Django se changera du rendu, de la vérification d'erreurs côté client et de la vérification d'erreurs côté serveur
# au moment de la récupération des informations et du traitement du formulaire.

class ContactForm(forms.Form):
    # Une classe héritant de forms.Form
    from_email = forms.EmailField(required=True)
    # L'attribut email
    subject = forms.CharField(required=True)
    # L'attribut sujet du formulaire
    message = forms.CharField(widget=forms.Textarea, required=True)
    # L'attribut dédié au message