# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.getcwd())
import json
import re

base_50 = {
  1: [
    {
      "id": "l1_q1",
      "question": "Comment dit-on 'Thank you very much' en français ?",
      "options": ["De rien", "Merci beaucoup", "S'il vous plaît", "Bonjour"],
      "correct": 1,
      "explanation": "'Merci beaucoup' is the direct translation of 'Thank you very much'. 'De rien' means 'You're welcome'."
    },
    {
      "id": "l1_q2",
      "question": "Quelle couleur obtient-on en mélangeant le bleu et le jaune ?",
      "options": ["Rouge", "Vert", "Orange", "Violet"],
      "correct": 1,
      "explanation": "Blue and yellow make green ('vert' in French)."
    },
    {
      "id": "l1_q3",
      "question": "Comment dit-on 'The sky' en français ?",
      "options": ["Le soleil", "La lune", "Le ciel", "La terre"],
      "correct": 2,
      "explanation": "'Le ciel' translates to 'The sky'."
    },
    {
      "id": "l1_q4",
      "question": "Traduisez le mot 'A bird' en français.",
      "options": ["Un oiseau", "Un poisson", "Un chat", "Un chien"],
      "correct": 0,
      "explanation": "'Un oiseau' is a bird. 'Poisson' is fish, 'chat' is cat, and 'chien' is dog."
    },
    {
      "id": "l1_q5",
      "question": "Quel est le contraire du mot 'Grand' ?",
      "options": ["Moyen", "Petit", "Large", "Long"],
      "correct": 1,
      "explanation": "'Petit' (small/short) is the opposite of 'Grand' (tall/big)."
    },
    {
      "id": "l1_q6",
      "question": "Comment dit-on 'Welcome' en français ?",
      "options": ["Au revoir", "S'il vous plaît", "Bienvenue", "Félicitations"],
      "correct": 2,
      "explanation": "'Bienvenue' means welcome. 'Au revoir' means goodbye, and 'Félicitations' means congratulations."
    },
    {
      "id": "l1_q7",
      "question": "Quelle est la traduction française de 'Good morning' ?",
      "options": ["Bonsoir", "Bonne nuit", "Bonjour", "Bon après-midi"],
      "correct": 2,
      "explanation": "'Bonjour' is used for 'good morning' or 'hello' during the day."
    },
    {
      "id": "l1_q8",
      "question": "Quel nombre correspond au mot 'Douze' ?",
      "options": ["2", "12", "20", "22"],
      "correct": 1,
      "explanation": "'Douze' is the French word for 12."
    },
    {
      "id": "l1_q9",
      "question": "Comment dit-on 'Monday' en français ?",
      "options": ["Mardi", "Mercredi", "Lundi", "Dimanche"],
      "correct": 2,
      "explanation": "The days of the week start with 'Lundi' (Monday)."
    },
    {
      "id": "l1_q10",
      "question": "Quelle est la traduction de 'The water' ?",
      "options": ["Le vin", "Le lait", "L'eau", "Le jus"],
      "correct": 2,
      "explanation": "'L'eau' is the French word for water."
    }
  ],
  2: [
    {
      "id": "l2_q1",
      "question": "Choisissez la forme correcte : Nous _____ du café le matin.",
      "options": ["boit", "buvons", "boivent", "boivez"],
      "correct": 1,
      "explanation": "For 'nous', the verb 'boire' is conjugated as 'buvons'."
    },
    {
      "id": "l2_q2",
      "question": "Quel pronom remplace le sujet dans : 'Marie et Sarah étudient l'électricité.'",
      "options": ["Elles", "Ils", "Nous", "Vous"],
      "correct": 0,
      "explanation": "'Marie et Sarah' are two females, so they are replaced by the plural feminine pronoun 'Elles'."
    },
    {
      "id": "l2_q3",
      "question": "Comment dit-on 'To build a robot' en français ?",
      "options": ["Détruire un robot", "Construire un robot", "Acheter un robot", "Réparer un robot"],
      "correct": 1,
      "explanation": "'Construire' means to build or construct. 'Détruire' means to destroy."
    },
    {
      "id": "l2_q4",
      "question": "Complétez : J'ai un projet très important _____ faire.",
      "options": ["à", "de", "pour", "en"],
      "correct": 0,
      "explanation": "We use 'à' after nouns indicating something to be done: 'un projet à faire' (a project to do)."
    },
    {
      "id": "l2_q5",
      "question": "Quel est le pluriel du mot 'Travail' ?",
      "options": ["Travails", "Travaux", "Travailes", "Travaulx"],
      "correct": 1,
      "explanation": "Nouns ending in '-ail' like 'travail' generally form their plural in '-aux' (travaux)."
    },
    {
      "id": "l2_q6",
      "question": "Choisissez la forme correcte : Hannah _____ passionnée de technologie.",
      "options": ["es", "suis", "est", "sont"],
      "correct": 2,
      "explanation": "'Hannah' is third-person singular (elle), so we use 'est' (conjugation of 'être')."
    },
    {
      "id": "l2_q7",
      "question": "Comment dit-on 'The computer' en français ?",
      "options": ["La télévision", "L'ordinateur", "Le téléphone", "L'écran"],
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
      "options": ["ont", "as", "avons", "avez"],
      "correct": 0,
      "explanation": "'Ils' takes the third-person plural conjugation of 'avoir', which is 'ont'."
    }
  ],
  3: [
    {
      "id": "l3_q1",
      "question": "Quel composant électrique Hannah conçoit-elle pour stocker temporairement de l'énergie ?",
      "options": ["Une résistance", "Un condensateur", "Une diode", "Un fusible"],
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
      "options": ["au-dessus de", "au-dessus des", "à côté des", "par terre des"],
      "correct": 1,
      "explanation": "We say 'au-dessus des nuages' (above the clouds) where 'des' is the contraction of 'de + les'."
    },
    {
      "id": "l3_q4",
      "question": "Complétez : Si nous avions du temps, nous _____ le drone aujourd'hui.",
      "options": ["testerions", "testerons", "testons", "eussions testé"],
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
      "options": ["commandé", "commandée", "commandes", "commandées"],
      "correct": 1,
      "explanation": "With 'avoir', the past participle agrees with the direct object ('la pièce de rechange', feminine singular) if it precedes the verb. Hence, 'commandée'."
    },
    {
      "id": "l3_q7",
      "question": "Quel est le synonyme de 'performant' ?",
      "options": ["Lent", "Efficace et compétent", "Facile à casser", "Inutile"],
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
      "options": ["Baromètre", "Multimètre (ou voltmètre)", "Tachymètre", "Thermomètre"],
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
    }
  ],
  4: [
    {
      "id": "l4_q1",
      "question": "Complétez : Bien que le vent _____ fort, le drone vole de manière stable.",
      "options": ["soit", "est", "sera", "fût"],
      "correct": 0,
      "explanation": "The conjunction 'bien que' (although) always requires the subjunctive mood. 'Soit' is the subjunctive present of 'être'."
    },
    {
      "id": "l4_q2",
      "question": "Quelle est la forme correcte du futur simple du verbe 'faire' à la première personne du pluriel (nous) ?",
      "options": ["faisons", "ferons", "ferions", "faisions"],
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
      "options": ["le", "la", "lui", "y"],
      "correct": 2,
      "explanation": "For indirect objects (à + person), we use 'lui' (singular indirect pronoun, works for both genders)."
    },
    {
      "id": "l4_q5",
      "question": "Complétez : Si Hannah _____ que le circuit était en court-circuit, elle l'aurait éteint.",
      "options": ["savait", "saurait", "avait su", "eût su"],
      "correct": 2,
      "explanation": "For past conditional results ('elle l'aurait éteint'), the 'si' clause requires the plus-que-parfait ('si Hannah avait su')."
    },
    {
      "id": "l4_q6",
      "question": "Traduisez le terme aéronautique : 'Lift' (la force opposée au poids).",
      "options": ["La traînée", "La portance", "La poussée", "Le tangage"],
      "correct": 1,
      "explanation": "'Lift' is 'la portance'. 'Drag' is 'la traînée', 'Thrust' is 'la poussée'."
    },
    {
      "id": "l4_q7",
      "question": "Complétez : C'est le projet _____ tout le monde parle dans l'équipe.",
      "options": ["que", "qui", "dont", "où"],
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
      "options": ["conçu", "conçus", "conçues", "conçoive"],
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
    }
  ],
  5: [
    {
      "id": "l5_q1",
      "question": "Quelle forme verbale convient : Il faut que vous _____ soin de ne pas court-circuiter la batterie.",
      "options": ["preniez", "prenez", "prendrez", "prissiez"],
      "correct": 0,
      "explanation": "'Il faut que' mandates the subjunctive mood. The subjunctive present of 'prendre' for 'vous' is 'preniez'."
    },
    {
      "id": "l5_q2",
      "question": "Quel terme décrit la résistance aérodynamique de l'air s'opposant à l'avancement du drone ?",
      "options": ["La portance", "La traînée", "La poussée", "Le lacet"],
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
      "options": ["résolvions", "résolvons", "résoudrons", "résoudrions"],
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
      "options": ["Prudement", "Prudemment", "Prudament", "Prudemant"],
      "correct": 1,
      "explanation": "Adjectives ending in '-ent' form their adverbs in '-emment' (pronounced 'am-ment'). Thus, 'prudemment'."
    },
    {
      "id": "l5_q10",
      "question": "Complétez la structure littéraire : Fussiez-vous plus attentive, vous _____ évité cette erreur de soudure.",
      "options": ["avez", "auriez", "eussiez", "auriez eu"],
      "correct": 1,
      "explanation": "'Fussiez-vous...' represents an inverted hypothetical clause (If you had been...). The main clause completes it with conditional past: 'vous auriez évité'."
    }
  ]
}

