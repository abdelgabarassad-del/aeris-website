import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 1. Locate start and end of renderProgressTracker loop
start_tracker = None
end_tracker = None
for i, l in enumerate(lines):
    if '// 1. Build table headers' in l:
        start_tracker = i
    if start_tracker is not None and 'const memberBonus = bonuses[member.id] || 0;' in l:
        end_tracker = i
        break

print(f"Tracker block from line {start_tracker+1} to {end_tracker+1}")

new_tracker_lines = [
    "      // 1. Build table headers\n",
    "      let headerHTML = '<thead><tr>';\n",
    "      headerHTML += '<th>Member Name</th>';\n",
    "      \n",
    "      tasks.forEach(t => {\n",
    "        const isMeeting = t.type === 'meeting';\n",
    "        let titleStr = isDragonUser() ? `🐲 ${t.title}` : (isSovietUser() ? `⭐ ${t.title}` : t.title);\n",
    "        let headerLabel = isMeeting ? `📅 ${escapeHtml(titleStr)}` : escapeHtml(titleStr);\n",
    "        let tooltip = escapeHtml(t.description || '');\n",
    "        if (isMeeting) {\n",
    "          if (t.meetingImportance === 'warning') tooltip += ' (Policy: ⚠️ Warning on absence)';\n",
    "          else if (t.meetingImportance === 'points') tooltip += ` (Policy: 📉 -${t.pointsDeduction || 5} pts deduction on absence)`;\n",
    "        }\n",
    "        headerHTML += `<th title=\"${tooltip}\" style=\"${isMeeting ? 'border-top: 3px solid #a855f7;' : ''}\">${headerLabel}</th>`;\n",
    "      });\n",
    "      \n",
    "      headerHTML += '<th style=\"text-align: center; min-width: 80px;\">Total Done</th>';\n",
    "      \n",
    "      // Render dynamic tier metric headers\n",
    "      pointConfig.tiers.forEach(tier => {\n",
    "        headerHTML += `<th style=\"text-align: center; min-width: 80px; color: ${tier.color};\">${tier.shortLabel}</th>`;\n",
    "      });\n",
    "      \n",
    "      headerHTML += '<th style=\"text-align: center; min-width: 80px; color: #a78bfa;\">Excused</th>';\n",
    "      headerHTML += '<th style=\"text-align: center; min-width: 80px; color: #f87171;\">Raw Missed</th>';\n",
    "      headerHTML += '<th style=\"text-align: center; min-width: 100px; color: #60a5fa;\">🏅 Bonuses</th>';\n",
    "      headerHTML += '<th style=\"text-align: center; min-width: 80px; color: #ef4444;\">Net Missed</th>';\n",
    "      headerHTML += '</tr></thead>';\n",
    "      \n",
    "      // Helper function to build member row HTML\n",
    "      function getMemberRowHTML(member) {\n",
    "        let rowHTML = '<tr>';\n",
    "        \n",
    "        let roleBadge = '';\n",
    "        if (member.role === 'ceo') {\n",
    "          roleBadge = '<span class=\"tracker-table__member-role tracker-table__member-role--ceo\">CEO</span>';\n",
    "        } else if (member.role === 'head') {\n",
    "          roleBadge = '<span class=\"tracker-table__member-role tracker-table__member-role--head\">Head</span>';\n",
    "        } else if (member.role === 'vice_head') {\n",
    "          roleBadge = '<span class=\"tracker-table__member-role tracker-table__member-role--vice_head\">Vice Head</span>';\n",
    "        }\n",
    "        \n",
    "        rowHTML += `\n",
    "          <td>\n",
    "            <span class=\"tracker-table__member-name\">${escapeHtml(member.name)}</span>\n",
    "            <span class=\"tracker-table__member-id\">${member.id}</span>\n",
    "            ${roleBadge}\n",
    "          </td>\n",
    "        `;\n",
    "        \n",
    "        let totalDone = 0;\n",
    "        const tierCounts = {};\n",
    "        pointConfig.tiers.forEach(t => tierCounts[t.key] = 0);\n",
    "        let notDone = 0;\n",
    "        let excusedCount = 0;\n",
    "        \n",
    "        tasks.forEach(t => {\n",
    "          const rawProgress = (t.memberProgress && t.memberProgress[member.id]) || 'unmarked';\n",
    "          const isMeeting = t.type === 'meeting';\n",
    "          const progress = isMeeting ? rawProgress : resolveProgressKey(currentDept, rawProgress);\n",
    "          \n",
    "          if (isMeeting) {\n",
    "            if (rawProgress === 'attended') {\n",
    "              totalDone++;\n",
    "            } else if (rawProgress === 'not_done') {\n",
    "              notDone++;\n",
    "            } else if (rawProgress === 'excused') {\n",
    "              excusedCount++;\n",
    "            }\n",
    "          } else {\n",
    "            if (progress === 'not_done') {\n",
    "              notDone++;\n",
    "            } else if (progress === 'excused') {\n",
    "              excusedCount++;\n",
    "            } else if (progress !== 'unmarked') {\n",
    "              totalDone++;\n",
    "              if (tierCounts[progress] !== undefined) {\n",
    "                tierCounts[progress]++;\n",
    "              }\n",
    "            }\n",
    "          }\n",
    "          \n",
    "          // Check editor permission: CEO, Vice Head, and Department Heads can edit\n",
    "          const activeUser = MEMBERS_DATABASE[currentReg];\n",
    "          const canEdit = activeUser && (\n",
    "            activeUser.role === 'ceo' || \n",
    "            activeUser.role === 'vice_head' || \n",
    "            (activeUser.role === 'head' && activeUser.depts.includes(currentDept))\n",
    "          );\n",
    "          \n",
    "          if (canEdit) {\n",
    "            let optionsHTML = '';\n",
    "            if (isMeeting) {\n",
    "              let missedLabel = '❌ Missed';\n",
    "              if (t.meetingImportance === 'warning') missedLabel = '❌ Missed (Warning)';\n",
    "              else if (t.meetingImportance === 'points') missedLabel = `❌ Missed (-${t.pointsDeduction || 5} pts)`;\n",
    "\n",
    "              optionsHTML = `\n",
    "                <option value=\"unmarked\" ${rawProgress === 'unmarked' ? 'selected' : ''}>Not Marked</option>\n",
    "                <option value=\"attended\" ${rawProgress === 'attended' ? 'selected' : ''}>✓ Attended</option>\n",
    "                <option value=\"excused\" ${rawProgress === 'excused' ? 'selected' : ''}>Excused</option>\n",
    "                <option value=\"not_done\" ${rawProgress === 'not_done' ? 'selected' : ''}>${missedLabel}</option>\n",
    "              `;\n",
    "            } else {\n",
    "              optionsHTML = `<option value=\"unmarked\" ${progress === 'unmarked' ? 'selected' : ''}>Not Marked</option>`;\n",
    "              pointConfig.tiers.forEach(tier => {\n",
    "                optionsHTML += `<option value=\"${tier.key}\" ${progress === tier.key ? 'selected' : ''}>${tier.label}</option>`;\n",
    "              });\n",
    "              optionsHTML += `<option value=\"not_done\" ${progress === 'not_done' ? 'selected' : ''}>Not Done</option>`;\n",
    "              optionsHTML += `<option value=\"excused\" ${progress === 'excused' ? 'selected' : ''}>Excused</option>`;\n",
    "            }\n",
    "            \n",
    "            rowHTML += `\n",
    "              <td>\n",
    "                <select class=\"eval-select eval-select--${progress}\" data-task-id=\"${t.id}\" data-member-id=\"${member.id}\">\n",
    "                  ${optionsHTML}\n",
    "                </select>\n",
    "              </td>\n",
    "            `;\n",
    "          } else {\n",
    "            let label = 'Not Marked';\n",
    "            if (isMeeting) {\n",
    "              if (rawProgress === 'attended') label = '✓ Attended';\n",
    "              else if (rawProgress === 'excused') label = 'Excused';\n",
    "              else if (rawProgress === 'not_done') {\n",
    "                if (t.meetingImportance === 'warning') label = '❌ Missed (Warning)';\n",
    "                else if (t.meetingImportance === 'points') label = `❌ Missed (-${t.pointsDeduction || 5} pts)`;\n",
    "                else label = '❌ Missed';\n",
    "              }\n",
    "            } else {\n",
    "              if (progress === 'not_done') label = 'Not Done';\n",
    "              else if (progress === 'excused') label = 'Excused';\n",
    "              else {\n",
    "                const matchingTier = pointConfig.tiers.find(tier => tier.key === progress);\n",
    "                if (matchingTier) label = matchingTier.shortLabel;\n",
    "              }\n",
    "            }\n",
    "            \n",
    "            rowHTML += `\n",
    "              <td>\n",
    "                <span class=\"eval-select eval-select--${progress}\" style=\"pointer-events: none; display: inline-block;\">${label}</span>\n",
    "              </td>\n",
    "            `;\n",
    "          }\n",
    "        });\n",
    "        \n"
]

