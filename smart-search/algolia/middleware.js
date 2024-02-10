const { initAlgolia } = require("./vendor/algolia-search");

const algoliaMiddleware = async (req, res, next) => {
  const index = await initAlgolia();
  req.algoliaIndex = index;
  next();
};

module.exports = algoliaMiddleware;
