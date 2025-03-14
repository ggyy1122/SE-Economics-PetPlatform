import { createStore } from "vuex";

const store = createStore({
  state() {
    return {
      isLoggedIn: false,
    };
  },
  mutations: {
    setLoginStatus(state, status) {
      state.isLoggedIn = status;
    },
  },
  actions: {
    checkLoginStatus({ commit }) {
        console.log("checkLoginStatus 被调用了！"); // ✅ 看看有没有执行到这里
      fetch("http://127.0.0.1:8000/api/person/login_status/", {
        method: "GET",
        credentials: "include",
      })
        .then(response => response.json())
        .then(data => {
            console.log("Vuex isLoggedIn:", data.message === "用户已登录"); // ✅ 检查是否更新
          commit("setLoginStatus", data.message === "用户已登录");
        })
        .catch(() => {
          commit("setLoginStatus", false);
        });
    },
  },
});

export default store;
