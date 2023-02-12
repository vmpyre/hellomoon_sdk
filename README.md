# Hello Moon Python SDK 

Python SDK for interacting with the [Official HelloMoon APIs - https://hellomoon.readme.io/](https://hellomoon.readme.io/).

## Installation

### Installing Using PIP (Recommended)
```python
pip install hellomoon
```

### Installing from Source

1. Clone the repository: `git clone https://github.com/vmpyre/hellomoon_sdk.git`

2. Change into the project directory: `cd hellomoon_sdk`

3. Install the dependencies: `pip install -r requirements.txt`

## Usage

First, import the SDK's classes for the APIs you'd like to use. 
```python
>> from hellomoon import NFTSummary
```
Then, create instances of the classes to interact with the corresponding API endpoints (in this case the NFT class):
```python
>> nft_api = NFT("<API_KEY_HERE>")
```
*Generate your API Key from here: https://hellomoon.readme.io/reference/get-your-api-key*

For example, you can use the `collection_stats()` method of the `NFTSummary` class to retrieve descriptive statistics of NFT collections:
```python
>> solana_monkey_business = "d515305e2b1de0026b5bf49fbb12e107
>> nft_api.collection_stats(helloMoonCollectionId=solana_monkey_business)
```
*That's it!* 

Response:
```json
{
  "data": [
    {
      "name": "Solana Monkey Business",
      "helloMoonCollectionId": "d515305e2b1de0026b5bf49fbb12e107",
      "slug": "solana-monkey-business",
      "supply": "5000",
      "currentOwnerCount": "2790",
      "avgPriceSol": "232.073169",
      "volume24Hr": "1856.585355",
      "volumeChange24Hr": "0.511200",
      "marketCapSol": "1158741.332817",
      "averageWashScore": "7.0574",
      "listingCount": "366",
      "mintPriceMode": null,
      "narrative": null
    }
  ],
  "paginationToken": "eyJuYW1lIjoiU29sYW5hIE1vbmtleSBCdXNpbmVzcyIsImhlbGxvTW9vbkNvbGxlY3Rpb25JZCI6ImQ1MTUzMDVlMmIxZGUwMDI2YjViZjQ5ZmJiMTJlMTA3In0="
}
```

The SDK provides functionality for interacting with all endpoints mentioned here: https://hellomoon.readme.io/ 

## Documentation
You can view the class methods below:
### NFT
- [collection_candlesticks()](https://hellomoon.readme.io/reference/post_v0-nft-collection-floorprice-candlesticks)
- [collection_mint_mapping()](https://hellomoon.readme.io/reference/post_v0-nft-collection-mints-1)
- [collection_name_mapping()](https://hellomoon.readme.io/reference/post_v0-nft-collection-name-1)
- [collection_volatility()](https://hellomoon.readme.io/reference/post_v0-nft-collection-volatility)
- [listing_status()](https://hellomoon.readme.io/reference/post_v0-nft-listing-status-1)
- [nft_listings()](https://hellomoon.readme.io/reference/post_v0-nft-listings-1)
- [metaplex_metadata()](https://hellomoon.readme.io/reference/post_v0-nft-mint-information-1)
- [mints_by_owner()](https://hellomoon.readme.io/reference/post_v0-nft-mints-by-owner-1)
- [primary_sales()](https://hellomoon.readme.io/reference/post_v0-nft-sales-primary-1)
- [secondary_sales()](https://hellomoon.readme.io/reference/post_v0-nft-sales-secondary-1)

### NFTSummary
- [collection_daily_sales_stats()](https://hellomoon.readme.io/reference/post_v0-nft-collection-daily-sales-stats)
- [collection_listing_stats()](https://hellomoon.readme.io/reference/post_v0-nft-collection-listing-1)
- [collection_overlap()](https://hellomoon.readme.io/reference/post_v0-nft-collection-overlap-1)
- [cumulative_nft_owners_over_time()](https://hellomoon.readme.io/reference/post_v0-nft-collection-ownership-cumulative-1)
- [collection_current_owners()](https://hellomoon.readme.io/reference/post_v0-nft-collection-ownership-current-1)
- [collection_distinct_owners_over_time()](https://hellomoon.readme.io/reference/post_v0-nft-collection-ownership-historical-1)
- [collection_holding_period()](https://hellomoon.readme.io/reference/post_v0-nft-collection-ownership-holding-period-1)
- [collection_top_holders()](https://hellomoon.readme.io/reference/post_v0-nft-collection-ownership-top-holders-1)
- [collection_program_usage()](https://hellomoon.readme.io/reference/post_v0-nft-collection-program-usage-1)
- [collection_stats_with_floor_price()](https://hellomoon.readme.io/reference/post_v0-nft-collection-stats-1)
- [collection_mint_stats()](https://hellomoon.readme.io/reference/post_v0-nft-collection-stats-primary-sales-1)
- [collection_washtrading_index()](https://hellomoon.readme.io/reference/post_v0-nft-collection-washtrading-1)
- [marketplace_stats()](https://hellomoon.readme.io/reference/post_v0-nft-market-stats-1)
- [market_sales_over_time()](https://hellomoon.readme.io/reference/post_v0-nft-sales-per-market-daily-1)


*See the Official Hello Moon documentation for additional information: https://hellomoon.readme.io/*

## Contribution
Feel free to open issues, pull requests and submit feedback. We appreciate your help!

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Thanks to the Hello Moon team for providing an amazing product.

## Disclaimer
The developer is not responsible for any errors or issues that may occur when using this SDK. Use at your own risk and feel free to report issues.

