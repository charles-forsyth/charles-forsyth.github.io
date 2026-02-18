async function fetchRepos() {
  try {
    const response = await fetch(
      'https://api.github.com/users/charles-forsyth/repos?sort=updated',
    );
    if (!response.ok) {
      console.error('Failed to fetch repos');
      return;
    }
    const repos = await response.json();
    renderRepos(repos);

    const searchInput = document.getElementById('repo-search');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        const term = e.target.value.toLowerCase();
        const filtered = repos.filter((repo) =>
          repo.name.toLowerCase().includes(term),
        );
        renderRepos(filtered);
      });
    }
  } catch (error) {
    console.error('Error fetching repos:', error);
  }
}

function renderRepos(repos) {
  const container = document.getElementById('repo-list');
  if (!container) return;

  container.innerHTML = repos
    .map(
      (repo) => `
      <div class="repo-card">
        <h4><a href="${repo.html_url}" target="_blank">${repo.name}</a></h4>
        <p>${repo.description || 'No description available.'}</p>
        <div class="repo-meta">
          <span><i class="fas fa-star"></i> ${repo.stargazers_count}</span>
          <span><i class="fas fa-code"></i> ${repo.language || 'N/A'}</span>
        </div>
      </div>
    `,
    )
    .join('');
}

document.addEventListener('DOMContentLoaded', fetchRepos);
