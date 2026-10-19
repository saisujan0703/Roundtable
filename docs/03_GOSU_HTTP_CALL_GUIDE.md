# Gosu Outbound HTTP & REST Call Guide

> **Target Codebase**: Guidewire PolicyCenter 10.2.1 (`project-version=10.2.1.1711`, Platform `10.201.1`, Gosu `1.14.26`, Amazon Corretto JDK 11)  
> **Source Directory**: `C:\GW10\PolicyCenter\modules\configuration`  
> **Generated Documentation**: `C:\Users\Student\Documents\roundtable\docs\03_GOSU_HTTP_CALL_GUIDE.md`

---

## 1. Overview: Outbound HTTP Capabilities in Gosu

Gosu runs on the JVM and seamlessly interoperates with Java classes. In PolicyCenter 10, outbound HTTP calls to an external REST service (such as a Python FastAPI service) can be made using three distinct approaches verified in the PolicyCenter codebase:

| Client Library | Verification in Codebase | Recommended Use |
| :--- | :--- | :--- |
| **Apache HttpComponents (HttpClient 4.5.x)** | **Verified**: `SmartCommsRestClient.gs` | **Recommended**: Rich connection pooling, JSON request bodies, header handling |
| **`java.net.HttpURLConnection`** | **Verified**: `HttpURLConnectionRequestHandler.gs` | Standard JDK without external dependencies |
| **`java.net.http.HttpClient` (Java 11)** | **Verified**: Runtime is Amazon Corretto JDK 11 (`jdk11.0.17_8`) | Clean modern Java 11 fluent API |

---

## 2. Real Codebase Examples

### Codebase Example 1: `SmartCommsRestClient.gs` (Apache HttpComponents)
Location: `modules/configuration/gsrc/gw/integration/document/production/smartcomms/client/SmartCommsRestClient.gs`

This is the primary production REST client pattern in PolicyCenter 10:
* **Imports** (Lines 10–19):
  ```gosu
  uses org.apache.http.HttpHeaders
  uses org.apache.http.client.HttpClient
  uses org.apache.http.client.methods.HttpUriRequest
  uses org.apache.http.client.methods.RequestBuilder
  uses org.apache.http.entity.ContentType
  uses org.apache.http.entity.StringEntity
  uses org.apache.http.impl.client.HttpClientBuilder
  ```
* **Client Creation** (Lines 37–42):
  ```gosu
  _client = HttpClientBuilder
      .create()
      .setMaxConnTotal(config.MaxTotalConns)
      .setMaxConnPerRoute(config.MaxConnPerRoute)
      .build()
  ```
* **POST Request Execution** (Lines 103–120):
  ```gosu
  var requestEntity = new StringEntity(jsonString)
  requestEntity.setContentType(ContentType.APPLICATION_JSON.MimeType)

  var request = RequestBuilder
      .post()
      .setUri(uri)
      .setEntity(requestEntity)
      .setHeader(HttpHeaders.CONTENT_TYPE, ContentType.APPLICATION_JSON.MimeType)
      .setHeader(HttpHeaders.ACCEPT, ContentType.APPLICATION_JSON.MimeType)
      .build()

  var response = _client.execute(request)
  ```

---

### Codebase Example 2: `HttpURLConnectionRequestHandler.gs` (Java Standard Library)
Location: `modules/configuration/gsrc/gw/plugin/geocode/impl/HttpURLConnectionRequestHandler.gs` (Lines 28–35)

```gosu
uses java.net.HttpURLConnection
uses java.net.URL

var request = new URL(hostName + url)
var client = request.openConnection() as HttpURLConnection
client.setRequestMethod("GET")
client.setConnectTimeout(timeout)
client.setReadTimeout(timeout)
```

And reading the response stream (from `HttpURLConnectionPendingResult.gs`, lines 28–42):
```gosu
var statusCode = client.getResponseCode()
using (var stream = new java.io.BufferedInputStream(client.getInputStream())) {
  // read stream
}
```

---

## 3. JSON Serialization / Deserialization in PolicyCenter

Three JSON parsers are verified in this codebase:

1. **Jackson (`com.fasterxml.jackson.databind.ObjectMapper`)**:
   - Verified in: `modules/configuration/gsrc/gw/plugin/geocode/impl/BingMapUtils.gs` (Lines 26–35)
   ```gosu
   uses com.fasterxml.jackson.databind.ObjectMapper
   uses com.fasterxml.jackson.databind.DeserializationFeature

   var mapper = new ObjectMapper().configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false)
   var myObj = mapper.readValue(jsonStream, MyClass)
   var jsonString = mapper.writeValueAsString(myObj)
   ```

2. **Guidewire `gw.api.json.JsonObject`**:
   - Verified in: `modules/configuration/gsrc/gw/web/payment/demo/CollectCreditCardPopupHelper.gs` (Lines 2, 27–31)
   ```gosu
   uses gw.api.json.JsonObject

   var json = new JsonObject()
   json.put("briefId", "BR-101")
   json.put("status", "Approved")
   ```

