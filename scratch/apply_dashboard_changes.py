import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# -------------------------------------------------------------
# 1. Update Task Upload Form HTML
# -------------------------------------------------------------
old_form_html = """      <!-- Task Upload Form (Head only) -->
      <div class="task-form-wrapper fade-in" id="task-form-wrapper" style="display: none;">
        <div class="task-form" id="task-form">
          <h3 class="task-form__title">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="12" y1="18" x2="12" y2="12"/><line x1="9" y1="15" x2="15" y2="15"/></svg>
            Upload New Task
          </h3>
          <div class="task-form__fields">
            <div class="form-group">
              <label for="task-title">Task Title</label>
              <input type="text" id="task-title" placeholder="Enter task title..." />
            </div>
            <div class="form-group">
              <label for="task-description">Description</label>
              <textarea id="task-description" rows="3" placeholder="Describe the task in detail..."></textarea>
            </div>
            <div class="form-row">
              <div class="form-group">
                <label for="task-priority">Priority</label>
                <select id="task-priority">
                  <option value="low">Low</option>
                  <option value="medium" selected>Medium</option>
                  <option value="high">High</option>
                  <option value="urgent">Urgent</option>
                </select>
              </div>
              <div class="form-group">
                <label for="task-deadline">Deadline</label>
                <input type="date" id="task-deadline" />
              </div>
            </div>
            <button class="btn-primary task-form__submit" id="submit-task">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
              Add Task
            </button>
          </div>
        </div>
      </div>"""

new_form_html = """      <!-- Task / Meeting Upload Form (Head, Vice Head, CEO) -->
      <div class="task-form-wrapper fade-in" id="task-form-wrapper" style="display: none;">
        <div class="task-form" id="task-form">
          <!-- Item Type Selector (Task vs Meeting) -->
          <div class="task-type-selector" id="task-type-selector" style="display: flex; gap: 10px; margin-bottom: 18px;">
            <button type="button" class="task-type-btn active" id="type-btn-task" data-type="task">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="12" y1="18" x2="12" y2="12"/><line x1="9" y1="15" x2="15" y2="15"/></svg>
              <span>📋 Task</span>
            </button>
            <button type="button" class="task-type-btn" id="type-btn-meeting" data-type="meeting">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
              <span>📅 Meeting</span>
            </button>
          </div>

          <h3 class="task-form__title" id="form-header-title">
            <svg id="form-header-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="12" y1="18" x2="12" y2="12"/><line x1="9" y1="15" x2="15" y2="15"/></svg>
            <span id="form-header-text">Upload New Task</span>
          </h3>
          <div class="task-form__fields">
            <div class="form-group">
              <label for="task-title" id="lbl-item-title">Task Title</label>
              <input type="text" id="task-title" placeholder="Enter task title..." />
            </div>
            <div class="form-group">
              <label for="task-description" id="lbl-item-desc">Description</label>
              <textarea id="task-description" rows="3" placeholder="Describe the task in detail..."></textarea>
            </div>
            <div class="form-row">
              <div class="form-group">
                <label for="task-priority" id="lbl-item-priority">Priority</label>
                <select id="task-priority">
                  <option value="low">Low</option>
                  <option value="medium" selected>Medium</option>
                  <option value="high">High</option>
                  <option value="urgent">Urgent</option>
                </select>
              </div>
              <div class="form-group">
                <label for="task-deadline" id="lbl-item-deadline">Deadline</label>
                <input type="date" id="task-deadline" />
              </div>
            </div>

            <!-- Meeting specific options (Importance / Penalty policy) -->
            <div id="meeting-options-wrapper" style="display: none; background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 14px 16px; margin-bottom: 16px;">
              <div class="form-row" style="align-items: flex-start; gap: 16px;">
                <div class="form-group" style="flex: 1;">
                  <label for="meeting-importance" style="display: flex; align-items: center; gap: 6px; font-weight: 600; color: var(--accent);">
                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
                    <span>Missed Meeting Policy</span>
                  </label>
                  <select id="meeting-importance" style="padding: 10px; border-radius: 8px; width: 100%; background: rgba(0, 0, 0, 0.3); border: 1px solid rgba(255, 255, 255, 0.15); color: inherit;">
                    <option value="none" selected>🟢 Standard (No penalties if missed)</option>
                    <option value="warning">⚠️ Official Warning (Issues warning if missed)</option>
                    <option value="points">📉 Deduct Points (Minuses custom score if missed)</option>
                  </select>
                </div>

                <div class="form-group" id="meeting-points-deduct-group" style="display: none; flex: 1;">
                  <label for="meeting-deduct-points" style="display: flex; align-items: center; gap: 6px; font-weight: 600; color: #f87171;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="8" y1="12" x2="16" y2="12"/></svg>
                    <span>Points to Minus (pts)</span>
                  </label>
                  <input type="number" id="meeting-deduct-points" min="1" max="100" value="5" placeholder="e.g. 5, 10..." style="padding: 10px; border-radius: 8px; width: 100%; background: rgba(0, 0, 0, 0.3); border: 1px solid rgba(239, 68, 68, 0.3); color: inherit;" />
                  <span style="font-size: 0.75rem; color: var(--white-muted); display: block; margin-top: 4px;">Members marked absent will lose this amount on the leaderboard.</span>
                </div>
              </div>
            </div>

            <button class="btn-primary task-form__submit" id="submit-task">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
              <span id="submit-task-text">Add Task</span>
            </button>
          </div>
        </div>
      </div>"""

