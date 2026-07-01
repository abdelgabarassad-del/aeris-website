with open('dashboard.html', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Vostok-1 manual
target1 = """              <div style="font-size: 0.72rem; line-height: 1.4; font-family: monospace;">
                <strong style="color: #60a5fa;">💡 How it works:</strong><br>
                Monitor and command Vostok-1 orbital parameters. Steer thrust direction and vector modes to manage orbit stability.<br><br>
                <strong style="color: #39ff14;">✔️ What to do:</strong><br>
                - Click **`🛰️ EMIT PING`** to send a radar echo scan.<br>
                - Adjust the **`THRUST DIRECTION`** slider or toggle vector modes between **`PROGRADE`**, **`RETROGRADE`**, or **`MANUAL DEG`** to steer.<br>
                - Click **`ENGAGE ENGINE DIRECTIVE`** to fire engines and alter velocity.<br>
                - Toggle switches like **`SPUTNIK BEACON`** to hear audio beacon signals.<br><br>
                <strong style="color: #ff5555;">❌ Emergency / Escape:</strong><br>
                - If alt &lt; 120km, re-entry starts. Click the **`CLICK TO FLIP COVER`** guard, then hit the big red **`EMERGENCY VEHICLE EJECT`** button to save the astronaut!
              </div>"""

replacement1 = """              <div style="font-size: 0.72rem; line-height: 1.4; font-family: monospace;">
                <strong style="color: #60a5fa;">💡 How it works:</strong><br>
                Monitor and command Vostok-1 orbital parameters. Steer thrust direction and vector modes to manage orbit stability.<br><br>
                <strong style="color: #39ff14;">✔️ What to do:</strong><br>
                - Click **<code>🛰️ EMIT PING</code>** to send a radar echo scan.<br>
                - Adjust the **<code>THRUST DIRECTION</code>** slider or toggle vector modes between **<code>PROGRADE</code>**, **<code>RETROGRADE</code>**, or **<code>MANUAL DEG</code>** to steer.<br>
                - Click **<code>ENGAGE ENGINE DIRECTIVE</code>** to fire engines and alter velocity.<br>
                - Toggle switches like **<code>SPUTNIK BEACON</code>** to hear audio beacon signals.<br><br>
                <strong style="color: #ff5555;">❌ Emergency / Escape:</strong><br>
                - If alt &lt; 120km, re-entry starts. Click the **<code>CLICK TO FLIP COVER</code>** guard, then hit the big red **<code>EMERGENCY VEHICLE EJECT</code>** button to save the astronaut!
              </div>"""
code = code.replace(target1, replacement1)

# 2. Update MiG-29 manual
target2 = """              <div style="font-size: 0.72rem; line-height: 1.4; font-family: monospace;">
                <strong style="color: #60a5fa;">💡 How it works:</strong><br>
                Steer a MiG-29 fighter jet. Lock onto target and fire missiles.<br><br>
                <strong style="color: #39ff14;">✔️ Controls:</strong><br>
                - Pitch/Roll: Drag sliders or use **`W/S`** (Pitch) and **`A/D`** (Roll) keys.<br>
                - Throttle: Use the **`Throttle Slider`** to adjust engine RPM.<br>
                - Afterburner: Toggle afterburner switch for supersonic speed (consumes fuel faster).<br>
                - Weapons: Click **`⚠️ SAFE: GUARD CLOSED`** cover to arm weapons, and click the big red **`🚀 ПУСК`** button (or press **`Spacebar`**) to fire at the locking target!
              </div>"""

replacement2 = """              <div style="font-size: 0.72rem; line-height: 1.4; font-family: monospace;">
                <strong style="color: #60a5fa;">💡 How it works:</strong><br>
                Steer a MiG-29 fighter jet. Lock onto target and fire missiles.<br><br>
                <strong style="color: #39ff14;">✔️ Controls:</strong><br>
                - Pitch/Roll: Drag sliders or use **<code>W/S</code>** (Pitch) and **<code>A/D</code>** (Roll) keys.<br>
                - Throttle: Use the **<code>Throttle Slider</code>** to adjust engine RPM.<br>
                - Afterburner: Toggle afterburner switch for supersonic speed (consumes fuel faster).<br>
                - Weapons: Click **<code>⚠️ SAFE: GUARD CLOSED</code>** cover to arm weapons, and click the big red **<code>🚀 ПУСК</code>** button (or press **<code>Spacebar</code>**) to fire at the locking target!
              </div>"""
code = code.replace(target2, replacement2)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(code)

print("Manual backticks fixed successfully")
