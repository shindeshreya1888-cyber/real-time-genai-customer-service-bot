import os


def load_customer_service_data():
    """
    Load the customer service knowledge base
    from the data folder.
    """

    # Get the project root directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Create path to customer_service.txt
    file_path = os.path.join(
        project_root,
        "data",
        "customer_service.txt"
    )

    # Check whether the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Knowledge base not found: {file_path}"
        )

    # Read the file
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text