if old_form_html in content:
    content = content.replace(old_form_html, new_form_html, 1)
    print("Replaced Task Form HTML.")
else:
    print("Warning: old_form_html not matched!")

# -------------------------------------------------------------
# 2. Update pushTaskToCloud to serialize type and meeting fields
# -------------------------------------------------------------
old_push_task = """    // Cloud sync: push a new task to the Google Sheet
    function pushTaskToCloud(task) {
      if (!_cloudSyncEnabled) return;
      const params = new URLSearchParams();
      params.append('action', 'addTask');
      params.append('id', task.id);
      params.append('title', task.title || '');
      params.append('description', task.description || '');
      params.append('priority', task.priority || 'medium');
      params.append('deadline', task.deadline || '');
      params.append('department', task.department || 'mechanical');
      params.append('status', task.status || 'todo');
      params.append('createdAt', task.createdAt || new Date().toISOString());
      params.append('isApproved', String(task.isApproved || false));
      params.append('notes', task.notes || '');
      params.append('memberProgress', JSON.stringify(task.memberProgress || {}));
      params.append('reviews', JSON.stringify(task.reviews || []));
      fetch(TASKS_SCRIPT_URL, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: params }).catch(function(){});
    }"""

new_push_task = """    // Cloud sync: push a new task to the Google Sheet
    function pushTaskToCloud(task) {
      if (!_cloudSyncEnabled) return;
      const params = new URLSearchParams();
      params.append('action', 'addTask');
      params.append('id', task.id);
      params.append('title', task.title || '');
      params.append('description', task.description || '');
      params.append('priority', task.priority || 'medium');
      params.append('deadline', task.deadline || '');
      params.append('department', task.department || 'mechanical');
      params.append('status', task.status || 'todo');
      params.append('type', task.type || 'task');
      params.append('meetingImportance', task.meetingImportance || 'none');
      params.append('pointsDeduction', String(task.pointsDeduction || 0));
      params.append('createdAt', task.createdAt || new Date().toISOString());
      params.append('isApproved', String(task.isApproved || false));
      params.append('notes', task.notes || '');
      params.append('memberProgress', JSON.stringify(task.memberProgress || {}));
      params.append('reviews', JSON.stringify(task.reviews || []));
      fetch(TASKS_SCRIPT_URL, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: params }).catch(function(){});
    }"""

if old_push_task in content:
    content = content.replace(old_push_task, new_push_task, 1)
    print("Replaced pushTaskToCloud.")
else:
    print("Warning: old_push_task not matched!")

