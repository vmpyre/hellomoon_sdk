from typing import List
from config.endpoints import MAINNET_BASE_URL
from helpers.utility import _make_post_request

class NFT:
    def __init__(self, api_key: str):
        self.base_url = MAINNET_BASE_URL
        self.api_key = api_key

    # https://docs.hellomoon.io/reference/post_v0-nft-collection-floorprice-candlesticks
    def collection_candlesticks(
        self, 
        helloMoonCollectionId: str, 
        startTime: int=None,
        granularity: List[str]=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/collection/floorprice/candlesticks"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://docs.hellomoon.io/reference/post_v0-nft-collection-mints
    def collection_mint_mapping(
        self, 
        helloMoonCollectionId: str, 
        nftMint: str=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/collection/mints"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://docs.hellomoon.io/reference/post_v0-nft-collection-name
    def collection_name_mapping(
        self, 
        helloMoonCollectionId: str, 
        collectionName: str=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/collection/name"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://docs.hellomoon.io/reference/post_v0-nft-collection-volatility
    def collection_volatility(
        self, 
        helloMoonCollectionId: str, 
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/collection/volatility"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://docs.hellomoon.io/reference/post_v0-nft-listing-status
    def listing_status(
        self, 
        helloMoonCollectionId: str=None, 
        nftMint: str=None,
        isListed: bool=None,
        marketplace: List[str]=None,
        price: int=None,
        blockTime: int=None,
        seller: str=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/listing-status"
        url = self.base_url + path

        return _make_post_request(url, self.api_key, payload)

    # https://docs.hellomoon.io/reference/post_v0-nft-listings
    def nft_listings(
        self, 
        helloMoonCollectionId: str=None, 
        nftMint: str=None,
        instructionName: List[str]=None,
        transactionId: str=None,
        blockId: int=None,
        market: List[str]=None,
        blockTime: int=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/listings"
        url = self.base_url + path

        return _make_post_request(url, self.api_key, payload)

    # https://docs.hellomoon.io/reference/post_v0-nft-mint-information
    def metaplex_metadata(
        self, 
        nftMint: str=None, 
        nftCollectionMint: str=None,
        verifiedCreator: str=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/mint_information"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://docs.hellomoon.io/reference/post_v0-nft-mints-by-owner
    def mints_by_owner(
        self, 
        nftMint: str=None, 
        helloMoonCollectionId: str=None,
        ownerAccount: str=None,
        nftCollectionMint: str=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/mints-by-owner"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://docs.hellomoon.io/reference/post_v0-nft-sales-primary
    def primary_sales(
        self, 
        nftMint: str=None, 
        helloMoonCollectionId: str=None,
        transactionId: str=None,
        mintProgram: List[str]=None,
        payer: str=None,
        paymentMint: str=None,
        wallet: str=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/sales/primary"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://docs.hellomoon.io/reference/post_v0-nft-sales-secondary
    def secondary_sales(
        self, 
        nftMint: str=None, 
        helloMoonCollectionId: str=None,
        buyer: str=None,
        seller: str=None,
        marketplace: List[str]=None,
        price: float=None,
        blockTime: int=None,
        blockId: int=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/sales/secondary"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)
