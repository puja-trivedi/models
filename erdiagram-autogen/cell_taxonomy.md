```mermaid
erDiagram
Embedding {
    string id  
    string embedding_key  
    float embedding_matrix  
    iri_type iri  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
ProvActivity {

}
ProvEntity {

}
ExpressionMatrix {
    string id  
    uriList content_url  
    ExpressionMatrixType matrix_type  
    iri_type iri  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
Cluster {
    string id  
    string name  
    integer number_of_observations  
    iri_type iri  
    stringList type  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
ClusterSet {
    string id  
    string name  
    iri_type iri  
    stringList type  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
CellTypeTaxonomy {
    string id  
    string accession_id  
    uriList content_url  
    string title  
    string schema_version  
    string batch_condition  
    string dendrogram  
    string hierarchy  
    string mode  
    boolean filter  
    string cluster_algorithm  
    string cluster_info  
    string default_embedding  
    string cellannotation_schema  
    string quality_control_markers  
    iri_type iri  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
CellTypeTaxon {
    string id  
    string name  
    string accession_id  
    integer order  
    string cell_type_ontology_term_id  
    integer number_of_cells  
    iri_type iri  
    stringList type  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
CellTypeSet {
    string id  
    string name  
    integer order  
    CellTypeSetType cell_type_set_type  
    iri_type iri  
    stringList type  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
Cell {
    string id  
    string cluster_id  
    string load_id  
    string assay  
    string assay_ontology_term_id  
    string anatomical_region  
    string anatomical_region_ontology_term_id  
    string brain_region_ontology_term_id  
    SuspensionType suspension_type  
    boolean is_primary_data  
    iri_type iri  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}

Embedding ||--|o ProvEntity : "was_derived_from"
Embedding ||--|o ProvActivity : "was_generated_by"
Embedding ||--}o Attribute : "has attribute"
ProvActivity ||--|o ProvEntity : "used"
ProvEntity ||--|o ProvEntity : "was_derived_from"
ProvEntity ||--|o ProvActivity : "was_generated_by"
ExpressionMatrix ||--}o GeneAnnotation : "has_variable"
ExpressionMatrix ||--|o ProvEntity : "was_derived_from"
ExpressionMatrix ||--|o ProvActivity : "was_generated_by"
ExpressionMatrix ||--}o Attribute : "has attribute"
Cluster ||--|o ClusterSet : "part_of_set"
Cluster ||--}o CellTypeTaxon : "has_parent"
Cluster ||--|o ProvEntity : "was_derived_from"
Cluster ||--|o ProvActivity : "was_generated_by"
Cluster ||--}o Attribute : "has attribute"
ClusterSet ||--}o ExpressionMatrix : "was_derived_from"
ClusterSet ||--|o ProvActivity : "was_generated_by"
ClusterSet ||--}o Attribute : "has attribute"
CellTypeTaxonomy ||--}o ClusterSet : "was_derived_from"
CellTypeTaxonomy ||--}o Embedding : "has_embedding"
CellTypeTaxonomy ||--}o ExpressionMatrix : "has_expression_matrix"
CellTypeTaxonomy ||--|o ProvActivity : "was_generated_by"
CellTypeTaxonomy ||--}o Attribute : "has attribute"
CellTypeTaxon ||--|o CellTypeTaxon : "has_parent"
CellTypeTaxon ||--|o CellTypeSet : "part_of_set"
CellTypeTaxon ||--}o GeneAnnotation : "curated_markers_to_primates"
CellTypeTaxon ||--}o GeneAnnotation : "curated_markers_to_mouse"
CellTypeTaxon ||--|o ProvEntity : "was_derived_from"
CellTypeTaxon ||--|o ProvActivity : "was_generated_by"
CellTypeTaxon ||--}o Attribute : "has attribute"
CellTypeSet ||--|o CellTypeSet : "has_parent"
CellTypeSet ||--|o CellTypeTaxonomy : "part_of_taxonomy"
CellTypeSet ||--|o ProvEntity : "was_derived_from"
CellTypeSet ||--|o ProvActivity : "was_generated_by"
CellTypeSet ||--}o Attribute : "has attribute"
Cell ||--|o Cluster : "part_of_cluster"
Cell ||--|o ProvEntity : "was_derived_from"
Cell ||--|o ProvActivity : "was_generated_by"
Cell ||--}o Attribute : "has attribute"

```

