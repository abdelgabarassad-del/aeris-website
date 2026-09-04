import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update renderProgressTracker table headers and member cells
old_tracker_block = """      // 1. Build table headers
      let headerHTML = '<thead><tr>';
      headerHTML += '<th>Member Name</th>';
      
      tasks.forEach(t => {
        const titleStr = isDragonUser() ? `🐲 ${t.title}` : (isSovietUser() ? `⭐ ${t.title}` : t.title);
        headerHTML += `<th title="${escapeHtml(t.description || '')}">${escapeHtml(titleStr)}</th>`;
      });
      
      headerHTML += '<th style="text-align: center; min-width: 80px;">Total Done</th>';
      
      // Render dynamic tier metric headers
      pointConfig.tiers.forEach(tier => {
        headerHTML += `<th style="text-align: center; min-width: 80px; color: ${tier.color};">${tier.shortLabel}</th>`;
      });
      
      headerHTML += '<th style="text-align: center; min-width: 80px; color: #a78bfa;">Excused</th>';
      headerHTML += '<th style="text-align: center; min-width: 80px; color: #f87171;">Raw Missed</th>';
      headerHTML += '<th style="text-align: center; min-width: 100px; color: #60a5fa;">🏅 Bonuses</th>';
      headerHTML += '<th style="text-align: center; min-width: 80px; color: #ef4444;">Net Missed</th>';
      headerHTML += '</tr></thead>';
      
      // Helper function to build member row HTML
      function getMemberRowHTML(member) {
        let rowHTML = '<tr>';
        
        let roleBadge = '';
        if (member.role === 'ceo') {
          roleBadge = '<span class="tracker-table__member-role tracker-table__member-role--ceo">CEO</span>';
        } else if (member.role === 'head') {
          roleBadge = '<span class="tracker-table__member-role tracker-table__member-role--head">Head</span>';
        } else if (member.role === 'vice_head') {
          roleBadge = '<span class="tracker-table__member-role tracker-table__member-role--vice_head">Vice Head</span>';
        }
        
        rowHTML += `
          <td>
            <span class="tracker-table__member-name">${escapeHtml(member.name)}</span>
            <span class="tracker-table__member-id">${member.id}</span>
            ${roleBadge}
          </td>
        `;
        
        let totalDone = 0;
        const tierCounts = {};
        pointConfig.tiers.forEach(t => tierCounts[t.key] = 0);
        let notDone = 0;
        let excusedCount = 0;
        
        tasks.forEach(t => {
          const rawProgress = (t.memberProgress && t.memberProgress[member.id]) || 'unmarked';
          const progress = resolveProgressKey(currentDept, rawProgress);
          
          if (progress === 'not_done') {
            notDone++;
          } else if (progress === 'excused') {
            excusedCount++;
          } else if (progress !== 'unmarked') {
            totalDone++;
            if (tierCounts[progress] !== undefined) {
              tierCounts[progress]++;
            }
          }
          
          // Check editor permission: CEO, Vice Head, and Department Heads can edit
          const activeUser = MEMBERS_DATABASE[currentReg];
          const canEdit = activeUser && (
            activeUser.role === 'ceo' || 
            activeUser.role === 'vice_head' || 
            (activeUser.role === 'head' && activeUser.depts.includes(currentDept))
          );
          
          if (canEdit) {
            let optionsHTML = `<option value="unmarked" ${progress === 'unmarked' ? 'selected' : ''}>Not Marked</option>`;
            pointConfig.tiers.forEach(tier => {
              optionsHTML += `<option value="${tier.key}" ${progress === tier.key ? 'selected' : ''}>${tier.label}</option>`;
            });
            optionsHTML += `<option value="not_done" ${progress === 'not_done' ? 'selected' : ''}>Not Done</option>`;
            optionsHTML += `<option value="excused" ${progress === 'excused' ? 'selected' : ''}>Excused</option>`;
            
            rowHTML += `
              <td>
                <select class="eval-select eval-select--${progress}" data-task-id="${t.id}" data-member-id="${member.id}">
                  ${optionsHTML}
                </select>
              </td>
            `;
          } else {
            let label = 'Not Marked';
            if (progress === 'not_done') label = 'Not Done';
            else if (progress === 'excused') label = 'Excused';
            else {
              const matchingTier = pointConfig.tiers.find(tier => tier.key === progress);
              if (matchingTier) label = matchingTier.shortLabel;
            }
            
            rowHTML += `
              <td>
                <span class="eval-select eval-select--${progress}" style="pointer-events: none; display: inline-block;">${label}</span>
              </td>
            `;
          }
        });"""

