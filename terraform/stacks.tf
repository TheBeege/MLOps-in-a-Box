data "zenml_stack_component" "artifact_store_local" {
    name   = "artifacts_dir"
    type   = "artifact_store"
}

resource "zenml_stack_component" "orchestrator_local" {
    name   = "local_docker"
    type   = "orchestrator"
    flavor = "local_docker"
}

resource "zenml_stack" "local" {
    name = "local-stack"
    components = {
        artifact_store = data.zenml_stack_component.artifact_store_local.id
        orchestrator   = zenml_stack_component.orchestrator_local.id
    }
    labels = {
        environment = "local"
    }
}