# -------------------------------------------------------------
# 3. Add Item Type DOM selections & Switcher logic + Update submitBtn & taskCard
# -------------------------------------------------------------
old_task_listeners = """    // Submit task
    submitBtn.addEventListener('click', () => {
      if (currentRole !== 'head') {
        alert("Access Denied: Only the CEO or Team Leaders can create tasks.");
        return;
      }
      const title = taskTitle.value.trim();
      const desc = taskDesc.value.trim();
      const priority = taskPriority.value;
      const deadline = taskDeadline.value;

      if (!title) {
        taskTitle.focus();
        taskTitle.style.borderColor = '#f87171';
        setTimeout(() => taskTitle.style.borderColor = '', 2000);
        return;
      }

      const tasks = getTasks();
      const newTask = {
        id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6),
        title,
        description: desc,
        priority,
        deadline,
        department: currentDept,
        status: 'todo',
        createdAt: new Date().toISOString()
      };
      tasks.push(newTask);
      saveTasks(tasks);
      pushTaskToCloud(newTask);

      // Reset form
      taskTitle.value = '';
      taskDesc.value = '';
      taskPriority.value = 'medium';
      taskDeadline.value = '';

      renderTasks();

      // Flash success
      const isFr = isFrenchUser();
      const isMickey = isMickeyUser();
      let successText = '✓ Added!';
      let defaultText = ' Add Task';
      if (isMickey) {
        successText = '✓ Hot dog! Ajoutée ! 🌭';
        defaultText = ' Ajouter la Tâche';
      } else if (isFr) {
        successText = '✓ Ajoutée !';
        defaultText = ' Ajouter la Tâche';
      }
      submitBtn.textContent = successText;
      submitBtn.style.background = '#7dd3a8';
      submitBtn.style.color = '';
      setTimeout(() => {
        submitBtn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>' + defaultText;
        submitBtn.style.background = '';
        submitBtn.style.color = '';
      }, 1500);
    });

    // Render tasks
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
    }"""

