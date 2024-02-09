const axios = require("axios");
const createWorker = require("tesseract.js").createWorker;
const { pdf } = require("pdf-to-img");
const fs = require("fs");
const path = require("path");

const assetsPath = path.join(__dirname, "assets");
if (!fs.existsSync(assetsPath)) {
  // If not, create the folder
  fs.mkdirSync(assetsPath);
}

const downloadImagesFromPDF = async (pdfPath, options = {}) => {
  try {
    const document = await pdf(pdfPath, options);

    const imagePaths = [];

    let counter = 1;
    for await (const image of document) {
      const imageName = `page${counter}.png`;
      const imagePath = path.join(assetsPath, imageName);

      // Download the image data from the remote URL
      const response = await axios({
        method: "get",
        url: image,
        responseType: "arraybuffer",
      });

      // Write the image data to the local file
      await fs.writeFile(imagePath, Buffer.from(response.data));
      imagePaths.push(imagePath);

      counter++;
    }

    return imagePaths;
  } catch (error) {
    throw error;
  }
};

const isPDF = (url) => {
  const urlPath = new URL(url).pathname;
  const fileExtension = path.extname(urlPath).toLowerCase();

  return fileExtension === ".pdf";
};

const extract = async (image_url) => {
  const worker = await createWorker("fra");
  const images = [];

  if (isPDF(image_url)) {
    try {
      const sources = await downloadImagesFromPDF(image_url);
      sources.forEach((image) => {
        images.push(image);
      });
    } catch (error) {
      console.error("Error downloading images from PDF:", error.message);
      return [];
    }
  } else {
    images.push(image_url);
  }

  const text_result = [];
  for (const image of images) {
    const ret = await worker.recognize(image);
    console.log(ret.data.text);
    text_result.push(ret.data.text);
  }

  await worker.terminate();
  return text_result.join(" ");
};

module.exports = { extract };
