import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update dragon-game-manual-modal
target1 = """            <div id="dragon-game-manual-modal" style="display: none; position: absolute; top: 70px; left: 16px; right: 16px; background: rgba(10, 20, 15, 0.99); z-index: 10005; border-radius: 8px; padding: 16px; font-family: monospace; max-height: 380px; overflow-y: auto; color: #e2e8f0; border: 2px solid #2d5a3f; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #2d5a3f; padding-bottom: 8px; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 0.95rem; color: #81c784; font-family: 'MedievalSharp', cursive;">📋 Guide de Vol - Chasse aux Moutons</h3>
                <button class="dragon-weapon-btn btn-sm" id="btn-dragon-game-manual-close" style="width: auto; padding: 2px 8px; font-size: 0.65rem; cursor: pointer;">Fermer [X]</button>
              </div>
              <div style="font-size: 0.72rem;"""

replacement1 = """            <div id="dragon-game-manual-modal" style="display: none; position: absolute; top: 70px; left: 16px; right: 16px; background: rgba(10, 20, 15, 0.99); z-index: 10005; border-radius: 8px; padding: 20px; font-family: monospace; max-height: 520px; overflow-y: auto; color: #e2e8f0; border: 2px solid #2d5a3f; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #2d5a3f; padding-bottom: 8px; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 1.15rem; color: #81c784; font-family: 'MedievalSharp', cursive;">📋 Guide de Vol - Chasse aux Moutons</h3>
                <button class="dragon-weapon-btn btn-sm" id="btn-dragon-game-manual-close" style="width: auto; padding: 4px 10px; font-size: 0.75rem; cursor: pointer;">Fermer [X]</button>
              </div>
              <div style="font-size: 0.88rem;"""
code = code.replace(target1, replacement1)

# 2. Update dragon-duel-manual-modal
target2 = """          <div id="dragon-duel-manual-modal" style="display: none; position: absolute; top: 70px; left: 16px; right: 16px; background: rgba(10, 20, 15, 0.99); z-index: 10005; border-radius: 8px; padding: 16px; font-family: monospace; max-height: 380px; overflow-y: auto; color: #e2e8f0; border: 2px solid #2d5a3f; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #2d5a3f; padding-bottom: 8px; margin-bottom: 12px;">
              <h3 style="margin: 0; font-size: 0.95rem; color: #81c784; font-family: 'MedievalSharp', cursive;">📋 Manuel d'Arène - Simulateur de Combat</h3>
              <button class="dragon-weapon-btn btn-sm" id="btn-dragon-duel-manual-close" style="width: auto; padding: 2px 8px; font-size: 0.65rem; cursor: pointer;">Fermer [X]</button>
            </div>
            <div style="font-size: 0.72rem;"""

replacement2 = """          <div id="dragon-duel-manual-modal" style="display: none; position: absolute; top: 70px; left: 16px; right: 16px; background: rgba(10, 20, 15, 0.99); z-index: 10005; border-radius: 8px; padding: 20px; font-family: monospace; max-height: 520px; overflow-y: auto; color: #e2e8f0; border: 2px solid #2d5a3f; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #2d5a3f; padding-bottom: 8px; margin-bottom: 12px;">
              <h3 style="margin: 0; font-size: 1.15rem; color: #81c784; font-family: 'MedievalSharp', cursive;">📋 Manuel d'Arène - Simulateur de Combat</h3>
              <button class="dragon-weapon-btn btn-sm" id="btn-dragon-duel-manual-close" style="width: auto; padding: 4px 10px; font-size: 0.75rem; cursor: pointer;">Fermer [X]</button>
            </div>
            <div style="font-size: 0.88rem;"""
code = code.replace(target2, replacement2)

# 3. Update vostok-manual-modal
target3 = """            <!-- Manual Modal Overlay for Vostok-1 -->
            <div id="vostok-manual-modal" style="display: none; position: absolute; top: 42px; left: 10px; right: 10px; background: rgba(10, 15, 20, 0.99); z-index: 10005; border-radius: 8px; padding: 16px; font-family: monospace; max-height: 380px; overflow-y: auto; color: #e2e8f0; border: 2px solid #546e7a; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #546e7a; padding-bottom: 8px; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 0.95rem; color: #81c784; text-transform: uppercase;">📋 Manual - Vostok-1 Command Center</h3>
                <button class="stitch-btn-music" id="btn-vostok-manual-close" style="width: auto; padding: 2px 8px; font-size: 0.65rem; cursor: pointer;">Fermer [X]</button>
              </div>
              <div style="font-size: 0.72rem;"""

