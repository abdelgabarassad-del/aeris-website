import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update dashboard.css
with open('dashboard.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

new_css = """
/* ==========================================================================
   KANBAN MEETING & TASK ENHANCEMENTS & ATTENDANCE TRACKER
   ========================================================================== */

/* Task Type Switcher */
.task-type-selector {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
  background: rgba(0, 0, 0, 0.25);
  padding: 5px;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  width: fit-content;
}

.task-type-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 18px;
  border-radius: 8px;
  font-family: var(--font-heading);
  font-size: 0.85rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  background: transparent;
  color: var(--white-muted);
  border: 1px solid transparent;
  cursor: pointer;
  transition: all 0.25s ease;
}

.task-type-btn:hover {
  color: var(--white);
  background: rgba(255, 255, 255, 0.06);
}

.task-type-btn.active {
  background: var(--accent);
  color: var(--bg-primary);
  border-color: var(--accent);
  box-shadow: 0 0 14px var(--accent-glow);
}

.task-type-btn.active[data-type="meeting"] {
  background: linear-gradient(135deg, #a855f7, #6366f1);
  color: #ffffff;
  border-color: #c084fc;
  box-shadow: 0 0 16px rgba(168, 85, 247, 0.4);
}

/* Meeting Specific Card Styles */
.task-card--meeting {
  border-left: 4px solid #a855f7 !important;
  background: linear-gradient(135deg, rgba(30, 27, 75, 0.35), rgba(15, 23, 42, 0.6)) !important;
}

.task-card__type-pill {
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 3px 8px;
  border-radius: 6px;
  background: rgba(168, 85, 247, 0.2);
  color: #c084fc;
  border: 1px solid rgba(168, 85, 247, 0.35);
}

.task-card__consequence-badge {
  font-size: 0.7rem;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 6px;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.task-card__consequence-badge--warning {
  background: rgba(245, 158, 11, 0.2);
  color: #fbbf24;
  border: 1px solid rgba(245, 158, 11, 0.4);
}

.task-card__consequence-badge--points {
  background: rgba(239, 68, 68, 0.2);
  color: #f87171;
  border: 1px solid rgba(239, 68, 68, 0.4);
}

/* Attendance Select Styling in Progress Tracker */
.eval-select--attended {
  background: rgba(16, 185, 129, 0.2) !important;
  color: #10b981 !important;
  border-color: rgba(16, 185, 129, 0.5) !important;
  font-weight: 700 !important;
}

.eval-select--excused {
  background: rgba(168, 85, 247, 0.2) !important;
  color: #c084fc !important;
  border-color: rgba(168, 85, 247, 0.5) !important;
}

.eval-select--not_done {
  background: rgba(239, 68, 68, 0.2) !important;
  color: #f87171 !important;
  border-color: rgba(239, 68, 68, 0.5) !important;
}
"""

if '/* Task Type Switcher */' not in css_content:
    css_content += "\n" + new_css
    with open('dashboard.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("Updated dashboard.css successfully.")
else:
    print("dashboard.css already contains new styles.")
