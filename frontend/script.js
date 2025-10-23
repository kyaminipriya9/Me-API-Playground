const API_BASE = "http://127.0.0.1:8000";

// ---------------- Profile ----------------
fetch(`${API_BASE}/profile`)
  .then(res => res.json())
  .then(data => {
    document.getElementById("name").textContent = data.name;
    document.getElementById("email").textContent = data.email;
    document.getElementById("education").textContent = data.education;
    document.getElementById("mobile").textContent = data.mobile;
    document.getElementById("address").textContent = data.address;
  });

// ---------------- Links ----------------
fetch(`${API_BASE}/links`)
  .then(res => res.json())
  .then(data => {
    const ul = document.getElementById("links");
    data.forEach(l => {
      const li = document.createElement("li");
      li.innerHTML = `<a href="${l.url}" target="_blank" rel="noopener noreferrer">${l.type}</a>`;
      ul.appendChild(li);
    });
  });

// ---------------- Skills ----------------
let allSkills = [];
fetch(`${API_BASE}/skills`)
  .then(res => res.json())
  .then(data => {
    allSkills = data;
    renderSkills(allSkills);
  });

function renderSkills(skills) {
  const container = document.getElementById("skills");
  container.innerHTML = "";
  skills.forEach(s => {
    const span = document.createElement("span");
    span.textContent = s.skill;
    span.className = "skill-badge";
    span.onclick = () => fetchProjects(s.skill);
    container.appendChild(span);
  });
}

// ---------------- Projects ----------------
function fetchProjects(skill = "") {
  let url = `${API_BASE}/projects`;
  if (skill) url += `?skill=${skill}`;
  fetch(url)
    .then(res => res.json())
    .then(data => {
      const container = document.getElementById("projects");
      container.innerHTML = "";
      if (data.length === 0) container.innerHTML = "<p>No projects found.</p>";
      data.forEach(p => {
        const div = document.createElement("div");
        div.className = "item";
        div.innerHTML = `<strong>${p.title}</strong>: ${p.description} <br><a href="${p.link}" target="_blank" rel="noopener noreferrer">Link</a>`;
        container.appendChild(div);
      });
    });
}

// Initial load
fetchProjects();

// ---------------- Work ----------------
fetch(`${API_BASE}/work`)
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById("work");
    if (data.length === 0) container.innerHTML = "<p>No work experience.</p>";
    data.forEach(w => {
      const div = document.createElement("div");
      div.className = "item";
      div.innerHTML = `<strong>${w.company} (${w.role})</strong>: ${w.description} <br>${w.start_date} - ${w.end_date}`;
      container.appendChild(div);
    });
  });

// ---------------- Skill Filter Input ----------------
document.getElementById("skillFilter").addEventListener("input", e => {
  const skill = e.target.value;
  fetchProjects(skill);
});
