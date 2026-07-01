with open('dashboard.html', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update dragon-game-manual-modal style & content
target1 = """            <div id="dragon-game-manual-modal" style="display: none; position: absolute; top: 70px; left: 16px; right: 16px; background: rgba(10, 20, 15, 0.99); z-index: 10005; border-radius: 8px; padding: 20px; font-family: monospace; max-height: 520px; overflow-y: auto; color: #e2e8f0; border: 2px solid #2d5a3f; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #2d5a3f; padding-bottom: 8px; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 1.15rem; color: #81c784; font-family: 'MedievalSharp', cursive;">📋 Guide de Vol - Chasse aux Moutons</h3>
                <button class="dragon-weapon-btn btn-sm" id="btn-dragon-game-manual-close" style="width: auto; padding: 4px 10px; font-size: 0.75rem; cursor: pointer;">Fermer [X]</button>
              </div>
              <div style="font-size: 0.88rem; line-height: 1.4; font-family: monospace;">
                <strong style="color: #60a5fa;">💡 How it works:</strong><br>
                Steer Krokmou (Toothless) to grab sheep while dodging hunter arrows.<br><br>
                <strong style="color: #39ff14;">✔️ What to do:</strong><br>
                - Move your cursor over the canvas: Krokmou follows your mouse position.<br>
                - Capture 🐑 **White Sheep** for standard points, and **Black/Gold Sheep** for bonus scores.<br>
                - **Left Click** to fire plasma blasts at incoming arrows to destroy them and protect yourself.<br><br>
                <strong style="color: #ff5555;">❌ What NOT to do:</strong><br>
                - Do not crash into the glowing red arrows fired by dragon hunters. They drain your energy (Health).<br>
                - Do not let your energy bar drop to 0%, or you will crash and trigger Game Over.<br><br>
                <strong style="color: #ffaa44;">🔍 What to look for:</strong><br>
                - Collect gold rings and shield bubbles for temporary power-ups and score multipliers.
              </div>
            </div>"""

replacement1 = """            <div id="dragon-game-manual-modal" style="display: none; position: absolute; top: 50px; left: 10px; right: 10px; background: rgba(10, 20, 15, 0.99); z-index: 10005; border-radius: 8px; padding: 20px; font-family: monospace; max-height: 600px; overflow-y: auto; color: #e2e8f0; border: 2px solid #2d5a3f; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #2d5a3f; padding-bottom: 8px; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 1.15rem; color: #81c784; font-family: 'MedievalSharp', cursive;">📋 Guide de Vol - Chasse aux Moutons</h3>
                <button class="dragon-weapon-btn btn-sm" id="btn-dragon-game-manual-close" style="width: auto; padding: 4px 10px; font-size: 0.75rem; cursor: pointer;">Fermer [X]</button>
              </div>
              <div style="font-size: 0.95rem; line-height: 1.6; font-family: system-ui, -apple-system, sans-serif;">
                <strong style="color: #60a5fa;">💡 MECHANICAL PRINCIPLE:</strong><br>
                Steer Krokmou (Toothless) to grab sheep while dodging hunter arrows. The flight algorithm tracks your mouse coordinates with a custom linear interpolation delay, creating a realistic physical sense of aerodynamic drag and inertia.<br><br>
                <strong style="color: #39ff14;">✔️ OPERATIONAL PROCEDURES:</strong><br>
                - <strong>Gliding</strong>: Move your cursor across the cockpit radar screen. Toothless will smoothly accelerate and glide toward the target coordinates.<br>
                - <strong>Tactical Capture</strong>: Intercept escaping livestock. Capture 🐑 <strong>White Sheep</strong> for standard points (+10 pts), and seek out rare <strong>Black & Golden Sheep</strong> (+25 / +50 pts) which yield high-value bonuses and dynamic score multipliers.<br>
                - <strong>Plasma Cannons</strong>: <strong>Left-click</strong> on the radar screen to discharge a high-energy blue plasma blast. These blasts detonate nearby threat vectors in a localized area-of-effect blast radius.<br><br>
                <strong style="color: #ff5555;">❌ SYSTEM THREATS:</strong><br>
                - <strong>Hunter Barrage</strong>: Avoid red archery fire from dragon-hunting ships. Each impact damages Toothless, draining your health envelope by 15%.<br>
                - <strong>Energy Exhaustion</strong>: If health degrades to 0%, a critical structural failure is simulated, culminating in an emergency crash landing (Game Over).<br><br>
                <strong style="color: #ffaa44;">🔍 FLIGHT STRATEGY & UPGRADES:</strong><br>
                - Scan the radar scope for gold rings and defensive shield bubbles. Activating a shield grants temporary immunity to arrow projectiles, allowing you to harvest sheep in heavy danger zones.
              </div>
            </div>"""
code = code.replace(target1, replacement1)

# 2. Update dragon-duel-manual-modal style & content
target2 = """          <div id="dragon-duel-manual-modal" style="display: none; position: absolute; top: 70px; left: 16px; right: 16px; background: rgba(10, 20, 15, 0.99); z-index: 10005; border-radius: 8px; padding: 20px; font-family: monospace; max-height: 520px; overflow-y: auto; color: #e2e8f0; border: 2px solid #2d5a3f; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #2d5a3f; padding-bottom: 8px; margin-bottom: 12px;">
              <h3 style="margin: 0; font-size: 1.15rem; color: #81c784; font-family: 'MedievalSharp', cursive;">📋 Manuel d'Arène - Simulateur de Combat</h3>
              <button class="dragon-weapon-btn btn-sm" id="btn-dragon-duel-manual-close" style="width: auto; padding: 4px 10px; font-size: 0.75rem; cursor: pointer;">Fermer [X]</button>
            </div>
            <div style="font-size: 0.88rem; line-height: 1.4; font-family: monospace;">
              <strong style="color: #60a5fa;">💡 How it works:</strong><br>
              Dodge and attack the wild dragon in turn-based combat inside the Berk Academy ring.<br><br>
              <strong style="color: #39ff14;">✔️ What to do:</strong><br>
              - Use **Tir Plasma** to deal maximum damage when your plasma reserve is high.<br>
              - Use **Attaque Feu** as a reliable medium damage, low cost attack.<br>
              - Use **Esquive Vent** to regain plasma (+15) and gain a 45% chance to dodge the next wild dragon strike.<br>
              - Consume saumon (**Poisson Soin**) to heal +35 HP if your health gets low.<br><br>
              <strong style="color: #ff5555;">❌ What NOT to do:</strong><br>
              - Do not exhaust all your plasma, or you won't be able to heal or perform high-damage strikes.<br>
              - Do not ignore your health level—if Krokmou falls to 0 HP, you lose.<br><br>
              <strong style="color: #ffaa44;">🔍 What to look for:</strong><br>
              - Monitor both the Wild Dragon's health bar and Krokmou's health/plasma bars.
            </div>
          </div>"""

replacement2 = """          <div id="dragon-duel-manual-modal" style="display: none; position: absolute; top: 50px; left: 10px; right: 10px; background: rgba(10, 20, 15, 0.99); z-index: 10005; border-radius: 8px; padding: 20px; font-family: monospace; max-height: 600px; overflow-y: auto; color: #e2e8f0; border: 2px solid #2d5a3f; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #2d5a3f; padding-bottom: 8px; margin-bottom: 12px;">
              <h3 style="margin: 0; font-size: 1.15rem; color: #81c784; font-family: 'MedievalSharp', cursive;">📋 Manuel d'Arène - Simulateur de Combat</h3>
              <button class="dragon-weapon-btn btn-sm" id="btn-dragon-duel-manual-close" style="width: auto; padding: 4px 10px; font-size: 0.75rem; cursor: pointer;">Fermer [X]</button>
            </div>
            <div style="font-size: 0.95rem; line-height: 1.6; font-family: system-ui, -apple-system, sans-serif;">
              <strong style="color: #60a5fa;">💡 TURN-BASED ARENA DYNAMICS:</strong><br>
              Engage in turn-based dragon tactics within the Berk Academy ring. Strategy revolves around resource management: optimizing your health points and plasma reserves.<br><br>
              <strong style="color: #39ff14;">✔️ COMBAT ACTION DIRECTIVES:</strong><br>
              - <strong>Tir Plasma (Plasma Strike)</strong>: Consumes <code>25 Plasma</code>. Deals <code>25-35 HP</code> damage. A high-output combat blast to neutralize targets quickly. Cannot be cast if reserves fall below cost.<br>
              - <strong>Attaque Feu (Firestrike)</strong>: Consumes <code>10 Plasma</code>. Deals <code>12-18 HP</code> damage. A cost-effective attack to chip away at enemy defenses.<br>
              - <strong>Esquive Vent (Wind Evade)</strong>: Cost: <code>0 Plasma</code>. Restores <code>+15 Plasma</code>. Grants a defensive buff with a <code>45% probability</code> to completely dodge the enemy's next incoming strike.<br>
              - <strong>Poisson Soin (Healing Salmon)</strong>: Cost: <code>0 Plasma</code>. Limit: <code>3 uses per match</code>. Instantly restores <code>+35 Health Points</code> to Krokmou.<br><br>
              <strong style="color: #ff5555;">❌ COMBAT THREATS:</strong><br>
              - Running out of plasma leaves you vulnerable and unable to fire heavy strikes.<br>
              - If Krokmou's health gauge drops to 0 HP, combat operations fail.<br><br>
              <strong style="color: #ffaa44;">🔍 TACTICAL RECOMMENDATIONS:</strong><br>
              - Begin the duel with Wind Evade to safely build up your plasma reserves.<br>
              - Time your healing Poisson Soin carefully; do not wait until your health is dangerously low, as the enemy might queue a critical strike.
            </div>
          </div>"""
code = code.replace(target2, replacement2)

# 3. Update vostok-manual-modal style & content
target3 = """            <!-- Manual Modal Overlay for Vostok-1 -->
            <div id="vostok-manual-modal" style="display: none; position: absolute; top: 42px; left: 10px; right: 10px; background: rgba(10, 15, 20, 0.99); z-index: 10005; border-radius: 8px; padding: 20px; font-family: monospace; max-height: 520px; overflow-y: auto; color: #e2e8f0; border: 2px solid #546e7a; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #546e7a; padding-bottom: 8px; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 1.15rem; color: #81c784; text-transform: uppercase;">📋 Manual - Vostok-1 Command Center</h3>
                <button class="stitch-btn-music" id="btn-vostok-manual-close" style="width: auto; padding: 4px 10px; font-size: 0.75rem; cursor: pointer;">Fermer [X]</button>
              </div>
              <div style="font-size: 0.88rem; line-height: 1.4; font-family: monospace;">
                <strong style="color: #60a5fa;">💡 How it works:</strong><br>
                Monitor and command Vostok-1 orbital parameters. Steer thrust direction and vector modes to manage orbit stability.<br><br>
                <strong style="color: #39ff14;">✔️ What to do:</strong><br>
                - Click **<code>🛰️ EMIT PING</code>** to send a radar echo scan.<br>
                - Adjust the **<code>THRUST DIRECTION</code>** slider or toggle vector modes between **<code>PROGRADE</code>**, **<code>RETROGRADE</code>**, or **<code>MANUAL DEG</code>** to steer.<br>
                - Click **<code>ENGAGE ENGINE DIRECTIVE</code>** to fire engines and alter velocity.<br>
                - Toggle switches like **<code>SPUTNIK BEACON</code>** to hear audio beacon signals.<br><br>
                <strong style="color: #ff5555;">❌ Emergency / Escape:</strong><br>
                - If alt &lt; 120km, re-entry starts. Click the **<code>CLICK TO FLIP COVER</code>** guard, then hit the big red **<code>EMERGENCY VEHICLE EJECT</code>** button to save the astronaut!
              </div>
            </div>"""

replacement3 = """            <!-- Manual Modal Overlay for Vostok-1 -->
            <div id="vostok-manual-modal" style="display: none; position: absolute; top: 38px; left: 6px; right: 6px; background: rgba(10, 15, 20, 0.99); z-index: 10005; border-radius: 8px; padding: 20px; font-family: monospace; max-height: 600px; overflow-y: auto; color: #e2e8f0; border: 2px solid #546e7a; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #546e7a; padding-bottom: 8px; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 1.15rem; color: #81c784; text-transform: uppercase;">📋 Manual - Vostok-1 Command Center</h3>
                <button class="stitch-btn-music" id="btn-vostok-manual-close" style="width: auto; padding: 4px 10px; font-size: 0.75rem; cursor: pointer;">Fermer [X]</button>
              </div>
              <div style="font-size: 0.95rem; line-height: 1.6; font-family: system-ui, -apple-system, sans-serif;">
                <strong style="color: #60a5fa;">💡 ORBITAL DYNAMICS & KEPLERIAN PHYSICS:</strong><br>
                Monitor and steer the Vostok-1 spacecraft in Earth orbit. The spacecraft operates under a real-time gravitational physics simulation. Gravitational pull is calculated relative to the Earth's center, requiring balance between velocity and orbital radius to maintain a stable trajectory.<br><br>
                <strong style="color: #39ff14;">✔️ COMMAND PROCEDURES:</strong><br>
                - <strong>Radar Diagnostics</strong>: Click <strong><code>🛰️ EMIT PING</code></strong> to trigger a radar ping, updating spacecraft coordinates on the telemetry scope.<br>
                - <strong>Vector Steering</strong>: Adjust the <strong><code>THRUST DIRECTION</code></strong> slider or toggle vector modes:<br>
                  &nbsp;&nbsp;&bull; <strong>PROGRADE</strong>: Aligns engine thrust along the flight path. Firing accelerates velocity and raises the orbit's apogee (highest point) on the opposite side of Earth.<br>
                  &nbsp;&nbsp;&bull; <strong>RETROGRADE</strong>: Aligns thrust against the flight path. Firing decelerates velocity, lowering the perigee (lowest point) to prepare for atmospheric re-entry.<br>
                  &nbsp;&nbsp;&bull; <strong>MANUAL DEG</strong>: Locks the thrust vector to a custom steering angle (0° - 360°) for manual orbital maneuvers.<br>
                - <strong>Engine Engagement</strong>: Press <strong><code>ENGAGE ENGINE DIRECTIVE</code></strong> to fire liquid-propellant thrusters. Firing consumes fuel and changes velocity.<br><br>
                <strong style="color: #ff5555;">❌ RE-ENTRY & ATMOSPHERIC DANGERS:</strong><br>
                - Safe orbital flight is maintained above 120km altitude.<br>
                - If altitude falls below 120km, the spacecraft enters dense atmospheric layers. Air friction will cause rapid drag deceleration, orbital decay, and extreme thermodynamic heating.<br>
                - <strong>Emergency Escape Protocol</strong>: In case of catastrophic orbital decay, flip open the safety cover and click the red <strong><code>EMERGENCY VEHICLE EJECT</code></strong> button. This jettisons the return capsule and deploys emergency parachutes to save the cosmonaut!
              </div>
            </div>"""
code = code.replace(target3, replacement3)

# 4. Update jet-manual-modal style & content
target4 = """            <!-- Manual Modal Overlay for MiG-29 -->
            <div id="jet-manual-modal" style="display: none; position: absolute; top: 42px; left: 10px; right: 10px; background: rgba(10, 15, 20, 0.99); z-index: 10005; border-radius: 8px; padding: 20px; font-family: monospace; max-height: 520px; overflow-y: auto; color: #e2e8f0; border: 2px solid #546e7a; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #546e7a; padding-bottom: 8px; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 1.15rem; color: #81c784; text-transform: uppercase;">📋 Manual - MiG-29 Cockpit Simulator</h3>
                <button class="stitch-btn-music" id="btn-jet-manual-close" style="width: auto; padding: 4px 10px; font-size: 0.75rem; cursor: pointer;">Fermer [X]</button>
              </div>
              <div style="font-size: 0.88rem; line-height: 1.4; font-family: monospace;">
                <strong style="color: #60a5fa;">💡 How it works:</strong><br>
                Steer a MiG-29 fighter jet. Lock onto target and fire missiles.<br><br>
                <strong style="color: #39ff14;">✔️ Controls:</strong><br>
                - Pitch/Roll: Drag sliders or use **<code>W/S</code>** (Pitch) and **<code>A/D</code>** (Roll) keys.<br>
                - Throttle: Use the **<code>Throttle Slider</code>** to adjust engine RPM.<br>
                - Afterburner: Toggle afterburner switch for supersonic speed (consumes fuel faster).<br>
                - Weapons: Click **<code>⚠️ SAFE: GUARD CLOSED</code>** cover to arm weapons, and click the big red **<code>🚀 ПУСК</code>** button (or press **<code>Spacebar</code>**) to fire at the locking target!
              </div>
            </div>"""

replacement4 = """            <!-- Manual Modal Overlay for MiG-29 -->
            <div id="jet-manual-modal" style="display: none; position: absolute; top: 38px; left: 6px; right: 6px; background: rgba(10, 15, 20, 0.99); z-index: 10005; border-radius: 8px; padding: 20px; font-family: monospace; max-height: 600px; overflow-y: auto; color: #e2e8f0; border: 2px solid #546e7a; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #546e7a; padding-bottom: 8px; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 1.15rem; color: #81c784; text-transform: uppercase;">📋 Manual - MiG-29 Cockpit Simulator</h3>
                <button class="stitch-btn-music" id="btn-jet-manual-close" style="width: auto; padding: 4px 10px; font-size: 0.75rem; cursor: pointer;">Fermer [X]</button>
              </div>
              <div style="font-size: 0.95rem; line-height: 1.6; font-family: system-ui, -apple-system, sans-serif;">
                <strong style="color: #60a5fa;">💡 AERODYNAMICS & COCKPIT SYSTEMS:</strong><br>
                Piloting a Mikoyan MiG-29 Fulcrum jet fighter. The simulator calculates aerodynamic lift based on airspeed, pitch angle, and local air density. G-force is dynamically updated based on roll angles and climbing rates.<br><br>
                <strong style="color: #39ff14;">✔️ FLIGHT INSTRUMENTS & CONTROLS:</strong><br>
                - <strong>Attitude Indicator (ADI)</strong>: Steer using the **<code>W/S</code>** keys (Pitch) and **<code>A/D</code>** keys (Roll), or drag the sliders.<br>
                  &nbsp;&nbsp;&bull; Positive pitch angles climb (gaining altitude but losing speed).<br>
                  &nbsp;&nbsp;&bull; Negative pitch angles dive (losing altitude but gaining speed).<br>
                  &nbsp;&nbsp;&bull; Rolling rolls the aircraft. Heavy banking turns generate high-G loads.<br>
                - <strong>Engine Thrust</strong>: Adjust the throttle slider. Engaged Afterburners provide massive thrust for supersonic flight (Mach > 1) but consume fuel at a rapid rate.<br>
                - <strong>Weapons Engagement</strong>:<br>
                  &nbsp;&nbsp;&bull; Open the physical safety cover by clicking on the **<code>⚠️ SAFE: GUARD CLOSED</code>** panel.<br>
                  &nbsp;&nbsp;&bull; Track target movements. When the target enters the locking zone and a high-pitched target lock tone sounds, the status changes to <strong>LOCK ACTIVE</strong>.<br>
                  &nbsp;&nbsp;&bull; Click the red <strong><code>🚀 ПУСК</code></strong> button or press the **<code>Spacebar</code>** to fire an AA-10 Alamo air-to-air missile.<br><br>
                <strong style="color: #ff5555;">❌ DEFENSIVE ACTIONS:</strong><br>
                - RWR (Radar Warning Receiver) alerts indicate an incoming enemy missile lock.<br>
                - Evade by performing G-force defensive breaks (sharp banking roll angles >30° or steep pitch angles >16°). Successful evasion triggers a tactical escape log.<br>
                - If hit, structural integrity is compromised, inducing fuel leaks and visual cracks on the cockpit canopy.
              </div>
            </div>"""
code = code.replace(target4, replacement4)

# 5. Update foxbat-manual-modal style & content
target5 = """            <!-- Manual Modal Overlay -->
            <div id="foxbat-manual-modal" style="display: none; position: absolute; top: 42px; left: 10px; right: 10px; background: rgba(10, 15, 20, 0.99); z-index: 10005; border-radius: 8px; padding: 20px; font-family: monospace; max-height: 520px; overflow-y: auto; color: #e2e8f0; border: 2px solid #546e7a; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #546e7a; padding-bottom: 8px; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 1.15rem; color: #81c784; text-transform: uppercase;">📋 Manual - MiG-25 Telemetry Console</h3>
                <button class="stitch-btn-music" id="btn-foxbat-manual-close" style="width: auto; padding: 4px 10px; font-size: 0.75rem; cursor: pointer;">Fermer [X]</button>
              </div>
              <div style="font-size: 0.88rem;"""

replacement5 = """            <!-- Manual Modal Overlay -->
            <div id="foxbat-manual-modal" style="display: none; position: absolute; top: 38px; left: 6px; right: 6px; background: rgba(10, 15, 20, 0.99); z-index: 10005; border-radius: 8px; padding: 20px; font-family: monospace; max-height: 600px; overflow-y: auto; color: #e2e8f0; border: 2px solid #546e7a; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #546e7a; padding-bottom: 8px; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 1.15rem; color: #81c784; text-transform: uppercase;">📋 Manual - MiG-25 Telemetry Console</h3>
                <button class="stitch-btn-music" id="btn-foxbat-manual-close" style="width: auto; padding: 4px 10px; font-size: 0.75rem; cursor: pointer;">Fermer [X]</button>
              </div>
              <div style="font-size: 0.95rem; line-height: 1.6; font-family: system-ui, -apple-system, sans-serif;"""
code = code.replace(target5, replacement5)

# Wait! We need to make sure the text of the MiG-25 manual is also detailed. Let's do that!
# Let's replace the inner HTML block of MiG-25 manual.
target_mig25_inner = """              <div style="font-size: 0.95rem; line-height: 1.6; font-family: system-ui, -apple-system, sans-serif;">
                <strong style="color: #60a5fa;">💡 How it works:</strong><br>
                Simulate twin R-15 jet engines. Maximize speed up to Mach 3.2 without burning the engines.<br><br>
                <strong style="color: #39ff14;">✔️ What to do:</strong><br>
                - Click the engine status buttons (initially **<code>OFFLINE</code>**) to start engines. Wait for idle (30% RPM).<br>
                - Push throttles past 85% and switch Afterburner to <code>ZONE 3</code> to speed up.<br>
                - Switch coolant flow to 50% or 100% to cool engines down during high EGT.<br>
                - Refill water-methanol when low.<br><br>
                <strong style="color: #ff5555;">❌ What NOT to do:</strong><br>
                - Do not run afterburners without cooling; EGT > 850°C melts core components (accumulates engine damage).<br>
                - Water-methanol qty drops quickly when flow is active; do not let it drop to 0% while afterburners are lit!
              </div>"""

replacement_mig25_inner = """              <div style="font-size: 0.95rem; line-height: 1.6; font-family: system-ui, -apple-system, sans-serif;">
                <strong style="color: #60a5fa;">💡 TURBOJET PROPULSION & THERMODYNAMICS:</strong><br>
                Simulate operating twin Tumansky R-15 turbojet engines on a MiG-25 Foxbat console. Designed for high-altitude Mach 3.2 intercept regimes, these engines generate extreme exhaust gas temperatures (EGT) that must be carefully managed to avoid compressor stalls and thermal structural failure.<br><br>
                <strong style="color: #39ff14;">✔️ ENGINE PRE-START & OPERATION:</strong><br>
                - <strong>Ignition Sequence</strong>: Set engine throttle dials to 0%. Click the left and right starter buttons to activate the ignition sequence. Wait for engine turbine RPM to stabilize at 30% idle speed.<br>
                - <strong>Exhaust Gas Temperature (EGT)</strong>: EGT stabilizes at 350°C at idle. Pushing the throttles forward increases RPM and EGT.<br>
                - <strong>Afterburner Zone 3</strong>: Push throttles past 85% and switch Afterburner to <code>ZONE 3</code> to engage reheat. This provides thrust for high Mach speeds but triggers high fuel consumption and rapid heat accumulation.<br>
                - <strong>Active Engine Cooling</strong>: When running at high power settings, switch the Water-Methanol injection flow rate to <code>50%</code> or <code>100%</code>. Cooling flow absorbs thermal energy, lowering engine EGT.<br>
                - <strong>Refilling Coolant</strong>: Monitor your Water-Methanol reserve. If empty, click **<code>🔧 REFILL W-M COOLANT</code>** to service the coolant reservoir.<br><br>
                <strong style="color: #ff5555;">❌ FLAMEOUTS & COMPRESSOR STALLS:</strong><br>
                - Operating afterburners without water-methanol cooling causes EGT to exceed the safety limit of 850°C.<br>
                - Sustained high temperature causes thermal structural damage, leading to compressor stalls, engine fires, or turbine flameouts (system offline).
              </div>"""

code = code.replace(target_mig25_inner, replacement_mig25_inner)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(code)

print("All manuals detailed, styled and enlarged successfully")