new_tracker_block = """      // 1. Build table headers
      let headerHTML = '<thead><tr>';
      headerHTML += '<th>Member Name</th>';
      
      tasks.forEach(t => {
        const isMeeting = t.type === 'meeting';
        let titleStr = isDragonUser() ? `🐲 ${t.title}` : (isSovietUser() ? `⭐ ${t.title}` : t.title);
        let headerLabel = isMeeting ? `📅 ${escapeHtml(titleStr)}` : escapeHtml(titleStr);
        let tooltip = escapeHtml(t.description || '');
        if (isMeeting) {
          if (t.meetingImportance === 'warning') tooltip += ' (Policy: ⚠️ Warning on absence)';
          else if (t.meetingImportance === 'points') tooltip += ` (Policy: 📉 -${t.pointsDeduction || 5} pts deduction on absence)`;
        }
        headerHTML += `<th title="${tooltip}" style="${isMeeting ? 'border-top: 3px solid #a855f7;' : ''}">${headerLabel}</th>`;
      });
      
      headerHTML += '<th style="text-align: center; min-width: 80px;">Total Done</th>';
      
      // Render dynamic tier metric headers
      pointConfig.tiers.forEach(tier => {
        headerHTML += `<th style="text-align: center; min-width: 80px; color: ${tier.color};">${tier.shortLabel}</th>`;
      });
      
      headerHTML += '<th style="text-align: center; min-width: 80px; color: #a78bfa;">Excused</th>';
      headerHTML += '<th style="text-align: center; min-width: 80px; color: #f87171;">Raw Missed</th>';
      headerHTML += '<th style="text-align: center; min-width: 100px; color: #60a5fa;">🏅 Bonuses</th>';
      headerHTML += '<th style="text-align: center; min-width: 80px; color: #ef4444;">Net Missed</th>';
      headerHTML += '</tr></thead>';
      
      // Helper function to build member row HTML
      function getMemberRowHTML(member) {
        let rowHTML = '<tr>';
        
        let roleBadge = '';
        if (member.role === 'ceo') {
          roleBadge = '<span class="tracker-table__member-role tracker-table__member-role--ceo">CEO</span>';
        } else if (member.role === 'head') {
          roleBadge = '<span class="tracker-table__member-role tracker-table__member-role--head">Head</span>';
        } else if (member.role === 'vice_head') {
          roleBadge = '<span class="tracker-table__member-role tracker-table__member-role--vice_head">Vice Head</span>';
        }
        
        rowHTML += `
          <td>
            <span class="tracker-table__member-name">${escapeHtml(member.name)}</span>
            <span class="tracker-table__member-id">${member.id}</span>
            ${roleBadge}
          </td>
        `;
        
        let totalDone = 0;
        const tierCounts = {};
        pointConfig.tiers.forEach(t => tierCounts[t.key] = 0);
        let notDone = 0;
        let excusedCount = 0;
        
        tasks.forEach(t => {
          const rawProgress = (t.memberProgress && t.memberProgress[member.id]) || 'unmarked';
          const isMeeting = t.type === 'meeting';
          const progress = isMeeting ? rawProgress : resolveProgressKey(currentDept, rawProgress);
          
          if (isMeeting) {
            if (rawProgress === 'attended') {
              totalDone++;
            } else if (rawProgress === 'not_done') {
              notDone++;
            } else if (rawProgress === 'excused') {
              excusedCount++;
            }
          } else {
            if (progress === 'not_done') {
              notDone++;
            } else if (progress === 'excused') {
              excusedCount++;
            } else if (progress !== 'unmarked') {
              totalDone++;
              if (tierCounts[progress] !== undefined) {
                tierCounts[progress]++;
              }
            }
          }
          
          // Check editor permission: CEO, Vice Head, and Department Heads can edit
          const activeUser = MEMBERS_DATABASE[currentReg];
          const canEdit = activeUser && (
            activeUser.role === 'ceo' || 
            activeUser.role === 'vice_head' || 
            (activeUser.role === 'head' && activeUser.depts.includes(currentDept))
          );
          
          if (canEdit) {
            let optionsHTML = '';
            if (isMeeting) {
              let missedLabel = '❌ Missed';
              if (t.meetingImportance === 'warning') missedLabel = '❌ Missed (Warning)';
              else if (t.meetingImportance === 'points') missedLabel = `❌ Missed (-${t.pointsDeduction || 5} pts)`;

              optionsHTML = `
                <option value="unmarked" ${rawProgress === 'unmarked' ? 'selected' : ''}>Not Marked</option>
                <option value="attended" ${rawProgress === 'attended' ? 'selected' : ''}>✓ Attended</option>
                <option value="excused" ${rawProgress === 'excused' ? 'selected' : ''}>Excused</option>
                <option value="not_done" ${rawProgress === 'not_done' ? 'selected' : ''}>${missedLabel}</option>
              `;
            } else {
              optionsHTML = `<option value="unmarked" ${progress === 'unmarked' ? 'selected' : ''}>Not Marked</option>`;
              pointConfig.tiers.forEach(tier => {
                optionsHTML += `<option value="${tier.key}" ${progress === tier.key ? 'selected' : ''}>${tier.label}</option>`;
              });
              optionsHTML += `<option value="not_done" ${progress === 'not_done' ? 'selected' : ''}>Not Done</option>`;
              optionsHTML += `<option value="excused" ${progress === 'excused' ? 'selected' : ''}>Excused</option>`;
            }
            
            rowHTML += `
              <td>
                <select class="eval-select eval-select--${progress}" data-task-id="${t.id}" data-member-id="${member.id}">
                  ${optionsHTML}
                </select>
              </td>
            `;
          } else {
            let label = 'Not Marked';
            if (isMeeting) {
              if (rawProgress === 'attended') label = '✓ Attended';
              else if (rawProgress === 'excused') label = 'Excused';
              else if (rawProgress === 'not_done') {
                if (t.meetingImportance === 'warning') label = '❌ Missed (Warning)';
                else if (t.meetingImportance === 'points') label = `❌ Missed (-${t.pointsDeduction || 5} pts)`;
                else label = '❌ Missed';
              }
            } else {
              if (progress === 'not_done') label = 'Not Done';
              else if (progress === 'excused') label = 'Excused';
              else {
                const matchingTier = pointConfig.tiers.find(tier => tier.key === progress);
                if (matchingTier) label = matchingTier.shortLabel;
              }
            }
            
            rowHTML += `
              <td>
                <span class="eval-select eval-select--${progress}" style="pointer-events: none; display: inline-block;">${label}</span>
              </td>
            `;
          }
        });"""