3. **`org.json.JSONObject`**:
   - Bundled in PolicyCenter classpath.

---

## 4. Production-Ready Gosu REST Client for Python FastAPI

Below is a complete, production-ready Gosu client class designed to communicate with the Roundtable Python FastAPI backend (`http://localhost:8000` or configurable endpoint).

**File Target**: `modules/configuration/gsrc/roundtable/client/RoundtableApiClient.gs`

```gosu
package roundtable.client

uses org.apache.http.client.methods.RequestBuilder
uses org.apache.http.impl.client.HttpClientBuilder
uses org.apache.http.entity.StringEntity
uses org.apache.http.entity.ContentType
uses org.apache.http.HttpHeaders
uses org.apache.http.client.config.RequestConfig
uses org.apache.http.util.EntityUtils
uses com.fasterxml.jackson.databind.ObjectMapper
uses com.fasterxml.jackson.databind.JsonNode
uses gw.api.system.PCLoggerCategory
uses org.slf4j.Logger
uses java.lang.Exception

/**
 * REST API Client for communicating between Guidewire PolicyCenter and the
 * external Roundtable Python FastAPI service.
 */
@Export
class RoundtableApiClient {

  private static final var LOGGER : Logger = PCLoggerCategory.INTEGRATION
  private var _baseUrl : String
  private var _timeoutMs : int

  /**
   * Initializes the client with default or environment-configured settings.
   */
  construct() {
    // Read from environment variable or system property, fallback to default FastAPI port
    _baseUrl = System.getProperty("roundtable.api.url") 
        ?: System.getenv("ROUNDTABLE_API_URL") 
        ?: "http://localhost:8000"
    _timeoutMs = 15000 // 15 seconds default timeout
  }

  construct(baseUrl : String, timeoutMs : int) {
    _baseUrl = baseUrl
    _timeoutMs = timeoutMs
  }

  /**
   * Builds an Apache HttpClient configured with connection and read timeouts.
   */
  private function createHttpClient() : org.apache.http.client.HttpClient {
    var requestConfig = RequestConfig.custom()
        .setConnectTimeout(_timeoutMs)
        .setSocketTimeout(_timeoutMs)
        .setConnectionRequestTimeout(_timeoutMs)
        .build()

    return HttpClientBuilder.create()
        .setDefaultRequestConfig(requestConfig)
        .build()
  }

  /**
   * Performs an outbound GET request to retrieve brief details or suggestions from FastAPI.
   *
   * @param endpoint Relative path (e.g. "/api/v1/briefs/BR-101")
   * @return Parsed JsonNode containing response data
   */
  public function get(endpoint : String) : JsonNode {
    var client = createHttpClient()
    var targetUrl = _baseUrl + endpoint
    LOGGER.info("RoundtableApiClient: Outbound GET to " + targetUrl)

    var request = RequestBuilder.get()
        .setUri(targetUrl)
        .setHeader(HttpHeaders.ACCEPT, ContentType.APPLICATION_JSON.MimeType)
        .build()

    try {
      var response = client.execute(request)
      var statusCode = response.getStatusLine().getStatusCode()
      var entity = response.getEntity()
      var responseBody = entity != null ? EntityUtils.toString(entity, "UTF-8") : ""

      if (statusCode < 200 or statusCode >= 300) {
        LOGGER.error("Roundtable API returned error status " + statusCode + ": " + responseBody)
        throw new Exception("Roundtable API error (HTTP " + statusCode + "): " + responseBody)
      }

      var mapper = new ObjectMapper()
      return mapper.readTree(responseBody)
    } catch (e : Exception) {
      LOGGER.error("Failed to execute GET against Roundtable API: " + e.Message, e)
      throw e
    }
  }

  /**
   * Performs an outbound POST request with JSON payload to FastAPI.
   *
   * @param endpoint Relative path (e.g. "/api/v1/briefs/generate")
   * @param jsonPayload Raw JSON string payload
   * @return Parsed JsonNode containing response data
   */
  public function post(endpoint : String, jsonPayload : String) : JsonNode {
    var client = createHttpClient()
    var targetUrl = _baseUrl + endpoint
    LOGGER.info("RoundtableApiClient: Outbound POST to " + targetUrl)

    var requestEntity = new StringEntity(jsonPayload, ContentType.APPLICATION_JSON)
    var request = RequestBuilder.post()
        .setUri(targetUrl)
        .setEntity(requestEntity)
        .setHeader(HttpHeaders.CONTENT_TYPE, ContentType.APPLICATION_JSON.MimeType)
        .setHeader(HttpHeaders.ACCEPT, ContentType.APPLICATION_JSON.MimeType)
        .build()

    try {
      var response = client.execute(request)
      var statusCode = response.getStatusLine().getStatusCode()
      var entity = response.getEntity()
      var responseBody = entity != null ? EntityUtils.toString(entity, "UTF-8") : ""

      if (statusCode < 200 or statusCode >= 300) {
        LOGGER.error("Roundtable API returned error status " + statusCode + ": " + responseBody)
        throw new Exception("Roundtable API error (HTTP " + statusCode + "): " + responseBody)
      }

      var mapper = new ObjectMapper()
      return mapper.readTree(responseBody)
    } catch (e : Exception) {
      LOGGER.error("Failed to execute POST against Roundtable API: " + e.Message, e)
      throw e
    }
  }

  /**
   * Calls the Python FastAPI endpoint to generate a new AI-assisted brief.
   *
   * @param title Proposed product title
   * @param targetLine Target line of business (e.g. "PersonalAuto", "CommercialProperty")
   * @param prompt User prompt / requirements description
   * @return Parsed JSON object from FastAPI
   */
  public function requestNewBrief(title : String, targetLine : String, prompt : String) : JsonNode {
    var mapper = new ObjectMapper()
    var payloadMap : java.util.Map<String, Object> = {
      "title" -> title,
      "target_line" -> targetLine,
      "prompt" -> prompt
    }
    var jsonString = mapper.writeValueAsString(payloadMap)
    return post("/api/v1/briefs/generate", jsonString)
  }

  /**
   * Notifies the FastAPI service of an approval status change in PolicyCenter.
   */
  public function notifyApproval(briefPublicId : String, teamName : String, status : String) {
    var mapper = new ObjectMapper()
    var payloadMap : java.util.Map<String, Object> = {
      "brief_id" -> briefPublicId,
      "team" -> teamName,
      "status" -> status,
      "updated_by" -> gw.plugin.util.CurrentUserUtil.CurrentUser.User.Credential.UserName
    }
    var jsonString = mapper.writeValueAsString(payloadMap)
    post("/api/v1/briefs/" + briefPublicId + "/approvals", jsonString)
  }
}
```

