from typing import List, Optional
from pydantic import BaseModel


class Product(BaseModel):
    title: str
    description: Optional[str] = None
    price: str
    images: Optional[List] = None

    class Config:
        schema_extra = {
            "example": [
                {
                    "description": "OpisNowa dostawa biżuterii z Włoch prosto z pracowni jubilerskiej z miasta Lido di Jesolo\n\nPiękny, męski sygnet z oczkiem z naturalnego szkła\n\n   kwaśna skała wylewna, złożona niemal wyłącznie ze szkliwa wulkanicznego, zawiera do 1% wody. Naturalne szkło powstaje w wyniku natychmiastowego stygnięcia magmy (lawy). Skład chemiczny (głównie dwutlenek krzemu) związany jest z typem lawy i obejmuje bardzo wiele form, od obsydianu ryolitowego po fonolitowy. Ulega rekrystalizacji, przyjmując kolor w zależności od aktualnej obecności pigmentu w chwili powstawania - w warunkach naturalnych dla przyrody oczywiście \n\nwykonany w znakomitej jakości z litej stali chirurgicznej o współczynniku gęstości 316L a następnie platerowanej prawdziwym srebrem próby 925 o grubości powłoki aż 15% grubości bazy czyli w tym przypadku stali nierdzewnej. \n   Całość została specjalnie wypolerowana oraz pokryta specjalnym lakierem jubilerskim \n\nTo piękny niepowtarzalny wzór z naturalnie powstałym w przyrodzie kamieniem - szkłem pełniącym role oczka\n\n• waga wyrobu razem z oczkiem 12,5 grama \n\n• platerowany srebrem - 15% bazy \n\n• próba srebra 925\n\n• oczko Obsidian Stone \n\n• dostępny każdy rozmiar \n\nJest to prawdziwy wyrób złotniczy który powstał we włoskiej pracowni stworzony zgodnie ze sztuką złotniczą. \n\nBiżuteria nie czarnieje, nie ściera się ani nie brudzi ponieważ srebro zarówno jak i stal chirurgiczna nie wchodzą w żadne reakcje z ciałem i są obojętne dla PH skóry człowieka\n\nSprzedaję w komplecie wraz \nz metką nominalną \npięknym zamykanym pudełkiem prezentowym \ndowodem zakupu\n\nOPCJE ZAKUPU:\n\nWysyłka \n\nZapraszam \n\n*zdjęcia oraz opis są mojego autorstwa i stanowią moją własność w myśl artykułu 305 ustawy o własności przemysłowej. Nie wyrażam zgody na kopiowanie, rozpowszechnianie oraz posługiwanie się",
                    "images": [
                        "https://storage.googleapis.com/sample-e9236.appspot.com/meski-sygnet-obsidian-platerowany-srebrem-pr9252cc2970344d1918decc6.jpeg"
                    ],
                    "title": "Męski sygnet Obsidian • platerowany srebrem pr925",
                    "price": "120",
                }
            ],
        }