if old_tracker_block in content:
    content = content.replace(old_tracker_block, new_tracker_block, 1)
    print("Successfully replaced renderProgressTracker block.")
else:
    print("Error: old_tracker_block not matched!")

# 2. Update handleEvalChange
old_eval_block = """    // Handles evaluation changes and triggers email alerts
    async function handleEvalChange(e) {
      const select = e.target;
      const taskId = select.dataset.taskId;
      const memberId = select.dataset.memberId;
      const newProgress = select.value;
      
      const tasks = getTasks();
      const task = tasks.find(t => t.id === taskId);
      if (!task) return;
      
      task.memberProgress = task.memberProgress || {};
      const oldProgress = task.memberProgress[memberId] || 'unmarked';
      
      // Update local storage representation
      task.memberProgress[memberId] = newProgress;
      
      // If changed to not_done and was not already marked not_done, trigger emails
      if (newProgress === 'not_done' && oldProgress !== 'not_done') {
        const member = MEMBERS_DATABASE[memberId];
        if (member) {
          task.notifiedMembers = task.notifiedMembers || [];
          if (!task.notifiedMembers.includes(memberId)) {
            task.notifiedMembers.push(memberId);
            
            // Save state immediately
            saveTasks(tasks);
            updateTaskInCloud(task.id, { memberProgress: task.memberProgress, notifiedMembers: task.notifiedMembers });
            
            // 1. Send automated missed task email to member
            const memberSubject = `Notice of Missed Task Target: "${task.title}"`;
            const memberBody = `Dear ${member.name},\\n\\nThis email is sent to inform you that your work on the task "${task.title}" in the ${task.department} department has been marked as Not Done by team leadership.\\n\\nPlease ensure you maintain timely progress on all assigned team targets. Contact your department head if you have any questions.\\n\\nBest regards,\\nA.E.R.I.S. Team Administration`;
            
            await sendMailerEmail(member.email, member.name, memberSubject, memberBody);
            
            // 2. Perform 3 missed tasks warning logic
            await checkMemberMissedTasks(memberId, task.department);
          }
        }
      } else {
        saveTasks(tasks);
        updateTaskInCloud(task.id, { memberProgress: task.memberProgress });
      }
      
      // Re-render Excel view
      renderProgressTracker();
    }"""

