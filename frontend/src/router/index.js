import Vue from "vue";
import Router from "vue-router";
import Home from "./page/home.vue";
import History from "./page/history.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home
    }, 
    {
      path: "/history",
      name: "History",
      component: History
    }
  ]
});
