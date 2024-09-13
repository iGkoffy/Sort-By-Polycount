
Trier par Nombre de Polygones (Sort By Polycount)

Ce script Python pour Blender permet de trier et d'afficher les objets mesh dans l'Outliner en fonction de leur nombre de polygones (polycount). Il modifie le nom de chaque objet mesh dans la scène en ajoutant le polycount au début du nom de l'objet. Cela facilite la gestion des objets complexes, l'optimisation des performances, et permet de rapidement identifier les modèles les plus lourds en termes de géométrie.

## Fonctionnalités :
- **Ajout du nombre de polygones au début du nom des objets** : Le script détecte tous les objets de type mesh dans la scène et renomme chaque objet en ajoutant son nombre de polygones au début du nom, sous la forme `[XXX polys] ObjectName`.
- **Gestion des objets de type Mesh uniquement** : Le script ignore tous les autres types d'objets (comme les lumières, caméras, etc.) et ne traite que les objets 3D de type mesh.
- **Optimisation visuelle dans l'Outliner** : Une fois le script exécuté, vous pouvez facilement trier les objets par polycount simplement en regardant leur nom dans l'Outliner de Blender.

## Comment ça marche :
1. **Détection des objets mesh** : Le script parcourt tous les objets dans la scène, et pour chaque objet de type `MESH`, il calcule le nombre de polygones en utilisant la fonction `len(obj.data.polygons)`.
2. **Renommage des objets** : Pour chaque objet mesh, le script modifie son nom en ajoutant le polycount au début du nom actuel, en suivant la structure `[XXX polys] NomObjet`.
3. **Mise à jour automatique dans l'Outliner** : Les changements de noms sont immédiatement visibles dans l'Outliner de Blender.

### Exécution du script :
1. Ouvrez Blender.
2. Allez dans l'onglet **Scripting**.
3. Copiez le script dans l'éditeur de texte de Blender.
4. Cliquez sur "Run Script" pour l'exécuter.
5. Les noms des objets mesh dans l'Outliner seront mis à jour pour inclure leur nombre de polygones au début du nom.

### Exemple de résultat :
Si vous avez un objet nommé `Cube`, après l'exécution du script, il sera renommé en :
```
[286 polys] Cube
```
Ce qui indique que cet objet possède 286 polygones.

## Pré-requis :
- Blender version 2.8 ou supérieure.
- Connaissance de base de l'utilisation du **Scripting** dans Blender.

## Utilisation pratique :
Ce script est utile pour les projets d'animation, de modélisation de jeux vidéo, et d'optimisation, où la gestion des objets avec un grand nombre de polygones est cruciale pour améliorer les performances de la scène.
