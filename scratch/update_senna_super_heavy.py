import sys
import os
import re

def main():
    dashboard_path = 'c:/Users/abdel/Desktop/aeris-website-main/dashboard.html'
    css_path = 'c:/Users/abdel/Desktop/aeris-website-main/dashboard.css'

    with open(dashboard_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update PERSONAL_GREETINGS for 231000393 to include "Welcome back, Ahmed Hany!"
    old_greeting = "'231000393': { name: 'Ahmed Hany', message: '🏎️ Welcome to the pit wall, Ahmed Hany! If you no longer go for a gap, you are no longer a racing driver. 🇧🇷🏁' },"
    new_greeting = "'231000393': { name: 'Ahmed Hany', message: '🏎️ Welcome back, Ahmed Hany! \"If you no longer go for a gap that exists, you are no longer a racing driver.\" 🇧🇷🏁' },"
    if old_greeting in html:
        html = html.replace(old_greeting, new_greeting, 1)

    # 2. Upgrade applySennaTheme to SUPER HEAVY status
    # Locate applySennaTheme block
    pattern = r'/\* ========== AYRTON SENNA THEME \(231000393 only\) ==========\ \*/.*?(?=/\* ========== LIGHTNING MCQUEEN THEME)'
    
    super_heavy_senna_js = """/* ========== AYRTON SENNA THEME (231000393 only) — SUPER HEAVY EDITION ========== */

    function isSennaUser() {
      return safeSession.getItem('aeris_auth_reg') === SENNA_REG;
    }

    // Audio synthesizer engine for Senna Theme
    function playSennaSound(type) {
      try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) return;
        const ctx = new AudioCtx();

        if (type === 'rev') {
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(320, ctx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(1550, ctx.currentTime + 0.45);
          osc.frequency.exponentialRampToValueAtTime(450, ctx.currentTime + 0.7);

          gain.gain.setValueAtTime(0.01, ctx.currentTime);
          gain.gain.linearRampToValueAtTime(0.25, ctx.currentTime + 0.08);
          gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.7);

          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start();
          osc.stop(ctx.currentTime + 0.7);
        } else if (type === 'pit_gun') {
          // Pneumatic air gun noise burst
          const bufferSize = ctx.sampleRate * 0.25;
          const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
          const data = buffer.getChannelData(0);
          for (let i = 0; i < bufferSize; i++) {
            data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (bufferSize * 0.3));
          }
          const noise = ctx.createBufferSource();
          noise.buffer = buffer;
          const filter = ctx.createBiquadFilter();
          filter.type = 'bandpass';
          filter.frequency.value = 1800;
          filter.Q.value = 3;
          const gain = ctx.createGain();
          gain.gain.setValueAtTime(0.3, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.25);

          noise.connect(filter);
          filter.connect(gain);
          gain.connect(ctx.destination);
          noise.start();
        } else if (type === 'radio') {
          // F1 Pit Radio Beep Chatter
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(1750, ctx.currentTime);
          osc.frequency.setValueAtTime(2200, ctx.currentTime + 0.08);
          gain.gain.setValueAtTime(0.12, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.2);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start();
          osc.stop(ctx.currentTime + 0.2);
        } else if (type === 'victory') {
          // Podium chord fanfare
          [440, 554.37, 659.25, 880].forEach((freq, idx) => {
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.value = freq;
            gain.gain.setValueAtTime(0.01, ctx.currentTime + idx * 0.08);
            gain.gain.linearRampToValueAtTime(0.15, ctx.currentTime + idx * 0.08 + 0.05);
            gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 1.2);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start(ctx.currentTime + idx * 0.08);
            osc.stop(ctx.currentTime + 1.2);
          });
        }
      } catch (e) {
        console.warn("Audio Context error:", e);
      }
    }

    function applySennaTheme() {
      if (!isSennaUser()) {
        document.body.classList.remove('senna-theme');
        document.querySelectorAll('.senna-corner, .senna-corner-tl, .senna-bubble, .senna-track, .senna-telemetry-card, .senna-speed-canvas, .senna-spark-container').forEach(el => el.remove());
        return;
      }

      document.body.classList.add('senna-theme');

      // 1. Customize top welcome banner explicitly with Ahmed Hany's name & F1 Helmet SVG
      const welcomeBanner = document.getElementById('welcome-banner');
      if (welcomeBanner) {
        const welcomeIcon = welcomeBanner.querySelector('.welcome-banner__icon');
        if (welcomeIcon) {
          welcomeIcon.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 100 100" class="senna-helmet-pulse">
              <circle cx="50" cy="50" r="46" fill="#FFE100" stroke="#009B3A" stroke-width="6"/>
              <path d="M 15 50 Q 50 20 85 50 L 85 62 Q 50 35 15 62 Z" fill="#003399"/>
              <rect x="25" y="48" width="50" height="14" rx="4" fill="#111111" opacity="0.9"/>
              <text x="50" y="86" font-family="'Luckiest Guy', sans-serif" font-size="22" fill="#009B3A" text-anchor="middle" font-weight="900">#1</text>
            </svg>
          `;
        }
        const welcomeText = welcomeBanner.querySelector('.welcome-banner__text');
        if (welcomeText) {
          welcomeText.innerHTML = `
            <span class="welcome-banner__greeting">🏎️ Welcome back, <strong>Ahmed Hany</strong>! ⚡</span>
            <span class="welcome-banner__role">Logged in as <strong>Ahmed Hany</strong> — Electrical Division Member | 🇧🇷 3x F1 World Champion Theme</span>
          `;
        }
      }

      # 2. Senna Badge float at bottom right
      if (!document.querySelector('.senna-corner')) {
        const corner = document.createElement('div');
        corner.className = 'senna-corner';
        corner.title = 'Ayrton Senna — Click for F1 Wisdom & Sound';
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
          playSennaSound('rev');
          setTimeout(() => bubble.classList.remove('show'), 5000);
        });
      }

      # 3. Senna corner top-left badge
      if (!document.querySelector('.senna-corner-tl')) {
        const cornerTL = document.createElement('div');
        cornerTL.className = 'senna-corner-tl';
        cornerTL.innerHTML = `🇧🇷 🏎️ AYRTON SENNA #1 🏁`;
        document.body.appendChild(cornerTL);
      }

      # 4. Racing track trail above task board
      const taskBoard = document.getElementById('task-board');
      if (taskBoard && !document.querySelector('.senna-track')) {
        const track = document.createElement('div');
        track.className = 'senna-track';
        track.innerHTML = `<span>🏎️ McLAREN MP4/4</span><span>⚡ ERS BOOST 100%</span><span>🏁 LAP 1/65 (INTERLAGOS)</span><span>🇧🇷 SENNA #1</span><span>🏎️💨 348 KM/H</span>`;
        taskBoard.parentNode.insertBefore(track, taskBoard);
      }

      # 5. Inject Super Heavy Telemetry & Steering Wheel Soundboard Card
      if (!document.querySelector('.senna-telemetry-card')) {
        const container = document.querySelector('.dashboard-page .container');
        if (container) {
          const telemetryCard = document.createElement('div');
          telemetryCard.className = 'senna-telemetry-card fade-in';
          telemetryCard.innerHTML = `
            <div class="senna-telemetry-header">
              <div class="senna-telemetry-title">
                <span class="senna-flag-icon">🇧🇷</span>
                <h3>AYRTON SENNA F1 SUPER HEAVY PIT WALL TELEMETRY</h3>
                <span class="senna-live-pill">LIVE PIT WALL</span>
              </div>
              <div class="senna-car-selector">
                <button class="senna-car-tab active" data-car="mp44">🏎️ MP4/4 (1988)</button>
                <button class="senna-car-tab" data-car="lotus99t">🟡 Lotus 99T (1987)</button>
                <button class="senna-car-tab" data-car="mp46">🔴 MP4/6 (1991)</button>
                <button class="senna-car-tab" data-car="lotus97t">🖤 Lotus 97T (1985)</button>
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
                    <span class="val" id="senna-lap">1:19.537</span>
                    <span class="unit">QUALIFYING</span>
                  </div>
                  <div class="senna-readout-box">
                    <span class="lbl">ELEC BUS</span>
                    <span class="val">24.8V</span>
                    <span class="unit">OK</span>
                  </div>
                </div>
              </div>
              <div class="senna-controls-section">
                <div class="senna-soundboard-grid">
                  <button class="senna-btn senna-btn--rev" id="senna-rev-btn">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>
                    <span>Rev V6 Engine</span>
                  </button>
                  <button class="senna-btn senna-btn--pit" id="senna-pit-btn">
                    <span>🔧 Pit Air Gun</span>
                  </button>
                  <button class="senna-btn senna-btn--radio" id="senna-radio-btn">
                    <span>📻 Radio Chatter</span>
                  </button>
                  <button class="senna-btn senna-btn--victory" id="senna-victory-btn">
                    <span>🏆 Podium Fanfare</span>
                  </button>
                </div>
                <div class="senna-reaction-wrapper">
                  <button class="senna-btn senna-btn--lights" id="senna-reaction-btn">
                    <span>🚥 Pit Start Light Challenge</span>
                  </button>
                  <div class="senna-reaction-result" id="senna-reaction-res">Click "Pit Start Light Challenge" to test reaction time!</div>
                </div>
              </div>
            </div>
          `;

          const welcomeBannerEl = document.getElementById('welcome-banner');
          if (welcomeBannerEl && welcomeBannerEl.nextSibling) {
            container.insertBefore(telemetryCard, welcomeBannerEl.nextSibling);
          } else {
            container.prepend(telemetryCard);
          }

          setupSennaSuperHeavyInteractions();
        }
      }

      # 6. Customize task form headers for Senna
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

      # 7. Start Mouse Cursor Spark Particles Engine
      initSennaSparkParticles();
    }

    # Mouse spark particles engine for Super Heavy Senna Theme
    function initSennaSparkParticles() {
      if (document.querySelector('.senna-spark-container')) return;
      const container = document.createElement('div');
      container.className = 'senna-spark-container';
      container.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:9999;overflow:hidden;';
      document.body.appendChild(container);

      let lastX = 0, lastY = 0;
      window.addEventListener('mousemove', (e) => {
        if (!document.body.classList.contains('senna-theme')) return;
        const dist = Math.hypot(e.clientX - lastX, e.clientY - lastY);
        if (dist > 25) {
          lastX = e.clientX;
          lastY = e.clientY;
          const spark = document.createElement('div');
          spark.className = 'senna-cursor-spark';
          const size = Math.random() * 6 + 4;
          const colors = ['#FFE100', '#009B3A', '#003399', '#E10600'];
          const color = colors[Math.floor(Math.random() * colors.length)];
          spark.style.cssText = `
            position: absolute;
            left: ${e.clientX}px;
            top: ${e.clientY}px;
            width: ${size}px;
            height: ${size}px;
            background: ${color};
            border-radius: 50%;
            box-shadow: 0 0 10px ${color};
            pointer-events: none;
            transition: all 0.6s cubic-bezier(0.1, 0.8, 0.3, 1);
            transform: translate(-50%, -50%) scale(1);
            opacity: 0.9;
          `;
          container.appendChild(spark);
          setTimeout(() => {
            spark.style.transform = `translate(${-50 + (Math.random() * 40 - 20)}%, ${-50 + Math.random() * 40 + 10}px) scale(0)`;
            spark.style.opacity = '0';
          }, 20);
          setTimeout(() => spark.remove(), 650);
        }
      });
    }

    # Senna Widget Interactions & Soundboard logic
    let sennaLightTimeout = null;
    let sennaStartTime = 0;

    function setupSennaSuperHeavyInteractions() {
      const revBtn = document.getElementById('senna-rev-btn');
      if (revBtn) {
        revBtn.onclick = () => {
          playSennaSound('rev');
          const rpmVal = document.getElementById('senna-rpm-val');
          const speedVal = document.getElementById('senna-speed');
          if (rpmVal) rpmVal.textContent = '15,200';
          if (speedVal) speedVal.textContent = '352';
          setTimeout(() => {
            if (rpmVal) rpmVal.textContent = '12,500';
            if (speedVal) speedVal.textContent = '332';
          }, 800);
        };
      }

      const pitBtn = document.getElementById('senna-pit-btn');
      if (pitBtn) {
        pitBtn.onclick = () => {
          playSennaSound('pit_gun');
        };
      }

      const radioBtn = document.getElementById('senna-radio-btn');
      if (radioBtn) {
        radioBtn.onclick = () => {
          playSennaSound('radio');
          const reactRes = document.getElementById('senna-reaction-res');
          if (reactRes) {
            reactRes.className = 'senna-reaction-result success';
            reactRes.innerHTML = '📻 <em>"Box Box Box, Ahmed! Push now! Telemetry looks optimal!"</em>';
          }
        };
      }

      const vicBtn = document.getElementById('senna-victory-btn');
      if (vicBtn) {
        vicBtn.onclick = () => {
          playSennaSound('victory');
          const reactRes = document.getElementById('senna-reaction-res');
          if (reactRes) {
            reactRes.className = 'senna-reaction-result success';
            reactRes.innerHTML = '🏆 <strong>P1 CHAMPION!</strong> 🏁 Chequered flag victory at Interlagos!';
          }
        };
      }

      # Car selector tabs logic
      const carTabs = document.querySelectorAll('.senna-car-tab');
      const carSpecs = {
        'mp44': { rpm: '12,500', speed: '332', lap: '1:19.537' },
        'lotus99t': { rpm: '11,800', speed: '320', lap: '1:21.140' },
        'mp46': { rpm: '14,200', speed: '345', lap: '1:18.200' },
        'lotus97t': { rpm: '11,200', speed: '315', lap: '1:24.010' }
      };

      carTabs.forEach(tab => {
        tab.onclick = () => {
          carTabs.forEach(t => t.classList.remove('active'));
          tab.classList.add('active');
          const car = tab.dataset.car;
          if (carSpecs[car]) {
            const rpmVal = document.getElementById('senna-rpm-val');
            const speedVal = document.getElementById('senna-speed');
            const lapVal = document.getElementById('senna-lap');
            if (rpmVal) rpmVal.textContent = carSpecs[car].rpm;
            if (speedVal) speedVal.textContent = carSpecs[car].speed;
            if (lapVal) lapVal.textContent = carSpecs[car].lap;
          }
          playSennaSound('rev');
        };
      });

      # Reaction Time Light Challenge
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
            playSennaSound('victory');
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
            playSennaSound('rev');
          }, delay);
        };
      }
    }

"""

    # Perform replace of Senna JS block
    html = re.sub(pattern, super_heavy_senna_js + "\n\n    ", html, flags=re.DOTALL)

    with open(dashboard_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print('Updated dashboard.html with Super Heavy Senna JS!')

    # 3. Upgrade dashboard.css with Super Heavy Senna Styles
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()

    css_pattern = r'/\* ==========================================================================\ \*\n   🏎️ AYRTON SENNA FORMULA 1 THEME \(231000393\).*?(?=/\* ==========================================================================\ \*\n   🏎️ LIGHTNING MCQUEEN THEME)'

    super_heavy_senna_css = """/* ==========================================================================
   🏎️ AYRTON SENNA FORMULA 1 SUPER HEAVY THEME (231000393)
   ========================================================================== */
body.senna-theme {
  --bg-primary: #080c14;
  --bg-secondary: #121927;
  --bg-card: rgba(18, 25, 39, 0.9);
  --accent: #ffe100; /* Senna Yellow */
  --accent-dim: #009b3a; /* Brasil Green */
  --accent-blue: #003399; /* Nacional Blue */
  --accent-red: #e10600; /* McLaren Red */
  --accent-glow: rgba(255, 225, 0, 0.35);
  background: #080c14 !important;
  color: #f8fafc !important;
  font-family: 'Fredoka', 'Nunito', sans-serif !important;
  cursor: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='28' height='28' viewBox='0 0 28 28'><text y='22' font-size='22'>🏎️</text></svg>") 2 2, auto !important;
}

/* Background Super Heavy Racing Grid & Carbon Mesh */
.senna-theme .dashboard-page {
  background: 
    radial-gradient(ellipse 900px 700px at 50% 15%, rgba(255, 225, 0, 0.12) 0%, transparent 75%),
    radial-gradient(ellipse 600px 500px at 85% 85%, rgba(0, 155, 58, 0.1) 0%, transparent 65%),
    radial-gradient(ellipse 600px 500px at 15% 75%, rgba(0, 51, 153, 0.12) 0%, transparent 65%),
    repeating-linear-gradient(45deg, rgba(255,225,0,0.02) 0, rgba(255,225,0,0.02) 2px, transparent 0, transparent 10px),
    #080c14 !important;
  background-attachment: fixed;
  position: relative;
}

/* Side Racing Stripes for Heavy Look */
.senna-theme .dashboard-page::before,
.senna-theme .dashboard-page::after {
  content: '';
  position: fixed;
  top: 0;
  bottom: 0;
  width: 8px;
  z-index: 99;
  pointer-events: none;
}
.senna-theme .dashboard-page::before {
  left: 0;
  background: linear-gradient(180deg, #ffe100 0%, #009b3a 50%, #003399 100%);
  box-shadow: 2px 0 15px rgba(255, 225, 0, 0.5);
}
.senna-theme .dashboard-page::after {
  right: 0;
  background: linear-gradient(180deg, #003399 0%, #009b3a 50%, #ffe100 100%);
  box-shadow: -2px 0 15px rgba(255, 225, 0, 0.5);
}

.senna-theme h1,
.senna-theme h2,
.senna-theme h3,
.senna-theme .page-title,
.senna-theme .welcome-banner__greeting {
  font-family: 'Luckiest Guy', 'Fredoka', cursive !important;
  letter-spacing: 1px !important;
}

/* Site Header Styling Override for Senna Theme */
.senna-theme .site-header {
  background: rgba(8, 12, 20, 0.95) !important;
  border-bottom: 2px solid #ffe100 !important;
  box-shadow: 0 4px 20px rgba(255, 225, 0, 0.25) !important;
}
.senna-theme .nav-links a {
  color: #e2e8f0 !important;
  font-weight: 600 !important;
}
.senna-theme .nav-links a:hover,
.senna-theme .nav-links a.active {
  color: #ffe100 !important;
  text-shadow: 0 0 10px rgba(255, 225, 0, 0.6) !important;
}

/* Senna Corner Helmet Badge */
.senna-theme .senna-corner {
  position: fixed;
  bottom: 24px;
  right: 24px;
  width: 66px;
  height: 66px;
  border-radius: 50%;
  background: linear-gradient(135deg, #ffe100 0%, #009b3a 50%, #003399 100%);
  border: 3px solid #ffffff;
  box-shadow: 0 8px 28px rgba(255, 225, 0, 0.5), inset 0 0 12px rgba(255, 255, 255, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 50;
  transition: transform 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.25s ease;
}

.senna-theme .senna-corner:hover {
  transform: scale(1.18) rotate(15deg);
  box-shadow: 0 12px 35px rgba(255, 225, 0, 0.8);
}

.senna-theme .senna-badge-helmet {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2px;
}

.senna-theme .senna-num {
  font-family: 'Luckiest Guy', cursive;
  font-size: 26px;
  color: #ffffff;
  text-shadow: 2px 2px 0px #000, -1px -1px 0px #000, 1px -1px 0px #000;
  font-style: italic;
}

.senna-theme .senna-flag {
  font-size: 18px;
}

.senna-theme .senna-bubble {
  position: fixed;
  bottom: 100px;
  right: 35px;
  background: #ffffff;
  color: #080c14;
  padding: 14px 20px;
  border-radius: 18px 18px 2px 18px;
  font-family: 'Fredoka', sans-serif;
  font-weight: 600;
  font-size: 0.92rem;
  max-width: 300px;
  opacity: 0;
  transform: translateY(10px) scale(0.9);
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  pointer-events: none;
  z-index: 100;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
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
  right: 22px;
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
  opacity: 0.9;
  z-index: 50;
  font-size: 0.88rem;
  font-weight: 800;
  color: #ffe100;
  background: rgba(8, 12, 20, 0.9);
  padding: 8px 16px;
  border-radius: 20px;
  border: 2px solid rgba(255, 225, 0, 0.4);
  letter-spacing: 1px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.5);
}

.senna-theme .senna-track {
  display: flex;
  align-items: center;
  justify-content: space-around;
  background: linear-gradient(90deg, rgba(255,225,0,0.15), rgba(0,155,58,0.15), rgba(0,51,153,0.15));
  border: 2px solid rgba(255, 225, 0, 0.3);
  border-radius: 14px;
  padding: 10px 20px;
  margin-bottom: 24px;
  font-size: 0.9rem;
  font-weight: 800;
  color: #ffe100;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
}

.senna-theme .senna-track span {
  animation: sennaPulse 2s infinite alternate;
}

@keyframes sennaPulse {
  0% { opacity: 0.75; transform: translateX(-2px); }
  100% { opacity: 1; transform: translateX(2px); }
}

/* Super Heavy Senna Telemetry Card Widget */
.senna-telemetry-card {
  background: linear-gradient(135deg, rgba(18, 25, 39, 0.98), rgba(8, 12, 20, 0.98));
  border: 2px solid #ffe100;
  border-radius: 18px;
  padding: 22px;
  margin-bottom: 28px;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6), inset 0 0 20px rgba(255, 225, 0, 0.08);
}

.senna-telemetry-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255, 225, 0, 0.25);
  padding-bottom: 14px;
  margin-bottom: 18px;
  flex-wrap: wrap;
  gap: 12px;
}

.senna-telemetry-title {
  display: flex;
  align-items: center;
  gap: 12px;
}

.senna-telemetry-title h3 {
  font-size: 1.15rem;
  color: #ffe100;
  margin: 0;
  text-transform: uppercase;
}

.senna-car-selector {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.senna-car-tab {
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 225, 0, 0.3);
  color: #94a3b8;
  padding: 6px 12px;
  border-radius: 8px;
  font-size: 0.78rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
}

.senna-car-tab:hover,
.senna-car-tab.active {
  background: #ffe100;
  color: #080c14;
  border-color: #ffe100;
  font-weight: 800;
  box-shadow: 0 0 12px rgba(255, 225, 0, 0.4);
}

.senna-telemetry-body {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 24px;
}

@media (max-width: 820px) {
  .senna-telemetry-body {
    grid-template-columns: 1fr;
  }
}

.senna-rpm-bar {
  background: rgba(0, 0, 0, 0.5);
  padding: 14px 18px;
  border-radius: 14px;
  border: 1px solid rgba(255, 225, 0, 0.2);
  margin-bottom: 16px;
}

.senna-rpm-label {
  font-size: 0.85rem;
  font-weight: 800;
  color: #cbd5e1;
  margin-bottom: 10px;
}

.senna-rpm-label span {
  color: #ffe100;
  font-family: 'VT323', monospace;
  font-size: 1.3rem;
}

.senna-shift-lights {
  display: flex;
  gap: 8px;
  justify-content: space-between;
}

.senna-shift-lights .light {
  flex: 1;
  height: 16px;
  border-radius: 4px;
  background: rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 0 4px rgba(0,0,0,0.5);
}

.senna-shift-lights .light.green.active {
  background: #009b3a;
  box-shadow: 0 0 12px #009b3a;
}

.senna-shift-lights .light.yellow.active {
  background: #ffe100;
  box-shadow: 0 0 12px #ffe100;
}

.senna-shift-lights .light.red.active {
  background: #e10600;
  box-shadow: 0 0 12px #e10600;
}

.senna-shift-lights .light.red.blink {
  animation: blink 0.4s infinite alternate;
}

.senna-readouts {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}

.senna-readout-box {
  background: rgba(0, 0, 0, 0.4);
  padding: 12px 8px;
  border-radius: 12px;
  border: 1px solid rgba(255, 225, 0, 0.2);
  text-align: center;
}

.senna-readout-box .lbl {
  display: block;
  font-size: 0.68rem;
  color: #94a3b8;
  font-weight: 800;
}

.senna-readout-box .val {
  display: block;
  font-family: 'VT323', monospace;
  font-size: 1.5rem;
  color: #ffe100;
  font-weight: 700;
}

.senna-readout-box .unit {
  display: block;
  font-size: 0.62rem;
  color: #64748b;
  font-weight: 700;
}

.senna-controls-section {
  display: flex;
  flex-direction: column;
  gap: 14px;
  justify-content: center;
}

.senna-soundboard-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.senna-btn {
  padding: 12px 16px;
  border-radius: 12px;
  font-family: 'Fredoka', sans-serif;
  font-weight: 700;
  font-size: 0.88rem;
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
  color: #080c14;
  box-shadow: 0 4px 15px rgba(255, 225, 0, 0.35);
}
.senna-btn--rev:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 22px rgba(255, 225, 0, 0.6);
}

.senna-btn--pit {
  background: linear-gradient(135deg, #009b3a 0%, #047857 100%);
  color: #ffffff;
  box-shadow: 0 4px 15px rgba(0, 155, 58, 0.35);
}
.senna-btn--pit:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 22px rgba(0, 155, 58, 0.6);
}

.senna-btn--radio {
  background: linear-gradient(135deg, #003399 0%, #1d4ed8 100%);
  color: #ffffff;
  box-shadow: 0 4px 15px rgba(0, 51, 153, 0.35);
}
.senna-btn--radio:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 22px rgba(0, 51, 153, 0.6);
}

.senna-btn--victory {
  background: linear-gradient(135deg, #e10600 0%, #b91c1c 100%);
  color: #ffffff;
  box-shadow: 0 4px 15px rgba(225, 6, 0, 0.35);
}
.senna-btn--victory:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 22px rgba(225, 6, 0, 0.6);
}

.senna-btn--lights {
  width: 100%;
  background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
  color: #ffe100;
  border: 1px solid rgba(255, 225, 0, 0.4);
  box-shadow: 0 4px 15px rgba(0,0,0,0.5);
}
.senna-btn--lights:hover {
  background: #ffe100;
  color: #080c14;
  font-weight: 800;
}

.senna-reaction-result {
  background: rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(255, 225, 0, 0.25);
  border-radius: 10px;
  padding: 10px 14px;
  font-size: 0.85rem;
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

/* Task Cards & Board styling for Super Heavy Senna Theme */
.senna-theme .task-column {
  background: rgba(18, 25, 39, 0.85) !important;
  border: 2px solid rgba(255, 225, 0, 0.3) !important;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4) !important;
}

.senna-theme .task-column__header {
  border-bottom: 3px solid #ffe100 !important;
  background: linear-gradient(90deg, rgba(255,225,0,0.15), transparent) !important;
}

.senna-theme .task-column__header h3 {
  color: #ffe100 !important;
}

.senna-theme .task-card {
  background: rgba(8, 12, 20, 0.95) !important;
  border: 1px solid rgba(255, 225, 0, 0.2) !important;
  transition: all 0.25s ease !important;
}

.senna-theme .task-card:hover {
  border-color: #ffe100 !important;
  box-shadow: 0 8px 28px rgba(255, 225, 0, 0.35) !important;
  transform: translateY(-4px) !important;
}

.senna-theme .dept-tab.active {
  background: #ffe100 !important;
  color: #080c14 !important;
  font-weight: 800 !important;
  box-shadow: 0 0 18px rgba(255, 225, 0, 0.5) !important;
}

.senna-theme .welcome-banner {
  background: linear-gradient(135deg, rgba(18, 25, 39, 0.98), rgba(8, 12, 20, 0.98)) !important;
  border: 2px solid #ffe100 !important;
  box-shadow: 0 10px 30px rgba(255, 225, 0, 0.3) !important;
}

.senna-theme .welcome-banner__icon {
  background: rgba(255, 225, 0, 0.15) !important;
  color: #ffe100 !important;
  border: 1px solid rgba(255, 225, 0, 0.3) !important;
}

.senna-theme .welcome-banner__greeting strong {
  color: #ffe100 !important;
}

.senna-theme input:focus,
.senna-theme textarea:focus,
.senna-theme select:focus {
  border-color: #ffe100 !important;
  box-shadow: 0 0 12px rgba(255, 225, 0, 0.4) !important;
}

.senna-helmet-pulse {
  animation: sennaPulse 2s infinite alternate;
}
"""

    css = re.sub(css_pattern, super_heavy_senna_css + "\n", css, flags=re.DOTALL)

    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

    print('Updated dashboard.css with Super Heavy Senna CSS!')

if __name__ == '__main__':
    main()
