export default class Projects extends HTMLElement {
  constructor(){
    super();
    this.projects = [];
    console.log("hej")
  }
  async connectedCallback(){
    this.projects = await this.getProjects();
    this.render();
  }
  async getProjects(){
    const response = await fetch('./src/projects.json')
    const result = await response.json();
    return result;
  }
  render(){
    this.innerHTML = `
      <h2>Mina Projekt</h2>
      <div class="project-container">
        ${this.projects.map(project => `
          <div class="project-card">
            <h3>${project.name}</h3>
            <img src="${project.image}" alt="${project.link}" class="project-image" />
            <div class="project-info">
              <p>${project.description}</p>
              <a href="#" class="project-link" data-link="${project.link}">Gå till projekt</a>
            </div>
          </div>
        `).join("")}
      </div>
    `;

    this.querySelectorAll('.project-link').forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        const url = link.dataset.link;
        window.open(url);
      });
    });

  }

}
