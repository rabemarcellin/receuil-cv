const swaggerJSDoc = require("swagger-jsdoc");
const swaggerUI = require("swagger-ui-express");
const app = require("./app");
const { DEPLOY_HOST, PORT } = require("./constant");

const options = {
  definition: {
    openapi: "3.0.0",
    info: {
      title: "Smart Search Profile by AI Algolia Search API",
      version: "1.0.0",
    },
    servers: [
      {
        url: DEPLOY_HOST || `http://127.0.0.1:${PORT}`,
      },
    ],
  },
  apis: ["./app.js"],
};

const swaggerSpec = swaggerJSDoc(options);

app.use("/", swaggerUI.serve, swaggerUI.setup(swaggerSpec));

app.listen(PORT, () => {
  console.log("smart search api running {*_*}");
});
