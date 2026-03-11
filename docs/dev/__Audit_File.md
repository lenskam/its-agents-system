## 1. Préparation de l’audit (à faire avant de solliciter l’équipe)

### 1.1. Clarifier vos objectifs pour l’équipe

Vous devez être capable d’expliquer simplement :

- **Pourquoi cet audit ?** « Nous allons construire ensemble une base de connaissances qui nous fera gagner du temps, évitera les répétitions et améliorera notre service. »
- **Qu’est‑ce que ça va changer pour eux ?** Moins de questions redondantes, des réponses plus rapides, une meilleure organisation, et à terme des outils (agents IA) qui les assisteront.
- **Ce que vous attendez d’eux** : leur expertise, leur honnêteté, leur participation active.

### 1.2. Questions adaptées à chaque rôle (selon RACI)

#### Pour le **Directeur** (Accountable de tout)

- Quels sont les **3 objectifs stratégiques** pour l’année ? Allez sur le marché externe (en dévélopant des produits), Travailler sur les projets auto-financés.
- Quelle place doit occuper Odoo dans ces objectifs ?
- Quels sont les **projets prioritaires** à court / moyen terme ?
- Quels sont les **indicateurs de succès** pour le support Odoo ? Manual de procedure à les indicateurs!
- Y a‑t‑il des **contraintes budgétaires ou techniques** à connaître ?
- Quelle est votre vision pour l’équipe dans 1 an ?
- J'aurai besion des **contacts des membres de l'equipe**
- , de **l'acces aux cannaux de communication** utilisés? 
- , et **l'access au plateforms/serveurs/drive**? Oui (to get)
-  et la **documentaton existante**? Oui (to get)
-  , list des **clients et/projects**? 10

#### Pour les **Ingénieurs Infrastructure** (Infra Eng 1 & 2)

- Pouvez‑vous me décrire l’infrastructure actuelle (serveurs, hébergement, bases de données) ? Server en local et Server Cloud
- Quels outils de **monitoring** utilisez‑vous ? Promethus and Grafana (but not installed on prod)
- Comment gérez‑vous les **sauvegardes** ? Sauvegarde des DB Odoo Chaque 00H. Sont‑elles testées ?
- Quels sont les **accès** (serveurs, bases) ? Sont‑ils documentés ?
- Avez‑vous des **scripts ou procédures** écrites ? 
- Quelles sont les **tâches répétitives** que vous aimeriez automatiser ?
- Quels sont les **problèmes récurrents** que vous rencontrez ?

#### Pour le **Développeur Backend / Odoo**

- Quels **modules Odoo** avez‑vous développés ou maintenus ?
- Quelle est la **version d’Odoo** utilisée en production ? ou pour chaque instance d'Odoo
- Avez‑vous une **documentation** pour ces développements ?
- Utilisez‑vous un **système de versioning** (Git) ? GitLab en local
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
- Quels sont les **types de demandes** les plus fréquents ?
- Avez‑vous des **réponses types** ou une base de connaissances ?
- Quels sont les **problèmes récurrents** qui pourraient être évités ?
- Qu’est‑ce qui vous **prend le plus de temps** ?
- Quels **outils** vous manquent ?
- - Quels sont les **défis majeurs** dans les implémentations ?

### 1.3. Grille de prise de notes

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