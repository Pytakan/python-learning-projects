from Resume_generator.user_info_module.Persone import Persone
from Resume_generator.format_convertor.Convertor_person_to_pdf import Convertor_person_to_pdf

class Format:
    def __init__(self, formate_name:str):
        self.supported_formats = ["pdf"]
        self.formate_name = formate_name.lower()
    def get_supported_formats(self):
        return self.supported_formats
    def is_supported(self):
        return self.formate_name in self.supported_formats
    
    def transform(self,path:str,persone:Persone):
        if (self.is_supported()):
                if (self.formate_name=="pdf"):
                    self.convert_to_pdf(path,persone)
        else:
            raise ValueError(f"Format '{self.formate_name}' is not supported for PDF conversion.")
    
        
    def convert_to_pdf(self, path:str, persone:Persone):
        converter = Convertor_person_to_pdf()
        converter.convert(persone, path)