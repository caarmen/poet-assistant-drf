# DefinitionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listDictionarys**](DefinitionsApi.md#listDictionarys) | **GET** /definitions/ | 
[**retrieveDictionary**](DefinitionsApi.md#retrieveDictionary) | **GET** /definitions/{rowid}/ | 


<a name="listDictionarys"></a>
# **listDictionarys**
> inline_response_200 listDictionarys(page, word)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **Integer**| A page number within the paginated result set. | [optional] [default to null]
 **word** | **String**| A search term. | [optional] [default to null]

### Return type

[**inline_response_200**](../Models/inline_response_200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="retrieveDictionary"></a>
# **retrieveDictionary**
> Dictionary retrieveDictionary(rowid, word)



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rowid** | **String**| A unique value identifying this dictionary. | [default to null]
 **word** | **String**| A search term. | [optional] [default to null]

### Return type

[**Dictionary**](../Models/Dictionary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