new_task_listeners = """    // Item Type & Meeting form state
    let activeItemType = 'task'; // 'task' | 'meeting'

    const typeBtnTask = document.getElementById('type-btn-task');
    const typeBtnMeeting = document.getElementById('type-btn-meeting');
    const meetingOptionsWrapper = document.getElementById('meeting-options-wrapper');
    const meetingImportance = document.getElementById('meeting-importance');
    const meetingPointsDeductGroup = document.getElementById('meeting-points-deduct-group');
    const meetingDeductPoints = document.getElementById('meeting-deduct-points');
    const formHeaderText = document.getElementById('form-header-text');
    const lblItemTitle = document.getElementById('lbl-item-title');
    const lblItemDesc = document.getElementById('lbl-item-desc');
    const lblItemDeadline = document.getElementById('lbl-item-deadline');
    const submitTaskText = document.getElementById('submit-task-text');

    function setItemType(type) {
      activeItemType = type;
      if (typeBtnTask) typeBtnTask.classList.toggle('active', type === 'task');
      if (typeBtnMeeting) typeBtnMeeting.classList.toggle('active', type === 'meeting');

      if (type === 'meeting') {
        if (meetingOptionsWrapper) meetingOptionsWrapper.style.display = 'block';
        if (formHeaderText) formHeaderText.textContent = 'Schedule New Meeting';
        if (lblItemTitle) lblItemTitle.textContent = 'Meeting Title / Topic';
        if (lblItemDesc) lblItemDesc.textContent = 'Agenda & Discussion Points';
        if (lblItemDeadline) lblItemDeadline.textContent = 'Meeting Date';
        if (taskTitle) taskTitle.placeholder = 'e.g. Weekly Technical Sync, Project Review...';
        if (taskDesc) taskDesc.placeholder = 'Outline meeting agenda, discussion topics, links...';
        if (submitTaskText) submitTaskText.textContent = 'Schedule Meeting';
      } else {
        if (meetingOptionsWrapper) meetingOptionsWrapper.style.display = 'none';
        if (formHeaderText) formHeaderText.textContent = 'Upload New Task';
        if (lblItemTitle) lblItemTitle.textContent = 'Task Title';
        if (lblItemDesc) lblItemDesc.textContent = 'Description';
        if (lblItemDeadline) lblItemDeadline.textContent = 'Deadline';
        if (taskTitle) taskTitle.placeholder = 'Enter task title...';
        if (taskDesc) taskDesc.placeholder = 'Describe the task in detail...';
        if (submitTaskText) submitTaskText.textContent = 'Add Task';
      }
    }

    if (typeBtnTask) typeBtnTask.addEventListener('click', () => setItemType('task'));
    if (typeBtnMeeting) typeBtnMeeting.addEventListener('click', () => setItemType('meeting'));

    if (meetingImportance) {
      meetingImportance.addEventListener('change', () => {
        if (meetingPointsDeductGroup) {
          meetingPointsDeductGroup.style.display = (meetingImportance.value === 'points') ? 'block' : 'none';
        }
      });
    }

    // Submit task or meeting
    submitBtn.addEventListener('click', () => {
      const currentReg = safeSession.getItem('aeris_auth_reg');
      const member = MEMBERS_DATABASE[currentReg];
      const isLeadership = currentRole === 'head' || (member && (member.role === 'head' || member.role === 'vice_head' || member.role === 'ceo'));
      if (!isLeadership) {
        alert("Access Denied: Only the CEO, Team Heads, or Vice Heads can create tasks or schedule meetings.");
        return;
      }
      const title = taskTitle.value.trim();
      const desc = taskDesc.value.trim();
      const priority = taskPriority.value;
      const deadline = taskDeadline.value;
      const itemType = activeItemType || 'task';

      if (!title) {
        taskTitle.focus();
        taskTitle.style.borderColor = '#f87171';
        setTimeout(() => taskTitle.style.borderColor = '', 2000);
        return;
      }

      const importance = (itemType === 'meeting' && meetingImportance) ? meetingImportance.value : 'none';
      const deductVal = (itemType === 'meeting' && importance === 'points' && meetingDeductPoints) ? (parseInt(meetingDeductPoints.value, 10) || 5) : 0;

      const tasks = getTasks();
      const newTask = {
        id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6),
        title,
        description: desc,
        priority,
        deadline,
        department: currentDept,
        status: 'todo',
        type: itemType, // 'task' | 'meeting'
        meetingImportance: importance, // 'none' | 'warning' | 'points'
        pointsDeduction: deductVal,
        createdAt: new Date().toISOString()
      };
      tasks.push(newTask);
      saveTasks(tasks);
      pushTaskToCloud(newTask);

      // Reset form
      taskTitle.value = '';
      taskDesc.value = '';
      taskPriority.value = 'medium';
      taskDeadline.value = '';
      if (meetingImportance) meetingImportance.value = 'none';
      if (meetingPointsDeductGroup) meetingPointsDeductGroup.style.display = 'none';
      if (meetingDeductPoints) meetingDeductPoints.value = '5';

      renderTasks();
      if (currentView === 'tracker') {
        renderProgressTracker();
      }

      // Flash success
      const isFr = isFrenchUser();
      const isMickey = isMickeyUser();
      let successText = itemType === 'meeting' ? '✓ Scheduled!' : '✓ Added!';
      let defaultText = itemType === 'meeting' ? ' Schedule Meeting' : ' Add Task';
      if (isMickey) {
        successText = itemType === 'meeting' ? '✓ Hot dog! Programmée ! 🌭' : '✓ Hot dog! Ajoutée ! 🌭';
        defaultText = itemType === 'meeting' ? ' Programmer la Réunion' : ' Ajouter la Tâche';
      } else if (isFr) {
        successText = itemType === 'meeting' ? '✓ Programmée !' : '✓ Ajoutée !';
        defaultText = itemType === 'meeting' ? ' Programmer la Réunion' : ' Ajouter la Tâche';
      }
      submitBtn.textContent = successText;
      submitBtn.style.background = '#7dd3a8';
      submitBtn.style.color = '';
      setTimeout(() => {
        submitBtn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg><span id="submit-task-text">' + defaultText + '</span>';
        submitBtn.style.background = '';
        submitBtn.style.color = '';
      }, 1500);
    });

    // Render tasks
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
      const isMeeting = task.type === 'meeting';
      const priorityLabels = { low: 'Low', medium: 'Medium', high: 'High', urgent: 'Urgent' };
      const deadlineStr = task.deadline ? new Date(task.deadline).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }) : '';
      const isOverdue = task.deadline && new Date(task.deadline) < new Date() && task.status !== 'done';

      let actions = '';
      if (currentRole !== 'advisor') {
        if (task.status === 'todo') {
          actions = `<button class="task-card__action" data-id="${task.id}" data-action="progress" title="${isMeeting ? 'Start meeting' : 'Start task'}">▶ ${isMeeting ? 'In Session' : 'Start'}</button>`;
        } else if (task.status === 'progress') {
          actions = `<button class="task-card__action" data-id="${task.id}" data-action="done" title="${isMeeting ? 'Conclude meeting' : 'Mark done'}">✓ ${isMeeting ? 'Concluded' : 'Done'}</button>`;
        }
      }

      const currentReg = safeSession.getItem('aeris_auth_reg');
      const member = MEMBERS_DATABASE[currentReg];
      const isLeadership = currentRole === 'head' || (member && (member.role === 'head' || member.role === 'vice_head' || member.role === 'ceo'));
      const deleteBtn = isLeadership ? `<button class="task-card__delete" data-id="${task.id}" title="Delete">&times;</button>` : '';

      let consequencePill = '';
      if (isMeeting) {
        if (task.meetingImportance === 'warning') {
          consequencePill = `<span class="task-card__consequence-badge task-card__consequence-badge--warning" title="Warning issued if missed">⚠️ Warning on Miss</span>`;
        } else if (task.meetingImportance === 'points') {
          consequencePill = `<span class="task-card__consequence-badge task-card__consequence-badge--points" title="${task.pointsDeduction || 5} pts deducted if missed">📉 -${task.pointsDeduction || 5} pts on Miss</span>`;
        }
      }

      const cardTypeClass = isMeeting ? 'task-card--meeting' : '';
      const typeBadge = isMeeting ? '<span class="task-card__type-pill">📅 Meeting</span>' : '';

      return `
        <div class="task-card task-card--${task.priority} ${cardTypeClass}" data-id="${task.id}" id="task-${task.id}">
          <div class="task-card__top">
            <div style="display: flex; align-items: center; gap: 6px; flex-wrap: wrap;">
              ${typeBadge}
              <span class="task-card__priority task-card__priority--${task.priority}">${priorityLabels[task.priority]}</span>
              ${consequencePill}
              ${task.isApproved ? `<span class="task-card__approved-pill">✓ Approved</span>` : ''}
            </div>
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
    }"""

