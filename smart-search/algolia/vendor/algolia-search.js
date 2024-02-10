const algoliasearch = require("algoliasearch");
const {
  ALGOLIA_APP_NAME,
  ALGOLIA_INDEX,
  ALGOLIA_SECRET,
} = require("../constant");
const { getDataSource } = require("../utils");

const initAlgolia = async () => {
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
    return index;
  } catch (error) {
    console.error("Error on save data source objects in Algolia:", error);
    throw error; // Propagate the error
  }
};

// Call initAlgolia and handle the promise rejection
initAlgolia().catch((error) => {
  console.error("Unhandled promise rejection:", error);
  process.exit(1); // Exit the process with an error code
});

module.exports = { initAlgolia };
