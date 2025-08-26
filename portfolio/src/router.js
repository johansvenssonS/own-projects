export default class Router extends HTMLElement {
  constructor() {
      super();

      this.currentRoute = "";

      this.allRoutes = {
          "": {
              view: "<start-view></start-view>",
              name: "start",
          },
          "project": {
              view: "<project-view></project-view>",
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
        const newRoute = location.hash.replace("#", "");
        this.currentRoute = newRoute;
    }
  }