if old_task_listeners in content:
    content = content.replace(old_task_listeners, new_task_listeners, 1)
    print("Replaced Task Listeners, Submit handler, and taskCard.")
else:
    print("Warning: old_task_listeners not matched!")

# -------------------------------------------------------------
# 4. Update handleTaskAction and handleTaskDelete permissions
# -------------------------------------------------------------
old_task_actions = """    function handleTaskAction(e) {
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
    }"""

new_task_actions = """    function handleTaskAction(e) {
      e.stopPropagation();
      const currentReg = safeSession.getItem('aeris_auth_reg');
      const member = MEMBERS_DATABASE[currentReg];
      const isLeadership = currentRole === 'head' || (member && (member.role === 'head' || member.role === 'vice_head' || member.role === 'ceo'));
      if (!isLeadership) {
        alert("Access Denied: Only the CEO, Team Heads, or Vice Heads can take action on tasks.");
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
      const currentReg = safeSession.getItem('aeris_auth_reg');
      const member = MEMBERS_DATABASE[currentReg];
      const isLeadership = currentRole === 'head' || (member && (member.role === 'head' || member.role === 'vice_head' || member.role === 'ceo'));
      if (!isLeadership) {
        alert("Access Denied: Only the CEO, Team Heads, or Vice Heads can delete tasks.");
        return;
      }
      const id = e.currentTarget.dataset.id;
      let tasks = getTasks();
      tasks = tasks.filter(t => t.id !== id);
      saveTasks(tasks);
      deleteTaskFromCloud(id);
      renderTasks();
    }"""

