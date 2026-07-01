with open('dashboard.html', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add gain node variables
target1 = "      let vostokMuted = false;\n      let mig29Muted = false;"
replacement1 = "      let vostokMuted = false;\n      let mig29Muted = false;\n      let humGainNode = null;\n      let staticGainNode = null;\n      let sirenGainNode = null;"
code = code.replace(target1, replacement1)

# 2. Update playSonarPing
target2 = """      function playSonarPing() {
        ensureAudioCtx();
        if (!window.sovietAudioCtx) return;"""
replacement2 = """      function playSonarPing() {
        ensureAudioCtx();
        if (!window.sovietAudioCtx || vostokMuted) return;"""
code = code.replace(target2, replacement2)

# 3. Update startSputnikBeep
target3 = "          if (!window.sovietAudioCtx || !sputnikActive) return;"
replacement3 = "          if (!window.sovietAudioCtx || !sputnikActive || vostokMuted) return;"
code = code.replace(target3, replacement3)

# 4. Update startHumStatic (humGain)
target4 = """        window.sovietHumOsc = window.sovietAudioCtx.createOscillator();
        const humGain = window.sovietAudioCtx.createGain();
        window.sovietHumOsc.type = 'triangle';
        window.sovietHumOsc.frequency.value = 60; // low frequency hum
        humGain.gain.value = 0.06;"""
replacement4 = """        window.sovietHumOsc = window.sovietAudioCtx.createOscillator();
        const humGain = window.sovietAudioCtx.createGain();
        humGainNode = humGain;
        window.sovietHumOsc.type = 'triangle';
        window.sovietHumOsc.frequency.value = 60; // low frequency hum
        humGain.gain.value = vostokMuted ? 0 : 0.06;"""
code = code.replace(target4, replacement4)

# 5. Update startHumStatic (staticGain)
target5 = """        const staticGain = window.sovietAudioCtx.createGain();
        staticGain.gain.value = 0.012;"""
replacement5 = """        const staticGain = window.sovietAudioCtx.createGain();
        staticGainNode = staticGain;
        staticGain.gain.value = vostokMuted ? 0 : 0.012;"""
code = code.replace(target5, replacement5)

# 6. Update triggerSiren
target6 = """          window.sovietSirenOsc = window.sovietAudioCtx.createOscillator();
          const sirenGain = window.sovietAudioCtx.createGain();
          window.sovietSirenOsc.type = 'sawtooth';
          window.sovietSirenOsc.frequency.value = 400;
          sirenGain.gain.value = 0.04;"""
replacement6 = """          window.sovietSirenOsc = window.sovietAudioCtx.createOscillator();
          const sirenGain = window.sovietAudioCtx.createGain();
          sirenGainNode = sirenGain;
          window.sovietSirenOsc.type = 'sawtooth';
          window.sovietSirenOsc.frequency.value = 400;
          sirenGain.gain.value = vostokMuted ? 0 : 0.04;"""
code = code.replace(target6, replacement6)

# 7. Add updateVostokSound function after triggerSiren definition
target7 = """        } else {
          sirenActive = false;
          if (sirenInterval) {
            clearInterval(sirenInterval);
            sirenInterval = null;
          }
          if (window.sovietSirenOsc) {
            try { window.sovietSirenOsc.stop(); } catch(e) {}
            window.sovietSirenOsc = null;
          }
        }
      }"""
replacement7 = """        } else {
          sirenActive = false;
          if (sirenInterval) {
            clearInterval(sirenInterval);
            sirenInterval = null;
          }
          if (window.sovietSirenOsc) {
            try { window.sovietSirenOsc.stop(); } catch(e) {}
            window.sovietSirenOsc = null;
          }
        }
      }

      function updateVostokSound() {
        if (humGainNode && window.sovietAudioCtx) {
          humGainNode.gain.setValueAtTime(vostokMuted ? 0 : 0.06, window.sovietAudioCtx.currentTime);
        }
        if (staticGainNode && window.sovietAudioCtx) {
          staticGainNode.gain.setValueAtTime(vostokMuted ? 0 : 0.012, window.sovietAudioCtx.currentTime);
        }
        if (sirenGainNode && window.sovietAudioCtx) {
          sirenGainNode.gain.setValueAtTime(vostokMuted ? 0 : 0.04, window.sovietAudioCtx.currentTime);
        }
      }"""
code = code.replace(target7, replacement7, 1) # Only first replacement!

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(code)

print("Vostok audio logic added successfully")