---

## 5. Alternative: Pure Java 11 `java.net.http.HttpClient` Pattern

Since PolicyCenter 10 runs on Java 11, the built-in `java.net.http.HttpClient` is also usable without any third-party JARs:

```gosu
package roundtable.client

uses java.net.URI
uses java.net.http.HttpClient
uses java.net.http.HttpRequest
uses java.net.http.HttpResponse
uses java.time.Duration

@Export
class SimpleJava11Client {

  public static function getJson(url : String) : String {
    var client = HttpClient.newBuilder()
        .connectTimeout(Duration.ofSeconds(10))
        .build()

    var request = HttpRequest.newBuilder()
        .uri(URI.create(url))
        .header("Accept", "application/json")
        .GET()
        .timeout(Duration.ofSeconds(10))
        .build()

    var response = client.send(request, HttpResponse.BodyHandlers.ofString())
    return response.body()
  }

  public static function postJson(url : String, jsonBody : String) : String {
    var client = HttpClient.newBuilder()
        .connectTimeout(Duration.ofSeconds(10))
        .build()

    var request = HttpRequest.newBuilder()
        .uri(URI.create(url))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
        .timeout(Duration.ofSeconds(15))
        .build()

    var response = client.send(request, HttpResponse.BodyHandlers.ofString())
    return response.body()
  }
}
```

---

## 6. Integrating the Outbound Call into the Brief Workflow

To invoke the FastAPI service and populate a `RoundtableBrief` entity in PolicyCenter:

```gosu
uses roundtable.client.RoundtableApiClient
uses entity.RoundtableBrief
uses gw.transaction.Transaction

function generateBriefFromFastAPI(title : String, targetLine : String, prompt : String) : RoundtableBrief {
  var client = new RoundtableApiClient()
  var responseJson = client.requestNewBrief(title, targetLine, prompt)

  var brief : RoundtableBrief
  Transaction.runWithNewBundle(\bundle -> {
    brief = new RoundtableBrief(bundle)
    brief.Title = responseJson.get("title")?.asText() ?: title
    brief.ProductSummary = responseJson.get("summary")?.asText()
    brief.TargetLineCode = targetLine
    brief.EvidenceText = responseJson.get("evidence")?.asText()
    brief.CompetitorComparison = responseJson.get("competitor_comparison")?.asText()
    brief.DirectionalEstimates = responseJson.get("directional_estimates")?.asText()
    brief.Citations = responseJson.get("citations")?.asText()
    brief.CreatedDate = java.util.Date.CurrentDate
    brief.ClaimsStatus = TC_PENDINGREVIEW
    brief.ActuarialStatus = TC_PENDINGREVIEW
    brief.UnderwritingStatus = TC_PENDINGREVIEW
    brief.MarketingStatus = TC_PENDINGREVIEW
    brief.ComplianceStatus = TC_PENDINGREVIEW
    brief.PushedToApd = false
  })
  return brief
}
```
