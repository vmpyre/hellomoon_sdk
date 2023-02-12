from typing import List
from config.endpoints import MAINNET_BASE_URL
from helpers.utility import _make_post_request

class NFTSummary:
    def __init__(self, api_key: str):
        self.base_url = MAINNET_BASE_URL
        self.api_key = api_key

    # https://hellomoon.readme.io/reference/post_v0-nft-collection-listing-1
    def collection_listing_stats(
        self, 
        helloMoonCollectionId: str, 
        blockId: int=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/collection/listing"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://hellomoon.readme.io/reference/post_v0-nft-collection-overlap-1
    def collection_overlap(
        self, 
        helloMoonCollectionId: str, 
        ownersOverlappings: int=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/collection/overlap"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://hellomoon.readme.io/reference/post_v0-nft-collection-ownership-cumulative-1
    def cumulative_nft_owners_over_time(
        self, 
        day: str, 
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/collection/ownership/cumulative"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://hellomoon.readme.io/reference/post_v0-nft-collection-ownership-current-1
    def collection_current_owners(
        self, 
        helloMoonCollectionId: str, 
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/collection/ownership/current"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://hellomoon.readme.io/reference/post_v0-nft-collection-ownership-historical-1
    def collection_distinct_owners_over_time(
        self, 
        helloMoonCollectionId: str, 
        numDistinct: int=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/collection/ownership/historical"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://hellomoon.readme.io/reference/post_v0-nft-collection-ownership-holding-period-1
    def collection_holding_period(
        self, 
        helloMoonCollectionId: str, 
        holdingPeriod: List[str]=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/collection/ownership/holding-period"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://hellomoon.readme.io/reference/post_v0-nft-collection-ownership-top-holders-1
    def collection_top_holders(
        self, 
        helloMoonCollectionId: str, 
        ownerAccount: str=None,
        amount: int=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        path = "/nft/collection/ownership/top-holders"
        url = self.base_url + path
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/collection/listing"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://hellomoon.readme.io/reference/post_v0-nft-collection-program-usage-1
    def collection_program_usage(
        self, 
        helloMoonCollectionId: str, 
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/collection/program-usage"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://hellomoon.readme.io/reference/post_v0-nft-collection-stats-1
    def collection_stats(
        self, 
        helloMoonCollectionId: str,
        volume24Hr: float=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/collection/stats"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://hellomoon.readme.io/reference/post_v0-nft-collection-stats-primary-sales-1
    def collection_mint_stats(
        self, 
        helloMoonCollectionId: str,
        latestMintBlockTime: int=None,
        numMinters: int=None,
        mintPrice: int=None,
        totalMintedBySmartMinters: int=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/collection/stats/primary-sales"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://hellomoon.readme.io/reference/post_v0-nft-collection-washtrading-1
    def collection_washtrading_index(
        self, 
        helloMoonCollectionId: str,
        index: int=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/collection/washtrading"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://hellomoon.readme.io/reference/post_v0-nft-market-stats-1
    def marketplace_stats(
        self, 
        market: List[str],
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/market-stats"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://hellomoon.readme.io/reference/post_v0-nft-sales-per-market-daily-1
    def market_sales_over_time(
        self, 
        market: List[str],
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/sales_per_market_daily"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)