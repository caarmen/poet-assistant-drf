# ThesaurusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listThesaurusEntrys**](ThesaurusApi.md#listThesaurusEntrys) | **GET** /thesaurus/ | 


<a name="listThesaurusEntrys"></a>
# **listThesaurusEntrys**
> inline_response_200_1 listThesaurusEntrys(page, word)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **Integer**| A page number within the paginated result set. | [optional] [default to null]
 **word** | **String**| A search term. | [optional] [default to null]

### Return type

[**inline_response_200_1**](../Models/inline_response_200_1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

