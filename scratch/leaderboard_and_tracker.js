// ==================== FUNCTION renderLeaderboard ====================
function renderLeaderboard(dept) {
      const table = document.getElementById('leaderboard-table');
      if (!table) return;

      const currentReg = safeSession.getItem('aeris_auth_reg');
      const activeUser = MEMBERS_DATABASE[currentReg] || ADVISORS[currentReg];

      // Full access roles: CEO, Head, Vice Head, or Eng. Mohamad (registration ID '5550')
      const hasFullAccess = (activeUser && (
        activeUser.role === 'ceo' ||
        activeUser.role === 'head' ||
        activeUser.role === 'vice_head'
      )) || currentReg === '5550';

      const tasks = getTasks().filter(t => t.department === dept);
      const bonuses = getMemberBonuses();

      // Get members of this department
      let deptMembers = Object.entries(MEMBERS_DATABASE)
        .filter(([id, m]) => !m.hide && m.depts.includes(dept))
        .map(([id, m]) => {
          let doneWell = 0;
          let donePoorly = 0;
          let notDone = 0;

          tasks.forEach(t => {
            const progress = (t.memberProgress && t.memberProgress[id]) || 'unmarked';
            if (progress === 'well') doneWell++;
            else if (progress === 'poorly') donePoorly++;
            else if (progress === 'not_done') notDone++;
          });

          const memberBonus = bonuses[id] || 0;
          // Calculate score: Done Well = 10 pts, Done Poorly = 5 pts, Bonus = 10 pts, Not Done = -5 pts
          const rawScore = (doneWell * 10) + (donePoorly * 5) + (memberBonus * 10) - (notDone * 5);
          const score = Math.max(0, rawScore);

          return {
            id,
            ...m,
            doneWell,
            donePoorly,
            notDone,
            bonus: memberBonus,
            score
          };
        });

      // Sort by score descending, then by name
      deptMembers.sort((a, b) => {
        if (b.score !== a.score) return b.score - a.score;
        return a.name.localeCompare(b.name);
      });

      if (deptMembers.length === 0) {
        table.innerHTML = `<tr><td style="text-align: center; padding: 30px; color: var(--white-muted);">No members registered in this department database.</td></tr>`;
        return;
      }

      // Generate HTML
      let html = `
        <thead>
          <tr style="border-bottom: 2px solid rgba(246, 242, 223, 0.15);">
            <th style="width: 80px; text-align: center; padding: 12px 8px;">Rank</th>
            <th style="padding: 12px 12px;">Member Name</th>
            <th style="text-align: center; padding: 12px 12px;">Done Well (+10)</th>
            <th style="text-align: center; padding: 12px 12px;">Done Poorly (+5)</th>
            <th style="text-align: center; padding: 12px 12px; color: #f87171;">Missed (-5)</th>
            <th style="text-align: center; padding: 12px 12px; color: #60a5fa;">🏅 Bonuses (+10)</th>
            <th style="text-align: center; width: 140px; padding: 12px 12px;">Overall Score</th>
          </tr>
        </thead>
        <tbody>
      `;

      deptMembers.forEach((m, idx) => {
        // Standard members can only see the 1st place (idx === 0) and their own row
        if (!hasFullAccess && idx !== 0 && m.id !== currentReg) {
          return;
        }

        const rank = idx + 1;
        let rankBadge = '';
        if (rank === 1) rankBadge = '<span style="font-size: 1.3rem;" title="1st Place Gold 🥇">🥇</span>';
        else if (rank === 2) rankBadge = '<span style="font-size: 1.3rem;" title="2nd Place Silver 🥈">🥈</span>';
        else if (rank === 3) rankBadge = '<span style="font-size: 1.3rem;" title="3rd Place Bronze 🥉">🥉</span>';
        else rankBadge = `<span style="font-family: var(--font-heading); color: var(--white-muted); font-size: 0.95rem;">#${rank}</span>`;

        let roleBadge = '';
        if (m.role === 'ceo') {
          roleBadge = '<span class="tracker-table__member-role tracker-table__member-role--ceo" style="margin-left: 8px;">CEO</span>';
        } else if (m.role === 'head') {
          roleBadge = '<span class="tracker

// ==================== FUNCTION renderProgressTracker ====================
function renderProgressTracker() {
      const trackerTable = document.getElementById('tracker-table');
      if (!trackerTable) return;
      
      const currentReg = safeSession.getItem('aeris_auth_reg');
      const activeUser = MEMBERS_DATABASE[currentReg] || ADVISORS[currentReg];
      const isGlobalViewer = currentReg === '231002350' || currentReg === 'test 3' || !!ADVISORS[currentReg];
      const hasDeptPermission = isGlobalViewer || (activeUser && activeUser.depts && activeUser.depts.includes(currentDept));
      
      if (!hasDeptPermission) {
        trackerTable.innerHTML = `<tr><td style="text-align: center; padding: 40px; color: #ef4444; font-weight: bold; font-size: 1.1rem;">🚫 Access Denied: You do not have permission to view the ${escapeHtml(currentDept)} division tracker.</td></tr>`;
        return;
      }
      
      const tasks = getTasks().filter(t => t.department === currentDept);
      
      // Filter out hidden members (Aries and Hanah) and map by department array membership
      let deptMembers = Object.entries(MEMBERS_DATABASE)
        .filter(([id, m]) => !m.hide && m.depts.includes(currentDept))
        .map(([id, m]) => ({ id, ...m }));
        
      const isFullViewer = TRACKER_FULL_VIEWERS.has(currentReg);
      const isLeadership = isFullViewer || (activeUser && (activeUser.role === 'ceo' || activeUser.role === 'head' || activeUser.role === 'vice_head'));
      
      if (!isLeadership) {
        // Standard members can only track their own progress row
        deptMembers = deptMembers.filter(m => m.id === currentReg);
      }
      
      if (deptMembers.length === 0) {
        trackerTable.innerHTML = `<tr><td style="text-align: center; padding: 30px; color: var(--white-muted);">No members registered in this department database.</td></tr>`;
        return;
      }
      
      const bonuses = getMemberBonuses();
      
      // 1. Build table headers
      let headerHTML = '<thead><tr>';
      headerHTML += '<th>Member Name</th>';
      
      tasks.forEach(t => {
        const titleStr = isDragonUser() ? `🐲 ${t.title}` : (isSovietUser() ? `⭐ ${t.title}` : t.title);
        headerHTML += `<th title="${escapeHtml(t.description || '')}">${escapeHtml(titleStr)}</th>`;
      });
      
      headerHTML += '<th style="text-align: center; min-width: 80px;">Total Done</th>';
      headerHTML += '<th style="text-align: center; min-width: 80px; color: #10b981;">Done Well</th>';
      headerHTML += '<th style="text-align: center; min-width: 80px; color: #f59e0b;">Done Poorly</th>';
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
        let doneWell = 0;
        let donePoorly = 0

// ==================== FUNCTION handleEvalChange ====================
function handleEvalChange(e) {
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
            const memberBody = `Dear ${member.name},\n\nThis email is sent to inform you that your work on the task "${task.title}" in the ${task.department} department has been marked as Not Done by team leadership.\n\nPlease ensure you maintain timely progress on all assigned team targets. Contact your department head if you have any questions.\n\nBest regards,\nA.E.R.I.S. Team Administration`;
            
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
    }

    // Handles bonus count adjustments
    async function handleBonusChange(e) {
      e.stopPropagation();
      const btn = e.currentTarget;
      const memberId = btn.dataset.memberId;
      const isPlus = btn.classList.contains('bonus-btn--plus');
      
      const bonuses = getMemberBonuses();
      let currentBonus = bonuses[memberId] || 0;
      
      if (isPlus) {
        currentBonus++;
      } else {
        currentBonus = Math.max(0, currentBonus - 1);
      }
      
      bonuses[memberId] = currentBonus;
      saveMemberBonuses(bonuses);
      
      logToMailerConsole(`Bonus update: ${MEMBERS_DATABASE[memberId]?.name} now has ${currentBonus} active bonuses.`, 'sys');
      
      // Trigger performance checks to see if warnings should be sent or cleared
      await checkMemberMissedTasks(memberId);
      
      renderProgressTracker();
    }

    // Renders the leaderboard ranking dynamically based on the sub-team
    function renderLeaderboard(dept) {
      const table = document.getElementById('leaderboard-table');
      if (!table) return;

      const currentReg = safeSession.getItem('aeris_auth_reg');
      const activeUser = MEMBERS_DATABASE[currentReg] || ADVISORS[currentReg];

      // Full access roles: CEO, Head, Vice Head, or Eng. Mohamad (registration ID '5550')
      const hasFullAccess = (activeUser && (
        activeUser.role === 'ceo' ||
        activeUser.role === 'head' ||
        activeUser.role === 'vice_head'
      )) || currentReg === '5550';

      const tasks = getTasks().filter(t => t.department === dept);
      const bonuses = getMemberBonuses();

      // Get members of this department
      let deptMembers = Object.entries(MEMBERS_DATABASE)
        .filter(([id, m]) => !m.hide && m.depts.includes(dept))
        .map(([id, m]) => {
          let doneWell = 

// ==================== FUNCTION openTaskModal ====================
function openTaskModal(taskId) {
      const tasks = getTasks();
      const task = tasks.find(t => t.id === taskId);
      if (!task) return;

      activeTaskId = taskId;

      // Populate basic info
      modalTaskTitle.textContent = task.title;
      modalTaskDesc.textContent = task.description || (isFrenchUser() ? 'Aucune description fournie.' : 'No description provided.');
      
      // Capitalize department
      const deptLabels = {
        'mechanical': isFrenchUser() ? 'Mécanique' : 'Mechanical',
        'electrical': isFrenchUser() ? 'Électrique' : 'Electrical',
        'software': isFrenchUser() ? 'Logiciel' : 'Software',
        'non-technical': 'TDR & Marketing'
      };
      modalTaskDept.textContent = deptLabels[task.department] || task.department;
      modalTaskDept.className = `task-modal__dept-badge task-modal__dept-badge--${task.department}`;
      // Priority translation/labels
      const priorityLabels = isSpongebobUser() ? {
        low: '⭐ Patrick Level',
        medium: '🦑 Squidward Level',
        high: '🧽 SpongeBob Level',
        urgent: '🦀 Mr. Krabs Level'
      } : {
        low: isFrenchUser() ? 'Basse' : 'Low',
        medium: isFrenchUser() ? 'Moyenne' : 'Medium',
        high: isFrenchUser() ? 'Haute' : 'High',
        urgent: isFrenchUser() ? 'Urgente' : 'Urgent'
      };

      modalTaskPriority.textContent = priorityLabels[task.priority] || task.priority;
      modalTaskPriority.className = `task-modal__priority-badge task-modal__priority-badge--${task.priority}`;

      // Show/hide approved badge
      if (task.isApproved) {
        modalTaskApprovedBadge.style.display = 'inline-flex';
        if (isFrenchUser()) {
          modalTaskApprovedBadge.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg> Approuvé par l'Advisor`;
        } else {
          modalTaskApprovedBadge.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg> Approved by Advisor`;
        }
      } else {
        modalTaskApprovedBadge.style.display = 'none';
      }

      // Format deadline
      if (task.deadline) {
        const dateOptions = { month: 'short', day: 'numeric', year: 'numeric' };
        modalTaskDeadline.textContent = new Date(task.deadline).toLocaleDateString(isFrenchUser() ? 'fr-FR' : 'en-US', dateOptions);
      } else {
        modalTaskDeadline.textContent = isFrenchUser() ? 'Aucune date limite' : 'No deadline';
      }

      // Render feedback reviews list
      renderModalReviews(task);

      // Check access permission for feedback form
      const regNum = safeSession.getItem('aeris_auth_reg');
      if (AUTHORIZED_REVIEWERS.has(regNum)) {
        modalFeedbackForm.style.display = 'block';
        modalFeedbackInput.value = '';
        modalApproveCheckbox.checked = false;
        // Make sure the approve checkbox label makes sense based on state
        if (task.isApproved) {
          modalApproveCheckbox.disabled = true;
          const labelSpan = modalApproveCheckbox.parentNode.querySelector('span:last-child');
          if (labelSpan) labelSpan.textContent = isFrenchUser() ? 'Déjà approuvé' : 'Already approved';
        } else {
          modalApproveCheckbox.disabled = false;
          const labelSpan = modalApproveCheckbox.parentNode.querySelector('span:last-child');
          if (labelSpan) labelSpan.textContent = isFrenchUser() ? 'Approuver la tâche' : 'Approve task completion';
        }
      } else {
        modalFeedbackForm.style.display = 'none';
      }

      // Show modal
      taskModal.style.display = 'flex';
      document.body.style.overflow = 'hidden'; // prevent page scroll
    }

    function closeTaskM

// ==================== FUNCTION renderModalReviews ====================
function renderModalReviews(task) {
      const reviews = task.reviews || [];
      if (reviews.length === 0) {
        modalFeedbackList.innerHTML = `
          <div class="feedback-list__empty">
            <p>${isFrenchUser() ? "Aucun commentaire ou avis n'a été ajouté." : "No reviews or feedback comments have been submitted yet."}</p>
          </div>
        `;
        return;
      }

      modalFeedbackList.innerHTML = reviews.map(rev => {
        const dateStr = new Date(rev.createdAt).toLocaleDateString(isFrenchUser() ? 'fr-FR' : 'en-US', {
          month: 'short',
          day: 'numeric',
          year: 'numeric',
          hour: 'numeric',
          minute: '2-digit'
        });

        // Determine if reviewer is faculty (professors or mentor) or CEO
        const isCEO = rev.authorRole === 'Project Founder & CEO' || rev.authorRole.includes('CEO');
        const badgeClass = isCEO ? 'feedback-card__badge--ceo' : 'feedback-card__badge--faculty';
        const approvalBadge = rev.isApproval ? `
          <span class="feedback-card__approval-badge">
            <svg xmlns="http://www.w3.org/2000/svg" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
            ${isFrenchUser() ? 'Approuvé' : 'Approved Task'}
          </span>
        ` : '';

        return `
          <div class="feedback-card ${rev.isApproval ? 'feedback-card--approved' : ''}">
            <div class="feedback-card__header">
              <div class="feedback-card__author-info">
                <strong class="feedback-card__author">${escapeHtml(rev.authorName)}</strong>
                <span class="feedback-card__badge ${badgeClass}">${escapeHtml(rev.authorRole)}</span>
              </div>
              <span class="feedback-card__date">${dateStr}</span>
            </div>
            <div class="feedback-card__content">${escapeHtml(rev.content).replace(/\n/g, '<br>')}</div>
            ${approvalBadge}
          </div>
        `;
      }).join('');
    }

    function submitReview() {
      if (!activeTaskId) return;
      const content = modalFeedbackInput.value.trim();
      if (!content) {
        modalFeedbackInput.focus();
        modalFeedbackInput.style.borderColor = '#f87171';
        setTimeout(() => modalFeedbackInput.style.borderColor = '', 2000);
        return;
      }

      const regNum = safeSession.getItem('aeris_auth_reg');
      if (!AUTHORIZED_REVIEWERS.has(regNum)) return;

      let authorName = 'Authorized Reviewer';
      let authorRole = 'Advisor';

      const advisor = ADVISORS[regNum];
      if (advisor) {
        authorName = advisor.name;
        authorRole = advisor.title;
      } else if (regNum === '231002350') {
        authorName = 'Abduljabar Asaad';
        authorRole = 'Project Founder & CEO';
      } else if (regNum === 'test 3') {
        authorName = 'Test User 3';
        authorRole = 'CEO (Test)';
      }

      const tasks = getTasks();
      const task = tasks.find(t => t.id === activeTaskId);
      if (task) {
        task.reviews = task.reviews || [];
        const isApproval = modalApproveCheckbox.checked;

        task.reviews.push({
          id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6),
          authorName,
          authorRole,
          content,
          createdAt: new Date().toISOString(),
          isApproval
        });

        if (isApproval) {
          task.isApproved = true;
        }

        saveTasks(tasks);
        updateTaskInCloud(task.id, {
          reviews: task.reviews,
          isApproved: task.isApproved,
          notes: task.notes || ''
        });
        renderTasks();

        // Refresh modal content immediately
        openTaskModal(activeTaskId);
      }
    }

    // Modal action bindings
    if (taskModalClose) taskModalClose.addEventListener('click', closeTaskModal);
    if (taskModalOverlay) taskModalO

// ==================== FUNCTION renderTasks ====================
function renderTasks() {
      const tasks = getTasks().filter(t => t.department === currentDept);

      const todo = tasks.filter(t => t.status === 'todo');
      const progress = tasks.filter(t => t.status === 'progress');
      const done = tasks.filter(t => t.status === 'done');

      document.getElementById('count-todo').textContent = todo.length;
      document.getElementById('count-progress').textContent = progress.length;
      document.getElementById('count-done').textContent = done.length;

      document.getElementById('tasks-todo').innerHTML = todo.map(t => taskCard(t)).join('');
      document.getElementById('tasks-progress').innerHTML = progress.map(t => taskCard(t)).join('');
      document.getElementById('tasks-done').innerHTML = done.map(t => taskCard(t)).join('');

      // Show/hide empty state
      if (tasks.length === 0) {
        emptyState.style.display = 'flex';
        taskBoard.style.display = 'none';
      } else {
        emptyState.style.display = 'none';
        taskBoard.style.display = 'grid';
      }

      // Attach card event listeners
      document.querySelectorAll('.task-card__action').forEach(btn => {
        btn.addEventListener('click', handleTaskAction);
      });
      document.querySelectorAll('.task-card__delete').forEach(btn => {
        btn.addEventListener('click', handleTaskDelete);
      });
      document.querySelectorAll('.task-card').forEach(card => {
        card.addEventListener('click', handleCardClick);
      });
    }

    function taskCard(task) {
      const priorityLabels = { low: 'Low', medium: 'Medium', high: 'High', urgent: 'Urgent' };
      const deadlineStr = task.deadline ? new Date(task.deadline).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }) : '';
      const isOverdue = task.deadline && new Date(task.deadline) < new Date() && task.status !== 'done';

      let actions = '';
      if (currentRole !== 'advisor') {
        if (task.status === 'todo') {
          actions = `<button class="task-card__action" data-id="${task.id}" data-action="progress" title="Start task">▶ Start</button>`;
        } else if (task.status === 'progress') {
          actions = `<button class="task-card__action" data-id="${task.id}" data-action="done" title="Mark done">✓ Done</button>`;
        }
      }

      const deleteBtn = currentRole === 'head' ? `<button class="task-card__delete" data-id="${task.id}" title="Delete task">&times;</button>` : '';

      return `
        <div class="task-card task-card--${task.priority}" data-id="${task.id}" id="task-${task.id}">
          <div class="task-card__top">
            <span class="task-card__priority task-card__priority--${task.priority}">${priorityLabels[task.priority]}</span>
            ${task.isApproved ? `<span class="task-card__approved-pill">✓ Approved</span>` : ''}
            ${deleteBtn}
          </div>
          <h4 class="task-card__title">${escapeHtml(task.title)}</h4>
          ${task.description ? `<p class="task-card__desc">${escapeHtml(task.description)}</p>` : ''}
          <div class="task-card__footer">
            ${deadlineStr ? `<span class="task-card__deadline ${isOverdue ? 'task-card__deadline--overdue' : ''}">
              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
              ${deadlineStr}
            </span>` : ''}
            ${actions}
          </div>
        </div>
      `;
    }

    function handleCardClick(e) {
      const taskId = e.currentTarget.dataset.id;
      openTaskModal(taskId);
    }

    function handleTaskAction(e) {
      e.stopPropagation();
      if (currentRole !== 'head') {
        alert("Access Denied: Only the CEO or Team Leaders can take action on tasks.");
        return;
      }
      const id = e.currentTarget.dataset.id;
     

// ==================== FUNCTION taskCard ====================
function taskCard(task) {
      const priorityLabels = { low: 'Low', medium: 'Medium', high: 'High', urgent: 'Urgent' };
      const deadlineStr = task.deadline ? new Date(task.deadline).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }) : '';
      const isOverdue = task.deadline && new Date(task.deadline) < new Date() && task.status !== 'done';

      let actions = '';
      if (currentRole !== 'advisor') {
        if (task.status === 'todo') {
          actions = `<button class="task-card__action" data-id="${task.id}" data-action="progress" title="Start task">▶ Start</button>`;
        } else if (task.status === 'progress') {
          actions = `<button class="task-card__action" data-id="${task.id}" data-action="done" title="Mark done">✓ Done</button>`;
        }
      }

      const deleteBtn = currentRole === 'head' ? `<button class="task-card__delete" data-id="${task.id}" title="Delete task">&times;</button>` : '';

      return `
        <div class="task-card task-card--${task.priority}" data-id="${task.id}" id="task-${task.id}">
          <div class="task-card__top">
            <span class="task-card__priority task-card__priority--${task.priority}">${priorityLabels[task.priority]}</span>
            ${task.isApproved ? `<span class="task-card__approved-pill">✓ Approved</span>` : ''}
            ${deleteBtn}
          </div>
          <h4 class="task-card__title">${escapeHtml(task.title)}</h4>
          ${task.description ? `<p class="task-card__desc">${escapeHtml(task.description)}</p>` : ''}
          <div class="task-card__footer">
            ${deadlineStr ? `<span class="task-card__deadline ${isOverdue ? 'task-card__deadline--overdue' : ''}">
              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
              ${deadlineStr}
            </span>` : ''}
            ${actions}
          </div>
        </div>
      `;
    }

    function handleCardClick(e) {
      const taskId = e.currentTarget.dataset.id;
      openTaskModal(taskId);
    }

    function handleTaskAction(e) {
      e.stopPropagation();
      if (currentRole !== 'head') {
        alert("Access Denied: Only the CEO or Team Leaders can take action on tasks.");
        return;
      }
      const id = e.currentTarget.dataset.id;
      const action = e.currentTarget.dataset.action;
      const tasks = getTasks();
      const task = tasks.find(t => t.id === id);
      if (task) {
        task.status = action;
        saveTasks(tasks);
        updateTaskInCloud(id, { status: action });
        renderTasks();
      }
    }

    function handleTaskDelete(e) {
      e.stopPropagation();
      if (currentRole !== 'head') {
        alert("Access Denied: Only the CEO or Team Leaders can delete tasks.");
        return;
      }
      const id = e.currentTarget.dataset.id;
      let tasks = getTasks();
      tasks = tasks.filter(t => t.id !== id);
      saveTasks(tasks);
      deleteTaskFromCloud(id);
      renderTasks();
    }

    function escapeHtml(str) {
      const div = document.createElement('div');
      div.textContent = str;
      return div.innerHTML;
    }

    /* ========== TASK DETAILS & FEEDBACK MODAL LOGIC ========== */
    let activeTaskId = null;

    const taskModal = document.getElementById('task-modal');
    const taskModalOverlay = document.getElementById('task-modal-overlay');
    const taskModalClose = document.getElementById('task-modal-close');
    const modalTaskDept = document.getElementById('modal-task-dept');
    const modalTaskPriority = document.getElementById('modal-task-priority');
    const modalTaskApprovedBadge = document.getElementById('modal-task-approved-badge');
    const modalTaskTitle = document.getElementById('modal-task-title');
    const modalTaskDesc = document.getElementById(

