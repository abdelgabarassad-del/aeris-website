# -*- coding: utf-8 -*-
import json
import re

new_questions = {
  1: [
    {
      "id": "l1_q11",
      "question": "Complétez avec l'article partitif correct : Hannah boit _____ eau minérale avant la session de test.",
      "options": ["de l'", "du", "de la", "des"],
      "correct": 0,
      "explanation": "Before a feminine or masculine singular noun beginning with a vowel, the partitive article is \"de l'\" (de l'eau)."
    },
    {
      "id": "l1_q12",
      "question": "Quel est le genre grammatical du mot \"problème\" en français ?",
      "options": ["Masculin (un problème)", "Féminin (une problème)", "Neutre", "Variable"],
      "correct": 0,
      "explanation": "Despite ending in \"-ème\", \"problème\" is masculine: on dit \"un problème\", \"le problème\"."
    },
    {
      "id": "l1_q13",
      "question": "Quel est le pluriel irrégulier du mot \"un œil\" ?",
      "options": ["Des œils", "Des yeux", "Des œils-de-bœuf", "Des yoeux"],
      "correct": 1,
      "explanation": "The plural of \"un œil\" (an eye) is \"des yeux\"."
    },
    {
      "id": "l1_q14",
      "question": "Complétez : L'équipe A.E.R.I.S. participe à une compétition _____ France et _____ Maroc.",
      "options": ["en / au", "à la / en", "au / à", "dans / au"],
      "correct": 0,
      "explanation": "Feminine country names use \"en\" (en France), while masculine country names use \"au\" (au Maroc)."
    },
    {
      "id": "l1_q15",
      "question": "Choisissez l'adjectif démonstratif correct : Regarde _____ oiseau voler au-dessus de nous.",
      "options": ["ce", "cet", "cette", "ces"],
      "correct": 1,
      "explanation": "Before a masculine singular noun starting with a vowel or silent h, \"ce\" becomes \"cet\" (cet oiseau)."
    },
    {
      "id": "l1_q16",
      "question": "Complétez : Hannah discute avec _____ amie ingénieure.",
      "options": ["sa", "son", "ses", "leur"],
      "correct": 1,
      "explanation": "Before a feminine singular noun starting with a vowel (\"amie\"), we use \"mon/ton/son\" instead of \"ma/ta/sa\" for euphony."
    },
    {
      "id": "l1_q17",
      "question": "Complétez la négation : Je n'ai _____ compris aux interférences électromagnétiques.",
      "options": ["jamais", "rien", "personne", "aucun"],
      "correct": 1,
      "explanation": "\"Ne... rien\" expresses \"nothing\" / \"not anything\": \"Je n'ai rien compris\" (I understood nothing)."
    },
    {
      "id": "l1_q18",
      "question": "Choisissez l'accord de couleur correct : Les fils électriques sont _____ et les connecteurs sont _____.",
      "options": ["marrons / oranges", "marron / orange", "marron / oranges", "marrons / orange"],
      "correct": 1,
      "explanation": "Colors derived from real-world objects/fruits like \"marron\" (chestnut) and \"orange\" remain invariable in the plural."
    },
    {
      "id": "l1_q19",
      "question": "Choisissez l'orthographe correcte : Nous _____ les calculs de poussée.",
      "options": ["commencons", "commençons", "commençont", "commençons-nous"],
      "correct": 1,
      "explanation": "Verbs in \"-cer\" take a cedilla (ç) before \"o\" and \"a\" to preserve the soft [s] sound: \"nous commençons\"."
    },
    {
      "id": "l1_q20",
      "question": "Il est 12h30. Quelle est l'expression correcte en français ?",
      "options": ["Il est midi et demie", "Il est midi et demi", "Il est douze heures demi", "Il est midi avec demi"],
      "correct": 1,
      "explanation": "\"Midi\" is masculine, so \"demi\" agrees in the masculine: \"midi et demi\" (unlike \"une heure et demie\")."
    },
    {
      "id": "l1_q21",
      "question": "Choisissez le pronom tonique : C'est _____ qui ai conçu la carte de distribution de puissance.",
      "options": ["moi", "je", "lui", "toi"],
      "correct": 0,
      "explanation": "After \"c'est\", we use tonic pronouns. Since the conjugated verb is \"ai\" (1st person), the tonic pronoun is \"moi\" (C'est moi qui...)."
    },
    {
      "id": "l1_q22",
      "question": "Quel est le genre du mot \"système\" en français ?",
      "options": ["Masculin (un système)", "Féminin (une système)", "Neutre", "Indéfini"],
      "correct": 0,
      "explanation": "Like many Greek-origin words ending in \"-ème\", \"système\" is masculine: \"un système embarqué\"."
    },
    {
      "id": "l1_q23",
      "question": "Quelle préposition indique la position intermédiaire : Le capteur est situé _____ la batterie et le contrôleur.",
      "options": ["parmi", "entre", "vers", "contre"],
      "correct": 1,
      "explanation": "\"Entre\" is used when locating an element between two distinct items."
    },
    {
      "id": "l1_q24",
      "question": "Complétez l'interrogation de quantité : _____ de voltmètres possédez-vous dans l'atelier ?",
      "options": ["Combien", "Comment", "Pourquoi", "Quel"],
      "correct": 0,
      "explanation": "\"Combien de\" is the standard interrogative structure used to ask \"how much / how many\"."
    },
    {
      "id": "l1_q25",
      "question": "Choisissez la forme correcte du verbe \"ranger\" : Nous _____ les outils après les essais.",
      "options": ["rangons", "rangeons", "rangeont", "rangez"],
      "correct": 1,
      "explanation": "Verbs ending in \"-ger\" keep an \"e\" before \"o\" (nous rangeons, nous mangeons) to maintain the soft [ʒ] sound."
    },
    {
      "id": "l1_q26",
      "question": "Comment dit-on \"Thursday\" en français ?",
      "options": ["Mardi", "Mercredi", "Jeudi", "Vendredi"],
      "correct": 2,
      "explanation": "Thursday is \"Jeudi\" in French (from Latin Dies Jovis)."
    },
    {
      "id": "l1_q27",
      "question": "Complétez : Il y a _____ bruit dans la soufflerie pendant le test aérodynamique.",
      "options": ["beaucoup de", "beaucoup du", "très de", "trop du"],
      "correct": 0,
      "explanation": "Adverbs of quantity (beaucoup, peu, trop, assez) are followed by \"de\" without an article: \"beaucoup de bruit\"."
    },
    {
      "id": "l1_q28",
      "question": "Quelle est la forme d'inversion interrogative correcte pour \"Tu viens au labo\" ?",
      "options": ["Viens-tu au labo ?", "Est-ce tu viens au labo ?", "Tu viens-tu au labo ?", "Viens tu au labo ?"],
      "correct": 0,
      "explanation": "Subject-verb inversion requires a hyphen between verb and pronoun: \"Viens-tu au labo ?\""
    },
    {
      "id": "l1_q29",
      "question": "Pour demander poliment un outil à un collègue, quelle formule est la plus polie ?",
      "options": ["Donne-moi le tournevis immédiatement.", "Pourriez-vous me passer le tournevis, s'il vous plaît ?", "Je veux le tournevis.", "Passe le tournevis."],
      "correct": 1,
      "explanation": "The conditional present \"Pourriez-vous... s'il vous plaît ?\" is the standard formula of French politeness."
    },
    {
      "id": "l1_q30",
      "question": "Comment s'écrit le nombre 80 en toutes lettres selon la règle d'orthographe classique ?",
      "options": ["Quatre-vingt", "Quatre-vingts", "Octante", "Quatres-vingts"],
      "correct": 1,
      "explanation": "\"Vingt\" takes an \"s\" in \"quatre-vingts\" when it multiplies 20 and is not followed by another number."
    }
  ],
  2: [
    {
      "id": "l2_q11",
      "question": "Choisissez le temps correct : Pendant qu'Hannah _____ le circuit imprimé, une alerte est apparue.",
      "options": ["soudait", "a soudé", "soudera", "soude"],
      "correct": 0,
      "explanation": "The background ongoing action in the past takes the imparfait (\"soudait\"), while the sudden interrupting event takes the passé composé (\"est apparue\")."
    },
    {
      "id": "l2_q12",
      "question": "Complétez avec le pronom COD : Les nouveaux capteurs gyroscopiques, Hannah _____ a installés ce matin.",
      "options": ["les", "leur", "en", "y"],
      "correct": 0,
      "explanation": "\"Les capteurs\" is a plural direct object (COD). It is replaced by \"les\". Note the past participle agreement: \"installés\"."
    },
    {
      "id": "l2_q13",
      "question": "Complétez avec le pronom COI : Hannah a parlé aux ingénieurs ? - Oui, elle _____ a expliqué le protocole.",
      "options": ["les", "leur", "lui", "y"],
      "correct": 1,
      "explanation": "\"Aux ingénieurs\" is plural indirect object (à + persons). The indirect object pronoun is \"leur\"."
    },
    {
      "id": "l2_q14",
      "question": "Complétez avec le pronom approprié : Penses-tu à l'inspection de sécurité ? - Oui, j'_____ pense sans cesse.",
      "options": ["y", "en", "le", "la"],
      "correct": 0,
      "explanation": "The verb \"penser à + chose\" is replaced by the adverbial pronoun \"y\": \"J'y pense\"."
    },
    {
      "id": "l2_q15",
      "question": "Complétez : As-tu besoin de résistances de 10k ohms ? - Oui, j'_____ ai besoin de plusieurs.",
      "options": ["y", "en", "les", "de ça"],
      "correct": 1,
      "explanation": "The expression \"avoir besoin de + chose/quantité\" is replaced by the pronoun \"en\": \"J'en ai besoin\"."
    },
    {
      "id": "l2_q16",
      "question": "Quelle est la forme du futur simple du verbe \"pouvoir\" pour \"nous\" ?",
      "options": ["pouvons", "pourrons", "pourrions", "pouvrons"],
      "correct": 1,
      "explanation": "The stem for \"pouvoir\" in future simple is \"pourr-\", giving \"nous pourrons\"."
    },
    {
      "id": "l2_q17",
      "question": "Choisissez le comparatif correct : Le nouveau moteur brushless a un _____ rendement que l'ancien.",
      "options": ["plus bon", "meilleur", "mieux", "plus meilleur"],
      "correct": 1,
      "explanation": "The comparative of the adjective \"bon\" is \"meilleur\" (never \"plus bon\")."
    },
    {
      "id": "l2_q18",
      "question": "Que signifie l'expression \"un ancien bâtiment\" par rapport à \"un bâtiment ancien\" ?",
      "options": ["Un ancien bâtiment = un vieux bâtiment ; Un bâtiment ancien = un ex-bâtiment", "Un ancien bâtiment = un précédent bâtiment ; Un bâtiment ancien = un vieux bâtiment", "Les deux ont exactement le même sens", "Un ancien bâtiment est plus moderne"],
      "correct": 1,
      "explanation": "Placed before the noun, \"ancien\" means former/previous (\"un ancien bâtiment\"); placed after, it means old/historic (\"un bâtiment ancien\")."
    },
    {
      "id": "l2_q19",
      "question": "Complétez : Hannah travaille sur ce microcontrôleur _____ trois heures et elle n'a pas fini.",
      "options": ["pendant", "depuis", "dans", "pour"],
      "correct": 1,
      "explanation": "\"Depuis\" denotes an action that started in the past and is still ongoing in the present."
    },
    {
      "id": "l2_q20",
      "question": "Choisissez l'auxiliaire correct : Hannah _____ descendue au sous-sol pour chercher l'oscilloscope.",
      "options": ["a", "est", "avait", "serait"],
      "correct": 1,
      "explanation": "Used intransitively (movement without direct object), \"descendre\" conjugates with \"être\": \"elle est descendue\"."
    },
    {
      "id": "l2_q21",
      "question": "Attention au faux ami ! En français, que signifie le mot \"actuellement\" ?",
      "options": ["En réalité / en fait", "À l'heure actuelle / en ce moment", "Éventuellement", "Certainement"],
      "correct": 1,
      "explanation": "\"Actuellement\" means \"currently / at present\". To say \"actually / in fact\", French uses \"en réalité\" or \"en fait\"."
    },
    {
      "id": "l2_q22",
      "question": "Choisissez le pronom relatif correct : Le schéma électrique _____ nous avons discuté est sur la table.",
      "options": ["que", "qui", "dont", "où"],
      "correct": 2,
      "explanation": "Since we say \"discuter de quelque chose\", the relative pronoun replacing \"de + nom\" is \"dont\"."
    },
    {
      "id": "l2_q23",
      "question": "Complétez avec le superlatif de l'adverbe \"bien\" : De toute l'équipe, c'est Hannah qui soude le _____.",
      "options": ["plus bon", "meilleur", "mieux", "plus bien"],
      "correct": 2,
      "explanation": "The comparative/superlative of the adverb \"bien\" is \"mieux\" (\"le mieux\")."
    },
    {
      "id": "l2_q24",
      "question": "Accord du verbe pronominal réfléchi : Les deux ingénieures se sont _____ des félicitations mutuelles.",
      "options": ["donné", "donnée", "données", "donnés"],
      "correct": 0,
      "explanation": "The direct object (COD) is \"des félicitations\", placed AFTER the verb. Therefore, the past participle \"donné\" does not agree with \"se\"."
    },
    {
      "id": "l2_q25",
      "question": "Quelle phrase exprime un conseil poli au conditionnel présent ?",
      "options": ["Tu dois vérifier la tension.", "Tu devrais vérifier la tension de la batterie.", "Tu as dû vérifier la tension.", "Tu devras vérifier la tension."],
      "correct": 1,
      "explanation": "\"Tu devrais...\" (conditional present of devoir) softens the obligation into a polite recommendation."
    },
    {
      "id": "l2_q26",
      "question": "Mettez à la voix passive : \"L'équipe assemble le fuselage du drone.\"",
      "options": ["Le fuselage du drone est assemblé par l'équipe.", "Le fuselage du drone sera assemblé par l'équipe.", "Le fuselage du drone a été assemblé par l'équipe.", "L'équipe est assemblée par le fuselage."],
      "correct": 0,
      "explanation": "Present indicative passive voice: \"est assemblé par...\"."
    },
    {
      "id": "l2_q27",
      "question": "Choisissez la préposition correcte : Hannah se rend au centre d'essais en vol _____ train.",
      "options": ["à", "en", "par", "dans le"],
      "correct": 1,
      "explanation": "Vehicles one enters inside generally take \"en\" (en train, en voiture, en avion)."
    },
    {
      "id": "l2_q28",
      "question": "Complétez la phrase négative : \"Qui a touché au fer à souder ?\" -> \"_____ n'y a touché.\"",
      "options": ["Rien", "Personne", "Jamais", "Aucunement"],
      "correct": 1,
      "explanation": "When answering a question about persons (\"Qui\"), the subject negative pronoun is \"Personne ne...\"."
    },
    {
      "id": "l2_q29",
      "question": "Quelle est la forme impérative affirmative correcte pour le verbe pronominal \"se dépêcher\" à la 2e personne du pluriel ?",
      "options": ["Vous dépêchez !", "Dépêchez-vous !", "Dépêchez vous !", "Se dépêchez !"],
      "correct": 1,
      "explanation": "In affirmative imperative for pronominal verbs, the pronoun follows the verb with a hyphen: \"Dépêchez-vous !\"."
    },
    {
      "id": "l2_q30",
      "question": "Quelle phrase utilise correctement le futur proche ?",
      "options": ["Hannah va calibrer les capteurs dans un instant.", "Hannah calibrera les capteurs.", "Hannah a calibré les capteurs.", "Hannah vient de calibrer les capteurs."],
      "correct": 0,
      "explanation": "The futur proche is formed with \"aller + infinitif\": \"va calibrer\"."
    }
  ],
  3: [
    {
      "id": "l3_q11",
      "question": "Choisissez l'accord du participe passé : Les cartes électroniques qu'Hannah a _____ fonctionnent parfaitement.",
      "options": ["conçu", "conçue", "conçus", "conçues"],
      "correct": 3,
      "explanation": "The direct object relative \"que\" refers to \"les cartes électroniques\" (feminine plural) and precedes the verb. The past participle must agree: \"conçues\"."
    },
    {
      "id": "l3_q12",
      "question": "Accord avec le pronom \"en\" : Des microcontrôleurs STM32, combien en as-tu _____ ?",
      "options": ["commandé", "commandée", "commandés", "commandées"],
      "correct": 0,
      "explanation": "The pronoun \"en\" does not trigger past participle agreement. The participle remains invariable: \"commandé\"."
    },
    {
      "id": "l3_q13",
      "question": "Accord du verbe pronominal réciproque : Les cheffes de pôle se sont _____ lors de la réunion de cadrage.",
      "options": ["parlé", "parlée", "parlés", "parlées"],
      "correct": 0,
      "explanation": "Since one says \"parler à quelqu'un\" (indirect object), \"se\" is COI. The past participle remains invariable: \"parlé\"."
    },
    {
      "id": "l3_q14",
      "question": "Accord du verbe pronominal réfléchi : Hannah s'est _____ les mains avec soin avant de souder les puces CMS.",
      "options": ["lavé", "lavée", "lavés", "lavées"],
      "correct": 0,
      "explanation": "The direct object (COD) is \"les mains\", located AFTER the verb. Therefore, the participle remains invariable: \"lavé\"."
    },
    {
      "id": "l3_q15",
      "question": "Complétez avec le mode subjonctif : Je suis ravi que vous _____ présents pour ce vol inaugural.",
      "options": ["êtes", "soyez", "seriez", "fûtes"],
      "correct": 1,
      "explanation": "Expressions of emotion/feeling (\"être ravi que\") require the subjunctive present: \"que vous soyez\"."
    },
    {
      "id": "l3_q16",
      "question": "Subjonctif ou Indicatif : Je ne pense pas que ce moteur _____ assez puissant.",
      "options": ["est", "soit", "sera", "était"],
      "correct": 1,
      "explanation": "Verbs of opinion used in the negative form (\"ne pas penser que\") express doubt and mandate the subjunctive mood: \"soit\"."
    },
    {
      "id": "l3_q17",
      "question": "Complétez : Coupez l'alimentation principale avant que le court-circuit ne _____ les composants.",
      "options": ["détruit", "détruise", "détruira", "détruisait"],
      "correct": 1,
      "explanation": "The conjunction \"avant que\" always mandates the subjunctive mood: \"détruise\"."
    },
    {
      "id": "l3_q18",
      "question": "Règle classique de l'Académie : Choisissez le mode correct après \"après que\" : Nous avons décollé après que la pluie _____.",
      "options": ["a cessé", "ait cessé", "cesse", "soit cessée"],
      "correct": 0,
      "explanation": "According to standard French grammar, \"après que\" expresses a completed fact and requires the indicative mood (passé composé: \"a cessé\"), not the subjunctive."
    },
    {
      "id": "l3_q19",
      "question": "Exprimez le regret / reproche au conditionnel passé : Vous _____ calibrer le compas avant le décollage !",
      "options": ["deviez", "auriez dû", "aurez dû", "eussiez dû"],
      "correct": 1,
      "explanation": "Conditional past (\"auriez dû + infinitif\") is the standard structure to express a retrospective reproach or regret."
    },
    {
      "id": "l3_q20",
      "question": "Quelle phrase utilise correctement le gérondif pour exprimer la simultanéité et le moyen ?",
      "options": ["C'est en mesurant le courant qu'Hannah a localisé la panne.", "En mesuré le courant, elle a trouvé la panne.", "Par mesurant le courant, elle a trouvé la panne.", "Mesurant le courant, elle trouvait la panne."],
      "correct": 0,
      "explanation": "The gérondif is formed with \"en + participe présent\": \"en mesurant\"."
    },
    {
      "id": "l3_q21",
      "question": "Concordance des temps au discours indirect : Hannah a annoncé : \"Je terminerai le banc de test ce soir.\" -> Hannah a annoncé qu'elle _____ le banc de test ce soir-là.",
      "options": ["terminera", "terminerait", "avait terminé", "termine"],
      "correct": 1,
      "explanation": "When the reporting verb is in the past (\"a annoncé\"), future simple transforms into conditional present (\"terminerait\")."
    },
    {
      "id": "l3_q22",
      "question": "Concession / Opposition : _____ les perturbations magnétiques, le drone a maintenu son cap.",
      "options": ["Bien que", "Malgré", "Quoique", "Pourtant"],
      "correct": 1,
      "explanation": "\"Malgré\" is followed directly by a noun phrase (\"les perturbations magnétiques\"), while \"bien que\" requires a clause with a conjugated verb in the subjunctive."
    },
    {
      "id": "l3_q23",
      "question": "Attention au faux ami : Dans la phrase \"Hannah assiste à la réunion des chefs de département\", que signifie \"assiste à\" ?",
      "options": ["Elle aide les chefs de département", "Elle est présente / participe comme auditrice", "Elle organise la réunion", "Elle refuse de venir"],
      "correct": 1,
      "explanation": "\"Assister à\" means \"to attend / be present at\". \"To assist/help\" translates to \"aider\" or \"porter assistance\"."
    },
    {
      "id": "l3_q24",
      "question": "Que signifie l'expression idiomatique \"mettre les bouchées doubles\" ?",
      "options": ["Manger deux fois plus à midi", "Accélérer considérablement son travail pour rattraper un retard", "Augmenter le prix du drone", "Diviser les tâches en deux parts égales"],
      "correct": 1,
      "explanation": "This idiom means speeding up efforts significantly to achieve an objective in time."
    },
    {
      "id": "l3_q25",
      "question": "Complétez avec la préposition appropriée : Hannah a réussi _____ stabiliser la boucle d'asservissement PID.",
      "options": ["à", "de", "pour", "en"],
      "correct": 0,
      "explanation": "The verb construction is \"réussir à faire quelque chose\"."
    },
    {
      "id": "l3_q26",
      "question": "Complétez : L'équipe de pilotage a décidé _____ reporter les essais en vol.",
      "options": ["à", "de", "pour", "sur"],
      "correct": 1,
      "explanation": "The verb construction is \"décider de faire quelque chose\"."
    },
    {
      "id": "l3_q27",
      "question": "Quel adverbe correspond à l'adjectif \"courant\" ?",
      "options": ["Couramment", "Courament", "Couramment-ment", "Couradement"],
      "correct": 0,
      "explanation": "Adjectives ending in \"-ant\" form adverbs in \"-amment\": \"courant -> couramment\"."
    },
    {
      "id": "l3_q28",
      "question": "Complétez avec le pronom relatif composé : L'objectif _____ aspire notre division est l'autonomie complète.",
      "options": ["auquel", "duquel", "dans lequel", "par lequel"],
      "correct": 0,
      "explanation": "The construction is \"aspirer à quelque chose\". With a masculine noun (\"l'objectif\"), \"à + lequel\" contracts to \"auquel\"."
    },
    {
      "id": "l3_q29",
      "question": "Ordre des pronoms à l'impératif affirmatif : \"Tu me donnes le voltmètre.\" -> À l'impératif affirmatif, on dit :",
      "options": ["Donne-moi-le !", "Donne-le-moi !", "Me le donne !", "Donne le me !"],
      "correct": 1,
      "explanation": "In affirmative imperative, the direct object pronoun precedes the indirect: \"Donne-le-moi !\"."
    },
    {
      "id": "l3_q30",
      "question": "Complétez avec le subjonctif : Il est indispensable que nous _____ toutes les données télémétriques.",
      "options": ["recueillons", "recueillions", "recueillerons", "recueillirions"],
      "correct": 1,
      "explanation": "The subjunctive present of \"recueillir\" for \"nous\" is \"que nous recueillions\" (with \"-ions\")."
    }
  ],
  4: [
    {
      "id": "l4_q11",
      "question": "Accord du participe passé suivi d'un infinitif : Les ingénieures qu'Hannah a _____ travailler sur le banc d'essai sont brillantes.",
      "options": ["vu", "vue", "vus", "vues"],
      "correct": 3,
      "explanation": "Since \"les ingénieures\" (f. pl.) is the agent performing the action of the infinitive \"travailler\", the participle agrees: \"vues\"."
    },
    {
      "id": "l4_q12",
      "question": "Accord du participe passé suivi d'un infinitif : La pièce de rechange qu'Hannah a _____ remplacer est introuvable.",
      "options": ["entendu", "entendue", "entendus", "entendues"],
      "correct": 0,
      "explanation": "The preceding object \"la pièce\" undergoes the action (\"être remplacée\") rather than doing it. The participle remains invariable: \"entendu\" / \"vu\"."
    },
    {
      "id": "l4_q13",
      "question": "Règle absolue pour \"faire\" + infinitif : Ces maquettes de drone, l'équipe les a _____ fabriquer en impression 3D.",
      "options": ["faites", "fait", "faits", "faite"],
      "correct": 1,
      "explanation": "The past participle of \"faire\" followed by an infinitive is ALWAYS invariable: \"les a fait fabriquer\"."
    },
    {
      "id": "l4_q14",
      "question": "Accord avec les verbes de mesure et durée : Les dix minutes que ce vol stationnaire a _____ ont paru une éternité.",
      "options": ["duré", "durée", "durés", "durées"],
      "correct": 0,
      "explanation": "Verbs indicating duration, weight, or cost (durer, peser, coûter, valoir) are intransitive; \"les dix minutes\" is an adverbial complement, not a direct object. The participle is invariable: \"duré\"."
    },
    {
      "id": "l4_q15",
      "question": "Complétez avec le subjonctif passé : Bien qu'Hannah _____ son banc de test hier, elle procède à une ultime vérification.",
      "options": ["a terminé", "ait terminé", "eût terminé", "aura terminé"],
      "correct": 1,
      "explanation": "To express anteriority in a subordinate clause requiring the subjunctive (\"bien que\"), we use the subjonctif passé: \"ait terminé\"."
    },
    {
      "id": "l4_q16",
      "question": "Le \"ne\" explétif dans le registre soutenu : Hannah craint que le régulateur de tension ne _____ sous forte charge.",
      "options": ["chauffe", "chauffe pas", "ait chauffé", "chauffât"],
      "correct": 0,
      "explanation": "After verbs of fear in the affirmative (craindre, avoir peur), formal French uses the non-negative \"ne\" explétif with subjunctive present: \"ne chauffe\"."
    },
    {
      "id": "l4_q17",
      "question": "Pronom relatif composé avec préposition : L'entreprise aérospatiale pour _____ Hannah conçoit ce circuit est leader du marché.",
      "options": ["lequel", "laquelle", "lesquels", "desquelles"],
      "correct": 1,
      "explanation": "\"Pour + nom féminin singulier (l'entreprise)\" -> \"pour laquelle\"."
    },
    {
      "id": "l4_q18",
      "question": "Complétez : L'incident technique à la suite _____ le vol a été suspendu était mineur.",
      "options": ["duquel", "auquel", "de laquelle", "desquels"],
      "correct": 0,
      "explanation": "The prepositional locution is \"à la suite de\". Combined with the masculine noun \"l'incident\", \"de + lequel\" becomes \"duquel\"."
    },
    {
      "id": "l4_q19",
      "question": "Mode après \"au cas où\" : Au cas où une baisse de tension _____ observée, activez la batterie de secours.",
      "options": ["soit", "serait", "est", "sera"],
      "correct": 1,
      "explanation": "The conditional conjunction \"au cas où\" is always followed by the conditional mood: \"serait observée\"."
    },
    {
      "id": "l4_q20",
      "question": "Distinguez les homophones : \"_____ soient vos doutes, gardez confiance en votre méthode.\"",
      "options": ["Quels que", "Quelques", "Quel que", "Quoique"],
      "correct": 0,
      "explanation": "Before the subjunctive verb \"soient\", \"quel(le)s que\" is written in two words and agrees with the subject \"vos doutes\" (masc. pl. -> \"Quels que\")."
    },
    {
      "id": "l4_q21",
      "question": "Distinguez \"quoique\" et \"quoi que\" : \"_____ vous fassiez, respectez scrupuleusement les consignes de sécurité.\"",
      "options": ["Quoique", "Quoi que", "Quoi-que", "Quoi qu'"],
      "correct": 1,
      "explanation": "\"Quoi que\" (in two words) means \"whatever / whatever thing that\", whereas \"quoique\" (in one word) means \"although / bien que\"."
    },
    {
      "id": "l4_q22",
      "question": "Distinction lexicale précise : Hannah a _____ son multimètre de précision dans l'atelier (objet transportable à la main).",
      "options": ["amené", "apporté", "emmené", "emporté"],
      "correct": 1,
      "explanation": "One uses \"apporter\" for objects that can be carried to a destination. \"Amener\" is strictly reserved for people, animals, or non-portable vehicles."
    },
    {
      "id": "l4_q23",
      "question": "Orthographe / Paronymie : Hannah est _____ présenter son rapport d'architecture électrique à 14h.",
      "options": ["censée", "sensée", "sencée", "cencée"],
      "correct": 0,
      "explanation": "\"Censé\" (with c) means \"supposed to\". \"Sensé\" (with s) means \"sensible / endowed with good sense\"."
    },
    {
      "id": "l4_q24",
      "question": "Vocabulaire soutenu : Quel est le synonyme soutenu de \"une seconde fois\" ou \"de nouveau\" ?",
      "options": ["Derechef", "Naguère", "Tant s'en faut", "D'ores et déjà"],
      "correct": 0,
      "explanation": "\"Derechef\" is an elevated adverb meaning \"anew / once again / immediately afterwards\"."
    },
    {
      "id": "l4_q25",
      "question": "Que signifie l'expression proverbiale \"tirer son épingle du jeu\" ?",
      "options": ["Jouer aux quilles avec adresse", "Se dégager habilement d'une situation complexe en préservant ses intérêts", "Tricher lors d'un concours", "Abandonner prématurément une tâche"],
      "correct": 1,
      "explanation": "This idiom means skillfully extricating oneself from a tricky situation while retaining an advantage."
    },
    {
      "id": "l4_q26",
      "question": "Complétez : Les essais auront lieu demain, à condition que la vitesse du vent _____ inférieure à 20 km/h.",
      "options": ["est", "soit", "sera", "fût"],
      "correct": 1,
      "explanation": "The conjunction \"à condition que\" requires the subjunctive mood: \"soit\"."
    },
    {
      "id": "l4_q27",
      "question": "Complétez : Le drone a atterri sans qu'aucun dommage ne _____ constaté sur le train d'atterrissage.",
      "options": ["soit", "est", "sera", "fut"],
      "correct": 0,
      "explanation": "\"Sans que\" always mandates the subjunctive mood: \"ne soit constaté\"."
    },
    {
      "id": "l4_q28",
      "question": "Nuance de liaison : Dans \"Ce prototype est prometteur, voire révolutionnaire\", que signifie \"voire\" ?",
      "options": ["C'est-à-dire", "Et même", "Au contraire", "Pour voir"],
      "correct": 1,
      "explanation": "\"Voire\" (from Old French \"voire\" = truly) means \"and even / and indeed\"."
    },
    {
      "id": "l4_q29",
      "question": "Que signifie l'expression soutenue \"avoir voix au chapitre\" ?",
      "options": ["Avoir une voix très puissante pour chanter", "Avoir le droit et l'autorité d'exprimer son avis et de participer à une décision", "Lire à voix haute un chapitre de livre", "Présider une cérémonie religieuse"],
      "correct": 1,
      "explanation": "Historically from monastic chapters where monks had voting rights, it means having an authoritative say in deliberations."
    },
    {
      "id": "l4_q30",
      "question": "Accord de l'adjectif verbal : Des signaux très _____ (stimuler) ont été détectés par le récepteur télémétrique.",
      "options": ["stimulants", "stimulans", "stimulants-ci", "stimulatifs"],
      "correct": 0,
      "explanation": "The verbal adjective agrees in gender and number: \"des signaux stimulants\"."
    }
  ],
  5: [
    {
      "id": "l5_q11",
      "question": "Conjugaison littéraire (Passé simple) : Dès qu'Hannah aperçut la surchauffe, elle _____ immédiatement l'alimentation.",
      "options": ["éteigna", "éteignit", "éteignat", "éteignît"],
      "correct": 1,
      "explanation": "The passé simple 3rd person singular of \"éteindre\" is \"elle éteignit\" (without circumflex)."
    },
    {
      "id": "l5_q12",
      "question": "Passé simple du verbe \"convaincre\" : Hannah _____ le jury par la rigueur de sa méthodologie.",
      "options": ["convainquit", "convainqua", "convaint", "convaincit"],
      "correct": 0,
      "explanation": "Verbs in \"-vaincre\" form their passé simple with \"-qui-\": \"elle convainquit\"."
    },
    {
      "id": "l5_q13",
      "question": "Passé simple du verbe \"acquérir\" : L'équipe A.E.R.I.S. _____ une solide réputation internationale.",
      "options": ["acquira", "acquit", "acquérut", "acquît"],
      "correct": 1,
      "explanation": "The passé simple of \"acquérir\" is \"il/elle acquit\" (3rd person singular)."
    },
    {
      "id": "l5_q14",
      "question": "Subjonctif imparfait dans la langue classique : Il eût fallu qu'Hannah _____ la documentation avant le test.",
      "options": ["lise", "lût", "lisît", "luise"],
      "correct": 1,
      "explanation": "In classical literary sequence of tenses after a past conditional, the subjunctive imperfect of \"lire\" is \"qu'elle lût\" (with circumflex on the û)."
    },
    {
      "id": "l5_q15",
      "question": "Accord du verbe avec un sujet collectif : La plupart des ingénieurs _____ la validation du nouveau banc d'essai.",
      "options": ["approuve", "approuvent", "approuveront seul", "a approuvé"],
      "correct": 1,
      "explanation": "With \"la plupart de\" followed by a plural noun, the verb ALWAYS agrees in the plural: \"approuvent\"."
    },
    {
      "id": "l5_q16",
      "question": "Règle d'accord spécifique : \"Plus d'un technicien _____ salué l'ingéniosité d'Hannah.\"",
      "options": ["ont", "a", "avaient", "furent"],
      "correct": 1,
      "explanation": "Grammatically, \"plus d'un\" takes a singular verb: \"plus d'un technicien a salué\" (unlike \"moins de deux\")."
    },
    {
      "id": "l5_q17",
      "question": "Orthographe contrastée : Participe présent vs Adjectif verbal : \"Une preuve particulièrement _____ (convaincre).\"",
      "options": ["convainquante", "convaincante", "convainquante-ci", "convainquante"],
      "correct": 1,
      "explanation": "The verbal adjective is spelled \"convaincant(e)\" (with a c), whereas the present participle is \"convainquant\" (with qu)."
    },
    {
      "id": "l5_q18",
      "question": "Accord des adjectifs de couleur composés : Hannah a choisi des hélices de drone _____ pour ses prototypes.",
      "options": ["bleu marine", "bleues marines", "bleues marine", "bleu marines"],
      "correct": 0,
      "explanation": "Compound color adjectives (bleu marine, vert clair, jaune poussin) are totally INVARIABLE."
    },
    {
      "id": "l5_q19",
      "question": "Inversion du sujet après adverbe initial : À peine l'impulsion fut-elle donnée que le moteur _____ son régime maximal.",
      "options": ["atteignit", "atteindra", "atteignait", "atteindrait"],
      "correct": 0,
      "explanation": "In narrative past after \"à peine... que\", we use the passé simple: \"atteignit\"."
    },
    {
      "id": "l5_q20",
      "question": "Pluriel des noms composés : Dans le laboratoire se trouvent plusieurs _____ de haute technologie.",
      "options": ["chefs-d'œuvre", "chef-d'œuvres", "chefs-d'œuvres", "chef-d'œuvre"],
      "correct": 0,
      "explanation": "In \"chef-d'œuvre\", only \"chef\" takes the plural \"s\"; \"d'œuvre\" is an invariable prepositional complement: \"des chefs-d'œuvre\"."
    },
    {
      "id": "l5_q21",
      "question": "Paronymie avancée : Des hypothèses formulées sans mesures empiriques relèvent de la pure _____ (et non de la conjoncture).",
      "options": ["conjecture", "conjoncture", "conjonction", "concrétion"],
      "correct": 0,
      "explanation": "\"Une conjecture\" is an opinion founded on probabilities or guesswork. \"Une conjoncture\" refers to the economic or geopolitical climate."
    },
    {
      "id": "l5_q22",
      "question": "Figure de style : \"Ce schéma de câblage n'est pas dénué d'élégance\" pour signifier qu'il est extrêmement élégant est :",
      "options": ["Une litote", "Une métaphore", "Une anaphore", "Un oxymore"],
      "correct": 0,
      "explanation": "A litote understates an idea to emphasize and intensify the positive meaning (\"saying less to mean more\")."
    },
    {
      "id": "l5_q23",
      "question": "Figure de style (Zeugme) : \"Hannah a gardé son calme et le contrôle du drone.\" De quelle figure s'agit-il ?",
      "options": ["Un zeugme (ou attelage)", "Une métonymie", "Un chiasme", "Une antiphrase"],
      "correct": 0,
      "explanation": "A zeugme links two words with different figurative and concrete meanings to the same verb (\"garder son calme / garder le contrôle\")."
    },
    {
      "id": "l5_q24",
      "question": "Connecteur soutenu : \"_____ les intempéries, la mission de reconnaissance aérienne a été couronnée de succès.\"",
      "options": ["Nonobstant", "Attendu que", "Quoiqu'à", "Envers"],
      "correct": 0,
      "explanation": "\"Nonobstant\" is a formal, legal and literary preposition meaning \"in spite of / notwithstanding\" (synonym of malgré)."
    },
    {
      "id": "l5_q25",
      "question": "Subjonctif après superlatif relatif : \"C'est le vol le plus impressionnant que nous _____ jamais accompli.\"",
      "options": ["ayons", "avons", "aurons", "aurions"],
      "correct": 0,
      "explanation": "Relative clauses depending on a superlative (\"le plus...\", \"le seul...\", \"l'unique...\") traditionally take the subjunctive mood: \"ayons accompli\"."
    },
    {
      "id": "l5_q26",
      "question": "Conditionnel passé 2e forme (style classique) : \"S'il avait été prévenu, l'ingénieur _____ prêté son concours.\"",
      "options": ["eût", "eut", "aurait eu", "eût été"],
      "correct": 0,
      "explanation": "The conditional past 2nd form uses the subjunctive plus-que-parfait auxiliary: \"il eût prêté\" (= \"il aurait prêté\")."
    },
    {
      "id": "l5_q27",
      "question": "Conjugaison d'un verbe défectif : Quelle est la forme correcte de 3e personne du singulier au présent de l'indicatif du verbe \"gésir\" (être étendu/gisant) ?",
      "options": ["Il gît", "Il gèse", "Il git", "Il gisse"],
      "correct": 0,
      "explanation": "The 3rd person singular present of \"gésir\" is \"il gît\" (with circumflex: Ci-gît...)."
    },
    {
      "id": "l5_q28",
      "question": "Connecteur de conséquence soutenu : \"La liaison radio est rompue, _____ le pilote automatique déclenche le retour au point de départ.\"",
      "options": ["partant", "cependant", "nonobstant", "quoique"],
      "correct": 0,
      "explanation": "In literary French, \"partant\" (adverb) means \"consequently / therefore / de ce fait\"."
    },
    {
      "id": "l5_q29",
      "question": "Paronymie : \"Cette interférence risque d'_____ gravement la transmission télémétrique.\"",
      "options": ["infecter", "infester", "affecter", "effectuer"],
      "correct": 2,
      "explanation": "\"Affecter\" means to influence or alter adversely. \"Infecter\" means contaminating with disease, and \"infester\" means invading in large destructive numbers."
    },
    {
      "id": "l5_q30",
      "question": "Subjonctif imparfait du verbe \"pouvoir\" : \"Le chef d'équipe doutait qu'Hannah _____ achever le prototype à temps.\"",
      "options": ["pût", "pouvait", "puisse", "pût-elle"],
      "correct": 0,
      "explanation": "The subjunctive imperfect 3rd person singular of \"pouvoir\" is \"qu'elle pût\" (with circumflex accent on the û)."
    }
  ]
}