if old_task_actions in content:
    content = content.replace(old_task_actions, new_task_actions, 1)
    print("Replaced handleTaskAction and handleTaskDelete.")
else:
    print("Warning: old_task_actions not matched!")

# -------------------------------------------------------------
# 5. Update openTaskModal to display meeting type and policy
# -------------------------------------------------------------
old_modal_dept = """      // Capitalize department
      const deptLabels = {
        'mechanical': isFrenchUser() ? 'Mécanique' : 'Mechanical',
        'electrical': isFrenchUser() ? 'Électrique' : 'Electrical',
        'software': isFrenchUser() ? 'Logiciel' : 'Software',
        'non-technical': 'TDR & Marketing'
      };
      modalTaskDept.textContent = deptLabels[task.department] || task.department;
      modalTaskDept.className = `task-modal__dept-badge task-modal__dept-badge--${task.department}`;"""

new_modal_dept = """      // Capitalize department & Type
      const deptLabels = {
        'mechanical': isFrenchUser() ? 'Mécanique' : 'Mechanical',
        'electrical': isFrenchUser() ? 'Électrique' : 'Electrical',
        'software': isFrenchUser() ? 'Logiciel' : 'Software',
        'non-technical': 'TDR & Marketing'
      };
      const typePrefix = task.type === 'meeting' ? '📅 Meeting • ' : '📋 Task • ';
      modalTaskDept.textContent = typePrefix + (deptLabels[task.department] || task.department);
      modalTaskDept.className = `task-modal__dept-badge task-modal__dept-badge--${task.department}`;"""

if old_modal_dept in content:
    content = content.replace(old_modal_dept, new_modal_dept, 1)
    print("Replaced modalTaskDept in openTaskModal.")
else:
    print("Warning: old_modal_dept not matched!")

# -------------------------------------------------------------
# 6. Update renderProgressTracker (table headers, cells, metrics)
# -------------------------------------------------------------
old_tracker_code = """      // 1. Build table headers
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

new_tracker_code = """      // 1. Build table headers
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

if old_tracker_code in content:
    content = content.replace(old_tracker_code, new_tracker_code, 1)
    print("Replaced renderProgressTracker table headers and cell rendering.")
else:
    print("Warning: old_tracker_code not matched!")

# -------------------------------------------------------------
# 7. Update handleEvalChange to handle meeting attendance logging
# -------------------------------------------------------------
old_handle_eval = """    // Handles evaluation changes and triggers email alerts
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

new_handle_eval = """    // Handles evaluation changes and triggers email alerts
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

if old_handle_eval in content:
    content = content.replace(old_handle_eval, new_handle_eval, 1)
    print("Replaced handleEvalChange.")
else:
    print("Warning: old_handle_eval not matched!")

# -------------------------------------------------------------
# 8. Update Leaderboard score calculation for meetings & deductions
# -------------------------------------------------------------
old_leaderboard_calc = """          const tierCounts = {};
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

new_leaderboard_calc = """          const tierCounts = {};
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

if old_leaderboard_calc in content:
    content = content.replace(old_leaderboard_calc, new_leaderboard_calc, 1)
    print("Replaced Leaderboard score calculation.")
else:
    print("Warning: old_leaderboard_calc not matched!")

# -------------------------------------------------------------
# 9. Update Task Form visibility check for Head, Vice Head, CEO
# -------------------------------------------------------------
old_perm_check = """          const regNum = safeSession.getItem('aeris_auth_reg');
          const member = MEMBERS_DATABASE[regNum];
          const isHead = member && (member.role === 'head' || member.role === 'ceo');
          taskForm.style.display = isHead ? 'block' : 'none';"""

new_perm_check = """          const regNum = safeSession.getItem('aeris_auth_reg');
          const member = MEMBERS_DATABASE[regNum];
          const isLeadership = member && (member.role === 'head' || member.role === 'vice_head' || member.role === 'ceo');
          taskForm.style.display = isLeadership ? 'block' : 'none';"""

if old_perm_check in content:
    content = content.replace(old_perm_check, new_perm_check, 1)
    print("Replaced task form visibility permission check.")
else:
    print("Warning: old_perm_check not matched!")

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Finished applying dashboard.html updates.")
