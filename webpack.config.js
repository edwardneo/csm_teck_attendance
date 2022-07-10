const LodashModuleReplacementPlugin = require("lodash-webpack-plugin");
const path = require("path");
const plugins = [new LodashModuleReplacementPlugin()];

module.exports = (env, argv) => {
  const config = {
    entry: "./frontend/src/index.js",
    output: {
      path: path.resolve(__dirname, "./frontend/static/frontend/")
    },
    resolve: {
      extensions: [".tsx", ".ts", ".js", ".json"]
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          include: path.resolve(__dirname, "./frontend/src/"),
          use: {
            loader: "babel-loader"
          }
        },
        {
          test: /\.tsx?$/,
          exclude: /node_modules/,
          include: path.resolve(__dirname, "./frontend/src/"),
          use: {
            loader: "babel-loader"
          }
        },
        {
          test: /\.svg$/,
          include: [
            path.resolve(__dirname, "./frontend/static/frontend/"),
            path.resolve(__dirname, "./frontend/templates/frontend/")
          ],
          use: [
            {
              loader: "@svgr/webpack",
              // Always inline styles into svg attributes because <style> tags would violate our CSP
              options: { svgoConfig: { plugins: [{ inlineStyles: { onlyMatchedOnce: false } }] } }
            }
          ]
        }
      ]
    },
    watchOptions: {
      ignored: /node_modules/
    },
    plugins: plugins,
    externals: { react: "React", "react-dom": "ReactDOM" }
  };
  if (argv.mode === "development") {
    config.devtool = "eval-source-map";
  }
  return config;
};