replacement3 = """            <!-- Manual Modal Overlay for Vostok-1 -->
            <div id="vostok-manual-modal" style="display: none; position: absolute; top: 42px; left: 10px; right: 10px; background: rgba(10, 15, 20, 0.99); z-index: 10005; border-radius: 8px; padding: 20px; font-family: monospace; max-height: 520px; overflow-y: auto; color: #e2e8f0; border: 2px solid #546e7a; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #546e7a; padding-bottom: 8px; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 1.15rem; color: #81c784; text-transform: uppercase;">📋 Manual - Vostok-1 Command Center</h3>
                <button class="stitch-btn-music" id="btn-vostok-manual-close" style="width: auto; padding: 4px 10px; font-size: 0.75rem; cursor: pointer;">Fermer [X]</button>
              </div>
              <div style="font-size: 0.88rem;"""
code = code.replace(target3, replacement3)

# 4. Update jet-manual-modal
target4 = """            <!-- Manual Modal Overlay for MiG-29 -->
            <div id="jet-manual-modal" style="display: none; position: absolute; top: 42px; left: 10px; right: 10px; background: rgba(10, 15, 20, 0.99); z-index: 10005; border-radius: 8px; padding: 16px; font-family: monospace; max-height: 380px; overflow-y: auto; color: #e2e8f0; border: 2px solid #546e7a; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #546e7a; padding-bottom: 8px; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 0.95rem; color: #81c784; text-transform: uppercase;">📋 Manual - MiG-29 Cockpit Simulator</h3>
                <button class="stitch-btn-music" id="btn-jet-manual-close" style="width: auto; padding: 2px 8px; font-size: 0.65rem; cursor: pointer;">Fermer [X]</button>
              </div>
              <div style="font-size: 0.72rem;"""

replacement4 = """            <!-- Manual Modal Overlay for MiG-29 -->
            <div id="jet-manual-modal" style="display: none; position: absolute; top: 42px; left: 10px; right: 10px; background: rgba(10, 15, 20, 0.99); z-index: 10005; border-radius: 8px; padding: 20px; font-family: monospace; max-height: 520px; overflow-y: auto; color: #e2e8f0; border: 2px solid #546e7a; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #546e7a; padding-bottom: 8px; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 1.15rem; color: #81c784; text-transform: uppercase;">📋 Manual - MiG-29 Cockpit Simulator</h3>
                <button class="stitch-btn-music" id="btn-jet-manual-close" style="width: auto; padding: 4px 10px; font-size: 0.75rem; cursor: pointer;">Fermer [X]</button>
              </div>
              <div style="font-size: 0.88rem;"""
code = code.replace(target4, replacement4)

# 5. Update foxbat-manual-modal
target5 = """            <!-- Manual Modal Overlay -->
            <div id="foxbat-manual-modal" style="display: none; position: absolute; top: 42px; left: 10px; right: 10px; background: rgba(10, 15, 20, 0.99); z-index: 10005; border-radius: 8px; padding: 16px; font-family: monospace; max-height: 380px; overflow-y: auto; color: #e2e8f0; border: 2px solid #546e7a; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #546e7a; padding-bottom: 8px; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 0.95rem; color: #81c784; text-transform: uppercase;">📋 Manual - MiG-25 Telemetry Console</h3>
                <button class="stitch-btn-music" id="btn-foxbat-manual-close" style="width: auto; padding: 2px 8px; font-size: 0.65rem; cursor: pointer;">Fermer [X]</button>
              </div>
              <div style="font-size: 0.72rem;"""

replacement5 = """            <!-- Manual Modal Overlay -->
            <div id="foxbat-manual-modal" style="display: none; position: absolute; top: 42px; left: 10px; right: 10px; background: rgba(10, 15, 20, 0.99); z-index: 10005; border-radius: 8px; padding: 20px; font-family: monospace; max-height: 520px; overflow-y: auto; color: #e2e8f0; border: 2px solid #546e7a; box-shadow: 0 4px 20px rgba(0,0,0,0.8); text-align: left;">
              <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #546e7a; padding-bottom: 8px; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 1.15rem; color: #81c784; text-transform: uppercase;">📋 Manual - MiG-25 Telemetry Console</h3>
                <button class="stitch-btn-music" id="btn-foxbat-manual-close" style="width: auto; padding: 4px 10px; font-size: 0.75rem; cursor: pointer;">Fermer [X]</button>
              </div>
              <div style="font-size: 0.88rem;"""
code = code.replace(target5, replacement5)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(code)

print("Manual modals resized successfully")
