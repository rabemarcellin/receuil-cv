require("dotenv").config();
const swaggerJSDoc = require("swagger-jsdoc");
const swaggerUI = require("swagger-ui-express");
const cors = require("cors");
const app = require("./app");

const PORT = process.env.PORT;

const options = {
  definition: {
    openapi: "3.0.0",
    info: {
      title: "CV Content Extractor API",
      version: "1.0.0",
    },
    servers: [
      {
        url: `http://localhost:${PORT}`,
      },
    ],
  },
  apis: ["./app.js"],
};

const swaggerSpec = swaggerJSDoc(options);

app.use(cors());
app.use("/", swaggerUI.serve, swaggerUI.setup(swaggerSpec));

app.listen(PORT, () => {
  console.log(`CV Content Extractor API listening on port ${PORT}`);
});
