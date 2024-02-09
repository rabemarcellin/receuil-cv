const express = require("express");
const { extract } = require("./utils");

const app = express();

app.use(express.json());

/**
 * @swagger
 * tags:
 *   name: Content Extraction
 *   description: API endpoints for content extraction
 */

/**
 * @swagger
 * path:
 *   /extract-text:
 *     get:
 *       summary: Extract text from an image
 *       tags: [Content Extraction]
 *       parameters:
 *         - in: query
 *           name: imageUrl
 *           schema:
 *             type: string
 *           description: URL of the image to extract text from
 *       responses:
 *         '200':
 *           description: Successful response with extracted text
 *           content:
 *             application/json:
 *               example:
 *                 extractedText: "This is the extracted text from the image."
 *         '400':
 *           description: Bad request if imageUrl is missing
 */
app.get("/extract-text", async (req, res, next) => {
  /**
   * @swagger
   * /extract-text:
   *   get:
   *     summary: Extract text from an image
   *     parameters:
   *       - in: query
   *         name: imageUrl
   *         required: true
   *         description: URL of the image to extract text from
   *         schema:
   *           type: string
   *     responses:
   *       '200':
   *         description: Successful response with extracted text
   *         content:
   *           application/json:
   *             example:
   *               extractedText: "This is the extracted text from the image."
   *       '400':
   *         description: Bad request if imageUrl is missing
   */

  const imageUrl = req.query.imageUrl;
  const text_result = await extract(imageUrl);

  /**
   * @swagger
   * /extract-text:
   *   get:
   *     responses:
   *       '200':
   *         content:
   *           application/json:
   *             example:
   *               extractedText: "This is the extracted text from the image."
   *       '400':
   *         description: Bad request if imageUrl is missing
   */
  res.json({ extractedText: text_result });
});

module.exports = app;
