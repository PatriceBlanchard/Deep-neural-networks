from siteweb.models import Post, PostCategory

post_category_all= PostCategory(name='All')
# Une meta catégorie pour récupérer toutes les catégories

def get_category_and_posts(category_name):
    # Retourner la catégorie et les posts associés à la catégorie

    posts = Post.objects.filter(published=True)
    # Récupérer l'ensemble des posts publiés

    if category_name == post_category_all.slug():
        # Si la category_name est all
        category = post_category_all
        # La variable catégorie prend pour valeur 'All'
    else :
        try :
            # Cas d'une catégorie spécifique existante
            category = PostCategory.objects.get(name__iexact=category_name)
            # La variable category pren dpour valeur la catégorie spécifique
            posts = posts.filter(category=category)
            # Seuls les posts de la catégorie spécifique sont récupérés
        except PostCategory.DoesNotExist:
            # Cas d'une catégorie inexistante
            category = PostCategory(name=category_name)
            posts = Post.objects.none()
            # Renvoie une sorte de liste vide spécifie à Django itérable et applicable avec un order.by

    posts = posts.order_by('-created_at')
    # Tri par date de création
    return category, posts
    # retourner les variables category et posts

def get_categories():
    # Récupérer toutes les catégories triées par
    categories = list(PostCategory.objects.all().order_by('name'))

    categories.insert(0, post_category_all)
    # Ajout de la catégorie 'All'
    return categories
