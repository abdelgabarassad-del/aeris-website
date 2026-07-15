/**
 * Hannah's French Challenge - Adaptive Exam Engine
 * Built for A.E.R.I.S. UAV Team
 */

(function() {
  // ==========================================
  // 1. QUESTION POOL (50 Questions, 5 Levels)
  // ==========================================
  const questionPool = {
    1: [
      {
        id: "l1_q1",
        question: "Comment dit-on 'Thank you very much' en français ?",
        options: ["De rien", "Merci beaucoup", "S'il vous plaît", "Bonjour"],
        correct: 1,
        explanation: "'Merci beaucoup' is the direct translation of 'Thank you very much'. 'De rien' means 'You're welcome'."
      },
      {
        id: "l1_q2",
        question: "Quelle couleur obtient-on en mélangeant le bleu et le jaune ?",
        options: ["Rouge", "Vert", "Orange", "Violet"],
        correct: 1,
        explanation: "Blue and yellow make green ('vert' in French)."
      },
      {
        id: "l1_q3",
        question: "Comment dit-on 'The sky' en français ?",
        options: ["Le soleil", "La lune", "Le ciel", "La terre"],
        correct: 2,
        explanation: "'Le ciel' translates to 'The sky'."
      },
      {
        id: "l1_q4",
        question: "Traduisez le mot 'A bird' en français.",
        options: ["Un oiseau", "Un poisson", "Un chat", "Un chien"],
        correct: 0,
        explanation: "'Un oiseau' is a bird. 'Poisson' is fish, 'chat' is cat, and 'chien' is dog."
      },
      {
        id: "l1_q5",
        question: "Quel est le contraire du mot 'Grand' ?",
        options: ["Moyen", "Petit", "Large", "Long"],
        correct: 1,
        explanation: "'Petit' (small/short) is the opposite of 'Grand' (tall/big)."
      },
      {
        id: "l1_q6",
        question: "Comment dit-on 'Welcome' en français ?",
        options: ["Au revoir", "S'il vous plaît", "Bienvenue", "Félicitations"],
        correct: 2,
        explanation: "'Bienvenue' means welcome. 'Au revoir' means goodbye, and 'Félicitations' means congratulations."
      },
      {
        id: "l1_q7",
        question: "Quelle est la traduction française de 'Good morning' ?",
        options: ["Bonsoir", "Bonne nuit", "Bonjour", "Bon après-midi"],
        correct: 2,
        explanation: "'Bonjour' is used for 'good morning' or 'hello' during the day."
      },
      {
        id: "l1_q8",
        question: "Quel nombre correspond au mot 'Douze' ?",
        options: ["2", "12", "20", "22"],
        correct: 1,
        explanation: "'Douze' is the French word for 12."
      },
      {
        id: "l1_q9",
        question: "Comment dit-on 'Monday' en français ?",
        options: ["Mardi", "Mercredi", "Lundi", "Dimanche"],
        correct: 2,
        explanation: "The days of the week start with 'Lundi' (Monday)."
      },
      {
        id: "l1_q10",
        question: "Quelle est la traduction de 'The water' ?",
        options: ["Le vin", "Le lait", "L'eau", "Le jus"],
        correct: 2,
        explanation: "'L'eau' is the French word for water."
      }
    ],
    2: [
      {
        id: "l2_q1",
        question: "Choisissez la forme correcte : Nous _____ du café le matin.",
        options: ["boit", "buvons", "boivent", "boivez"],
        correct: 1,
        explanation: "For 'nous', the verb 'boire' is conjugated as 'buvons'."
      },
      {
        id: "l2_q2",
        question: "Quel pronom remplace le sujet dans : 'Marie et Sarah étudient l'électricité.'",
        options: ["Elles", "Ils", "Nous", "Vous"],
        correct: 0,
        explanation: "'Marie et Sarah' are two females, so they are replaced by the plural feminine pronoun 'Elles'."
      },
      {
        id: "l2_q3",
        question: "Comment dit-on 'To build a robot' en français ?",
        options: ["Détruire un robot", "Construire un robot", "Acheter un robot", "Réparer un robot"],
        correct: 1,
        explanation: "'Construire' means to build or construct. 'Détruire' means to destroy."
      },
      {
        id: "l2_q4",
        question: "Complétez : J'ai un projet très important _____ faire.",
        options: ["à", "de", "pour", "en"],
        correct: 0,
        explanation: "We use 'à' after nouns indicating something to be done: 'un projet à faire' (a project to do)."
      },
      {
        id: "l2_q5",
        question: "Quel est le pluriel du mot 'Travail' ?",
        options: ["Travails", "Travaux", "Travailes", "Travaulx"],
        correct: 1,
        explanation: "Nouns ending in '-ail' like 'travail' generally form their plural in '-aux' (travaux)."
      },
      {
        id: "l2_q6",
        question: "Choisissez la forme correcte : Hannah _____ passionnée de technologie.",
        options: ["es", "suis", "est", "sont"],
        correct: 2,
        explanation: "'Hannah' is third-person singular (elle), so we use 'est' (conjugation of 'être')."
      },
      {
        id: "l2_q7",
        question: "Comment dit-on 'The computer' en français ?",
        options: ["La télévision", "L'ordinateur", "Le téléphone", "L'écran"],
        correct: 1,
        explanation: "'L'ordinateur' is the French word for computer."
      },
      {
        id: "l2_q8",
        question: "Quelle phrase est grammaticalement correcte ?",
        options: [
          "Elle aime concevoir des drones.",
          "Elle aiment concevoir des drones.",
          "Elle aime concevons des drones.",
          "Elle aimez concevoir des drones."
        ],
        correct: 0,
        explanation: "'Elle' takes the singular verb 'aime', followed by the infinitive 'concevoir' (to design)."
      },
      {
        id: "l2_q9",
        question: "Traduisez : 'Where is the lab?'",
        options: [
          "Qui est au labo ?",
          "Où est le laboratoire ?",
          "Comment fonctionne le laboratoire ?",
          "Quand ouvre le laboratoire ?"
        ],
        correct: 1,
        explanation: "'Where' translates to 'Où', so 'Où est le laboratoire ?' is correct."
      },
      {
        id: "l2_q10",
        question: "Complétez : Ils _____ un cours d'aérodynamique.",
        options: ["ont", "as", "avons", "avez"],
        correct: 0,
        explanation: "'Ils' takes the third-person plural conjugation of 'avoir', which is 'ont'."
      }
    ],
    3: [
      {
        id: "l3_q1",
        question: "Quel composant électrique Hannah conçoit-elle pour stocker temporairement de l'énergie ?",
        options: ["Une résistance", "Un condensateur", "Une diode", "Un fusible"],
        correct: 1,
        explanation: "A capacitor ('un condensateur') stores electrical energy, whereas a resistor ('une résistance') limits current."
      },
      {
        id: "l3_q2",
        question: "Traduisez : 'Hannah is the Vice Head of the Electrical division.'",
        options: [
          "Hannah est la directrice en chef du logiciel.",
          "Hannah est la responsable adjointe de la division électrique.",
          "Hannah gère le département mécanique de l'équipe.",
          "Hannah conçoit les hélices de drone."
        ],
        correct: 1,
        explanation: "'Responsable adjointe' is the proper translation for 'Vice Head' (or Deputy Head) of a division."
      },
      {
        id: "l3_q3",
        question: "Choisissez la préposition correcte : Le drone vole _____ les nuages.",
        options: ["au-dessus de", "au-dessus des", "à côté des", "par terre des"],
        correct: 1,
        explanation: "We say 'au-dessus des nuages' (above the clouds) where 'des' is the contraction of 'de + les'."
      },
      {
        id: "l3_q4",
        question: "Complétez : Si nous avions du temps, nous _____ le drone aujourd'hui.",
        options: ["testerions", "testerons", "testons", "eussions testé"],
        correct: 0,
        explanation: "After a 'si' clause in the imparfait ('si nous avions'), the main clause must be in the conditional present ('nous testerions')."
      },
      {
        id: "l3_q5",
        question: "Comment dit-on 'Unmanned Aerial Vehicle (UAV)' en français ?",
        options: [
          "Un aéronef supersonique sans passager",
          "Un véhicule aérien sans pilote (ou drone)",
          "Un robot de détection terrestre",
          "Une fusée spatiale automatisée"
        ],
        correct: 1,
        explanation: "'UAV' is literally 'Véhicule Aérien sans Pilote', commonly referred to simply as 'un drone'."
      },
      {
        id: "l3_q6",
        question: "Choisissez l'accord du participe passé : La pièce de rechange que j'ai _____ (commander) est arrivée.",
        options: ["commandé", "commandée", "commandes", "commandées"],
        correct: 1,
        explanation: "With 'avoir', the past participle agrees with the direct object ('la pièce de rechange', feminine singular) if it precedes the verb. Hence, 'commandée'."
      },
      {
        id: "l3_q7",
        question: "Quel est le synonyme de 'performant' ?",
        options: ["Lent", "Efficace et compétent", "Facile à casser", "Inutile"],
        correct: 1,
        explanation: "'Performant' implies high efficiency, competence, or quality execution."
      },
      {
        id: "l3_q8",
        question: "Traduisez : 'I will finish my electrical diagram tomorrow.'",
        options: [
          "Je finissais mon schéma électrique hier.",
          "Je finirai mon schéma électrique demain.",
          "Je finis mes composants électriques ce soir.",
          "J'aurais fini mon schéma électrique hier."
        ],
        correct: 1,
        explanation: "'I will finish' is the futur simple: 'Je finirai'. 'Diagram' in electrical engineering is 'schéma'."
      },
      {
        id: "l3_q9",
        question: "Pour mesurer la tension d'une batterie, Hannah utilise un _____.",
        options: ["Baromètre", "Multimètre (ou voltmètre)", "Tachymètre", "Thermomètre"],
        correct: 1,
        explanation: "A multimeter ('multimètre') configured as a voltmeter is used to measure electrical voltage ('tension')."
      },
      {
        id: "l3_q10",
        question: "Que signifie l'expression idiomatique 'avoir du pain sur la planche' ?",
        options: [
          "Être très riche",
          "Avoir beaucoup de travail à faire",
          "Avoir faim avant un vol",
          "Préparer une expérience scientifique"
        ],
        correct: 1,
        explanation: "This common idiom means having a lot of work or tasks lined up."
      }
    ],
    4: [
      {
        id: "l4_q1",
        question: "Complétez : Bien que le vent _____ fort, le drone vole de manière stable.",
        options: ["soit", "est", "sera", "fût"],
        correct: 0,
        explanation: "The conjunction 'bien que' (although) always requires the subjunctive mood. 'Soit' is the subjunctive present of 'être'."
      },
      {
        id: "l4_q2",
        question: "Quelle est la forme correcte du futur simple du verbe 'faire' à la première personne du pluriel (nous) ?",
        options: ["faisons", "ferons", "ferions", "faisions"],
        correct: 1,
        explanation: "'Ferons' is the future simple form. 'Ferions' is the conditional present, and 'faisons' is indicative present."
      },
      {
        id: "l4_q3",
        question: "Traduisez : 'She succeeded in calibrating the flight controller.'",
        options: [
          "Elle veut calibrer le contrôleur de vol.",
          "Elle a réussi à calibrer le contrôleur de vol.",
          "Elle essayait de réparer la télécommande de vol.",
          "Elle a échoué à configurer le pilote automatique."
        ],
        correct: 1,
        explanation: "'She succeeded in [doing something]' translates to 'Elle a réussi à [faire quelque chose]'."
      },
      {
        id: "l4_q4",
        question: "Choisissez le pronom correct : Je parle à Hannah. -> Je _____ parle.",
        options: ["le", "la", "lui", "y"],
        correct: 2,
        explanation: "For indirect objects (à + person), we use 'lui' (singular indirect pronoun, works for both genders)."
      },
      {
        id: "l4_q5",
        question: "Complétez : Si Hannah _____ que le circuit était en court-circuit, elle l'aurait éteint.",
        options: ["savait", "saurait", "avait su", "eût su"],
        correct: 2,
        explanation: "For past conditional results ('elle l'aurait éteint'), the 'si' clause requires the plus-que-parfait ('si Hannah avait su')."
      },
      {
        id: "l4_q6",
        question: "Traduisez le terme aéronautique : 'Lift' (la force opposée au poids).",
        options: ["La traînée", "La portance", "La poussée", "Le tangage"],
        correct: 1,
        explanation: "'Lift' is 'la portance'. 'Drag' is 'la traînée', 'Thrust' is 'la poussée'."
      },
      {
        id: "l4_q7",
        question: "Complétez : C'est le projet _____ tout le monde parle dans l'équipe.",
        options: ["que", "qui", "dont", "où"],
        correct: 2,
        explanation: "We say 'parler de quelque chose' (to speak of/about something). The relative pronoun representing 'de + object' is 'dont'."
      },
      {
        id: "l4_q8",
        question: "Comment dit-on 'To troubleshoot a circuit' en français ?",
        options: [
          "Dépanner (ou diagnostiquer) un circuit",
          "Fabriquer un circuit imprimé",
          "Brûler un composant de circuit",
          "Dessiner le schéma électrique"
        ],
        correct: 0,
        explanation: "'Troubleshoot' means detecting and correcting faults, which corresponds to 'dépanner' or 'diagnostiquer'."
      },
      {
        id: "l4_q9",
        question: "Choisissez le participe passé correct : Les drones que nous avons _____ (concevoir) volent très vite.",
        options: ["conçu", "conçus", "conçues", "conçoive"],
        correct: 1,
        explanation: "The direct object 'les drones' (masculine plural) precedes the verb conjugated with 'avoir'. The participle 'conçu' becomes 'conçus'."
      },
      {
        id: "l4_q10",
        question: "Que signifie 'battre le fer tant qu'il est chaud' ?",
        options: [
          "Faire de la soudure électrique",
          "Agir rapidement tant que la situation est favorable",
          "Attendre patiemment que les autres décident",
          "Chauffer les composants avant le test"
        ],
        correct: 1,
        explanation: "This idiom means to take advantage of a favorable opportunity immediately."
      }
    ],
    5: [
      {
        id: "l5_q1",
        question: "Quelle forme verbale convient : Il faut que vous _____ soin de ne pas court-circuiter la batterie.",
        options: ["preniez", "prenez", "prendrez", "prissiez"],
        correct: 0,
        explanation: "'Il faut que' mandates the subjunctive mood. The subjunctive present of 'prendre' for 'vous' is 'preniez'."
      },
      {
        id: "l5_q2",
        question: "Quel terme décrit la résistance aérodynamique de l'air s'opposant à l'avancement du drone ?",
        options: ["La portance", "La traînée", "La poussée", "Le lacet"],
        correct: 1,
        explanation: "'La traînée' is the aerodynamic drag force that resists forward motion."
      },
      {
        id: "l5_q3",
        question: "Quelle phrase exprime une hypothèse irréalisable dans le présent ?",
        options: [
          "Si Hannah a des composants, elle répare le drone.",
          "Si Hannah avait plus de transistors, elle concevrait le filtre aujourd'hui.",
          "Si Hannah aura le temps, elle viendra au labo.",
          "Si Hannah avait fini hier, le drone volerait déjà."
        ],
        correct: 1,
        explanation: "An irrealis condition in the present uses 'si + imparfait -> conditionnel présent'. The second option fits perfectly."
      },
      {
        id: "l5_q4",
        question: "Que signifie l'idiome 'mettre la charrue avant les bœufs' ?",
        options: [
          "Faire les choses dans le désordre, commencer par la fin",
          "Installer la batterie avant les moteurs du drone",
          "Travailler dans l'agriculture",
          "Se préparer méticuleusement à une présentation"
        ],
        correct: 0,
        explanation: "This means doing things in the wrong order (putting the cart before the horse)."
      },
      {
        id: "l5_q5",
        question: "Traduisez : 'The drone flew autonomously despite electromagnetic interference.'",
        options: [
          "Le drone a volé de manière autonome bien que l'électromagnétisme fût stable.",
          "Le drone a volé de manière autonome en dépit des interférences électromagnétiques.",
          "Le drone volait sans pilote malgré la télémétrie endommagée.",
          "Le drone a fait un vol automatique car les circuits étaient brouillés."
        ],
        correct: 1,
        explanation: "'In spite of / despite' translates to 'en dépit de' or 'malgré'. 'Electromagnetic interference' is 'interférences électromagnétiques'."
      },
      {
        id: "l5_q6",
        question: "Choisissez la forme correcte : Il est impératif que nous _____ ce problème d'alimentation électrique.",
        options: ["résolvions", "résolvons", "résoudrons", "résoudrions"],
        correct: 0,
        explanation: "'Il est impératif que' requires the subjunctive mood. The subjunctive present of 'résoudre' for 'nous' is 'résolvions'."
      },
      {
        id: "l5_q7",
        question: "Dans le jargon technique de l'atelier, que signifie 'rendre l'âme' pour un microcontrôleur ?",
        options: [
          "Être mis à jour avec le dernier micrologiciel",
          "Griller ou cesser définitivement de fonctionner",
          "Envoyer des données télémétriques",
          "Surchauffer légèrement"
        ],
        correct: 1,
        explanation: "'Rendre l'âme' (literally: surrender the soul) is a colloquial expression meaning to die or break down completely."
      },
      {
        id: "l5_q8",
        question: "Traduisez : 'Hannah, who has designed the telemetry module, is correcting the code.'",
        options: [
          "Hannah conçoit le module de télémétrie en corrigeant le code.",
          "Hannah, qui a conçu le module de télémétrie, corrige le code.",
          "Hannah, dont le module télémétrique est fini, a corrigé le code.",
          "Hannah a codé le module télémétrique pour corriger des erreurs."
        ],
        correct: 1,
        explanation: "'Who has designed' is the relative clause 'qui a conçu', followed by present progressive/simple 'corrige le code'."
      },
      {
        id: "l5_q9",
        question: "Choisissez l'orthographe correcte de l'adverbe dérivé de l'adjectif 'prudent' :",
        options: ["Prudement", "Prudemment", "Prudament", "Prudemant"],
        correct: 1,
        explanation: "Adjectives ending in '-ent' form their adverbs in '-emment' (pronounced 'am-ment'). Thus, 'prudemment'."
      },
      {
        id: "l5_q10",
        question: "Complétez la structure littéraire : Fussiez-vous plus attentive, vous _____ évité cette erreur de soudure.",
        options: ["avez", "auriez", "eussiez", "auriez eu"],
        correct: 1,
        explanation: "'Fussiez-vous...' represents an inverted hypothetical clause (If you had been...). The main clause completes it with conditional past: 'vous auriez évité'."
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
