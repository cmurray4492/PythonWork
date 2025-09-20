import nbformat
from nbconvert import HTMLExporter
from nbconvert.filters import widgetsdatatypefilter

# --- DISABLE the WidgetsDataTypeFilter completely ---
widgetsdatatypefilter.WidgetsDataTypeFilter.__call__ = lambda self, output, **kwargs: output
# ------------------------------------------------------

notebook_path = "CDM.ipynb"
output_html_path = "cdm.html"

# Load the notebook
nb = nbformat.read(notebook_path, as_version=4)

# Remove any remaining widget outputs
for cell in nb.cells:
    if cell.cell_type == "code" and "outputs" in cell:
        new_outputs = []
        for output in cell["outputs"]:
            # Skip widget-view outputs entirely
            if "data" in output and "application/vnd.jupyter.widget-view+json" in output["data"]:
                continue
            # Remove any widget metadata
            if "metadata" in output and "widgets" in output["metadata"]:
                output["metadata"].pop("widgets", None)
            new_outputs.append(output)
        cell["outputs"] = new_outputs

# Export to HTML
html_exporter = HTMLExporter()
html_exporter.template_name = "classic"

body, resources = html_exporter.from_notebook_node(nb)

# Save HTML
with open(output_html_path, "w", encoding="utf-8") as f:
    f.write(body)

print(f"Notebook exported successfully to {output_html_path} without widget errors.")
