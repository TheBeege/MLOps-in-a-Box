from zenml import step

from llm_engineering.model.finetuning.finetune import finetune


@step
def train(
    finetuning_type: str,
    model_name: str,
    num_train_epochs: int,
    per_device_train_batch_size: int,
    learning_rate: float,
    output_dir: str = "output",
    dataset_huggingface_workspace: str = "TheBeege",
    is_dummy: bool = False,
) -> None:
    finetune(
        finetuning_type=finetuning_type,
        model_name=model_name,
        output_dir=output_dir,
        num_train_epochs=num_train_epochs,
        per_device_train_batch_size=per_device_train_batch_size,
        learning_rate=learning_rate,
        dataset_huggingface_workspace=dataset_huggingface_workspace,
        is_dummy=is_dummy,
    )
