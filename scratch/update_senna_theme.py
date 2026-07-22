import sys
import os

def main():
    dashboard_path = 'c:/Users/abdel/Desktop/aeris-website-main/dashboard.html'
    css_path = 'c:/Users/abdel/Desktop/aeris-website-main/dashboard.css'

    with open(dashboard_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update ALL_MEMBERS
    target_all_mem = "const ALL_MEMBERS = new Set([\n      '251000861'"
    replace_all_mem = "const ALL_MEMBERS = new Set([\n      '231000393', '251000861'"
    if target_all_mem in html:
        html = html.replace(target_all_mem, replace_all_mem, 1)

    # 2. Add SENNA_REG constant
    target_regs = "const LOVE_REG = '7676767766';"
    replace_regs = "const SENNA_REG = '231000393';\n    const LOVE_REG = '7676767766';"
    if target_regs in html:
        html = html.replace(target_regs, replace_regs, 1)

    # 3. Add to MEMBERS_DATABASE under Electrical Division
    target_elec = "'241012132': { name: 'Bassem Toulan', depts: ['electrical'], role: 'head', email: 'toulanbassem@gmail.com' },"
    replace_elec = "'241012132': { name: 'Bassem Toulan', depts: ['electrical'], role: 'head', email: 'toulanbassem@gmail.com' },\n      '231000393': { name: 'Ahmed Hany', depts: ['electrical'], role: 'member', email: 'ahmed.hany@aeris-team.org' },"
    if target_elec in html:
        html = html.replace(target_elec, replace_elec, 1)

    # 4. Add activeTheme === 'senna' in renderDashboardGuide
    target_active_theme = 'if (regNum === \'231002350\') activeTheme = "soviet";'
    replace_active_theme = 'if (regNum === \'231000393\') activeTheme = "senna";\n      else if (regNum === \'231002350\') activeTheme = "soviet";'
    if target_active_theme in html:
        html = html.replace(target_active_theme, replace_active_theme, 1)

    # 5. Add guide block for activeTheme === 'senna' in member section
    target_guide_block = "if (activeTheme === 'spongebob') {"
    replace_guide_block = """if (activeTheme === 'senna') {
          title = "🏎️ McLaren MP4/4 Telemetry & Race Control Guide";
          welcome = "🏎️ Sba7 el fol, Ahmed Hany! 'If you no longer go for a gap that exists, you are no longer a racing driver.' Welcome to the Electrical pit wall! 🇧🇷🏁";
          items = [
            "<strong>Telemetry Feed:</strong> Click the Electrical tab to monitor real-time task telemetry and circuit progress in read-only mode.",
            "<strong>Pit Wall Data:</strong> Click task cards to inspect advisory notes, sensor metrics, and circuit directives. Action buttons (Start/Done) are restricted to pit crew leaders.",
            "<strong>Senna Telemetry & Shift Light HUD:</strong> Use the interactive Ayrton Senna telemetry HUD below to listen to legendary V6 Turbo engine revs, test your reaction time on pit start lights, and cycle through iconic Senna quotes.",
            "<strong>Team Pit Ledger (Finances):</strong> Access the Budget Tracker to monitor electrical component spendings. Total team income and net budget stats are locked in the team motorhome."
          ];
        } else if (activeTheme === 'spongebob') {"""
    if target_guide_block in html:
        html = html.replace(target_guide_block, replace_guide_block, 1)

    # 6. Add PERSONAL_GREETINGS
    target_greetings = "'2006': { name: 'Hanah'"
    replace_greetings = "'231000393': { name: 'Ahmed Hany', message: '🏎️ Welcome to the pit wall, Ahmed Hany! If you no longer go for a gap, you are no longer a racing driver. 🇧🇷🏁' },\n      '2006': { name: 'Hanah'"
    if target_greetings in html:
        html = html.replace(target_greetings, replace_greetings, 1)

    # 7. Add sessionReg early theme check
    target_session_theme = "if (sessionReg === '231002350') document.body.classList.add('soviet-theme');"
    replace_session_theme = "if (sessionReg === '231000393') document.body.classList.add('senna-theme');\n      if (sessionReg === '231002350') document.body.classList.add('soviet-theme');"
    if target_session_theme in html:
        html = html.replace(target_session_theme, replace_session_theme, 1)

    # 8. Add handleAuth early theme check
    target_auth_theme = "if (regNum === SOVIET_REG) document.body.classList.add('soviet-theme');"
    replace_auth_theme = "if (regNum === SENNA_REG) document.body.classList.add('senna-theme');\n      if (regNum === SOVIET_REG) document.body.classList.add('soviet-theme');"
    if target_auth_theme in html:
        html = html.replace(target_auth_theme, replace_auth_theme, 1)

    # 9. Add applySennaTheme() in central theme loader
    target_loader = "applyMcQueenTheme();"
    replace_loader = "applySennaTheme();\n        applyMcQueenTheme();"
    if target_loader in html:
        html = html.replace(target_loader, replace_loader, 1)

    # 10. Add applySennaTheme implementation before McQueen theme block
    target_mcqueen_block = "/* ========== LIGHTNING MCQUEEN THEME (231003934 only) ========== */"
    senna_implementation = """/* ========== AYRTON SENNA THEME (231000393 only) ========== */

    function isSennaUser() {
      return safeSession.getItem('aeris_auth_reg') === SENNA_REG;
    }

    function applySennaTheme() {
      if (!isSennaUser()) {
        document.body.classList.remove('senna-theme');
        document.querySelectorAll('.senna-corner, .senna-corner-tl, .senna-bubble, .senna-track, .senna-telemetry-card').forEach(el => el.remove());
        return;
      }

      document.body.classList.add('senna-theme');

      // Customize welcome banner icon to be a racing car/helmet SVG
      const welcomeBanner = document.getElementById('welcome-banner');
      if (welcomeBanner) {
        const welcomeIcon = welcomeBanner.querySelector('.welcome-banner__icon');
        if (welcomeIcon) {
          welcomeIcon.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFE100" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="car-spin"><rect x="1" y="3" width="15" height="13" rx="2" ry="2"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>`;
        }
      }

      // Senna Badge float at bottom right
      if (!document.querySelector('.senna-corner')) {
        const corner = document.createElement('div');
        corner.className = 'senna-corner';
        corner.title = 'Ayrton Senna — Click for Wisdom';
        corner.innerHTML = `<div class="senna-badge-helmet"><span class="senna-num">1</span><span class="senna-flag">🇧🇷</span></div>`;
        document.body.appendChild(corner);

        const bubble = document.createElement('div');
        bubble.className = 'senna-bubble';
        document.body.appendChild(bubble);

        const quotes = [
          "If you no longer go for a gap that exists, you are no longer a racing driver. 🏎️🏁",
          "I have no idols. I admire work, dedication and competence. ⚡",
          "And so you touch this limit, something happens and suddenly you can go even further. 🚀",
          "I am not designed to come second or third. I am designed to win. 🏆",
          "With your mind power, your determination, your instinct, and experience, you can fly very high. 🇧🇷",
          "Racing, competing, it's in my blood. It's part of me, it's part of my life! 🏎️💨",
          "On a given day, a given circumstance, you think you have a limit. And you then touch this limit, then something happens and suddenly you can go a little bit further. ✨"
        ];

        corner.addEventListener('click', () => {
          const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
          bubble.textContent = randomQuote;
          bubble.classList.add('show');
          playSennaEngineRev(1200, 0.35);
          setTimeout(() => bubble.classList.remove('show'), 4500);
        });
      }

      // Senna corner top-left badge
      if (!document.querySelector('.senna-corner-tl')) {
        const cornerTL = document.createElement('div');
        cornerTL.className = 'senna-corner-tl';
        cornerTL.innerHTML = `🇧🇷 🏎️ AYRTON SENNA #1 🏁`;
        document.body.appendChild(cornerTL);
      }

      // Racing track trail above task board
      const taskBoard = document.getElementById('task-board');
      if (taskBoard && !document.querySelector('.senna-track')) {
        const track = document.createElement('div');
        track.className = 'senna-track';
        track.innerHTML = `<span>🏎️ MP4/4</span><span>⚡ ERS READY</span><span>🏁 LAP 1/65</span><span>🇧🇷 SENNA #1</span><span>🏎️💨 330 KM/H</span>`;
        taskBoard.parentNode.insertBefore(track, taskBoard);
      }

      // Inject Telemetry & Engine Sound Synthesizer Card into dashboard view
      if (!document.querySelector('.senna-telemetry-card')) {
        const container = document.querySelector('.dashboard-page .container');
        if (container) {
          const telemetryCard = document.createElement('div');
          telemetryCard.className = 'senna-telemetry-card fade-in';
          telemetryCard.innerHTML = `
            <div class="senna-telemetry-header">
              <div class="senna-telemetry-title">
                <span class="senna-flag-icon">🇧🇷</span>
                <h3>AYRTON SENNA F1 TELEMETRY & SHIFT LIGHT CONTROL</h3>
                <span class="senna-live-pill">LIVE PIT WALL</span>
              </div>
              <div class="senna-telemetry-stats">
                <span class="senna-stat">CIRCUIT: <strong>INTERLAGOS</strong></span>
                <span class="senna-stat">CAR: <strong>McLAREN MP4/4 V6 TURBO</strong></span>
              </div>
            </div>
            <div class="senna-telemetry-body">
              <div class="senna-gauge-section">
                <div class="senna-rpm-bar">
                  <div class="senna-rpm-label">ENGINE TACHOMETER: <span id="senna-rpm-val">12,500</span> RPM</div>
                  <div class="senna-shift-lights">
                    <span class="light green active"></span>
                    <span class="light green active"></span>
                    <span class="light green active"></span>
                    <span class="light yellow active"></span>
                    <span class="light yellow active"></span>
                    <span class="light red active"></span>
                    <span class="light red blink"></span>
                  </div>
                </div>
                <div class="senna-readouts">
                  <div class="senna-readout-box">
                    <span class="lbl">SPEED</span>
                    <span class="val" id="senna-speed">332</span>
                    <span class="unit">KM/H</span>
                  </div>
                  <div class="senna-readout-box">
                    <span class="lbl">GEAR</span>
                    <span class="val" id="senna-gear">6</span>
                    <span class="unit">MANUAL</span>
                  </div>
                  <div class="senna-readout-box">
                    <span class="lbl">BEST LAP</span>
                    <span class="val">1:19.537</span>
                    <span class="unit">QUALIFYING</span>
                  </div>
                  <div class="senna-readout-box">
                    <span class="lbl">VOLTAGE</span>
                    <span class="val">24.8V</span>
                    <span class="unit">ELEC BUS</span>
                  </div>
                </div>
              </div>
              <div class="senna-controls-section">
                <button class="senna-btn senna-btn--rev" id="senna-rev-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>
                  <span>Rev Honda V6 Turbo Engine</span>
                </button>
                <button class="senna-btn senna-btn--lights" id="senna-reaction-btn">
                  <span>🚥 Pit Start Light Challenge</span>
                </button>
                <div class="senna-reaction-result" id="senna-reaction-res">Click "Pit Start Light Challenge" to test reaction time!</div>
              </div>
            </div>
          `;
          
          const welcomeBannerEl = document.getElementById('welcome-banner');
          if (welcomeBannerEl && welcomeBannerEl.nextSibling) {
            container.insertBefore(telemetryCard, welcomeBannerEl.nextSibling);
          } else {
            container.prepend(telemetryCard);
          }

          setupSennaWidgetInteractions();
        }
      }

      // Customize task form headers for Senna
      const formTitle = document.querySelector('.task-form__title');
      if (formTitle) {
        const svg = formTitle.querySelector('svg');
        formTitle.textContent = '';
        if (svg) formTitle.appendChild(svg);
        formTitle.append(' Log Electrical Sensor Directive / Task');
      }

      const labelTaskTitle = document.querySelector('label[for="task-title"]');
      if (labelTaskTitle) labelTaskTitle.textContent = '🏎️ Circuit Target / Directive';

      const labelTaskDesc = document.querySelector('label[for="task-description"]');
      if (labelTaskDesc) labelTaskDesc.textContent = '🔧 Telemetry & Wiring Specs';

      const labelTaskPriority = document.querySelector('label[for="task-priority"]');
      if (labelTaskPriority) labelTaskPriority.textContent = '⚡ Engine RPM / Voltage';

      const prioritySelect = document.getElementById('task-priority');
      if (prioritySelect) {
        prioritySelect.querySelector('option[value="low"]').textContent = '🟢 Pit Lane Limiter (Low)';
        prioritySelect.querySelector('option[value="medium"]').textContent = '🟡 V6 Turbo Mid-Power (Med)';
        prioritySelect.querySelector('option[value="high"]').textContent = '🔴 DRS Maximum Boost (High)';
        prioritySelect.querySelector('option[value="urgent"]').textContent = '🚨 POLE POSITION QUALIFYING (Urgent)';
      }

      const labelTaskDeadline = document.querySelector('label[for="task-deadline"]');
      if (labelTaskDeadline) labelTaskDeadline.textContent = '🏁 Chequered Flag ETA';

      const submitTaskBtn = document.getElementById('submit-task');
      if (submitTaskBtn) {
        const svg = submitTaskBtn.querySelector('svg');
        submitTaskBtn.textContent = '';
        if (svg) submitTaskBtn.appendChild(svg);
        submitTaskBtn.append(' Launch Telemetry Task!');
      }
    }

    // Web Audio API engine rev synthesizer for Senna theme
    function playSennaEngineRev(targetFreq = 950, duration = 0.4) {
      try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) return;
        const ctx = new AudioCtx();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(300, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(targetFreq, ctx.currentTime + duration * 0.7);
        osc.frequency.exponentialRampToValueAtTime(400, ctx.currentTime + duration);

        gain.gain.setValueAtTime(0.01, ctx.currentTime);
        gain.gain.linearRampToValueAtTime(0.2, ctx.currentTime + 0.05);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start();
        osc.stop(ctx.currentTime + duration);
      } catch (e) {
        console.warn("Audio Context blocked or not supported:", e);
      }
    }

    // Senna Pit Start Light Challenge Logic
    let sennaLightTimeout = null;
    let sennaStartTime = 0;

    function setupSennaWidgetInteractions() {
      const revBtn = document.getElementById('senna-rev-btn');
      if (revBtn) {
        revBtn.onclick = () => {
          playSennaEngineRev(1400, 0.7);
          const rpmVal = document.getElementById('senna-rpm-val');
          const speedVal = document.getElementById('senna-speed');
          if (rpmVal) rpmVal.textContent = '14,800';
          if (speedVal) speedVal.textContent = '348';
          setTimeout(() => {
            if (rpmVal) rpmVal.textContent = '12,500';
            if (speedVal) speedVal.textContent = '332';
          }, 800);
        };
      }

      const reactBtn = document.getElementById('senna-reaction-btn');
      const reactRes = document.getElementById('senna-reaction-res');
      if (reactBtn && reactRes) {
        reactBtn.onclick = () => {
          if (reactBtn.dataset.state === 'waiting') {
            clearTimeout(sennaLightTimeout);
            reactBtn.dataset.state = 'idle';
            reactRes.className = 'senna-reaction-result early';
            reactRes.textContent = '❌ FALSE START! You jumped the start lights!';
            return;
          }

          if (reactBtn.dataset.state === 'go') {
            const reactionTime = Math.round(performance.now() - sennaStartTime);
            reactBtn.dataset.state = 'idle';
            reactRes.className = 'senna-reaction-result success';
            let rating = '🏎️ Senna Speed!';
            if (reactionTime < 220) rating = '⚡ GOD-LIKE REACTION! (Senna Level)';
            else if (reactionTime < 300) rating = '🏆 F1 Podium Reaction!';
            else rating = '🏎️ Good Pit Stop!';
            reactRes.innerHTML = `🏁 Reaction Time: <strong>${reactionTime} ms</strong> — ${rating}`;
            return;
          }

          reactBtn.dataset.state = 'waiting';
          reactRes.className = 'senna-reaction-result waiting';
          reactRes.textContent = '🔴 RED LIGHTS ON... Wait for lights OUT! 🔴';
          
          const delay = 2000 + Math.random() * 2500;
          sennaLightTimeout = setTimeout(() => {
            reactBtn.dataset.state = 'go';
            sennaStartTime = performance.now();
            reactRes.className = 'senna-reaction-result go';
            reactRes.textContent = '🟢 LIGHTS OUT! CLICK NOW! 🚀';
            playSennaEngineRev(1100, 0.2);
          }, delay);
        };
      }
    }


    """
    if target_mcqueen_block in html:
        html = html.replace(target_mcqueen_block, senna_implementation + target_mcqueen_block, 1)

    with open(dashboard_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print('Updated dashboard.html successfully!')

    # Now update dashboard.css
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()

    senna_css = """
/* ==========================================================================
   🏎️ AYRTON SENNA FORMULA 1 THEME (231000393)
   ========================================================================== */
body.senna-theme {
  --bg-primary: #0b0f19;
  --bg-secondary: #151c2c;
  --bg-card: rgba(21, 28, 44, 0.85);
  --accent: #ffe100; /* Senna Yellow */
  --accent-dim: #009b3a; /* Brasil Green */
  --accent-glow: rgba(255, 225, 0, 0.3);
  background: #0b0f19 !important;
  color: #f1f5f9 !important;
  font-family: 'Fredoka', 'Nunito', sans-serif !important;
  cursor: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='28' height='28' viewBox='0 0 28 28'><text y='22' font-size='22'>🏎️</text></svg>") 2 2, auto !important;
}

.senna-theme .dashboard-page {
  background: 
    radial-gradient(ellipse 800px 600px at 50% 20%, rgba(255, 225, 0, 0.08) 0%, transparent 70%),
    radial-gradient(ellipse 500px 400px at 80% 80%, rgba(0, 155, 58, 0.06) 0%, transparent 60%),
    radial-gradient(ellipse 500px 400px at 20% 70%, rgba(0, 51, 153, 0.08) 0%, transparent 60%),
    var(--bg-primary) !important;
  background-attachment: fixed;
}

.senna-theme h1,
.senna-theme h2,
.senna-theme h3,
.senna-theme .page-title,
.senna-theme .welcome-banner__greeting {
  font-family: 'Luckiest Guy', 'Fredoka', cursive !important;
  letter-spacing: 1px !important;
}

/* Senna Corner Helmet Badge */
.senna-theme .senna-corner {
  position: fixed;
  bottom: 24px;
  right: 24px;
  width: 62px;
  height: 62px;
  border-radius: 50%;
  background: linear-gradient(135deg, #ffe100 0%, #009b3a 50%, #003399 100%);
  border: 3px solid #ffffff;
  box-shadow: 0 8px 24px rgba(255, 225, 0, 0.4), inset 0 0 10px rgba(255, 255, 255, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 50;
  transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.2s ease;
}

.senna-theme .senna-corner:hover {
  transform: scale(1.15) rotate(12deg);
  box-shadow: 0 12px 32px rgba(255, 225, 0, 0.7);
}

.senna-theme .senna-badge-helmet {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2px;
}

.senna-theme .senna-num {
  font-family: 'Luckiest Guy', cursive;
  font-size: 24px;
  color: #ffffff;
  text-shadow: 2px 2px 0px #000, -1px -1px 0px #000, 1px -1px 0px #000;
  font-style: italic;
}

.senna-theme .senna-flag {
  font-size: 16px;
}

.senna-theme .senna-bubble {
  position: fixed;
  bottom: 96px;
  right: 35px;
  background: #ffffff;
  color: #0b0f19;
  padding: 12px 18px;
  border-radius: 16px 16px 2px 16px;
  font-family: 'Fredoka', sans-serif;
  font-weight: 600;
  font-size: 0.88rem;
  max-width: 280px;
  opacity: 0;
  transform: translateY(10px) scale(0.9);
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  pointer-events: none;
  z-index: 100;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
  border: 3px solid #ffe100;
}

.senna-theme .senna-bubble.show {
  opacity: 1;
  transform: translateY(0) scale(1);
}

.senna-theme .senna-bubble::after {
  content: '';
  position: absolute;
  bottom: -9px;
  right: 20px;
  border-width: 9px 9px 0;
  border-style: solid;
  border-color: #ffe100 transparent;
  display: block;
  width: 0;
}

.senna-theme .senna-corner-tl {
  position: fixed;
  top: 90px;
  left: 24px;
  opacity: 0.85;
  z-index: 50;
  font-size: 0.85rem;
  font-weight: 700;
  color: #ffe100;
  background: rgba(11, 15, 25, 0.85);
  padding: 6px 14px;
  border-radius: 20px;
  border: 1px solid rgba(255, 225, 0, 0.3);
  letter-spacing: 1px;
}

.senna-theme .senna-track {
  display: flex;
  align-items: center;
  justify-content: space-around;
  background: linear-gradient(90deg, rgba(255,225,0,0.1), rgba(0,155,58,0.1), rgba(0,51,153,0.1));
  border: 1px solid rgba(255, 225, 0, 0.2);
  border-radius: 12px;
  padding: 8px 16px;
  margin-bottom: 20px;
  font-size: 0.85rem;
  font-weight: 700;
  color: #ffe100;
}

.senna-theme .senna-track span {
  animation: sennaPulse 2s infinite alternate;
}

@keyframes sennaPulse {
  0% { opacity: 0.7; transform: translateX(-2px); }
  100% { opacity: 1; transform: translateX(2px); }
}

/* Senna Telemetry Card Widget */
.senna-telemetry-card {
  background: linear-gradient(135deg, rgba(21, 28, 44, 0.95), rgba(11, 15, 25, 0.95));
  border: 2px solid rgba(255, 225, 0, 0.35);
  border-radius: 16px;
  padding: 20px;
  margin-bottom: 24px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 0 15px rgba(255, 225, 0, 0.05);
}

.senna-telemetry-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255, 225, 0, 0.2);
  padding-bottom: 12px;
  margin-bottom: 16px;
  flex-wrap: wrap;
  gap: 10px;
}

.senna-telemetry-title {
  display: flex;
  align-items: center;
  gap: 10px;
}

.senna-telemetry-title h3 {
  font-size: 1.05rem;
  color: #ffe100;
  margin: 0;
}

.senna-live-pill {
  background: #e10600;
  color: #fff;
  font-size: 0.65rem;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: 10px;
  letter-spacing: 1px;
  animation: pulse 1.5s infinite;
}

.senna-telemetry-stats {
  display: flex;
  gap: 16px;
  font-size: 0.8rem;
  color: #94a3b8;
}

.senna-telemetry-stats strong {
  color: #fff;
}

.senna-telemetry-body {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

@media (max-width: 768px) {
  .senna-telemetry-body {
    grid-template-columns: 1fr;
  }
}

.senna-rpm-bar {
  background: rgba(0, 0, 0, 0.4);
  padding: 12px 16px;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.05);
  margin-bottom: 14px;
}

.senna-rpm-label {
  font-size: 0.8rem;
  font-weight: 700;
  color: #cbd5e1;
  margin-bottom: 8px;
}

.senna-rpm-label span {
  color: #ffe100;
  font-family: 'VT323', monospace;
  font-size: 1.2rem;
}

.senna-shift-lights {
  display: flex;
  gap: 8px;
  justify-content: space-between;
}

.senna-shift-lights .light {
  flex: 1;
  height: 14px;
  border-radius: 4px;
  background: rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 0 4px rgba(0,0,0,0.5);
}

.senna-shift-lights .light.green.active {
  background: #009b3a;
  box-shadow: 0 0 10px #009b3a;
}

.senna-shift-lights .light.yellow.active {
  background: #ffe100;
  box-shadow: 0 0 10px #ffe100;
}

.senna-shift-lights .light.red.active {
  background: #e10600;
  box-shadow: 0 0 10px #e10600;
}

.senna-shift-lights .light.red.blink {
  animation: blink 0.4s infinite alternate;
}

.senna-readouts {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
}

.senna-readout-box {
  background: rgba(0, 0, 0, 0.3);
  padding: 10px;
  border-radius: 10px;
  border: 1px solid rgba(255, 225, 0, 0.15);
  text-align: center;
}

.senna-readout-box .lbl {
  display: block;
  font-size: 0.65rem;
  color: #94a3b8;
  font-weight: 700;
}

.senna-readout-box .val {
  display: block;
  font-family: 'VT323', monospace;
  font-size: 1.4rem;
  color: #ffe100;
  font-weight: 700;
}

.senna-readout-box .unit {
  display: block;
  font-size: 0.6rem;
  color: #64748b;
}

.senna-controls-section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 12px;
}

.senna-btn {
  padding: 12px 18px;
  border-radius: 12px;
  font-family: 'Fredoka', sans-serif;
  font-weight: 700;
  font-size: 0.9rem;
  cursor: pointer;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.25s ease;
}

.senna-btn--rev {
  background: linear-gradient(135deg, #ffe100 0%, #f59e0b 100%);
  color: #0b0f19;
  box-shadow: 0 4px 15px rgba(255, 225, 0, 0.3);
}

.senna-btn--rev:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255, 225, 0, 0.5);
}

.senna-btn--lights {
  background: linear-gradient(135deg, #009b3a 0%, #003399 100%);
  color: #ffffff;
  box-shadow: 0 4px 15px rgba(0, 155, 58, 0.3);
}

.senna-btn--lights:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 155, 58, 0.5);
}

.senna-reaction-result {
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 225, 0, 0.2);
  border-radius: 10px;
  padding: 10px 14px;
  font-size: 0.82rem;
  text-align: center;
  color: #cbd5e1;
}

.senna-reaction-result.waiting {
  border-color: #e10600;
  color: #ff4d4d;
}

.senna-reaction-result.go {
  border-color: #009b3a;
  color: #00ff66;
  font-weight: 800;
}

.senna-reaction-result.success {
  border-color: #ffe100;
  color: #ffe100;
}

.senna-reaction-result.early {
  border-color: #ef4444;
  color: #ef4444;
}

/* Task Cards & Board styling for Senna Theme */
.senna-theme .task-column {
  background: rgba(21, 28, 44, 0.7) !important;
  border: 1px solid rgba(255, 225, 0, 0.2) !important;
}

.senna-theme .task-column__header {
  border-bottom: 2px solid #ffe100 !important;
}

.senna-theme .task-column__header h3 {
  color: #ffe100 !important;
}

.senna-theme .task-card {
  background: rgba(11, 15, 25, 0.9) !important;
  border: 1px solid rgba(255, 225, 0, 0.15) !important;
  transition: all 0.25s ease !important;
}

.senna-theme .task-card:hover {
  border-color: #ffe100 !important;
  box-shadow: 0 6px 20px rgba(255, 225, 0, 0.25) !important;
  transform: translateY(-3px) !important;
}

.senna-theme .dept-tab.active {
  background: #ffe100 !important;
  color: #0b0f19 !important;
  font-weight: 700 !important;
  box-shadow: 0 0 15px rgba(255, 225, 0, 0.4) !important;
}

.senna-theme .welcome-banner {
  background: linear-gradient(135deg, rgba(21, 28, 44, 0.95), rgba(11, 15, 25, 0.95)) !important;
  border: 2px solid #ffe100 !important;
  box-shadow: 0 8px 25px rgba(255, 225, 0, 0.2) !important;
}

.senna-theme .welcome-banner__icon {
  background: rgba(255, 225, 0, 0.15) !important;
  color: #ffe100 !important;
}

.senna-theme .welcome-banner__greeting strong {
  color: #ffe100 !important;
}

.senna-theme input:focus,
.senna-theme textarea:focus,
.senna-theme select:focus {
  border-color: #ffe100 !important;
  box-shadow: 0 0 10px rgba(255, 225, 0, 0.3) !important;
}
"""

    mcqueen_css_header = "/* ==========================================================================\n   🏎️ LIGHTNING MCQUEEN THEME (231003934)"
    if mcqueen_css_header in css:
        css = css.replace(mcqueen_css_header, senna_css + "\n" + mcqueen_css_header, 1)

    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

    print('Updated dashboard.css successfully!')

if __name__ == '__main__':
    main()
