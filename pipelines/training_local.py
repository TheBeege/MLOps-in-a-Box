from zenml import pipeline

from steps import training as training_steps


@pipeline
def training(
    finetuning_type: str = "sft",
    model_name: str = "DeepSeek-R1-0528-Qwen3-8B",
    num_train_epochs: int = 3,
    per_device_train_batch_size: int = 2,
    learning_rate: float = 3e-4,
    dataset_huggingface_workspace: str = "TheBeege",
    is_dummy: bool = False,
) -> None:
    training_steps.local_train(
        finetuning_type=finetuning_type,
        model_name=model_name,
        num_train_epochs=num_train_epochs,
        per_device_train_batch_size=per_device_train_batch_size,
        learning_rate=learning_rate,
        dataset_huggingface_workspace=dataset_huggingface_workspace,
        is_dummy=is_dummy,
    )
