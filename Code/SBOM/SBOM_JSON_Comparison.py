#import the json library
import json

# Open the Json format SBOM files, here we are considering Syft and Blackduck and sbom in cycloneDX format
with open('sbom_cdx_syft_reponame.json', 'r') as syft_sbom_file:
    syft_sbom = json.load(syft_sbom_file)

with open('sbom_cdx_bd_reponame.json', 'r') as bd_sbom_file:
    bd_sbom = json.load(bd_sbom_file)

# THis function handles missing fields, ensuring they won’t cause errors by returning an empty list or dictionary if a field is missing in one of the SBOMs.
def get_field(data, field):
    return data.get(field, [])

# Compare the meta data of two files
def metadata_comparison(syft, blackduck):
    syft_metadata = syft.get("metadata", {})
    blackduck_metadata = blackduck.get("metadata", {})
    print("Metadata Comparison:")
    print(f"Syft: {len(syft_metadata)} metadata fields")
    print(f"BlackDuck: {len(blackduck_metadata)} metadata fields")

# Component comparison by matching on common fields like 'name' and 'version'
def components_comparison(syft, blackduck):
    syft_components = get_field(syft, "components")
    blackduck_components = get_field(blackduck, "components")
    syft_component_names = {comp['name']: comp.get('version') for comp in syft_components}
    blackduck_component_names = {comp['name']: comp.get('version') for comp in blackduck_components}

    print("\nComponent Comparison:")
    print(f"Syft: {len(syft_components)} components")
    print(f"BlackDuck: {len(blackduck_components)} components")

    # Compare and get info on which components are in one but not the other
    only_in_syft = set(syft_component_names) - set(blackduck_component_names)
    only_in_blackduck = set(blackduck_component_names) - set(syft_component_names)

    print(f"Components only in Syft: {len(only_in_syft)}")
    print(f"Components only in BlackDuck: {len(only_in_blackduck)}")

# Compare vulnerabilities
def vulnerabilities_comparison(syft, blackduck):
    syft_vulnerabilities = get_field(syft, "vulnerabilities")
    blackduck_vulnerabilities = get_field(blackduck, "vulnerabilities")
    
    print("\nVulnerability Comparison:")
    print(f"Syft: {len(syft_vulnerabilities)} vulnerabilities")
    print(f"BlackDuck: {len(blackduck_vulnerabilities)} vulnerabilities")

# Compare dependencies
def dependencies_comparison(syft, blackduck):
    syft_dependencies = get_field(syft, "dependencies")
    blackduck_dependencies = get_field(blackduck, "dependencies")
    
    print("\nDependency Comparison:")
    print(f"Syft: {len(syft_dependencies)} dependencies")
    print(f"BlackDuck: {len(blackduck_dependencies)} dependencies")

# Call the functions to perform comparison
metadata_comparison(syft_sbom , bd_sbom)
components_comparison(syft_sbom , bd_sbom)
vulnerabilities_comparison(syft_sbom ,bd_sbom)
dependencies_comparison(syft_sbom , bd_sbom)
