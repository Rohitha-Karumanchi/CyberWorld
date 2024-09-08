## This holds code samples and information related to SBOM.
### SBOM_JSON_comparision.py: 
* Code to compare two SBOM files in CycloneDX (CDX) format
* Even if SBOMs are in CycloneDX (CDX) format, there might be structural differences in the way they populate the data, even though they adhere to the same specification.
##### Code focuses on comparing similarities in the overall structure, such as:
* metadata: Information about the SBOM generation, like tool version, author, and timestamp.
* components: The list of components (libraries, dependencies) detected in the application.
* dependencies: Relationships between the components.
* vulnerabilities: List of vulnerabilities associated with the components (if applicable).
##### Even if the details within these sections differ, using this code you can still:
* Count the number of components, vulnerabilities, and dependencies.
* Compare fields that are likely to be present in both SBOMs.
