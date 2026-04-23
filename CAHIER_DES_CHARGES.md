# Cahier des Charges — Projet LeloMaurice Portfolio

**Méthode :** Agile / Scrum  
**Version :** 1.0  
**Date :** 23 Avril 2026  
**Auteur :** LeloMaurice  
**Statut :** En cours de développement

---

## 1. Contexte du Projet

### 1.1 Objectif Principal

Développer un portfolio professionnel moderne permettant de présenter mes projets, compétences, services et de faciliter les contacts avec des potentiels clients ou employeurs.

### 1.2 Problématique Actuelle

- Absence de site web personnel professionnel
- Difficulté à mettre en valeur mes réalisations
- Manque de canal de contact structuré
- Pas de visibilité sur les visiteurs du site

### 1.3 Objectifs Stratégiques

| Objectif | Indicateur de Succès |
|----------|---------------------|
| Présenter mon portfolio | Site accessible avec projets |
| Faciliter le contact | Formulaire fonctionnel |
| Analyser le trafic | Dashboard analytics |
| Automatiser les réponses | Chatbot IA |

---

## 2. Équipe Projet

| Rôle | Responsable |
|------|-------------|
| Product Owner | LeloMaurice |
| Développeur | LeloMaurice |
| Designer UI/UX | LeloMaurice |
| QA / Tests | LeloMaurice |

---

## 3. Backlog du Produit

### 3.1 User Stories — Sprint 1 (Foundation)

| ID | User Story | Priorité | Estimation |
|----|------------|----------|-------------|
| US-01 | En tant que visiteur, je veux voir une page d'accueil attractive | MUST | 3 pts |
| US-02 | En tant que visiteur, je veux naviguer facilement sur le site | MUST | 2 pts |
| US-03 | En tant que propriétaire, je veux administrer le contenu via /admin | MUST | 5 pts |

### 3.2 User Stories — Sprint 2 (Portfolio)

| ID | User Story | Priorité | Estimation |
|----|------------|----------|-------------|
| US-04 | En tant que visiteur, je veux voir la liste de mes projets | MUST | 3 pts |
| US-05 | En tant que visiteur, je veux voir les détails d'un projet | MUST | 2 pts |
| US-06 | En tant que propriétaire, je veux ajouter/modifier des projets | MUST | 3 pts |

### 3.3 User Stories — Sprint 3 (Compétences)

| ID | User Story | Priorité | Estimation |
|----|------------|----------|-------------|
| US-07 | En tant que visiteur, je veux voir mes compétences techniques | SHOULD | 2 pts |
| US-08 | En tant que visiteur, je veux voir mes expériences professionnelles | SHOULD | 2 pts |
| US-09 | En tant que propriétaire, je veux gérer les compétences | SHOULD | 3 pts |

### 3.4 User Stories — Sprint 4 (Contact)

| ID | User Story | Priorité | Estimation |
|----|------------|----------|-------------|
| US-10 | En tant que visiteur, je veux envoyer un message via un formulaire | MUST | 3 pts |
| US-11 | En tant que propriétaire, je veux voir les messages reçus | MUST | 2 pts |
| US-12 | En tant que visiteur, je veux recevoir une confirmation par email | COULD | 1 pt |

### 3.5 User Stories — Sprint 5 (Avancé)

| ID | User Story | Priorité | Estimation |
|----|------------|----------|-------------|
| US-13 | En tant que propriétaire, je veux voir les statistiques de visite | SHOULD | 3 pts |
| US-14 | En tant que visiteur, je veux discuter avec un chatbot IA | COULD | 5 pts |
| US-15 | En tant que développeur, je veux une API REST pour mes données | COULD | 5 pts |

---

## 4. Critères d'Acceptation

### 4.1 Page d'Accueil

- [ ] Header avec logo et navigation
- [ ] Section hero avec présentation
- [ ] Liens vers projets et compétences
- [ ] Design responsive (mobile/tablet/desktop)

### 4.2 Portfolio

- [ ] Liste des projets avec images
- [ ] Page détail avec description, technologies, lien
- [ ] CRUD complet via admin Django

### 4.3 Compétences

- [ ] Affichage visuel (barres, icônes, etc.)
- [ ] Catégorisation (techniques, soft skills)
- [ ] Mise à jour via admin

### 4.4 Formulaire de Contact

- [ ] Champs : nom, email, sujet, message
- [ ] Validation des données
- [ ] Enregistrement en base
- [ ] Email de confirmation (optionnel)

### 4.5 Analytics

- [ ] Dashboard avec graphiques
- [ ] Suivi des pages vues
- [ ] Suivi des visiteurs uniques
- [ ] Middleware de tracking

### 4.6 Chatbot IA

- [ ] Interface de chat
- [ ] Intégration API IA
- [ ] Réponses contextuelles

### 4.7 API REST

- [ ] Endpoints pour projets
- [ ] Endpoints pour compétences
- [ ] Authentification (optionnel)
- [ ] Documentation Swagger

---

## 5. Architecture Technique

### 5.1 Stack

```
Python 3.12+ → Django 6.0.4 → Gunicorn
PostgreSQL → SQLite (dev)
Nginx → Docker
```

### 5.2 Structure des Apps

```
apps/
├── core/        # Pages principales (home, about)
├── projects/    # Gestion portfolio
├── skills/      # Compétences & expériences
├── contact/     # Formulaire contact
├── crm/         # Gestion clients
├── analytics/   # Statistiques & tracking
├── ai/          # Chatbot IA
└── api/         # REST API
```

### 5.3 Base de Données

| Modèle | Description |
|--------|-------------|
| Project | Titre, description, image, technologies, lien |
| Skill | Nom, catégorie, niveau, icône |
| ContactMessage | Nom, email, sujet, message, date |
| PageView | Page, IP, date, user-agent |

---

## 6. Planification des Sprints

| Sprint | Durée | Objectif | Livrable |
|--------|-------|----------|----------|
| Sprint 1 | 1 sem | Foundation | Site fonctionnel, admin |
| Sprint 2 | 1 sem | Portfolio | CRUD projets complet |
| Sprint 3 | 1 sem | Compétences | Section skills |
| Sprint 4 | 1 sem | Contact | Formulaire + CRM |
| Sprint 5 | 1 sem | Avancé | Analytics, IA, API |

**Durée totale estimée :** 5 semaines

---

## 7. Risques et Mitigation

| Risque | Probabilité | Impact | Mitigation |
|--------|--------------|--------|-------------|
| Délais trop courts | Moyenne | Élevé | Buffer de 20% par sprint |
| Complexité IA | Haute | Moyen | Simplifier le chatbot |
| Performance | Basse | Moyen | Optimisation images |
| Sécurité | Moyenne | Élevé | Mise à jour dépendances |

---

## 8. Glossaire

| Terme | Définition |
|-------|-------------|
| **Backlog** | Liste des fonctionnalités à développer |
| **Sprint** | Cycle de développement (1-4 semaines) |
| **User Story** | Description d'une fonctionnalité du point de vue utilisateur |
| **MVP** | Minimum Viable Product — Version minimale fonctionnelle |
| **CRUD** | Create, Read, Update, Delete |

---

## 9. Annexes

### 9.1 Wireframes (à venir)

- Page d'accueil
- Page projets
- Page compétences
- Formulaire de contact
- Dashboard analytics

### 9.2 Charte Graphique (à venir)

- Couleurs principales
- Typographie
- Icônes
- Images

---

**Document généré le 23 Avril 2026**  
*Méthode Agile — Approche itérative et incrémentale*