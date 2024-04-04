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

    const queries = formatQueries(["query1", "query2", "query3"]); // Example queries
    
    // Perform multiple queries
    const { results } = await client.multipleQueries(queries);

    return results;
  } catch (error) {
    console.error("Error on save data source objects in Algolia:", error);
    throw error; // Propagate the error
  }
};

// Call initAlgolia and handle the promise rejection
searchUsingAlgolia().catch((error) => {
  console.error("Unhandled promise rejection:", error);
  process.exit(1); // Exit the process with an error code
});

module.exports = { searchUsingAlgolia };
