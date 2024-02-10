require("dotenv").config();

const DATA_SOURCE_API = process.env.DATA_SOURCE_API;
const ALGOLIA_INDEX = process.env.ALGOLIA_INDEX;
const ALGOLIA_APP_NAME = process.env.ALGOLIA_APP_NAME;
const ALGOLIA_SECRET = process.env.ALGOLIA_SECRET;
const PORT = process.env.PORT;
const DEPLOY_HOST = process.env.DEPLOY_HOST;

module.exports = {
  DATA_SOURCE_API,
  ALGOLIA_APP_NAME,
  ALGOLIA_INDEX,
  ALGOLIA_SECRET,
  PORT,
  DEPLOY_HOST,
};
