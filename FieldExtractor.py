from typing import List
from haystack import Document, component


@component
class FieldExtractor:
 
    @component.output_types(result = any)
    def run(self, documents: List[Document]):
     
        # response with all files info extracted
        response = []
        for doc in documents:

            # text of a file
            data = {}
            text = doc.content
            subtotal = 0
            lines = text.splitlines()
            for line in lines:
                if line.lower().startswith("emitent:"):

                    # luam partea a doua de dupa ':' . 
                    data['emitent'] = line.split(':',1)[1].strip()
                elif line.lower().startswith("client:"):
                    data['client'] = line.split(':',1)[1].strip()
                
                elif line.lower().startswith("data:"):
                    data['data'] = line.split(':',1)[1].strip()

                elif 'factur' and ':' in line.lower():
                    data['invoice_number'] = line.split(':',1)[1].strip()

                elif line.lower().startswith("total"):
                    data['total'] = line.split()[-1]

                else:
                    parts = line.split()
                    if parts > 3:
                        subtotal += parts[-1]

            if int(data['total']) != subtotal:
                raise (Exception("Invoice faulty. Subtotal is not equal to total."))

            response.append(data)


        return {"response":response}

