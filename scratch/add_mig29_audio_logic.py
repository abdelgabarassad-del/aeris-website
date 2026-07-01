with open('dashboard.html', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update updateJetEngineSound
target1 = """      function updateJetEngineSound() {
        if (!jetAudioRunning || !sovietAudioCtx) return;
        let targetFreq = 70 + (jetThrottle / 100) * 160;
        let targetGain = 0.02 + (jetThrottle / 100) * 0.06;
        if (jetAfterburner) {
          targetFreq += 350;
          targetGain += 0.10;
        }
        if (jetFuel <= 0) {
          targetFreq = 0;
          targetGain = 0;
        }
        if (jetFilterNode) jetFilterNode.frequency.setValueAtTime(targetFreq, sovietAudioCtx.currentTime);
        if (jetGainNode) jetGainNode.gain.setValueAtTime(targetGain, sovietAudioCtx.currentTime);
      }"""

replacement1 = """      function updateJetEngineSound() {
        if (!jetAudioRunning || !sovietAudioCtx) return;
        let targetFreq = 70 + (jetThrottle / 100) * 160;
        let targetGain = mig29Muted ? 0 : (0.02 + (jetThrottle / 100) * 0.06);
        if (jetAfterburner) {
          targetFreq += 350;
          if (!mig29Muted) targetGain += 0.10;
        }
        if (jetFuel <= 0) {
          targetFreq = 0;
          targetGain = 0;
        }
        if (jetFilterNode) jetFilterNode.frequency.setValueAtTime(targetFreq, sovietAudioCtx.currentTime);
        if (jetGainNode) jetGainNode.gain.setValueAtTime(targetGain, sovietAudioCtx.currentTime);
      }"""
code = code.replace(target1, replacement1)

# 2. Update Missile Launch sound
target2 = """          // Synthesize missile launch sound
          try {
            const osc = sovietAudioCtx.createOscillator();
            const gain = sovietAudioCtx.createGain();
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(600, sovietAudioCtx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(60, sovietAudioCtx.currentTime + 0.8);
            
            gain.gain.setValueAtTime(0.25, sovietAudioCtx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.0001, sovietAudioCtx.currentTime + 0.8);
            
            osc.connect(gain);
            gain.connect(sovietAudioCtx.destination);
            osc.start();
            osc.stop(sovietAudioCtx.currentTime + 0.8);
          } catch(err) {}"""

replacement2 = """          // Synthesize missile launch sound
          try {
            if (!mig29Muted) {
              const osc = sovietAudioCtx.createOscillator();
              const gain = sovietAudioCtx.createGain();
              osc.type = 'sawtooth';
              osc.frequency.setValueAtTime(600, sovietAudioCtx.currentTime);
              osc.frequency.exponentialRampToValueAtTime(60, sovietAudioCtx.currentTime + 0.8);
              
              gain.gain.setValueAtTime(0.25, sovietAudioCtx.currentTime);
              gain.gain.exponentialRampToValueAtTime(0.0001, sovietAudioCtx.currentTime + 0.8);
              
              osc.connect(gain);
              gain.connect(sovietAudioCtx.destination);
              osc.start();
              osc.stop(sovietAudioCtx.currentTime + 0.8);
            }
          } catch(err) {}"""
code = code.replace(target2, replacement2)

# 3. Update warning alert beep tones
target3 = """        // 13. Play sound alerts
        if (isLocked) {
          lockSoundBeepTimer++;
          if (lockSoundBeepTimer % 5 === 0) {
            try {
              const osc = sovietAudioCtx.createOscillator();
              const gain = sovietAudioCtx.createGain();
              osc.type = 'sine';
              osc.frequency.setValueAtTime(1400, sovietAudioCtx.currentTime);
              gain.gain.setValueAtTime(0.08, sovietAudioCtx.currentTime);
              gain.gain.exponentialRampToValueAtTime(0.0001, sovietAudioCtx.currentTime + 0.12);
              osc.connect(gain);
              gain.connect(sovietAudioCtx.destination);
              osc.start();
              osc.stop(sovietAudioCtx.currentTime + 0.12);
            } catch(e) {}
          }
        }
        
        // Incoming missile alert beeping tone
        if (enemyMissileActive) {
          if (Math.round(enemyMissileProgress * 100) % 8 === 0) {
            try {
              const osc = sovietAudioCtx.createOscillator();
              const gain = sovietAudioCtx.createGain();
              osc.type = 'sawtooth';
              osc.frequency.setValueAtTime(800, sovietAudioCtx.currentTime);
              gain.gain.setValueAtTime(0.12, sovietAudioCtx.currentTime);
              gain.gain.exponentialRampToValueAtTime(0.0001, sovietAudioCtx.currentTime + 0.08);
              osc.connect(gain);
              gain.connect(sovietAudioCtx.destination);
              osc.start();
              osc.stop(sovietAudioCtx.currentTime + 0.08);
            } catch(e) {}
          }
        }"""

replacement3 = """        // 13. Play sound alerts
        if (isLocked && !mig29Muted) {
          lockSoundBeepTimer++;
          if (lockSoundBeepTimer % 5 === 0) {
            try {
              const osc = sovietAudioCtx.createOscillator();
              const gain = sovietAudioCtx.createGain();
              osc.type = 'sine';
              osc.frequency.setValueAtTime(1400, sovietAudioCtx.currentTime);
              gain.gain.setValueAtTime(0.08, sovietAudioCtx.currentTime);
              gain.gain.exponentialRampToValueAtTime(0.0001, sovietAudioCtx.currentTime + 0.12);
              osc.connect(gain);
              gain.connect(sovietAudioCtx.destination);
              osc.start();
              osc.stop(sovietAudioCtx.currentTime + 0.12);
            } catch(e) {}
          }
        }
        
        // Incoming missile alert beeping tone
        if (enemyMissileActive && !mig29Muted) {
          if (Math.round(enemyMissileProgress * 100) % 8 === 0) {
            try {
              const osc = sovietAudioCtx.createOscillator();
              const gain = sovietAudioCtx.createGain();
              osc.type = 'sawtooth';
              osc.frequency.setValueAtTime(800, sovietAudioCtx.currentTime);
              gain.gain.setValueAtTime(0.12, sovietAudioCtx.currentTime);
              gain.gain.exponentialRampToValueAtTime(0.0001, sovietAudioCtx.currentTime + 0.08);
              osc.connect(gain);
              gain.connect(sovietAudioCtx.destination);
              osc.start();
              osc.stop(sovietAudioCtx.currentTime + 0.08);
            } catch(e) {}
          }
        }"""
code = code.replace(target3, replacement3)

# 4. Update evasive maneuver sound
target4 = """            // Swoosh sound
            try {
              const osc = sovietAudioCtx.createOscillator();
              const gain = sovietAudioCtx.createGain();
              osc.type = 'triangle';
              osc.frequency.setValueAtTime(800, sovietAudioCtx.currentTime);
              osc.frequency.exponentialRampToValueAtTime(150, sovietAudioCtx.currentTime + 0.4);
              gain.gain.setValueAtTime(0.2, sovietAudioCtx.currentTime);
              gain.gain.exponentialRampToValueAtTime(0.0001, sovietAudioCtx.currentTime + 0.4);
              osc.connect(gain);
              gain.connect(sovietAudioCtx.destination);
              osc.start();
              osc.stop(sovietAudioCtx.currentTime + 0.42);
            } catch(e) {}"""

replacement4 = """            // Swoosh sound
            try {
              if (!mig29Muted) {
                const osc = sovietAudioCtx.createOscillator();
                const gain = sovietAudioCtx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(800, sovietAudioCtx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(150, sovietAudioCtx.currentTime + 0.4);
                gain.gain.setValueAtTime(0.2, sovietAudioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.0001, sovietAudioCtx.currentTime + 0.4);
                osc.connect(gain);
                gain.connect(sovietAudioCtx.destination);
                osc.start();
                osc.stop(sovietAudioCtx.currentTime + 0.42);
              }
            } catch(e) {}"""
code = code.replace(target4, replacement4)

# 5. Update impact detonation sound
target5 = """            // Impact detonation sound
            try {
              const osc = sovietAudioCtx.createOscillator();
              const gain = sovietAudioCtx.createGain();
              osc.type = 'sawtooth';
              osc.frequency.setValueAtTime(90, sovietAudioCtx.currentTime);
              osc.frequency.exponentialRampToValueAtTime(15, sovietAudioCtx.currentTime + 0.8);
              gain.gain.setValueAtTime(0.4, sovietAudioCtx.currentTime);
              gain.gain.exponentialRampToValueAtTime(0.0001, sovietAudioCtx.currentTime + 0.8);
              osc.connect(gain);
              gain.connect(sovietAudioCtx.destination);
              osc.start();
              osc.stop(sovietAudioCtx.currentTime + 0.85);
            } catch(e) {}"""

replacement5 = """            // Impact detonation sound
            try {
              if (!mig29Muted) {
                const osc = sovietAudioCtx.createOscillator();
                const gain = sovietAudioCtx.createGain();
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(90, sovietAudioCtx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(15, sovietAudioCtx.currentTime + 0.8);
                gain.gain.setValueAtTime(0.4, sovietAudioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.0001, sovietAudioCtx.currentTime + 0.8);
                osc.connect(gain);
                gain.connect(sovietAudioCtx.destination);
                osc.start();
                osc.stop(sovietAudioCtx.currentTime + 0.85);
              }
            } catch(e) {}"""
code = code.replace(target5, replacement5)

# 6. Update crash explosion noise burst
target6 = """            // Play synthetic crash explosion noise burst
            try {
              const osc = sovietAudioCtx.createOscillator();
              const gain = sovietAudioCtx.createGain();
              osc.type = 'sawtooth';
              osc.frequency.setValueAtTime(120, sovietAudioCtx.currentTime);
              osc.frequency.exponentialRampToValueAtTime(10, sovietAudioCtx.currentTime + 0.6);
              gain.gain.setValueAtTime(0.3, sovietAudioCtx.currentTime);
              gain.gain.exponentialRampToValueAtTime(0.0001, sovietAudioCtx.currentTime + 0.6);
              osc.connect(gain);
              gain.connect(sovietAudioCtx.destination);
              osc.start();
              osc.stop(sovietAudioCtx.currentTime + 0.6);
            } catch(e) {}"""

replacement6 = """            // Play synthetic crash explosion noise burst
            try {
              if (!mig29Muted) {
                const osc = sovietAudioCtx.createOscillator();
                const gain = sovietAudioCtx.createGain();
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(120, sovietAudioCtx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(10, sovietAudioCtx.currentTime + 0.6);
                gain.gain.setValueAtTime(0.3, sovietAudioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.0001, sovietAudioCtx.currentTime + 0.6);
                osc.connect(gain);
                gain.connect(sovietAudioCtx.destination);
                osc.start();
                osc.stop(sovietAudioCtx.currentTime + 0.6);
              }
            } catch(e) {}"""
code = code.replace(target6, replacement6)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(code)

print("MiG-29 audio logic added successfully")
