export default class Landing extends HTMLElement {
  // connect component
  connectedCallback() {
      this.innerHTML =    `
                           <projects-component></projects-component>

                           `;
  }
}