from dataclasses import dataclass, field

@dataclass
class URLSchema:
    _id:str
    url:str
    shortened_url:str