lines = lines[:start_tracker] + new_tracker_lines + lines[end_tracker:]

# 2. Locate start and end of leaderboard score calculation
start_board = None
end_board = None
for i, l in enumerate(lines):
    if 'pointConfig.tiers.forEach(t => tierCounts[t.key] = 0);' in l and 'const memberBonus = bonuses[id] || 0;' in lines[i+15]:
        start_board = i
    if start_board is not None and 'const score = Math.max(0, rawScore);' in l:
        end_board = i + 1
        break

print(f"Leaderboard block from line {start_board+1} to {end_board+1}")

new_board_lines = [
    "          const tierCounts = {};\n",
    "          pointConfig.tiers.forEach(t => tierCounts[t.key] = 0);\n",
    "          let notDone = 0;\n",
    "          let excused = 0;\n",
    "          let meetingPointsDeduction = 0;\n",
    "          let meetingAttendedPoints = 0;\n",
    "          let standardTaskNotDone = 0;\n",
    "          \n",
    "          tasks.forEach(t => {\n",
    "            const rawProgress = (t.memberProgress && t.memberProgress[id]) || 'unmarked';\n",
    "            const isMeeting = t.type === 'meeting';\n",
    "\n",
    "            if (isMeeting) {\n",
    "              if (rawProgress === 'attended') {\n",
    "                meetingAttendedPoints += (pointConfig.bonusPoints || 3);\n",
    "              } else if (rawProgress === 'not_done') {\n",
    "                notDone++;\n",
    "                if (t.meetingImportance === 'points') {\n",
    "                  meetingPointsDeduction += (Number(t.pointsDeduction) || 5);\n",
    "                }\n",
    "              } else if (rawProgress === 'excused') {\n",
    "                excused++;\n",
    "              }\n",
    "            } else {\n",
    "              const progress = resolveProgressKey(dept, rawProgress);\n",
    "              if (progress === 'not_done') {\n",
    "                notDone++;\n",
    "                standardTaskNotDone++;\n",
    "              } else if (progress === 'excused') {\n",
    "                excused++;\n",
    "              } else if (tierCounts[progress] !== undefined) {\n",
    "                tierCounts[progress]++;\n",
    "              }\n",
    "            }\n",
    "          });\n",
    "\n",
    "          const memberBonus = bonuses[id] || 0;\n",
    "          \n",
    "          // Calculate score based on department configuration\n",
    "          let tierScoreTotal = 0;\n",
    "          pointConfig.tiers.forEach(tier => {\n",
    "            tierScoreTotal += (tierCounts[tier.key] || 0) * tier.points;\n",
    "          });\n",
    "          \n",
    "          const rawScore = tierScoreTotal + meetingAttendedPoints + (memberBonus * pointConfig.bonusPoints) - (standardTaskNotDone * (pointConfig.missedPenalty || 0)) - meetingPointsDeduction;\n",
    "          const score = Math.max(0, rawScore);\n"
]

lines = lines[:start_board] + new_board_lines + lines[end_board:]

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Patch applied cleanly to dashboard.html!")