new_eval_block = """    // Handles evaluation changes and triggers email alerts
    async function handleEvalChange(e) {
      const select = e.target;
      const taskId = select.dataset.taskId;
      const memberId = select.dataset.memberId;
      const newProgress = select.value;
      
      const tasks = getTasks();
      const task = tasks.find(t => t.id === taskId);
      if (!task) return;
      
      task.memberProgress = task.memberProgress || {};
      const oldProgress = task.memberProgress[memberId] || 'unmarked';
      
      // Update local storage representation
      task.memberProgress[memberId] = newProgress;

      const isMeeting = task.type === 'meeting';
      const member = MEMBERS_DATABASE[memberId];

      if (isMeeting) {
        if (newProgress === 'attended') {
          logToMailerConsole(`Attendance marked: ${member?.name} attended meeting "${task.title}".`, 'sys');
        } else if (newProgress === 'not_done') {
          if (task.meetingImportance === 'points') {
            logToMailerConsole(`Meeting missed: ${member?.name} missed "${task.title}" (-${task.pointsDeduction || 5} pts deduction applied).`, 'sys');
          } else if (task.meetingImportance === 'warning') {
            logToMailerConsole(`Meeting missed: ${member?.name} missed "${task.title}" (⚠️ Formal warning policy).`, 'sys');
          }
        }
      }
      
      // If changed to not_done and was not already marked not_done, trigger emails
      if (newProgress === 'not_done' && oldProgress !== 'not_done') {
        if (member) {
          task.notifiedMembers = task.notifiedMembers || [];
          if (!task.notifiedMembers.includes(memberId)) {
            task.notifiedMembers.push(memberId);
            
            // Save state immediately
            saveTasks(tasks);
            updateTaskInCloud(task.id, { memberProgress: task.memberProgress, notifiedMembers: task.notifiedMembers });
            
            // 1. Send automated notice email to member
            const itemTypeName = isMeeting ? 'Meeting' : 'Task';
            const memberSubject = `Notice of Missed ${itemTypeName} Target: "${task.title}"`;
            let penaltyNotice = '';
            if (isMeeting && task.meetingImportance === 'points') {
              penaltyNotice = ` A score deduction of -${task.pointsDeduction || 5} points has been applied.`;
            } else if (isMeeting && task.meetingImportance === 'warning') {
              penaltyNotice = ' This missed meeting is recorded under official team attendance warnings.';
            }
            const memberBody = `Dear ${member.name},\\n\\nThis email is sent to inform you that your status on the ${itemTypeName} "${task.title}" in the ${task.department} department has been marked as Missed/Not Done by team leadership.${penaltyNotice}\\n\\nPlease ensure you maintain timely progress and attend all scheduled team sessions. Contact your department head if you have any questions.\\n\\nBest regards,\\nA.E.R.I.S. Team Administration`;
            
            await sendMailerEmail(member.email, member.name, memberSubject, memberBody);
            
            // 2. Perform 3 missed tasks warning logic
            await checkMemberMissedTasks(memberId, task.department);
          }
        }
      } else {
        saveTasks(tasks);
        updateTaskInCloud(task.id, { memberProgress: task.memberProgress });
      }
      
      // Re-render Excel view
      renderProgressTracker();
    }"""

