const express = require("express");
const cors = require("cors");
const algoliaMiddleware = require("./middleware");
const { DEPLOY_HOST, PORT } = require("./constant");

const app = express();

app.use(
  cors({
    origin: DEPLOY_HOST || `http://localhost:${PORT}`,
    methods: "GET,HEAD,PUT,PATCH,POST,DELETE",
    credentials: true,
  })
);
app.use(express.json());

/**
 * @swagger
 * components:
 *   schemas:
 *     SearchResult:
 *       type: object
 *
 *
 * /search:
 *   get:
 *     summary: Search in Algolia
 *     description: Search in Algolia using the provided query
 *     parameters:
 *       - in: query
 *         name: query
 *         required: true
 *         schema:
 *           type: string
 *         description: The search query
 *     responses:
 *       200:
 *         description: Successful search
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/SearchResult'
 *       500:
 *         description: Internal Server Error
 */
app.get("/search", algoliaMiddleware, async (req, res, next) => {
  if (!req.algoliaIndex) {
    res.status(400).send({ error: "algoliasearch index not found" });
  }
  const query = req.query.query;
  const result = await req.algoliaIndex.search(query);
  res.json(result);
});

module.exports = app;