# Import new questions from generate_french_exam
from scratch.generate_french_exam import new_questions

full_pool = {}
for lvl in range(1, 6):
    full_pool[lvl] = base_50[lvl] + new_questions[lvl]
    print(f"Level {lvl}: {len(full_pool[lvl])} questions")

total = sum(len(full_pool[lvl]) for lvl in range(1, 6))
print(f"Total Questions: {total}")

with open('french-exam.js', 'r', encoding='utf-8') as f:
    orig_code = f.read()

json_pool_str = json.dumps(full_pool, ensure_ascii=False, indent=4)

pattern = r'const questionPool = \{.*?\n  \};\n\n  // ==========================================\n  // 2\. WIDGET STATE MANAGEMENT'
replacement = f'const questionPool = {json_pool_str};\n\n  // ==========================================\n  // 2. WIDGET STATE MANAGEMENT'

new_code = re.sub(pattern, replacement, orig_code, flags=re.DOTALL)
new_code = new_code.replace("QUESTION POOL (50 Questions, 5 Levels)", "QUESTION POOL (150 Questions, 5 Levels)")

with open('french-exam.js', 'w', encoding='utf-8') as f:
    f.write(new_code)

with open('aeris-website-main/french-exam.js', 'w', encoding='utf-8') as f:
    f.write(new_code)

print("Successfully compiled and updated french-exam.js with all 150 questions!")
