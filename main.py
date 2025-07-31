from haystack import Pipeline
from haystack.components.converters import TikaDocumentConverter

from FieldExtractor import FieldExtractor


converter = TikaDocumentConverter()

fieldExtractor = FieldExtractor()

paths = ['files/bt_invoice_template_1.pdf']

pipeline = Pipeline()

pipeline.add_component("converter", converter)
pipeline.add_component("extractor", fieldExtractor)

pipeline.connect("converter","extractor")


response  = pipeline.run({"converter": {"sources": paths}})

print(response)