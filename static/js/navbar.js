/* navbar.js – injected into every page */
document.addEventListener('DOMContentLoaded', function () {
  const navHTML = `
  <nav class="arc-navbar navbar navbar-expand-lg">
    <div class="container-fluid px-4">
      <!-- LOGO -->
      <a href="{% url 'dashboard' %}" class="arc-logo me-3">
        <div class="logo-icon"><i class="bi bi-book-half"></i></div>
        ARC<span class="logo-dot">·</span>Reader
      </a>

      <!-- SEARCH (center) -->
      <div class="arc-search input-group mx-auto d-none d-md-flex" style="max-width:380px;">
        <input type="text" class="form-control" placeholder="Search documents, notes, highlights…"/>
        <button class="btn"><i class="bi bi-search"></i></button>
      </div>

      <!-- RIGHT CONTROLS -->
      <div class="d-flex align-items-center gap-2 ms-auto">
        <!-- Notifications -->
        <a href="#" class="nav-icon-btn">
          <i class="bi bi-bell"></i>
          <span class="nav-badge">3</span>
        </a>

        <!-- User Dropdown -->
        <div class="dropdown">
          <div class="arc-avatar" data-bs-toggle="dropdown" aria-expanded="false">RK</div>
          <ul class="dropdown-menu dropdown-menu-end shadow border-0" style="border-radius:14px; min-width:200px; margin-top:8px; border:1.5px solid var(--arc-border)!important;">
            <li class="px-3 py-2 border-bottom">
              <div class="fw-600 text-dark" style="font-size:.9rem;">Rahul Kumar</div>
              <div class="text-muted" style="font-size:.78rem;">rahul@example.com</div>
            </li>
            <li><a class="dropdown-item py-2" href="#"><i class="bi bi-person me-2 text-primary"></i>Profile</a></li>
            <li><a class="dropdown-item py-2" href="#"><i class="bi bi-gear me-2 text-primary"></i>Settings</a></li>
            <li><hr class="dropdown-divider my-1"/></li>
            <li><a class="dropdown-item py-2 text-danger" href="{% url 'login' %}"><i class="bi bi-box-arrow-right me-2"></i>Logout</a></li>
          </ul>
        </div>
      </div>
    </div>
  </nav>`;

  const placeholder = document.getElementById('arc-navbar');
  if (placeholder) placeholder.outerHTML = navHTML;
});
