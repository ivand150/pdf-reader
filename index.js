import { PdfReader } from "pdfreader";

let rows = {}; // indexed by y-position

const flushRows = () => {
  Object.keys(rows) // => array of y-positions (type: float)
    .sort((y1, y2) => parseFloat(y1) - parseFloat(y2)) // sort float positions
    .forEach((y) => console.log((rows[y] || []).join("")));
  rows = {}; // clear rows for next page
}

const getContent = async (src) => {
    new PdfReader().parseFileItems(src, (err, item) => {
        console.log(item)
        if (err) {
            console.error({ err });
          } else if (!item) {
            flushRows();
            console.log("END OF FILE");
          } else if (item.page) {
            flushRows(); // print the rows of the previous page
            console.log("PAGE:", item.page);
          } else if (item.text) {
            // accumulate text items into rows object, per line
            (rows[item.y] = rows[item.y] || []).push(item.text);
          }
    });
}

getContent("nomina2.pdf")