if old_eval_block in content:
    content = content.replace(old_eval_block, new_eval_block, 1)
    print("Successfully replaced handleEvalChange block.")
else:
    print("Error: old_eval_block not matched!")

# 3. Update renderLeaderboard score calculation
old_board_block = """          const tierCounts = {};
          pointConfig.tiers.forEach(t => tierCounts[t.key] = 0);
          let notDone = 0;
          let excused = 0;
          
          tasks.forEach(t => {
            const rawProgress = (t.memberProgress && t.memberProgress[id]) || 'unmarked';
            const progress = resolveProgressKey(dept, rawProgress);
            
            if (progress === 'not_done') notDone++;
            else if (progress === 'excused') excused++;
            else if (tierCounts[progress] !== undefined) {
              tierCounts[progress]++;
            }
          });
          
          const memberBonus = bonuses[id] || 0;
          
          // Calculate score based on department configuration
          let tierScoreTotal = 0;
          pointConfig.tiers.forEach(tier => {
            tierScoreTotal += (tierCounts[tier.key] || 0) * tier.points;
          });
          
          const rawScore = tierScoreTotal + (memberBonus * pointConfig.bonusPoints) - (notDone * (pointConfig.missedPenalty || 0));
          const score = Math.max(0, rawScore);"""

new_board_block = """          const tierCounts = {};
          pointConfig.tiers.forEach(t => tierCounts[t.key] = 0);
          let notDone = 0;
          let excused = 0;
          let meetingPointsDeduction = 0;
          let meetingAttendedPoints = 0;
          let standardTaskNotDone = 0;
          
          tasks.forEach(t => {
            const rawProgress = (t.memberProgress && t.memberProgress[id]) || 'unmarked';
            const isMeeting = t.type === 'meeting';

            if (isMeeting) {
              if (rawProgress === 'attended') {
                meetingAttendedPoints += (pointConfig.bonusPoints || 3);
              } else if (rawProgress === 'not_done') {
                notDone++;
                if (t.meetingImportance === 'points') {
                  meetingPointsDeduction += (Number(t.pointsDeduction) || 5);
                }
              } else if (rawProgress === 'excused') {
                excused++;
              }
            } else {
              const progress = resolveProgressKey(dept, rawProgress);
              if (progress === 'not_done') {
                notDone++;
                standardTaskNotDone++;
              } else if (progress === 'excused') {
                excused++;
              } else if (tierCounts[progress] !== undefined) {
                tierCounts[progress]++;
              }
            }
          });
          
          const memberBonus = bonuses[id] || 0;
          
          // Calculate score based on department configuration
          let tierScoreTotal = 0;
          pointConfig.tiers.forEach(tier => {
            tierScoreTotal += (tierCounts[tier.key] || 0) * tier.points;
          });
          
          const rawScore = tierScoreTotal + meetingAttendedPoints + (memberBonus * pointConfig.bonusPoints) - (standardTaskNotDone * (pointConfig.missedPenalty || 0)) - meetingPointsDeduction;
          const score = Math.max(0, rawScore);"""

if old_board_block in content:
    content = content.replace(old_board_block, new_board_block, 1)
    print("Successfully replaced renderLeaderboard calculation block.")
else:
    print("Error: old_board_block not matched!")

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("All dashboard.html updates applied!")
