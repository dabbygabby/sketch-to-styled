import sketch from "sketch";
const fs = require("@skpm/fs");

export default function () {
  const doc = sketch.getSelectedDocument();
  const selectedLayers = doc.selectedLayers;
  const selectedCount = selectedLayers.length;

  if (selectedCount === 0) {
    sketch.UI.message("No layers are selected.");
  } else {
    try {
      var file =
        "~/Desktop/freelanceCode.nosync/sketch2Styled/sketch-to-styled/output/";
      const options = { formats: "json", output: file, overwriting: true };
      sketch.export(selectedLayers.layers[0], options);
      sketch.UI.alert("exported file", "check new json");
    } catch (err) {
      sketch.UI.alert("export file error", err.toString());
    }
  }
}
