const algoliasearch = require("algoliasearch");
const {
  ALGOLIA_APP_NAME,
  ALGOLIA_INDEX,
  ALGOLIA_SECRET,
} = require("../constant");
const { getDataSource } = require("../utils");


const formatQueries = (queries) => {
  return queries.map(query => ({
    indexName: ALGOLIA_INDEX,
    query: query
  }))
}

const searchUsingAlgolia = async (queries) => {
  try {
    
    const client = algoliasearch(ALGOLIA_APP_NAME, ALGOLIA_SECRET);
    const index = client.initIndex(ALGOLIA_INDEX);
    const dataSource = await getDataSource();

    // Ensure each object has a unique identifier
    const objectsWithObjectID = dataSource.map((data) => ({
      ...data,
      objectID: data.id.toString(),
    }));

    // Save objects to Algolia
    await index.saveObjects(objectsWithObjectID);

    console.log("Index save objects successfully");

    const formattedQueries = formatQueries(queries); // Rename the variable to avoid conflict
    
    // Perform multiple queries
    const { results } = await client.multipleQueries(formattedQueries);


    return results.map(result => result.hits).reduce((acc, hits) => acc.concat(hits), []) || []
  } catch (error) {
    console.error("Error on save data source objects in Algolia:", error);
    throw error; // Propagate the error
  }
};


module.exports = { searchUsingAlgolia };
