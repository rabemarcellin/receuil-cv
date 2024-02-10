const axios = require("axios");
const { DATA_SOURCE_API } = require("./constant");

const getDataSource = async () => {
  const apiUrl = DATA_SOURCE_API;
  const response = await axios.get(apiUrl);
  return response.data;
};

module.exports = { getDataSource };
