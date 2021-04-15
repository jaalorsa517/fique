/* eslint-disable prettier/prettier */
const path = require("path");

module.exports = {
  transpileDependencies: [],
  chainWebpack: (config) => {
    config.plugin("html").tap((args) => {
      args[0].title = "Asomufi";
      return args;
    });
    const types = ["vue-modules", "vue", "normal-modules", "normal"];
    types.forEach((type) =>
      addStyleResource(config.module.rule("stylus").oneOf(type))
    );
  },
  pwa: {
    name: "My App",
    themeColor: "#4DBA87",
    msTileColor: "#000000",
    appleMobileWebAppCapable: "yes",
    appleMobileWebAppStatusBarStyle: "black",

    // configure the workbox plugin
    workboxPluginMode: "GenerateSW",
    workboxOptions: {
      swDest: "service-worker",
      skipWaiting: true
    }
  }
};

function addStyleResource(rule) {
  rule
    .use("style-resource")
    .loader("style-resources-loader")
    .options({
      patterns: [
        path.resolve(__dirname, "./src/styles/vars.styl"),
        path.resolve(__dirname, "./src/styles/mixins.styl")
      ]
    });
}
