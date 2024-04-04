const express = require("express");
const cors = require("cors");
const { DEPLOY_HOST, PORT } = require("./constant");
const { searchUsingAlgolia } = require("./vendor/algolia-search");

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
 *   post:
 *     summary: Search in Algolia
 *     description: Search in Algolia using the provided query
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               queries:
 *                 type: array
 *                 items:
 *                   type: string
 *             required:
 *               - queries
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
app.post("/search", async (req, res) => {
  const queries = req.body.queries;
  const result = await searchUsingAlgolia(queries)
  res.json(result);
});

module.exports = app;
