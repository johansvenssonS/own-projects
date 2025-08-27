export default class Router extends HTMLElement {
  constructor() {
      super();

      this.currentRoute = "";

      this.allRoutes = {
          "": {
              view: "<landing-view></landing-view>",
              name: "start",
          },
          "project": {
              view: "<landing-view></landing-view>",
              name: "hejhej",
          }
  }     
}

  get routes() {
      return this.allRoutes;
  }

    // connect component
    connectedCallback() {
        window.addEventListener('hashchange', () => {
            this.resolveRoute();
        });

        this.resolveRoute();
    }

      resolveRoute() {
      this.currentRoute = location.hash.replace("#", "");

      this.render();
  }

  render() {
      this.innerHTML = this.routes[this.currentRoute]?.view || "<not-found></not-found>";
  }
}