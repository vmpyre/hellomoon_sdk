from typing import List
from config.endpoints import MAINNET_BASE_URL
from helpers.utility import _make_post_request

class NFTSummary:
    def __init__(self, api_key: str):
        self.base_url = MAINNET_BASE_URL
        self.api_key = api_key

    # https://docs.hellomoon.io/reference/post_v0-nft-collection-daily-sales-stats
    def collection_daily_sales_stats(
        self, 
        helloMoonCollectionId: str=None, 
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/collection/listing"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://docs.hellomoon.io/reference/post_v0-nft-collection-listing
    def collection_listing_stats(
        self, 
        helloMoonCollectionId: str=None, 
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

    # https://docs.hellomoon.io/reference/post_v0-nft-collection-overlap
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

    # https://docs.hellomoon.io/reference/post_v0-nft-collection-ownership-cumulative
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

    # https://docs.hellomoon.io/reference/post_v0-nft-collection-ownership-current
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

    # https://docs.hellomoon.io/reference/post_v0-nft-collection-ownership-historical
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

    # https://docs.hellomoon.io/reference/post_v0-nft-collection-ownership-holding-period
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

    # https://docs.hellomoon.io/reference/post_v0-nft-collection-ownership-top-holders
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

    # https://docs.hellomoon.io/reference/post_v0-nft-collection-program-usage
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

    # https://docs.hellomoon.io/reference/post_v0-nft-collection-stats
    def collection_stats_with_floor_price(
        self, 
        helloMoonCollectionId: str=None,
        granularity: List[str]=None,
        startTime: int=None,
        limit: int=None,
        page: int=None,
        paginationToken: str=None
        ):
        
        arguments = locals()
        payload = {key: value for key, value in arguments.items() if value is not None and key != "self"}

        path = "/nft/collection/stats"
        url = self.base_url + path
        return _make_post_request(url, self.api_key, payload)

    # https://docs.hellomoon.io/reference/post_v0-nft-collection-stats-primary-sales
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

    # https://docs.hellomoon.io/reference/post_v0-nft-market-stats
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

    # https://docs.hellomoon.io/reference/post_v0-nft-sales-per-market-daily
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
