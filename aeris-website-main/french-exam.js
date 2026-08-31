/**
 * Hannah's French Challenge - Adaptive Exam Engine
 * Built for A.E.R.I.S. UAV Team
 */

(function() {
  // ==========================================
  // 1. QUESTION POOL (150 Questions, 5 Levels)
  // ==========================================
  const questionPool = {
    "1": [
        {
            "id": "l1_q1",
            "question": "Comment dit-on 'Thank you very much' en français ?",
            "options": [
                "De rien",
                "Merci beaucoup",
                "S'il vous plaît",
                "Bonjour"
            ],
            "correct": 1,
            "explanation": "'Merci beaucoup' is the direct translation of 'Thank you very much'. 'De rien' means 'You're welcome'."
        },
        {
            "id": "l1_q2",
            "question": "Quelle couleur obtient-on en mélangeant le bleu et le jaune ?",
            "options": [
                "Rouge",
                "Vert",
                "Orange",
                "Violet"
            ],
            "correct": 1,
            "explanation": "Blue and yellow make green ('vert' in French)."
        },
        {
            "id": "l1_q3",
            "question": "Comment dit-on 'The sky' en français ?",
            "options": [
                "Le soleil",
                "La lune",
                "Le ciel",
                "La terre"
            ],
            "correct": 2,
            "explanation": "'Le ciel' translates to 'The sky'."
        },
        {
            "id": "l1_q4",
            "question": "Traduisez le mot 'A bird' en français.",
            "options": [
                "Un oiseau",
                "Un poisson",
                "Un chat",
                "Un chien"
            ],
            "correct": 0,
            "explanation": "'Un oiseau' is a bird. 'Poisson' is fish, 'chat' is cat, and 'chien' is dog."
        },
        {
            "id": "l1_q5",
            "question": "Quel est le contraire du mot 'Grand' ?",
            "options": [
                "Moyen",
                "Petit",
                "Large",
                "Long"
            ],
            "correct": 1,
            "explanation": "'Petit' (small/short) is the opposite of 'Grand' (tall/big)."
        },
        {
            "id": "l1_q6",
            "question": "Comment dit-on 'Welcome' en français ?",
            "options": [
                "Au revoir",
                "S'il vous plaît",
                "Bienvenue",
                "Félicitations"
            ],
            "correct": 2,
            "explanation": "'Bienvenue' means welcome. 'Au revoir' means goodbye, and 'Félicitations' means congratulations."
        },
        {
            "id": "l1_q7",
            "question": "Quelle est la traduction française de 'Good morning' ?",
            "options": [
                "Bonsoir",
                "Bonne nuit",
                "Bonjour",
                "Bon après-midi"
            ],
            "correct": 2,
            "explanation": "'Bonjour' is used for 'good morning' or 'hello' during the day."
        },
        {
            "id": "l1_q8",
            "question": "Quel nombre correspond au mot 'Douze' ?",
            "options": [
                "2",
                "12",
                "20",
                "22"
            ],
            "correct": 1,
            "explanation": "'Douze' is the French word for 12."
        },
        {
            "id": "l1_q9",
            "question": "Comment dit-on 'Monday' en français ?",
            "options": [
                "Mardi",
                "Mercredi",
                "Lundi",
                "Dimanche"
            ],
            "correct": 2,
            "explanation": "The days of the week start with 'Lundi' (Monday)."
        },
        {
            "id": "l1_q10",
            "question": "Quelle est la traduction de 'The water' ?",
            "options": [
                "Le vin",
                "Le lait",
                "L'eau",
                "Le jus"
            ],
            "correct": 2,
            "explanation": "'L'eau' is the French word for water."
        },
        {
            "id": "l1_q11",
            "question": "Complétez avec l'article partitif correct : Hannah boit _____ eau minérale avant la session de test.",
            "options": [
                "de l'",
                "du",
                "de la",
                "des"
            ],
            "correct": 0,
            "explanation": "Before a feminine or masculine singular noun beginning with a vowel, the partitive article is \"de l'\" (de l'eau)."
        },
        {
            "id": "l1_q12",
            "question": "Quel est le genre grammatical du mot \"problème\" en français ?",
            "options": [
                "Masculin (un problème)",
                "Féminin (une problème)",
                "Neutre",
                "Variable"
            ],
            "correct": 0,
            "explanation": "Despite ending in \"-ème\", \"problème\" is masculine: on dit \"un problème\", \"le problème\"."
        },
        {
            "id": "l1_q13",
            "question": "Quel est le pluriel irrégulier du mot \"un œil\" ?",
            "options": [
                "Des œils",
                "Des yeux",
                "Des œils-de-bœuf",
                "Des yoeux"
            ],
            "correct": 1,
            "explanation": "The plural of \"un œil\" (an eye) is \"des yeux\"."
        },
        {
            "id": "l1_q14",
            "question": "Complétez : L'équipe A.E.R.I.S. participe à une compétition _____ France et _____ Maroc.",
            "options": [
                "en / au",
                "à la / en",
                "au / à",
                "dans / au"
            ],
            "correct": 0,
            "explanation": "Feminine country names use \"en\" (en France), while masculine country names use \"au\" (au Maroc)."
        },
        {
            "id": "l1_q15",
            "question": "Choisissez l'adjectif démonstratif correct : Regarde _____ oiseau voler au-dessus de nous.",
            "options": [
                "ce",
                "cet",
                "cette",
                "ces"
            ],
            "correct": 1,
            "explanation": "Before a masculine singular noun starting with a vowel or silent h, \"ce\" becomes \"cet\" (cet oiseau)."
        },
        {
            "id": "l1_q16",
            "question": "Complétez : Hannah discute avec _____ amie ingénieure.",
            "options": [
                "sa",
                "son",
                "ses",
                "leur"
            ],
            "correct": 1,
            "explanation": "Before a feminine singular noun starting with a vowel (\"amie\"), we use \"mon/ton/son\" instead of \"ma/ta/sa\" for euphony."
        },
        {
            "id": "l1_q17",
            "question": "Complétez la négation : Je n'ai _____ compris aux interférences électromagnétiques.",
            "options": [
                "jamais",
                "rien",
                "personne",
                "aucun"
            ],
            "correct": 1,
            "explanation": "\"Ne... rien\" expresses \"nothing\" / \"not anything\": \"Je n'ai rien compris\" (I understood nothing)."
        },
        {
            "id": "l1_q18",
            "question": "Choisissez l'accord de couleur correct : Les fils électriques sont _____ et les connecteurs sont _____.",
            "options": [
                "marrons / oranges",
                "marron / orange",
                "marron / oranges",
                "marrons / orange"
            ],
            "correct": 1,
            "explanation": "Colors derived from real-world objects/fruits like \"marron\" (chestnut) and \"orange\" remain invariable in the plural."
        },
        {
            "id": "l1_q19",
            "question": "Choisissez l'orthographe correcte : Nous _____ les calculs de poussée.",
            "options": [
                "commencons",
                "commençons",
                "commençont",
                "commençons-nous"
            ],
            "correct": 1,
            "explanation": "Verbs in \"-cer\" take a cedilla (ç) before \"o\" and \"a\" to preserve the soft [s] sound: \"nous commençons\"."
        },
        {
            "id": "l1_q20",
            "question": "Il est 12h30. Quelle est l'expression correcte en français ?",
            "options": [
                "Il est midi et demie",
                "Il est midi et demi",
                "Il est douze heures demi",
                "Il est midi avec demi"
            ],
            "correct": 1,
            "explanation": "\"Midi\" is masculine, so \"demi\" agrees in the masculine: \"midi et demi\" (unlike \"une heure et demie\")."
        },
        {
            "id": "l1_q21",
            "question": "Choisissez le pronom tonique : C'est _____ qui ai conçu la carte de distribution de puissance.",
            "options": [
                "moi",
                "je",
                "lui",
                "toi"
            ],
            "correct": 0,
            "explanation": "After \"c'est\", we use tonic pronouns. Since the conjugated verb is \"ai\" (1st person), the tonic pronoun is \"moi\" (C'est moi qui...)."
        },
        {
            "id": "l1_q22",
            "question": "Quel est le genre du mot \"système\" en français ?",
            "options": [
                "Masculin (un système)",
                "Féminin (une système)",
                "Neutre",
                "Indéfini"
            ],
            "correct": 0,
            "explanation": "Like many Greek-origin words ending in \"-ème\", \"système\" is masculine: \"un système embarqué\"."
        },
        {
            "id": "l1_q23",
            "question": "Quelle préposition indique la position intermédiaire : Le capteur est situé _____ la batterie et le contrôleur.",
            "options": [
                "parmi",
                "entre",
                "vers",
                "contre"
            ],
            "correct": 1,
            "explanation": "\"Entre\" is used when locating an element between two distinct items."
        },
        {
            "id": "l1_q24",
            "question": "Complétez l'interrogation de quantité : _____ de voltmètres possédez-vous dans l'atelier ?",
            "options": [
                "Combien",
                "Comment",
                "Pourquoi",
                "Quel"
            ],
            "correct": 0,
            "explanation": "\"Combien de\" is the standard interrogative structure used to ask \"how much / how many\"."
        },
        {
            "id": "l1_q25",
            "question": "Choisissez la forme correcte du verbe \"ranger\" : Nous _____ les outils après les essais.",
            "options": [
                "rangons",
                "rangeons",
                "rangeont",
                "rangez"
            ],
            "correct": 1,
            "explanation": "Verbs ending in \"-ger\" keep an \"e\" before \"o\" (nous rangeons, nous mangeons) to maintain the soft [ʒ] sound."
        },
        {
            "id": "l1_q26",
            "question": "Comment dit-on \"Thursday\" en français ?",
            "options": [
                "Mardi",
                "Mercredi",
                "Jeudi",
                "Vendredi"
            ],
            "correct": 2,
            "explanation": "Thursday is \"Jeudi\" in French (from Latin Dies Jovis)."
        },
        {
            "id": "l1_q27",
            "question": "Complétez : Il y a _____ bruit dans la soufflerie pendant le test aérodynamique.",
            "options": [
                "beaucoup de",
                "beaucoup du",
                "très de",
                "trop du"
            ],
            "correct": 0,
            "explanation": "Adverbs of quantity (beaucoup, peu, trop, assez) are followed by \"de\" without an article: \"beaucoup de bruit\"."
        },
        {
            "id": "l1_q28",
            "question": "Quelle est la forme d'inversion interrogative correcte pour \"Tu viens au labo\" ?",
            "options": [
                "Viens-tu au labo ?",
                "Est-ce tu viens au labo ?",
                "Tu viens-tu au labo ?",
                "Viens tu au labo ?"
            ],
            "correct": 0,
            "explanation": "Subject-verb inversion requires a hyphen between verb and pronoun: \"Viens-tu au labo ?\""
        },
        {
            "id": "l1_q29",
            "question": "Pour demander poliment un outil à un collègue, quelle formule est la plus polie ?",
            "options": [
                "Donne-moi le tournevis immédiatement.",
                "Pourriez-vous me passer le tournevis, s'il vous plaît ?",
                "Je veux le tournevis.",
                "Passe le tournevis."
            ],
            "correct": 1,
            "explanation": "The conditional present \"Pourriez-vous... s'il vous plaît ?\" is the standard formula of French politeness."
        },
        {
            "id": "l1_q30",
            "question": "Comment s'écrit le nombre 80 en toutes lettres selon la règle d'orthographe classique ?",
            "options": [
                "Quatre-vingt",
                "Quatre-vingts",
                "Octante",
                "Quatres-vingts"
            ],
            "correct": 1,
            "explanation": "\"Vingt\" takes an \"s\" in \"quatre-vingts\" when it multiplies 20 and is not followed by another number."
        }
    ],
    "2": [
        {
            "id": "l2_q1",
            "question": "Choisissez la forme correcte : Nous _____ du café le matin.",
            "options": [
                "boit",
                "buvons",
                "boivent",
                "boivez"
            ],
            "correct": 1,
            "explanation": "For 'nous', the verb 'boire' is conjugated as 'buvons'."
        },
        {
            "id": "l2_q2",
            "question": "Quel pronom remplace le sujet dans : 'Marie et Sarah étudient l'électricité.'",
            "options": [
                "Elles",
                "Ils",
                "Nous",
                "Vous"
            ],
            "correct": 0,
            "explanation": "'Marie et Sarah' are two females, so they are replaced by the plural feminine pronoun 'Elles'."
        },
        {
            "id": "l2_q3",
            "question": "Comment dit-on 'To build a robot' en français ?",
            "options": [
                "Détruire un robot",
                "Construire un robot",
                "Acheter un robot",
                "Réparer un robot"
            ],
            "correct": 1,
            "explanation": "'Construire' means to build or construct. 'Détruire' means to destroy."
        },
        {
            "id": "l2_q4",
            "question": "Complétez : J'ai un projet très important _____ faire.",
            "options": [
                "à",
                "de",
                "pour",
                "en"
            ],
            "correct": 0,
            "explanation": "We use 'à' after nouns indicating something to be done: 'un projet à faire' (a project to do)."
        },
        {
            "id": "l2_q5",
            "question": "Quel est le pluriel du mot 'Travail' ?",
            "options": [
                "Travails",
                "Travaux",
                "Travailes",
                "Travaulx"
            ],
            "correct": 1,
            "explanation": "Nouns ending in '-ail' like 'travail' generally form their plural in '-aux' (travaux)."
        },
        {
            "id": "l2_q6",
            "question": "Choisissez la forme correcte : Hannah _____ passionnée de technologie.",
            "options": [
                "es",
                "suis",
                "est",
                "sont"
            ],
            "correct": 2,
            "explanation": "'Hannah' is third-person singular (elle), so we use 'est' (conjugation of 'être')."
        },
        {
            "id": "l2_q7",
            "question": "Comment dit-on 'The computer' en français ?",
            "options": [
                "La télévision",
                "L'ordinateur",
                "Le téléphone",
                "L'écran"
            ],
            "correct": 1,
            "explanation": "'L'ordinateur' is the French word for computer."
        },
        {
            "id": "l2_q8",
            "question": "Quelle phrase est grammaticalement correcte ?",
            "options": [
                "Elle aime concevoir des drones.",
                "Elle aiment concevoir des drones.",
                "Elle aime concevons des drones.",
                "Elle aimez concevoir des drones."
            ],
            "correct": 0,
            "explanation": "'Elle' takes the singular verb 'aime', followed by the infinitive 'concevoir' (to design)."
        },
        {
            "id": "l2_q9",
            "question": "Traduisez : 'Where is the lab?'",
            "options": [
                "Qui est au labo ?",
                "Où est le laboratoire ?",
                "Comment fonctionne le laboratoire ?",
                "Quand ouvre le laboratoire ?"
            ],
            "correct": 1,
            "explanation": "'Where' translates to 'Où', so 'Où est le laboratoire ?' is correct."
        },
        {
            "id": "l2_q10",
            "question": "Complétez : Ils _____ un cours d'aérodynamique.",
            "options": [
                "ont",
                "as",
                "avons",
                "avez"
            ],
            "correct": 0,
            "explanation": "'Ils' takes the third-person plural conjugation of 'avoir', which is 'ont'."
        },
        {
            "id": "l2_q11",
            "question": "Choisissez le temps correct : Pendant qu'Hannah _____ le circuit imprimé, une alerte est apparue.",
            "options": [
                "soudait",
                "a soudé",
                "soudera",
                "soude"
            ],
            "correct": 0,
            "explanation": "The background ongoing action in the past takes the imparfait (\"soudait\"), while the sudden interrupting event takes the passé composé (\"est apparue\")."
        },
        {
            "id": "l2_q12",
            "question": "Complétez avec le pronom COD : Les nouveaux capteurs gyroscopiques, Hannah _____ a installés ce matin.",
            "options": [
                "les",
                "leur",
                "en",
                "y"
            ],
            "correct": 0,
            "explanation": "\"Les capteurs\" is a plural direct object (COD). It is replaced by \"les\". Note the past participle agreement: \"installés\"."
        },
        {
            "id": "l2_q13",
            "question": "Complétez avec le pronom COI : Hannah a parlé aux ingénieurs ? - Oui, elle _____ a expliqué le protocole.",
            "options": [
                "les",
                "leur",
                "lui",
                "y"
            ],
            "correct": 1,
            "explanation": "\"Aux ingénieurs\" is plural indirect object (à + persons). The indirect object pronoun is \"leur\"."
        },
        {
            "id": "l2_q14",
            "question": "Complétez avec le pronom approprié : Penses-tu à l'inspection de sécurité ? - Oui, j'_____ pense sans cesse.",
            "options": [
                "y",
                "en",
                "le",
                "la"
            ],
            "correct": 0,
            "explanation": "The verb \"penser à + chose\" is replaced by the adverbial pronoun \"y\": \"J'y pense\"."
        },
        {
            "id": "l2_q15",
            "question": "Complétez : As-tu besoin de résistances de 10k ohms ? - Oui, j'_____ ai besoin de plusieurs.",
            "options": [
                "y",
                "en",
                "les",
                "de ça"
            ],
            "correct": 1,
            "explanation": "The expression \"avoir besoin de + chose/quantité\" is replaced by the pronoun \"en\": \"J'en ai besoin\"."
        },
        {
            "id": "l2_q16",
            "question": "Quelle est la forme du futur simple du verbe \"pouvoir\" pour \"nous\" ?",
            "options": [
                "pouvons",
                "pourrons",
                "pourrions",
                "pouvrons"
            ],
            "correct": 1,
            "explanation": "The stem for \"pouvoir\" in future simple is \"pourr-\", giving \"nous pourrons\"."
        },
        {
            "id": "l2_q17",
            "question": "Choisissez le comparatif correct : Le nouveau moteur brushless a un _____ rendement que l'ancien.",
            "options": [
                "plus bon",
                "meilleur",
                "mieux",
                "plus meilleur"
            ],
            "correct": 1,
            "explanation": "The comparative of the adjective \"bon\" is \"meilleur\" (never \"plus bon\")."
        },
        {
            "id": "l2_q18",
            "question": "Que signifie l'expression \"un ancien bâtiment\" par rapport à \"un bâtiment ancien\" ?",
            "options": [
                "Un ancien bâtiment = un vieux bâtiment ; Un bâtiment ancien = un ex-bâtiment",
                "Un ancien bâtiment = un précédent bâtiment ; Un bâtiment ancien = un vieux bâtiment",
                "Les deux ont exactement le même sens",
                "Un ancien bâtiment est plus moderne"
            ],
            "correct": 1,
            "explanation": "Placed before the noun, \"ancien\" means former/previous (\"un ancien bâtiment\"); placed after, it means old/historic (\"un bâtiment ancien\")."
        },
        {
            "id": "l2_q19",
            "question": "Complétez : Hannah travaille sur ce microcontrôleur _____ trois heures et elle n'a pas fini.",
            "options": [
                "pendant",
                "depuis",
                "dans",
                "pour"
            ],
            "correct": 1,
            "explanation": "\"Depuis\" denotes an action that started in the past and is still ongoing in the present."
        },
        {
            "id": "l2_q20",
            "question": "Choisissez l'auxiliaire correct : Hannah _____ descendue au sous-sol pour chercher l'oscilloscope.",
            "options": [
                "a",
                "est",
                "avait",
                "serait"
            ],
            "correct": 1,
            "explanation": "Used intransitively (movement without direct object), \"descendre\" conjugates with \"être\": \"elle est descendue\"."
        },
        {
            "id": "l2_q21",
            "question": "Attention au faux ami ! En français, que signifie le mot \"actuellement\" ?",
            "options": [
                "En réalité / en fait",
                "À l'heure actuelle / en ce moment",
                "Éventuellement",
                "Certainement"
            ],
            "correct": 1,
            "explanation": "\"Actuellement\" means \"currently / at present\". To say \"actually / in fact\", French uses \"en réalité\" or \"en fait\"."
        },
        {
            "id": "l2_q22",
            "question": "Choisissez le pronom relatif correct : Le schéma électrique _____ nous avons discuté est sur la table.",
            "options": [
                "que",
                "qui",
                "dont",
                "où"
            ],
            "correct": 2,
            "explanation": "Since we say \"discuter de quelque chose\", the relative pronoun replacing \"de + nom\" is \"dont\"."
        },
        {
            "id": "l2_q23",
            "question": "Complétez avec le superlatif de l'adverbe \"bien\" : De toute l'équipe, c'est Hannah qui soude le _____.",
            "options": [
                "plus bon",
                "meilleur",
                "mieux",
                "plus bien"
            ],
            "correct": 2,
            "explanation": "The comparative/superlative of the adverb \"bien\" is \"mieux\" (\"le mieux\")."
        },
        {
            "id": "l2_q24",
            "question": "Accord du verbe pronominal réfléchi : Les deux ingénieures se sont _____ des félicitations mutuelles.",
            "options": [
                "donné",
                "donnée",
                "données",
                "donnés"
            ],
            "correct": 0,
            "explanation": "The direct object (COD) is \"des félicitations\", placed AFTER the verb. Therefore, the past participle \"donné\" does not agree with \"se\"."
        },
        {
            "id": "l2_q25",
            "question": "Quelle phrase exprime un conseil poli au conditionnel présent ?",
            "options": [
                "Tu dois vérifier la tension.",
                "Tu devrais vérifier la tension de la batterie.",
                "Tu as dû vérifier la tension.",
                "Tu devras vérifier la tension."
            ],
            "correct": 1,
            "explanation": "\"Tu devrais...\" (conditional present of devoir) softens the obligation into a polite recommendation."
        },
        {
            "id": "l2_q26",
            "question": "Mettez à la voix passive : \"L'équipe assemble le fuselage du drone.\"",
            "options": [
                "Le fuselage du drone est assemblé par l'équipe.",
                "Le fuselage du drone sera assemblé par l'équipe.",
                "Le fuselage du drone a été assemblé par l'équipe.",
                "L'équipe est assemblée par le fuselage."
            ],
            "correct": 0,
            "explanation": "Present indicative passive voice: \"est assemblé par...\"."
        },
        {
            "id": "l2_q27",
            "question": "Choisissez la préposition correcte : Hannah se rend au centre d'essais en vol _____ train.",
            "options": [
                "à",
                "en",
                "par",
                "dans le"
            ],
            "correct": 1,
            "explanation": "Vehicles one enters inside generally take \"en\" (en train, en voiture, en avion)."
        },
        {
            "id": "l2_q28",
            "question": "Complétez la phrase négative : \"Qui a touché au fer à souder ?\" -> \"_____ n'y a touché.\"",
            "options": [
                "Rien",
                "Personne",
                "Jamais",
                "Aucunement"
            ],
            "correct": 1,
            "explanation": "When answering a question about persons (\"Qui\"), the subject negative pronoun is \"Personne ne...\"."
        },
        {
            "id": "l2_q29",
            "question": "Quelle est la forme impérative affirmative correcte pour le verbe pronominal \"se dépêcher\" à la 2e personne du pluriel ?",
            "options": [
                "Vous dépêchez !",
                "Dépêchez-vous !",
                "Dépêchez vous !",
                "Se dépêchez !"
            ],
            "correct": 1,
            "explanation": "In affirmative imperative for pronominal verbs, the pronoun follows the verb with a hyphen: \"Dépêchez-vous !\"."
        },
        {
            "id": "l2_q30",
            "question": "Quelle phrase utilise correctement le futur proche ?",
            "options": [
                "Hannah va calibrer les capteurs dans un instant.",
                "Hannah calibrera les capteurs.",
                "Hannah a calibré les capteurs.",
                "Hannah vient de calibrer les capteurs."
            ],
            "correct": 0,
            "explanation": "The futur proche is formed with \"aller + infinitif\": \"va calibrer\"."
        }
    ],
    "3": [
        {
            "id": "l3_q1",
            "question": "Quel composant électrique Hannah conçoit-elle pour stocker temporairement de l'énergie ?",
            "options": [
                "Une résistance",
                "Un condensateur",
                "Une diode",
                "Un fusible"
            ],
            "correct": 1,
            "explanation": "A capacitor ('un condensateur') stores electrical energy, whereas a resistor ('une résistance') limits current."
        },
        {
            "id": "l3_q2",
            "question": "Traduisez : 'Hannah is the Vice Head of the Electrical division.'",
            "options": [
                "Hannah est la directrice en chef du logiciel.",
                "Hannah est la responsable adjointe de la division électrique.",
                "Hannah gère le département mécanique de l'équipe.",
                "Hannah conçoit les hélices de drone."
            ],
            "correct": 1,
            "explanation": "'Responsable adjointe' is the proper translation for 'Vice Head' (or Deputy Head) of a division."
        },
        {
            "id": "l3_q3",
            "question": "Choisissez la préposition correcte : Le drone vole _____ les nuages.",
            "options": [
                "au-dessus de",
                "au-dessus des",
                "à côté des",
                "par terre des"
            ],
            "correct": 1,
            "explanation": "We say 'au-dessus des nuages' (above the clouds) where 'des' is the contraction of 'de + les'."
        },
        {
            "id": "l3_q4",
            "question": "Complétez : Si nous avions du temps, nous _____ le drone aujourd'hui.",
            "options": [
                "testerions",
                "testerons",
                "testons",
                "eussions testé"
            ],
            "correct": 0,
            "explanation": "After a 'si' clause in the imparfait ('si nous avions'), the main clause must be in the conditional present ('nous testerions')."
        },
        {
            "id": "l3_q5",
            "question": "Comment dit-on 'Unmanned Aerial Vehicle (UAV)' en français ?",
            "options": [
                "Un aéronef supersonique sans passager",
                "Un véhicule aérien sans pilote (ou drone)",
                "Un robot de détection terrestre",
                "Une fusée spatiale automatisée"
            ],
            "correct": 1,
            "explanation": "'UAV' is literally 'Véhicule Aérien sans Pilote', commonly referred to simply as 'un drone'."
        },
        {
            "id": "l3_q6",
            "question": "Choisissez l'accord du participe passé : La pièce de rechange que j'ai _____ (commander) est arrivée.",
            "options": [
                "commandé",
                "commandée",
                "commandes",
                "commandées"
            ],
            "correct": 1,
            "explanation": "With 'avoir', the past participle agrees with the direct object ('la pièce de rechange', feminine singular) if it precedes the verb. Hence, 'commandée'."
        },
        {
            "id": "l3_q7",
            "question": "Quel est le synonyme de 'performant' ?",
            "options": [
                "Lent",
                "Efficace et compétent",
                "Facile à casser",
                "Inutile"
            ],
            "correct": 1,
            "explanation": "'Performant' implies high efficiency, competence, or quality execution."
        },
        {
            "id": "l3_q8",
            "question": "Traduisez : 'I will finish my electrical diagram tomorrow.'",
            "options": [
                "Je finissais mon schéma électrique hier.",
                "Je finirai mon schéma électrique demain.",
                "Je finis mes composants électriques ce soir.",
                "J'aurais fini mon schéma électrique hier."
            ],
            "correct": 1,
            "explanation": "'I will finish' is the futur simple: 'Je finirai'. 'Diagram' in electrical engineering is 'schéma'."
        },
        {
            "id": "l3_q9",
            "question": "Pour mesurer la tension d'une batterie, Hannah utilise un _____.",
            "options": [
                "Baromètre",
                "Multimètre (ou voltmètre)",
                "Tachymètre",
                "Thermomètre"
            ],
            "correct": 1,
            "explanation": "A multimeter ('multimètre') configured as a voltmeter is used to measure electrical voltage ('tension')."
        },
        {
            "id": "l3_q10",
            "question": "Que signifie l'expression idiomatique 'avoir du pain sur la planche' ?",
            "options": [
                "Être très riche",
                "Avoir beaucoup de travail à faire",
                "Avoir faim avant un vol",
                "Préparer une expérience scientifique"
            ],
            "correct": 1,
            "explanation": "This common idiom means having a lot of work or tasks lined up."
        },
        {
            "id": "l3_q11",
            "question": "Choisissez l'accord du participe passé : Les cartes électroniques qu'Hannah a _____ fonctionnent parfaitement.",
            "options": [
                "conçu",
                "conçue",
                "conçus",
                "conçues"
            ],
            "correct": 3,
            "explanation": "The direct object relative \"que\" refers to \"les cartes électroniques\" (feminine plural) and precedes the verb. The past participle must agree: \"conçues\"."
        },
        {
            "id": "l3_q12",
            "question": "Accord avec le pronom \"en\" : Des microcontrôleurs STM32, combien en as-tu _____ ?",
            "options": [
                "commandé",
                "commandée",
                "commandés",
                "commandées"
            ],
            "correct": 0,
            "explanation": "The pronoun \"en\" does not trigger past participle agreement. The participle remains invariable: \"commandé\"."
        },
        {
            "id": "l3_q13",
            "question": "Accord du verbe pronominal réciproque : Les cheffes de pôle se sont _____ lors de la réunion de cadrage.",
            "options": [
                "parlé",
                "parlée",
                "parlés",
                "parlées"
            ],
            "correct": 0,
            "explanation": "Since one says \"parler à quelqu'un\" (indirect object), \"se\" is COI. The past participle remains invariable: \"parlé\"."
        },
        {
            "id": "l3_q14",
            "question": "Accord du verbe pronominal réfléchi : Hannah s'est _____ les mains avec soin avant de souder les puces CMS.",
            "options": [
                "lavé",
                "lavée",
                "lavés",
                "lavées"
            ],
            "correct": 0,
            "explanation": "The direct object (COD) is \"les mains\", located AFTER the verb. Therefore, the participle remains invariable: \"lavé\"."
        },
        {
            "id": "l3_q15",
            "question": "Complétez avec le mode subjonctif : Je suis ravi que vous _____ présents pour ce vol inaugural.",
            "options": [
                "êtes",
                "soyez",
                "seriez",
                "fûtes"
            ],
            "correct": 1,
            "explanation": "Expressions of emotion/feeling (\"être ravi que\") require the subjunctive present: \"que vous soyez\"."
        },
        {
            "id": "l3_q16",
            "question": "Subjonctif ou Indicatif : Je ne pense pas que ce moteur _____ assez puissant.",
            "options": [
                "est",
                "soit",
                "sera",
                "était"
            ],
            "correct": 1,
            "explanation": "Verbs of opinion used in the negative form (\"ne pas penser que\") express doubt and mandate the subjunctive mood: \"soit\"."
        },
        {
            "id": "l3_q17",
            "question": "Complétez : Coupez l'alimentation principale avant que le court-circuit ne _____ les composants.",
            "options": [
                "détruit",
                "détruise",
                "détruira",
                "détruisait"
            ],
            "correct": 1,
            "explanation": "The conjunction \"avant que\" always mandates the subjunctive mood: \"détruise\"."
        },
        {
            "id": "l3_q18",
            "question": "Règle classique de l'Académie : Choisissez le mode correct après \"après que\" : Nous avons décollé après que la pluie _____.",
            "options": [
                "a cessé",
                "ait cessé",
                "cesse",
                "soit cessée"
            ],
            "correct": 0,
            "explanation": "According to standard French grammar, \"après que\" expresses a completed fact and requires the indicative mood (passé composé: \"a cessé\"), not the subjunctive."
        },
        {
            "id": "l3_q19",
            "question": "Exprimez le regret / reproche au conditionnel passé : Vous _____ calibrer le compas avant le décollage !",
            "options": [
                "deviez",
                "auriez dû",
                "aurez dû",
                "eussiez dû"
            ],
            "correct": 1,
            "explanation": "Conditional past (\"auriez dû + infinitif\") is the standard structure to express a retrospective reproach or regret."
        },
        {
            "id": "l3_q20",
            "question": "Quelle phrase utilise correctement le gérondif pour exprimer la simultanéité et le moyen ?",
            "options": [
                "C'est en mesurant le courant qu'Hannah a localisé la panne.",
                "En mesuré le courant, elle a trouvé la panne.",
                "Par mesurant le courant, elle a trouvé la panne.",
                "Mesurant le courant, elle trouvait la panne."
            ],
            "correct": 0,
            "explanation": "The gérondif is formed with \"en + participe présent\": \"en mesurant\"."
        },
        {
            "id": "l3_q21",
            "question": "Concordance des temps au discours indirect : Hannah a annoncé : \"Je terminerai le banc de test ce soir.\" -> Hannah a annoncé qu'elle _____ le banc de test ce soir-là.",
            "options": [
                "terminera",
                "terminerait",
                "avait terminé",
                "termine"
            ],
            "correct": 1,
            "explanation": "When the reporting verb is in the past (\"a annoncé\"), future simple transforms into conditional present (\"terminerait\")."
        },
        {
            "id": "l3_q22",
            "question": "Concession / Opposition : _____ les perturbations magnétiques, le drone a maintenu son cap.",
            "options": [
                "Bien que",
                "Malgré",
                "Quoique",
                "Pourtant"
            ],
            "correct": 1,
            "explanation": "\"Malgré\" is followed directly by a noun phrase (\"les perturbations magnétiques\"), while \"bien que\" requires a clause with a conjugated verb in the subjunctive."
        },
        {
            "id": "l3_q23",
            "question": "Attention au faux ami : Dans la phrase \"Hannah assiste à la réunion des chefs de département\", que signifie \"assiste à\" ?",
            "options": [
                "Elle aide les chefs de département",
                "Elle est présente / participe comme auditrice",
                "Elle organise la réunion",
                "Elle refuse de venir"
            ],
            "correct": 1,
            "explanation": "\"Assister à\" means \"to attend / be present at\". \"To assist/help\" translates to \"aider\" or \"porter assistance\"."
        },
        {
            "id": "l3_q24",
            "question": "Que signifie l'expression idiomatique \"mettre les bouchées doubles\" ?",
            "options": [
                "Manger deux fois plus à midi",
                "Accélérer considérablement son travail pour rattraper un retard",
                "Augmenter le prix du drone",
                "Diviser les tâches en deux parts égales"
            ],
            "correct": 1,
            "explanation": "This idiom means speeding up efforts significantly to achieve an objective in time."
        },
        {
            "id": "l3_q25",
            "question": "Complétez avec la préposition appropriée : Hannah a réussi _____ stabiliser la boucle d'asservissement PID.",
            "options": [
                "à",
                "de",
                "pour",
                "en"
            ],
            "correct": 0,
            "explanation": "The verb construction is \"réussir à faire quelque chose\"."
        },
        {
            "id": "l3_q26",
            "question": "Complétez : L'équipe de pilotage a décidé _____ reporter les essais en vol.",
            "options": [
                "à",
                "de",
                "pour",
                "sur"
            ],
            "correct": 1,
            "explanation": "The verb construction is \"décider de faire quelque chose\"."
        },
        {
            "id": "l3_q27",
            "question": "Quel adverbe correspond à l'adjectif \"courant\" ?",
            "options": [
                "Couramment",
                "Courament",
                "Couramment-ment",
                "Couradement"
            ],
            "correct": 0,
            "explanation": "Adjectives ending in \"-ant\" form adverbs in \"-amment\": \"courant -> couramment\"."
        },
        {
            "id": "l3_q28",
            "question": "Complétez avec le pronom relatif composé : L'objectif _____ aspire notre division est l'autonomie complète.",
            "options": [
                "auquel",
                "duquel",
                "dans lequel",
                "par lequel"
            ],
            "correct": 0,
            "explanation": "The construction is \"aspirer à quelque chose\". With a masculine noun (\"l'objectif\"), \"à + lequel\" contracts to \"auquel\"."
        },
        {
            "id": "l3_q29",
            "question": "Ordre des pronoms à l'impératif affirmatif : \"Tu me donnes le voltmètre.\" -> À l'impératif affirmatif, on dit :",
            "options": [
                "Donne-moi-le !",
                "Donne-le-moi !",
                "Me le donne !",
                "Donne le me !"
            ],
            "correct": 1,
            "explanation": "In affirmative imperative, the direct object pronoun precedes the indirect: \"Donne-le-moi !\"."
        },
        {
            "id": "l3_q30",
            "question": "Complétez avec le subjonctif : Il est indispensable que nous _____ toutes les données télémétriques.",
            "options": [
                "recueillons",
                "recueillions",
                "recueillerons",
                "recueillirions"
            ],
            "correct": 1,
            "explanation": "The subjunctive present of \"recueillir\" for \"nous\" is \"que nous recueillions\" (with \"-ions\")."
        }
    ],
    "4": [
        {
            "id": "l4_q1",
            "question": "Complétez : Bien que le vent _____ fort, le drone vole de manière stable.",
            "options": [
                "soit",
                "est",
                "sera",
                "fût"
            ],
            "correct": 0,
            "explanation": "The conjunction 'bien que' (although) always requires the subjunctive mood. 'Soit' is the subjunctive present of 'être'."
        },
        {
            "id": "l4_q2",
            "question": "Quelle est la forme correcte du futur simple du verbe 'faire' à la première personne du pluriel (nous) ?",
            "options": [
                "faisons",
                "ferons",
                "ferions",
                "faisions"
            ],
            "correct": 1,
            "explanation": "'Ferons' is the future simple form. 'Ferions' is the conditional present, and 'faisons' is indicative present."
        },
        {
            "id": "l4_q3",
            "question": "Traduisez : 'She succeeded in calibrating the flight controller.'",
            "options": [
                "Elle veut calibrer le contrôleur de vol.",
                "Elle a réussi à calibrer le contrôleur de vol.",
                "Elle essayait de réparer la télécommande de vol.",
                "Elle a échoué à configurer le pilote automatique."
            ],
            "correct": 1,
            "explanation": "'She succeeded in [doing something]' translates to 'Elle a réussi à [faire quelque chose]'."
        },
        {
            "id": "l4_q4",
            "question": "Choisissez le pronom correct : Je parle à Hannah. -> Je _____ parle.",
            "options": [
                "le",
                "la",
                "lui",
                "y"
            ],
            "correct": 2,
            "explanation": "For indirect objects (à + person), we use 'lui' (singular indirect pronoun, works for both genders)."
        },
        {
            "id": "l4_q5",
            "question": "Complétez : Si Hannah _____ que le circuit était en court-circuit, elle l'aurait éteint.",
            "options": [
                "savait",
                "saurait",
                "avait su",
                "eût su"
            ],
            "correct": 2,
            "explanation": "For past conditional results ('elle l'aurait éteint'), the 'si' clause requires the plus-que-parfait ('si Hannah avait su')."
        },
        {
            "id": "l4_q6",
            "question": "Traduisez le terme aéronautique : 'Lift' (la force opposée au poids).",
            "options": [
                "La traînée",
                "La portance",
                "La poussée",
                "Le tangage"
            ],
            "correct": 1,
            "explanation": "'Lift' is 'la portance'. 'Drag' is 'la traînée', 'Thrust' is 'la poussée'."
        },
        {
            "id": "l4_q7",
            "question": "Complétez : C'est le projet _____ tout le monde parle dans l'équipe.",
            "options": [
                "que",
                "qui",
                "dont",
                "où"
            ],
            "correct": 2,
            "explanation": "We say 'parler de quelque chose' (to speak of/about something). The relative pronoun representing 'de + object' is 'dont'."
        },
        {
            "id": "l4_q8",
            "question": "Comment dit-on 'To troubleshoot a circuit' en français ?",
            "options": [
                "Dépanner (ou diagnostiquer) un circuit",
                "Fabriquer un circuit imprimé",
                "Brûler un composant de circuit",
                "Dessiner le schéma électrique"
            ],
            "correct": 0,
            "explanation": "'Troubleshoot' means detecting and correcting faults, which corresponds to 'dépanner' or 'diagnostiquer'."
        },
        {
            "id": "l4_q9",
            "question": "Choisissez le participe passé correct : Les drones que nous avons _____ (concevoir) volent très vite.",
            "options": [
                "conçu",
                "conçus",
                "conçues",
                "conçoive"
            ],
            "correct": 1,
            "explanation": "The direct object 'les drones' (masculine plural) precedes the verb conjugated with 'avoir'. The participle 'conçu' becomes 'conçus'."
        },
        {
            "id": "l4_q10",
            "question": "Que signifie 'battre le fer tant qu'il est chaud' ?",
            "options": [
                "Faire de la soudure électrique",
                "Agir rapidement tant que la situation est favorable",
                "Attendre patiemment que les autres décident",
                "Chauffer les composants avant le test"
            ],
            "correct": 1,
            "explanation": "This idiom means to take advantage of a favorable opportunity immediately."
        },
        {
            "id": "l4_q11",
            "question": "Accord du participe passé suivi d'un infinitif : Les ingénieures qu'Hannah a _____ travailler sur le banc d'essai sont brillantes.",
            "options": [
                "vu",
                "vue",
                "vus",
                "vues"
            ],
            "correct": 3,
            "explanation": "Since \"les ingénieures\" (f. pl.) is the agent performing the action of the infinitive \"travailler\", the participle agrees: \"vues\"."
        },
        {
            "id": "l4_q12",
            "question": "Accord du participe passé suivi d'un infinitif : La pièce de rechange qu'Hannah a _____ remplacer est introuvable.",
            "options": [
                "entendu",
                "entendue",
                "entendus",
                "entendues"
            ],
            "correct": 0,
            "explanation": "The preceding object \"la pièce\" undergoes the action (\"être remplacée\") rather than doing it. The participle remains invariable: \"entendu\" / \"vu\"."
        },
        {
            "id": "l4_q13",
            "question": "Règle absolue pour \"faire\" + infinitif : Ces maquettes de drone, l'équipe les a _____ fabriquer en impression 3D.",
            "options": [
                "faites",
                "fait",
                "faits",
                "faite"
            ],
            "correct": 1,
            "explanation": "The past participle of \"faire\" followed by an infinitive is ALWAYS invariable: \"les a fait fabriquer\"."
        },
        {
            "id": "l4_q14",
            "question": "Accord avec les verbes de mesure et durée : Les dix minutes que ce vol stationnaire a _____ ont paru une éternité.",
            "options": [
                "duré",
                "durée",
                "durés",
                "durées"
            ],
            "correct": 0,
            "explanation": "Verbs indicating duration, weight, or cost (durer, peser, coûter, valoir) are intransitive; \"les dix minutes\" is an adverbial complement, not a direct object. The participle is invariable: \"duré\"."
        },
        {
            "id": "l4_q15",
            "question": "Complétez avec le subjonctif passé : Bien qu'Hannah _____ son banc de test hier, elle procède à une ultime vérification.",
            "options": [
                "a terminé",
                "ait terminé",
                "eût terminé",
                "aura terminé"
            ],
            "correct": 1,
            "explanation": "To express anteriority in a subordinate clause requiring the subjunctive (\"bien que\"), we use the subjonctif passé: \"ait terminé\"."
        },
        {
            "id": "l4_q16",
            "question": "Le \"ne\" explétif dans le registre soutenu : Hannah craint que le régulateur de tension ne _____ sous forte charge.",
            "options": [
                "chauffe",
                "chauffe pas",
                "ait chauffé",
                "chauffât"
            ],
            "correct": 0,
            "explanation": "After verbs of fear in the affirmative (craindre, avoir peur), formal French uses the non-negative \"ne\" explétif with subjunctive present: \"ne chauffe\"."
        },
        {
            "id": "l4_q17",
            "question": "Pronom relatif composé avec préposition : L'entreprise aérospatiale pour _____ Hannah conçoit ce circuit est leader du marché.",
            "options": [
                "lequel",
                "laquelle",
                "lesquels",
                "desquelles"
            ],
            "correct": 1,
            "explanation": "\"Pour + nom féminin singulier (l'entreprise)\" -> \"pour laquelle\"."
        },
        {
            "id": "l4_q18",
            "question": "Complétez : L'incident technique à la suite _____ le vol a été suspendu était mineur.",
            "options": [
                "duquel",
                "auquel",
                "de laquelle",
                "desquels"
            ],
            "correct": 0,
            "explanation": "The prepositional locution is \"à la suite de\". Combined with the masculine noun \"l'incident\", \"de + lequel\" becomes \"duquel\"."
        },
        {
            "id": "l4_q19",
            "question": "Mode après \"au cas où\" : Au cas où une baisse de tension _____ observée, activez la batterie de secours.",
            "options": [
                "soit",
                "serait",
                "est",
                "sera"
            ],
            "correct": 1,
            "explanation": "The conditional conjunction \"au cas où\" is always followed by the conditional mood: \"serait observée\"."
        },
        {
            "id": "l4_q20",
            "question": "Distinguez les homophones : \"_____ soient vos doutes, gardez confiance en votre méthode.\"",
            "options": [
                "Quels que",
                "Quelques",
                "Quel que",
                "Quoique"
            ],
            "correct": 0,
            "explanation": "Before the subjunctive verb \"soient\", \"quel(le)s que\" is written in two words and agrees with the subject \"vos doutes\" (masc. pl. -> \"Quels que\")."
        },
        {
            "id": "l4_q21",
            "question": "Distinguez \"quoique\" et \"quoi que\" : \"_____ vous fassiez, respectez scrupuleusement les consignes de sécurité.\"",
            "options": [
                "Quoique",
                "Quoi que",
                "Quoi-que",
                "Quoi qu'"
            ],
            "correct": 1,
            "explanation": "\"Quoi que\" (in two words) means \"whatever / whatever thing that\", whereas \"quoique\" (in one word) means \"although / bien que\"."
        },
        {
            "id": "l4_q22",
            "question": "Distinction lexicale précise : Hannah a _____ son multimètre de précision dans l'atelier (objet transportable à la main).",
            "options": [
                "amené",
                "apporté",
                "emmené",
                "emporté"
            ],
            "correct": 1,
            "explanation": "One uses \"apporter\" for objects that can be carried to a destination. \"Amener\" is strictly reserved for people, animals, or non-portable vehicles."
        },
        {
            "id": "l4_q23",
            "question": "Orthographe / Paronymie : Hannah est _____ présenter son rapport d'architecture électrique à 14h.",
            "options": [
                "censée",
                "sensée",
                "sencée",
                "cencée"
            ],
            "correct": 0,
            "explanation": "\"Censé\" (with c) means \"supposed to\". \"Sensé\" (with s) means \"sensible / endowed with good sense\"."
        },
        {
            "id": "l4_q24",
            "question": "Vocabulaire soutenu : Quel est le synonyme soutenu de \"une seconde fois\" ou \"de nouveau\" ?",
            "options": [
                "Derechef",
                "Naguère",
                "Tant s'en faut",
                "D'ores et déjà"
            ],
            "correct": 0,
            "explanation": "\"Derechef\" is an elevated adverb meaning \"anew / once again / immediately afterwards\"."
        },
        {
            "id": "l4_q25",
            "question": "Que signifie l'expression proverbiale \"tirer son épingle du jeu\" ?",
            "options": [
                "Jouer aux quilles avec adresse",
                "Se dégager habilement d'une situation complexe en préservant ses intérêts",
                "Tricher lors d'un concours",
                "Abandonner prématurément une tâche"
            ],
            "correct": 1,
            "explanation": "This idiom means skillfully extricating oneself from a tricky situation while retaining an advantage."
        },
        {
            "id": "l4_q26",
            "question": "Complétez : Les essais auront lieu demain, à condition que la vitesse du vent _____ inférieure à 20 km/h.",
            "options": [
                "est",
                "soit",
                "sera",
                "fût"
            ],
            "correct": 1,
            "explanation": "The conjunction \"à condition que\" requires the subjunctive mood: \"soit\"."
        },
        {
            "id": "l4_q27",
            "question": "Complétez : Le drone a atterri sans qu'aucun dommage ne _____ constaté sur le train d'atterrissage.",
            "options": [
                "soit",
                "est",
                "sera",
                "fut"
            ],
            "correct": 0,
            "explanation": "\"Sans que\" always mandates the subjunctive mood: \"ne soit constaté\"."
        },
        {
            "id": "l4_q28",
            "question": "Nuance de liaison : Dans \"Ce prototype est prometteur, voire révolutionnaire\", que signifie \"voire\" ?",
            "options": [
                "C'est-à-dire",
                "Et même",
                "Au contraire",
                "Pour voir"
            ],
            "correct": 1,
            "explanation": "\"Voire\" (from Old French \"voire\" = truly) means \"and even / and indeed\"."
        },
        {
            "id": "l4_q29",
            "question": "Que signifie l'expression soutenue \"avoir voix au chapitre\" ?",
            "options": [
                "Avoir une voix très puissante pour chanter",
                "Avoir le droit et l'autorité d'exprimer son avis et de participer à une décision",
                "Lire à voix haute un chapitre de livre",
                "Présider une cérémonie religieuse"
            ],
            "correct": 1,
            "explanation": "Historically from monastic chapters where monks had voting rights, it means having an authoritative say in deliberations."
        },
        {
            "id": "l4_q30",
            "question": "Accord de l'adjectif verbal : Des signaux très _____ (stimuler) ont été détectés par le récepteur télémétrique.",
            "options": [
                "stimulants",
                "stimulans",
                "stimulants-ci",
                "stimulatifs"
            ],
            "correct": 0,
            "explanation": "The verbal adjective agrees in gender and number: \"des signaux stimulants\"."
        }
    ],
    "5": [
        {
            "id": "l5_q1",
            "question": "Quelle forme verbale convient : Il faut que vous _____ soin de ne pas court-circuiter la batterie.",
            "options": [
                "preniez",
                "prenez",
                "prendrez",
                "prissiez"
            ],
            "correct": 0,
            "explanation": "'Il faut que' mandates the subjunctive mood. The subjunctive present of 'prendre' for 'vous' is 'preniez'."
        },
        {
            "id": "l5_q2",
            "question": "Quel terme décrit la résistance aérodynamique de l'air s'opposant à l'avancement du drone ?",
            "options": [
                "La portance",
                "La traînée",
                "La poussée",
                "Le lacet"
            ],
            "correct": 1,
            "explanation": "'La traînée' is the aerodynamic drag force that resists forward motion."
        },
        {
            "id": "l5_q3",
            "question": "Quelle phrase exprime une hypothèse irréalisable dans le présent ?",
            "options": [
                "Si Hannah a des composants, elle répare le drone.",
                "Si Hannah avait plus de transistors, elle concevrait le filtre aujourd'hui.",
                "Si Hannah aura le temps, elle viendra au labo.",
                "Si Hannah avait fini hier, le drone volerait déjà."
            ],
            "correct": 1,
            "explanation": "An irrealis condition in the present uses 'si + imparfait -> conditionnel présent'. The second option fits perfectly."
        },
        {
            "id": "l5_q4",
            "question": "Que signifie l'idiome 'mettre la charrue avant les bœufs' ?",
            "options": [
                "Faire les choses dans le désordre, commencer par la fin",
                "Installer la batterie avant les moteurs du drone",
                "Travailler dans l'agriculture",
                "Se préparer méticuleusement à une présentation"
            ],
            "correct": 0,
            "explanation": "This means doing things in the wrong order (putting the cart before the horse)."
        },
        {
            "id": "l5_q5",
            "question": "Traduisez : 'The drone flew autonomously despite electromagnetic interference.'",
            "options": [
                "Le drone a volé de manière autonome bien que l'électromagnétisme fût stable.",
                "Le drone a volé de manière autonome en dépit des interférences électromagnétiques.",
                "Le drone volait sans pilote malgré la télémétrie endommagée.",
                "Le drone a fait un vol automatique car les circuits étaient brouillés."
            ],
            "correct": 1,
            "explanation": "'In spite of / despite' translates to 'en dépit de' or 'malgré'. 'Electromagnetic interference' is 'interférences électromagnétiques'."
        },
        {
            "id": "l5_q6",
            "question": "Choisissez la forme correcte : Il est impératif que nous _____ ce problème d'alimentation électrique.",
            "options": [
                "résolvions",
                "résolvons",
                "résoudrons",
                "résoudrions"
            ],
            "correct": 0,
            "explanation": "'Il est impératif que' requires the subjunctive mood. The subjunctive present of 'résoudre' for 'nous' is 'résolvions'."
        },
        {
            "id": "l5_q7",
            "question": "Dans le jargon technique de l'atelier, que signifie 'rendre l'âme' pour un microcontrôleur ?",
            "options": [
                "Être mis à jour avec le dernier micrologiciel",
                "Griller ou cesser définitivement de fonctionner",
                "Envoyer des données télémétriques",
                "Surchauffer légèrement"
            ],
            "correct": 1,
            "explanation": "'Rendre l'âme' (literally: surrender the soul) is a colloquial expression meaning to die or break down completely."
        },
        {
            "id": "l5_q8",
            "question": "Traduisez : 'Hannah, who has designed the telemetry module, is correcting the code.'",
            "options": [
                "Hannah conçoit le module de télémétrie en corrigeant le code.",
                "Hannah, qui a conçu le module de télémétrie, corrige le code.",
                "Hannah, dont le module télémétrique est fini, a corrigé le code.",
                "Hannah a codé le module télémétrique pour corriger des erreurs."
            ],
            "correct": 1,
            "explanation": "'Who has designed' is the relative clause 'qui a conçu', followed by present progressive/simple 'corrige le code'."
        },
        {
            "id": "l5_q9",
            "question": "Choisissez l'orthographe correcte de l'adverbe dérivé de l'adjectif 'prudent' :",
            "options": [
                "Prudement",
                "Prudemment",
                "Prudament",
                "Prudemant"
            ],
            "correct": 1,
            "explanation": "Adjectives ending in '-ent' form their adverbs in '-emment' (pronounced 'am-ment'). Thus, 'prudemment'."
        },
        {
            "id": "l5_q10",
            "question": "Complétez la structure littéraire : Fussiez-vous plus attentive, vous _____ évité cette erreur de soudure.",
            "options": [
                "avez",
                "auriez",
                "eussiez",
                "auriez eu"
            ],
            "correct": 1,
            "explanation": "'Fussiez-vous...' represents an inverted hypothetical clause (If you had been...). The main clause completes it with conditional past: 'vous auriez évité'."
        },
        {
            "id": "l5_q11",
            "question": "Conjugaison littéraire (Passé simple) : Dès qu'Hannah aperçut la surchauffe, elle _____ immédiatement l'alimentation.",
            "options": [
                "éteigna",
                "éteignit",
                "éteignat",
                "éteignît"
            ],
            "correct": 1,
            "explanation": "The passé simple 3rd person singular of \"éteindre\" is \"elle éteignit\" (without circumflex)."
        },
        {
            "id": "l5_q12",
            "question": "Passé simple du verbe \"convaincre\" : Hannah _____ le jury par la rigueur de sa méthodologie.",
            "options": [
                "convainquit",
                "convainqua",
                "convaint",
                "convaincit"
            ],
            "correct": 0,
            "explanation": "Verbs in \"-vaincre\" form their passé simple with \"-qui-\": \"elle convainquit\"."
        },
        {
            "id": "l5_q13",
            "question": "Passé simple du verbe \"acquérir\" : L'équipe A.E.R.I.S. _____ une solide réputation internationale.",
            "options": [
                "acquira",
                "acquit",
                "acquérut",
                "acquît"
            ],
            "correct": 1,
            "explanation": "The passé simple of \"acquérir\" is \"il/elle acquit\" (3rd person singular)."
        },
        {
            "id": "l5_q14",
            "question": "Subjonctif imparfait dans la langue classique : Il eût fallu qu'Hannah _____ la documentation avant le test.",
            "options": [
                "lise",
                "lût",
                "lisît",
                "luise"
            ],
            "correct": 1,
            "explanation": "In classical literary sequence of tenses after a past conditional, the subjunctive imperfect of \"lire\" is \"qu'elle lût\" (with circumflex on the û)."
        },
        {
            "id": "l5_q15",
            "question": "Accord du verbe avec un sujet collectif : La plupart des ingénieurs _____ la validation du nouveau banc d'essai.",
            "options": [
                "approuve",
                "approuvent",
                "approuveront seul",
                "a approuvé"
            ],
            "correct": 1,
            "explanation": "With \"la plupart de\" followed by a plural noun, the verb ALWAYS agrees in the plural: \"approuvent\"."
        },
        {
            "id": "l5_q16",
            "question": "Règle d'accord spécifique : \"Plus d'un technicien _____ salué l'ingéniosité d'Hannah.\"",
            "options": [
                "ont",
                "a",
                "avaient",
                "furent"
            ],
            "correct": 1,
            "explanation": "Grammatically, \"plus d'un\" takes a singular verb: \"plus d'un technicien a salué\" (unlike \"moins de deux\")."
        },
        {
            "id": "l5_q17",
            "question": "Orthographe contrastée : Participe présent vs Adjectif verbal : \"Une preuve particulièrement _____ (convaincre).\"",
            "options": [
                "convainquante",
                "convaincante",
                "convainquante-ci",
                "convainquante"
            ],
            "correct": 1,
            "explanation": "The verbal adjective is spelled \"convaincant(e)\" (with a c), whereas the present participle is \"convainquant\" (with qu)."
        },
        {
            "id": "l5_q18",
            "question": "Accord des adjectifs de couleur composés : Hannah a choisi des hélices de drone _____ pour ses prototypes.",
            "options": [
                "bleu marine",
                "bleues marines",
                "bleues marine",
                "bleu marines"
            ],
            "correct": 0,
            "explanation": "Compound color adjectives (bleu marine, vert clair, jaune poussin) are totally INVARIABLE."
        },
        {
            "id": "l5_q19",
            "question": "Inversion du sujet après adverbe initial : À peine l'impulsion fut-elle donnée que le moteur _____ son régime maximal.",
            "options": [
                "atteignit",
                "atteindra",
                "atteignait",
                "atteindrait"
            ],
            "correct": 0,
            "explanation": "In narrative past after \"à peine... que\", we use the passé simple: \"atteignit\"."
        },
        {
            "id": "l5_q20",
            "question": "Pluriel des noms composés : Dans le laboratoire se trouvent plusieurs _____ de haute technologie.",
            "options": [
                "chefs-d'œuvre",
                "chef-d'œuvres",
                "chefs-d'œuvres",
                "chef-d'œuvre"
            ],
            "correct": 0,
            "explanation": "In \"chef-d'œuvre\", only \"chef\" takes the plural \"s\"; \"d'œuvre\" is an invariable prepositional complement: \"des chefs-d'œuvre\"."
        },
        {
            "id": "l5_q21",
            "question": "Paronymie avancée : Des hypothèses formulées sans mesures empiriques relèvent de la pure _____ (et non de la conjoncture).",
            "options": [
                "conjecture",
                "conjoncture",
                "conjonction",
                "concrétion"
            ],
            "correct": 0,
            "explanation": "\"Une conjecture\" is an opinion founded on probabilities or guesswork. \"Une conjoncture\" refers to the economic or geopolitical climate."
        },
        {
            "id": "l5_q22",
            "question": "Figure de style : \"Ce schéma de câblage n'est pas dénué d'élégance\" pour signifier qu'il est extrêmement élégant est :",
            "options": [
                "Une litote",
                "Une métaphore",
                "Une anaphore",
                "Un oxymore"
            ],
            "correct": 0,
            "explanation": "A litote understates an idea to emphasize and intensify the positive meaning (\"saying less to mean more\")."
        },
        {
            "id": "l5_q23",
            "question": "Figure de style (Zeugme) : \"Hannah a gardé son calme et le contrôle du drone.\" De quelle figure s'agit-il ?",
            "options": [
                "Un zeugme (ou attelage)",
                "Une métonymie",
                "Un chiasme",
                "Une antiphrase"
            ],
            "correct": 0,
            "explanation": "A zeugme links two words with different figurative and concrete meanings to the same verb (\"garder son calme / garder le contrôle\")."
        },
        {
            "id": "l5_q24",
            "question": "Connecteur soutenu : \"_____ les intempéries, la mission de reconnaissance aérienne a été couronnée de succès.\"",
            "options": [
                "Nonobstant",
                "Attendu que",
                "Quoiqu'à",
                "Envers"
            ],
            "correct": 0,
            "explanation": "\"Nonobstant\" is a formal, legal and literary preposition meaning \"in spite of / notwithstanding\" (synonym of malgré)."
        },
        {
            "id": "l5_q25",
            "question": "Subjonctif après superlatif relatif : \"C'est le vol le plus impressionnant que nous _____ jamais accompli.\"",
            "options": [
                "ayons",
                "avons",
                "aurons",
                "aurions"
            ],
            "correct": 0,
            "explanation": "Relative clauses depending on a superlative (\"le plus...\", \"le seul...\", \"l'unique...\") traditionally take the subjunctive mood: \"ayons accompli\"."
        },
        {
            "id": "l5_q26",
            "question": "Conditionnel passé 2e forme (style classique) : \"S'il avait été prévenu, l'ingénieur _____ prêté son concours.\"",
            "options": [
                "eût",
                "eut",
                "aurait eu",
                "eût été"
            ],
            "correct": 0,
            "explanation": "The conditional past 2nd form uses the subjunctive plus-que-parfait auxiliary: \"il eût prêté\" (= \"il aurait prêté\")."
        },
        {
            "id": "l5_q27",
            "question": "Conjugaison d'un verbe défectif : Quelle est la forme correcte de 3e personne du singulier au présent de l'indicatif du verbe \"gésir\" (être étendu/gisant) ?",
            "options": [
                "Il gît",
                "Il gèse",
                "Il git",
                "Il gisse"
            ],
            "correct": 0,
            "explanation": "The 3rd person singular present of \"gésir\" is \"il gît\" (with circumflex: Ci-gît...)."
        },
        {
            "id": "l5_q28",
            "question": "Connecteur de conséquence soutenu : \"La liaison radio est rompue, _____ le pilote automatique déclenche le retour au point de départ.\"",
            "options": [
                "partant",
                "cependant",
                "nonobstant",
                "quoique"
            ],
            "correct": 0,
            "explanation": "In literary French, \"partant\" (adverb) means \"consequently / therefore / de ce fait\"."
        },
        {
            "id": "l5_q29",
            "question": "Paronymie : \"Cette interférence risque d'_____ gravement la transmission télémétrique.\"",
            "options": [
                "infecter",
                "infester",
                "affecter",
                "effectuer"
            ],
            "correct": 2,
            "explanation": "\"Affecter\" means to influence or alter adversely. \"Infecter\" means contaminating with disease, and \"infester\" means invading in large destructive numbers."
        },
        {
            "id": "l5_q30",
            "question": "Subjonctif imparfait du verbe \"pouvoir\" : \"Le chef d'équipe doutait qu'Hannah _____ achever le prototype à temps.\"",
            "options": [
                "pût",
                "pouvait",
                "puisse",
                "pût-elle"
            ],
            "correct": 0,
            "explanation": "The subjunctive imperfect 3rd person singular of \"pouvoir\" is \"qu'elle pût\" (with circumflex accent on the û)."
        }
    ]
};

  // ==========================================
  // 2. WIDGET STATE MANAGEMENT
  // ==========================================
  const state = {
    currentLevel: 3, // Start at level 3 (Medium)
    score: 0,
    consecutiveCorrect: 0,
    totalAnswered: 0,
    askedQuestions: { 1: [], 2: [], 3: [], 4: [], 5: [] },
    activeQuestion: null,
    isMinimized: false,
    isOpen: false,
    sessionEnded: false
  };

  // Difficulty names mapping
  const levelLabels = {
    1: { name: "1: Débutant 📘", desc: "Very Easy vocab & numbers" },
    2: { name: "2: Intermédiaire Débutant 🟢", desc: "Basic verbs & syntax" },
    3: { name: "3: Intermédiaire 🟡", desc: "Tenses & Electrical vocab" },
    4: { name: "4: Intermédiaire Avancé 🟠", desc: "Subjunctive & UAV terms" },
    5: { name: "5: Avancé/Expert 🔴", desc: "Complex expressions & idioms" }
  };

  // Target streak required for mastery victory
  const VICTORY_STREAK = 5;

  // ==========================================
  // 3. UI GENERATION (INJECTING THE DOM)
  // ==========================================
  function injectWidgetDOM() {
    // 3a. Create launcher
    const launcher = document.createElement("button");
    launcher.className = "french-launcher";
    launcher.id = "frenchLauncherBtn";
    launcher.innerHTML = `
      <span class="flag">🇫🇷</span>
      <span>Défis d'Hannah</span>
    `;
    document.body.appendChild(launcher);

    // 3b. Create main widget
    const widget = document.createElement("div");
    widget.className = "french-widget";
    widget.id = "frenchWidgetWindow";
    widget.innerHTML = `
      <!-- Header -->
      <div class="french-widget-header" id="frenchWidgetHeader">
        <h3 class="french-widget-title">
          <span>🇫🇷</span> Défi Français d'Hannah
        </h3>
        <div class="french-widget-controls">
          <button class="french-control-btn" id="frenchMinBtn" title="Minimize">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/></svg>
          </button>
          <button class="french-control-btn" id="frenchCloseBtn" title="Close">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
          </button>
        </div>
      </div>

      <!-- Intro Screen -->
      <div class="french-screen" id="frenchIntroScreen">
        <div style="font-size: 50px; margin-bottom: 15px;">🎓</div>
        <h4 class="french-screen-title">Prête pour le test, Hannah ?</h4>
        <p class="french-screen-desc">
          Un examen adaptatif pour tester ton français !<br><br>
          📈 Réponds juste et les questions deviennent plus dures.<br>
          📉 Réponds faux et elles deviennent plus faciles.<br>
          🏆 Atteins le <strong>Niveau 5 (Expert)</strong> et obtiens une série de 5 réponses correctes d'affilée pour remporter le certificat de maîtrise !
        </p>
        <button class="french-start-btn" id="frenchStartBtn">Commencer le Défi</button>
      </div>

      <!-- Victory Screen (Hidden by default) -->
      <div class="french-screen hidden" id="frenchVictoryScreen">
        <canvas class="french-confetti-canvas" id="frenchConfettiCanvas"></canvas>
        <h4 class="french-screen-title" style="color: #f1c40f;">🏆 Félicitations, Hannah!</h4>
        <p class="french-screen-desc">Tu as bravé toutes les questions de niveau expert avec brio !</p>
        
        <div class="french-certificate">
          <div class="certificate-seal">📜</div>
          <div>Certificat de Maîtrise</div>
          <div class="certificate-name">Hannah Ahmed</div>
          <div style="font-size: 10px; color: var(--fr-text-muted); margin-top: 5px;">
            Délivré par le département A.E.R.I.S. French Institute
          </div>
        </div>

        <button class="french-start-btn" id="frenchRestartBtn" style="background: var(--fr-accent);">Recommencer</button>
      </div>

      <!-- Game Body -->
      <div class="french-widget-body" id="frenchWidgetBody">
        <!-- Stats -->
        <div class="french-stats">
          <div class="french-difficulty-badge diff-3" id="frenchDiffBadge">Niveau 3</div>
          <div class="french-score-tracker">
            Score: <span class="french-score-val" id="frenchScoreVal">0</span> | 
            Série: <span class="french-score-val" id="frenchStreakVal">0</span>
          </div>
        </div>

        <!-- Gauge -->
        <div class="french-gauge-container">
          <div class="french-gauge-bar" id="frenchGaugeBar"></div>
        </div>

        <!-- Question Area -->
        <div class="french-question-card">
          <div class="french-question-text" id="frenchQuestionText">
            Chargement de la question...
          </div>
          <div class="french-options-container" id="frenchOptionsContainer">
            <!-- Dynamically generated options -->
          </div>
          
          <!-- Feedback panel -->
          <div class="french-feedback-panel" id="frenchFeedbackPanel">
            <p class="french-feedback-text" id="frenchFeedbackText">
              Explication de la réponse...
            </p>
            <button class="french-next-btn" id="frenchNextBtn">
              Question Suivante ➔
            </button>
          </div>
        </div>
      </div>
    `;
    document.body.appendChild(widget);

    setupEventListeners();
  }

  // ==========================================
  // 4. LOGIC ENGINE
  // ==========================================
  function setupEventListeners() {
    const launcher = document.getElementById("frenchLauncherBtn");
    const widget = document.getElementById("frenchWidgetWindow");
    const header = document.getElementById("frenchWidgetHeader");
    const closeBtn = document.getElementById("frenchCloseBtn");
    const minBtn = document.getElementById("frenchMinBtn");
    const startBtn = document.getElementById("frenchStartBtn");
    const restartBtn = document.getElementById("frenchRestartBtn");
    const nextBtn = document.getElementById("frenchNextBtn");

    // Open/Toggle from Launcher
    launcher.addEventListener("click", () => {
      openWidget();
    });

    // Close Button
    closeBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      closeWidget();
    });

    // Minimize Button
    minBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      toggleMinimize();
    });

    // Click header of minimized card to expand
    header.addEventListener("click", () => {
      if (state.isMinimized) {
        toggleMinimize();
      }
    });

    // Start Game
    startBtn.addEventListener("click", () => {
      document.getElementById("frenchIntroScreen").classList.add("hidden");
      resetGame();
      loadNextQuestion();
    });

    // Restart Game
    restartBtn.addEventListener("click", () => {
      document.getElementById("frenchVictoryScreen").classList.add("hidden");
      resetGame();
      loadNextQuestion();
    });

    // Next Question
    nextBtn.addEventListener("click", () => {
      loadNextQuestion();
    });

    // Setup hover/click trigger on Hannah's profile card
    hookHannahProfileCard();
  }

  function hookHannahProfileCard() {
    const hannahCard = document.getElementById("board-elec-vice");
    if (hannahCard) {
      hannahCard.style.cursor = "pointer";
      hannahCard.title = "Cliquez pour le défi français d'Hannah ! 🇫🇷";
      hannahCard.classList.add("pulse-highlight");

      hannahCard.addEventListener("click", () => {
        openWidget();
        // Scroll widget into view if needed (it is fixed position, so just opening is enough)
        // Add a nice bounce animation to widget to get attention
        const widget = document.getElementById("frenchWidgetWindow");
        widget.classList.add("widget-bounce");
        setTimeout(() => {
          widget.classList.remove("widget-bounce");
        }, 400);
      });
    }
  }

  function openWidget() {
    const launcher = document.getElementById("frenchLauncherBtn");
    const widget = document.getElementById("frenchWidgetWindow");
    
    state.isOpen = true;
    state.isMinimized = false;
    launcher.classList.add("hidden");
    widget.classList.remove("minimized");
    widget.classList.add("open");
  }

  function closeWidget() {
    const launcher = document.getElementById("frenchLauncherBtn");
    const widget = document.getElementById("frenchWidgetWindow");
    
    state.isOpen = false;
    launcher.classList.remove("hidden");
    widget.classList.remove("open");
    widget.classList.remove("minimized");
    stopConfetti();
  }

  function toggleMinimize() {
    const widget = document.getElementById("frenchWidgetWindow");
    const minBtn = document.getElementById("frenchMinBtn");

    state.isMinimized = !state.isMinimized;
    if (state.isMinimized) {
      widget.classList.add("minimized");
      minBtn.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"/></svg>
      `;
      minBtn.title = "Maximize";
    } else {
      widget.classList.remove("minimized");
      minBtn.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/></svg>
      `;
      minBtn.title = "Minimize";
    }
  }

  function resetGame() {
    state.currentLevel = 3;
    state.score = 0;
    state.consecutiveCorrect = 0;
    state.totalAnswered = 0;
    state.sessionEnded = false;
    // Clear asked question history
    for (let level in state.askedQuestions) {
      state.askedQuestions[level] = [];
    }
    updateStatsUI();
  }

  function updateStatsUI() {
    const diffBadge = document.getElementById("frenchDiffBadge");
    const scoreVal = document.getElementById("frenchScoreVal");
    const streakVal = document.getElementById("frenchStreakVal");
    const gaugeBar = document.getElementById("frenchGaugeBar");

    // Update level label
    const labelInfo = levelLabels[state.currentLevel];
    diffBadge.innerText = `Niveau ${state.currentLevel}`;
    diffBadge.className = `french-difficulty-badge diff-${state.currentLevel}`;
    diffBadge.title = labelInfo.desc;

    // Update numbers
    scoreVal.innerText = state.score;
    streakVal.innerText = `${state.consecutiveCorrect}/${state.currentLevel === 5 ? VICTORY_STREAK : '∞'}`;

    // Update gauge width: maps level 1-5 to 20%-100%
    const percentage = state.currentLevel * 20;
    gaugeBar.style.width = `${percentage}%`;
    // Rotate background gradient positions for extra dynamic aesthetic
    gaugeBar.style.backgroundPosition = `${(5 - state.currentLevel) * 25}% 0%`;
  }

  function loadNextQuestion() {
    // Hide feedback panel
    document.getElementById("frenchFeedbackPanel").style.display = "none";

    // 1. Pick a question from the current difficulty level
    const levelQuestions = questionPool[state.currentLevel];
    const askedList = state.askedQuestions[state.currentLevel];

    // Filter out questions already asked in this level
    let available = levelQuestions.filter(q => !askedList.includes(q.id));

    // If all questions in this level have been asked, reset the history for this level to avoid blockages
    if (available.length === 0) {
      state.askedQuestions[state.currentLevel] = [];
      available = levelQuestions;
    }

    // Pick a random question
    const randomIndex = Math.floor(Math.random() * available.length);
    const chosenQuestion = available[randomIndex];

    // Record it as asked
    state.askedQuestions[state.currentLevel].push(chosenQuestion.id);
    state.activeQuestion = chosenQuestion;

    // 2. Render the question text and options
    const questionTextEl = document.getElementById("frenchQuestionText");
    const optionsContainer = document.getElementById("frenchOptionsContainer");

    questionTextEl.innerText = chosenQuestion.question;
    optionsContainer.innerHTML = "";

    chosenQuestion.options.forEach((optionText, index) => {
      const button = document.createElement("button");
      button.className = "french-option-btn";
      button.innerHTML = `
        <span>${optionText}</span>
        <span class="option-icon"></span>
      `;
      button.addEventListener("click", () => handleAnswer(index, button));
      optionsContainer.appendChild(button);
    });
  }

  function handleAnswer(selectedIndex, selectedButton) {
    const q = state.activeQuestion;
    const isCorrect = (selectedIndex === q.correct);
    const buttons = document.querySelectorAll(".french-option-btn");
    const feedbackPanel = document.getElementById("frenchFeedbackPanel");
    const feedbackText = document.getElementById("frenchFeedbackText");
    const widget = document.getElementById("frenchWidgetWindow");

    // Disable all options
    buttons.forEach((btn, index) => {
      btn.disabled = true;
      const iconSpan = btn.querySelector(".option-icon");

      if (index === q.correct) {
        btn.classList.add("correct");
        iconSpan.innerHTML = `✓`;
      } else if (index === selectedIndex) {
        btn.classList.add("incorrect");
        iconSpan.innerHTML = `✗`;
      }
    });

    state.totalAnswered++;

    if (isCorrect) {
      // Correct!
      state.score += state.currentLevel * 10;
      state.consecutiveCorrect++;
      
      // Visual bounce micro-animation
      widget.classList.add("widget-bounce");
      setTimeout(() => widget.classList.remove("widget-bounce"), 400);

      // Level adaptation logic
      if (state.currentLevel < 5) {
        state.currentLevel++;
        state.consecutiveCorrect = 0; // Reset streak count for the new level
      } else {
        // Already at Level 5 (Expert)
        if (state.consecutiveCorrect >= VICTORY_STREAK) {
          // Trigger Victory Certificate!
          state.sessionEnded = true;
          setTimeout(showVictoryScreen, 1200);
          return;
        }
      }
    } else {
      // Incorrect!
      state.consecutiveCorrect = 0;

      // Visual shake micro-animation
      widget.classList.add("widget-shake");
      setTimeout(() => widget.classList.remove("widget-shake"), 400);

      // Level adaptation logic
      if (state.currentLevel > 1) {
        state.currentLevel--;
      }
    }

    // Update stats immediately after adjusting level
    updateStatsUI();

    // Show feedback and explanation
    feedbackText.innerHTML = `
      <strong>${isCorrect ? "Excellent ! " : "Oups ! "}</strong> 
      La bonne réponse était : <em>${q.options[q.correct]}</em>.<br>
      <span style="font-size:11px;">${q.explanation}</span>
    `;
    feedbackPanel.style.display = "block";
    
    // Scroll feedback panel into view if scrollbar exists
    const body = document.getElementById("frenchWidgetBody");
    body.scrollTop = body.scrollHeight;
  }

  // ==========================================
  // 5. VICTORY & CONFETTI CELEBRATION
  // ==========================================
  let confettiInterval = null;
  let confettiAnimId = null;

  function showVictoryScreen() {
    document.getElementById("frenchVictoryScreen").classList.remove("hidden");
    startConfetti();
  }

  function startConfetti() {
    const canvas = document.getElementById("frenchConfettiCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");

    // Adjust canvas size to parent width/height
    const resizeCanvas = () => {
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;
    };
    resizeCanvas();
    window.addEventListener("resize", resizeCanvas);

    const particles = [];
    const colors = ["#2ecc71", "#3498db", "#f1c40f", "#e67e22", "#e74c3c", "#9b59b6", "#f6f2df"];

    function createParticle() {
      return {
        x: Math.random() * canvas.width,
        y: -10 - Math.random() * 20,
        size: 4 + Math.random() * 6,
        color: colors[Math.floor(Math.random() * colors.length)],
        speedX: -2 + Math.random() * 4,
        speedY: 2 + Math.random() * 4,
        rotation: Math.random() * 360,
        rotationSpeed: -4 + Math.random() * 8
      };
    }

    // Spawn initial particles
    for (let i = 0; i < 50; i++) {
      particles.push(createParticle());
    }

    // Periodically add more
    confettiInterval = setInterval(() => {
      if (particles.length < 120) {
        particles.push(createParticle());
      }
    }, 150);

    function animate() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        p.x += p.speedX;
        p.y += p.speedY;
        p.rotation += p.rotationSpeed;

        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate((p.rotation * Math.PI) / 180);
        ctx.fillStyle = p.color;
        // Draw small rectangles or circles
        if (i % 2 === 0) {
          ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 1.5);
        } else {
          ctx.beginPath();
          ctx.arc(0, 0, p.size / 2, 0, Math.PI * 2);
          ctx.fill();
        }
        ctx.restore();

        // Recycle particles that fall off bottom or sides
        if (p.y > canvas.height || p.x < 0 || p.x > canvas.width) {
          particles[i] = createParticle();
        }
      }

      confettiAnimId = requestAnimationFrame(animate);
    }

    animate();
  }

  function stopConfetti() {
    if (confettiInterval) {
      clearInterval(confettiInterval);
      confettiInterval = null;
    }
    if (confettiAnimId) {
      cancelAnimationFrame(confettiAnimId);
      confettiAnimId = null;
    }
  }

  // ==========================================
  // 6. INITIALIZATION
  // ==========================================
  if (document.readyState === "complete" || document.readyState === "interactive") {
    injectWidgetDOM();
  } else {
    document.addEventListener("DOMContentLoaded", injectWidgetDOM);
  }

})();
