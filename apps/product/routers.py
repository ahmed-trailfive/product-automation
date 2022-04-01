from fastapi import APIRouter, Request, Depends
from typing import Dict, List
from apps.product.schema import Product
from apps.user.routers import User, get_current_active_user

import concurrent.futures
from apps.product.selenium.upload_product import Automation

router = APIRouter()


@router.get(
    "/get-all-collection-ids",
    description="Get all collection ids",
    response_model=Dict,
)
async def get_collections(
    request: Request, current_user: User = Depends(get_current_active_user)
) -> dict:
    collections = request.app.db.get_collections()
    return {num: collection.id for num, collection in enumerate(collections)}


@router.get(
    "/get-products-list",
    response_model=List[Product],
    description="Get all products from collection",
)
async def read_items(
    request: Request,
    current_user: User = Depends(get_current_active_user),
) -> List[Product]:

    collection = request.app.db.get_collections()
    ret_dict = []
    for i in collection:
        docs = request.app.db.get_documents(i.id)
        for doc in docs:
            product = doc.to_dict()
            ret_dict.append(product)
    return ret_dict


@router.get(
    "/get-products-by-collection-id/{collection_id}",
    response_model=List[Product],
    description="Use this endpoint to get all products of a specific collection",
)
async def get_products_by_collection_id(
    request: Request,
    collection_id: str,
    current_user: User = Depends(get_current_active_user),
) -> List[Product]:
    docs = request.app.db.get_documents(collection_id)
    ret_dict = []
    for doc in docs:
        product = doc.to_dict()
        ret_dict.append(product)
    return ret_dict


@router.get(
    "/upload-products-by-collection-id/{collection_id}/{max_threads}",
    description="Use this endpoint to get all products of a specific collection",
    response_description="Returns the list of the name of the products uploaded",
)
async def get_products_by_collection_id(
    request: Request,
    collection_id: str,
    max_threads: int = 2,
    current_user: User = Depends(get_current_active_user),
) -> List:
    docs = request.app.db.get_documents(collection_id)
    auto = Automation(request)

    ret_dict = []
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=max_threads,
    ) as executor:
        for doc in docs:
            product = doc.to_dict()
            title = product["title"]
            description = product["description"]
            price = product["price"]
            image = product["images"]
            executor.submit(auto.put_input_elements, title, description, price, image)
            ret_dict.append(title)

    return ret_dict
