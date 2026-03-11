# Guide pratique pour mener l’audit avec votre équipe ITS

Vous avez en main deux documents précieux :  
- `_PRE_AUDIT.md` : la méthodologie de collecte et d’organisation.  
- `_ITS_RACI_MATRIX.md` : la matrice des rôles et responsabilités.

Ce guide vous aide à **mettre en œuvre concrètement l’audit** avec vos trois collaborateurs, en tenant compte de la RACI, pour **rassembler toutes les informations nécessaires** et **embarquer l’équipe dans votre vision**.

---

## 1. Préparation de l’audit (à faire avant de solliciter l’équipe)

### 1.1. Clarifier vos objectifs pour l’équipe

Vous devez être capable d’expliquer simplement :

- **Pourquoi cet audit ?** « Nous allons construire ensemble une base de connaissances qui nous fera gagner du temps, évitera les répétitions et améliorera notre service. »
- **Qu’est‑ce que ça va changer pour eux ?** Moins de questions redondantes, des réponses plus rapides, une meilleure organisation, et à terme des outils (agents IA) qui les assisteront.
- **Ce que vous attendez d’eux** : leur expertise, leur honnêteté, leur participation active.

### 1.2. Préparer l’infrastructure de collecte

| Outil | Usage | Lien / Installation |
|-------|-------|---------------------|
| **Bitwarden** | Centraliser tous les mots de passe (serveurs, Odoo, bases, comptes clients). | [bitwarden.com](https://bitwarden.com) – créer un compte entreprise (gratuit jusqu’à 2 utilisateurs, mais vous êtes 4 ? la version teams est payante ; alternative : **Vaultwarden** auto-hébergé ou **KeePass** partagé) |
| **Google Drive** | Stocker les fichiers (contrats, exports WhatsApp, rapports). | Créer un dossier partagé `ITS-Audit-2026` avec sous‑dossiers par type. |
| **GitHub** | Versionner la documentation technique (procédures, guides). | Créer un dépôt privé `knowledge-base`. |
| **Google Forms** | Enquête écrite anonyme (optionnel). | Créer un formulaire simple. |
| **Tableur (Google Sheets)** | Suivi de l’avancement, liste des accès, matrice de compétences. | Créer une feuille de suivi. |

### 1.3. Définir votre planning

| Jour | Action |
|------|--------|
| **Jour 1** | Réunion de lancement (30‑45 min) |
| **Jours 2‑3** | Entretiens individuels (30 min chacun) |
| **Jour 4** | Collecte des documents et exports |
| **Jour 5** | Synthèse et premier classement |
| **Semaine 2** | Rédaction des premières procédures, mise en place de Bitwarden |

---

## 2. Lancement : réunion d’équipe

### 2.1. Ordre du jour proposé

1. **Présentation** (5 min) : qui je suis, mon rôle (Responsable Support Odoo), mon objectif : améliorer notre efficacité collective.
2. **La vision** (5 min) : construire une mémoire d’entreprise, des outils qui nous aident, un meilleur service client.
3. **Les bénéfices concrets** (5 min) :
   - Moins de recherches fastidieuses.
   - Moins d’erreurs.
   - À terme, un assistant IA qui répond aux questions courantes.
4. **Le plan d’audit** (10 min) :
   - Nous allons faire un état des lieux ensemble.
   - Entretiens individuels pour comprendre votre quotidien.
   - Collecte des documents existants.
   - Centralisation des accès (sécurité).
5. **Questions / réponses** (10 min).
6. **Prochaines étapes** : prise de rendez‑vous individuels.

### 2.2. Message à envoyer après la réunion

```markdown
Bonjour à tous,

Merci pour votre accueil aujourd’hui ! Je suis ravi de commencer cette aventure avec vous.

Comme convenu, voici les prochaines étapes :

1. **Entretiens individuels** (30 min) – je vais vous envoyer une invitation pour qu’on parle de votre rôle, vos difficultés, et de ce qui pourrait vous faciliter la vie.
2. **Centralisation des accès** – nous allons utiliser Bitwarden pour ranger tous nos mots de passe en toute sécurité. Je vous enverrai une invitation pour rejoindre l’organisation.
3. **Collecte des documents** – merci de commencer à rassembler tout ce qui pourrait être utile (procédures, notes, exports WhatsApp, etc.). Nous verrons ensemble où les stocker.

L’objectif est simple : **arrêter de chercher l’information, la trouver tout de suite**.

N’hésitez pas si vous avez des questions avant nos entretiens.

À très vite,
[Votre prénom]
```

---

## 3. Conduite des entretiens individuels

### 3.1. Structure type d’un entretien

- Durée : 30 minutes maximum.
- Cadre : informel, bienveillant, à l’écoute.
- Prendre des notes (Google Docs ou carnet).

### 3.2. Questions adaptées à chaque rôle (selon RACI)

#### Pour le **Directeur** (Accountable de tout)

- Quels sont les **3 objectifs stratégiques** pour l’année ?
- Quelle place doit occuper Odoo dans ces objectifs ?
- Quels sont les **projets prioritaires** à court / moyen terme ?
- Quels sont les **indicateurs de succès** pour le support Odoo ?
- Y a‑t‑il des **contraintes budgétaires ou techniques** à connaître ?
- Quelle est votre vision pour l’équipe dans 1 an ?
- J'aurai besion des contacts des membres de l'equipe, de l'acces aux cannaux de communication utilisés, et l'access au plateforms/serveurs/drive et la documentaton existante

#### Pour les **Ingénieurs Infrastructure** (Infra Eng 1 & 2)

- Pouvez‑vous me décrire l’infrastructure actuelle (serveurs, hébergement, bases de données) ?
- Quels outils de **monitoring** utilisez‑vous ?
- Comment gérez‑vous les **sauvegardes** ? Sont‑elles testées ?
- Quels sont les **accès** (serveurs, bases) ? Sont‑ils documentés ?
- Avez‑vous des **scripts ou procédures** écrites ?
- Quelles sont les **tâches répétitives** que vous aimeriez automatiser ?
- Quels sont les **problèmes récurrents** que vous rencontrez ?

#### Pour le **Développeur Backend / Odoo**

- Quels **modules Odoo** avez‑vous développés ou maintenus ?
- Quelle est la **version d’Odoo** utilisée en production ? ou pour chaque instance d'Odoo
- Avez‑vous une **documentation** pour ces développements ?
- Utilisez‑vous un **système de versioning** (Git) ?
- Quelles sont vos **difficultés quotidiennes** ?
- Comment gereé-vous les projects de development d'application? A-t'il des documents pour les projects passé?
- Comment gereé-vous les demandes de mise-ajour ou nouvels fonctionalités?
- Qu’aimeriez‑vous améliorer dans le processus de développement ?

#### Pour le **Développeur Mobile**

- Quelles **applications mobiles** sont en cours ou déjà livrées ?
- Sont‑elles connectées à Odoo ? Via quelle API ?
- Quelle documentation existe pour ces apps ?
- Quels sont les **points bloquants** actuels ?

#### Pour le **Responsable Odoo / Lead**

- Comment sont **gérés les projets Odoo** (méthodologie, suivi) ?
- Quels sont les **clients principaux** et leurs spécificités ?
- Y a‑t‑il un **catalogue de services** Odoo ?
- Comment se fait la **formation des utilisateurs** ? A-t-il des support de formation ecrit?
- - Qu’est‑ce qui vous **prend le plus de temps** ?
- Quels sont les **défis majeurs** dans les implémentations ?

#### Pour le **Support Odoo / Helpdesk**

- Comment les **tickets** sont‑ils actuellement traités ? 
- Quels sont les **types de demandes** les plus fréquents ? Liste exist!
- Avez‑vous des **réponses types** ou une base de connaissances ? Quelque fichier docs exists!
- Quels sont les **problèmes récurrents** qui pourraient être évités ? Liste exist!
- Qu’est‑ce qui vous **prend le plus de temps** ? Niveau 1 = 15-30m, Niveau= 1-3jours
- Quels **outils** vous manquent ? 
- - Quels sont les **défis majeurs** dans les implémentations ? Connexion lente, manque ressource humaine.

### 3.3. Grille de prise de notes

| Colonnes |
|----------|
| **Nom** |
| **Rôle** |
| **Responsabilités principales** |
| **Outils utilisés** |
| **Accès / identifiants mentionnés** |
| **Documents existants** |
| **Difficultés / frustrations** |
| **Suggestions d’amélioration** |
| **Informations techniques** (versions, serveurs, etc.) |

Utilisez un **Google Sheet** partagé avec vous seul en écriture (confidentiel).

---

## 4. Enquête écrite (complémentaire)

Après les entretiens, envoyez un **formulaire Google Forms** pour collecter des données standardisées et des idées.

**Questions suggérées :**

1. Quels sont les **3 problèmes** que vous rencontrez le plus souvent dans votre travail ?
2. Quelles **procédures** aimeriez‑vous voir documentées en priorité ?
3. Quels **accès** vous manquent ou sont difficiles à obtenir ?
4. Avez‑vous des **suggestions d’amélioration** pour l’équipe ?
5. Sur une échelle de 1 à 5, comment évaluez‑vous la **circulation de l’information** dans l’équipe ?
6. Que faudrait‑il pour que vous vous sentiez **mieux outillé(e)** ?

Le formulaire peut être anonyme si vous le souhaitez, mais précisez que cela aidera à prioriser.

---

## 5. Collecte des documents existants

### 5.1. Types de documents à rechercher

- **Procédures internes** (même informelles, dans des emails)
- **Guides utilisateurs** (PDF, Word)
- **Comptes rendus de réunions**
- **Exports de tickets** (depuis Odoo Helpdesk)
- **Conversations WhatsApp** avec clients (export)
- **Contrats clients** (si disponibles)
- **Spécifications de projets** (TDR, cahiers des charges)
- **Scripts** (backup, déploiement, audit)
- **Documentation technique** (architecture, schémas réseau)

### 5.2. Méthode de collecte

- Demandez à chacun de **déposer** ce qu’il a dans un dossier Google Drive dédié, par exemple :
  - `📁 Collecte_Documents / [Nom] /`
- Ou organisez une **session de partage d’écran** pour récupérer les fichiers ensemble.
- Pour les exports WhatsApp : chaque membre peut exporter les conversations importantes (sur mobile : paramètres > exporter la discussion). Il faudra ensuite les anonymiser ou les stocker dans un endroit sécurisé.

### 5.3. Classement initial

Dès que les documents arrivent, rangez‑les dans la structure définie :

```
📁 ITS-Knowledge-Base (Drive)
├── 📁 01_Clients
├── 📁 02_Projets
├── 📁 03_Procédures                
├── 📁 04_Technique
├── 📁 05_Archives_WhatsApp
└── 📁 06_Audit_2026 (vos notes)
```

Pour GitHub, vous créerez les fichiers Markdown plus tard, après nettoyage.

---

## 6. Centralisation des accès avec Bitwarden

### 6.1. Création de l’organisation

- Allez sur [bitwarden.com](https://bitwarden.com) et créez un compte **Organisation** (gratuit pour 2 utilisateurs, payant au‑delà ; alternative : utiliser **Vaultwarden** en auto‑hébergement).
- Invitez les membres de l’équipe par email.

### 6.2. Structure des dossiers

Créez des dossiers logiques :

- Serveurs (SSH)
- Bases de données (PostgreSQL)
- Odoo (admin, utilisateurs)
- Comptes clients (si besoin)
- Emails professionnels
- API (clés)
- WiFi / divers

### 6.3. Collecte des identifiants

Pendant les entretiens, notez les identifiants mentionnés, puis :

- Soit vous les saisissez vous‑même dans Bitwarden (en tant qu’admin) et partagez les dossiers avec les bonnes personnes.
- Soit vous donnez un accès en écriture limité pour que chacun ajoute ses propres comptes.

**Règle d’or** : plus aucun mot de passe dans un fichier Excel ou sur un post‑it.

---

## 7. Faire adhérer l’équipe : la communication continue

### 7.1. Réunion de mi‑parcours (fin de semaine 1)

Présentez une première synthèse : ce que vous avez appris, les points forts, les points faibles, et surtout les **premières actions concrètes** qui vont améliorer leur quotidien.

### 7.2. Quick wins immédiats

- **Exemple** : Vous avez trouvé une procédure manquante, vous la rédigez et la partagez.
- **Exemple** : Vous mettez en place un canal WhatsApp dédié aux annonces importantes.
- **Exemple** : Vous partagez un lien vers Bitwarden et chacun peut enfin retrouver le mot de passe du serveur sans demander à un collègue.

Ces petites victoires créent la confiance et montrent que votre démarche est utile.

### 7.3. Impliquer l’équipe dans la documentation

- Demandez à chacun de **rédiger une procédure** sur un sujet qu’il maîtrise. Utilisez le template fourni dans `_PRE_AUDIT.md`.
- Fixez une deadline courte (ex : vendredi) et offrez un petit encouragement (reconnaissance publique, chocolats…).
- Montrez que vous valorisez leur expertise.

### 7.4. Principe du « par l’exemple »

- **Ne dites pas** « il faut documenter », **montrez** en documentant vous‑même un processus que vous avez observé.
- **Ne dites pas** « on va utiliser Bitwarden », installez‑le, montrez à quel point c’est simple et sécurisé.
- **Ne dites pas** « on va améliorer le support », traitez vous‑même quelques tickets en appliquant les bonnes pratiques.

Votre action inspire plus que vos discours.

---

## 8. Outil de suivi global (Tableau de bord de l’audit)

Créez un **Google Sheets** avec les onglets suivants :

### 8.1. Suivi des entretiens

| Nom | Rôle | Date | Fait ? | Notes principales |
|-----|------|------|--------|-------------------|
| ... | ...  | ...  | [x]    | ...               |

### 8.2. Inventaire des accès

| Système | URL/IP | Identifiant (dans Bitwarden) | Responsable | Commentaire |
|---------|--------|-------------------------------|-------------|-------------|
| Serveur Odoo prod | 192.168.1.10 | (lien Bitwarden) | Infra1 | ... |

### 8.3. Documents collectés

| Nom du fichier | Source | Emplacement (Drive) | Traité pour KB ? |
|----------------|--------|----------------------|------------------|
| contrat_alpha.pdf | Client A | `01_Clients/Alpha/` | [ ] |

### 8.4. Actions

| Action | Responsable | Deadline | Statut |
|--------|-------------|----------|--------|
| Rédiger procédure backup | Infra1 | 15/03 | À faire |
| Exporter conversations WhatsApp | Tous | 12/03 | En cours |

---

## 9. Message récapitulatif après l’audit (semaine 2)

```markdown
Bonjour l’équipe,

Nous avons terminé la première phase d’audit ! Un grand merci pour votre participation et votre honnêteté.

**Ce que nous avons appris :**
- [2‑3 points marquants]
- [Les forces de l’équipe]
- [Les axes d’amélioration]

**Ce que nous mettons en place immédiatement :**
1. Tous les accès sont désormais dans Bitwarden – plus de perte de temps à chercher un mot de passe.
2. Un dossier Google Drive structuré pour ranger tous nos documents – vous y avez tous accès.
3. Un dépôt GitHub pour la documentation technique – on commence par 3 procédures cette semaine (chacun choisit la sienne).

**Prochaine étape :**
- Nous allons commencer à alimenter la base de connaissances.
- Je vous présenterai la semaine prochaine un premier prototype d’assistant IA capable de répondre aux questions courantes.

Encore merci pour votre implication. Ensemble, nous allons faire de notre support une référence !

[Votre prénom]
```

---

## 10. Synthèse : le fil conducteur

| Étape | Objectif | Clé de réussite |
|-------|----------|------------------|
| **Préparation** | Outils prêts, message clair | Avoir une vision simple et motivante |
| **Lancement** | Présenter le « pourquoi » et le « comment » | Être enthousiaste, à l’écoute |
| **Entretiens** | Comprendre les réalités de chacun | Questions ouvertes, absence de jugement |
| **Collecte** | Rassembler toute l’information | Organisation rigoureuse, suivi |
| **Centralisation** | Sécuriser les accès | Bitwarden, expliquer son utilité |
| **Quick wins** | Montrer rapidement des résultats positifs | Choisir des actions visibles et utiles |
| **Implication** | Faire participer l’équipe à la documentation | Valoriser leurs contributions |
| **Suivi** | Maintenir la dynamique | Réunions courtes, tableau de bord |

Avec cette approche, vous ne faites pas seulement un audit : vous **construisez une nouvelle culture d’équipe** fondée sur la transparence, la collaboration et l’amélioration continue. Exactement ce dont vous avez besoin pour que votre vision devienne réalité, non pas par la parole, mais par l’action collective.