import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

interface HeadersComponents {
  isClose: boolean;
}

let _headersComponents = {
  isClose: false
};

export default new Vuex.Store({
  state: {
    headersComponents: _headersComponents
  },
  getters: {
    headersComponentesIsClose: state => state.headersComponents.isClose
  },
  mutations: {
    setHeadersButtonClose(state) {
      state.headersComponents.isClose = !state.headersComponents.isClose;
    }
  },
  actions: {},
  modules: {}
});
