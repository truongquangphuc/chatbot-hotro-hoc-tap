from config import Config
from loader import DataLoader


def run_chat_engine(index,query_str):
    # Create chat engine that can be used to query the index
    chat_engine = index.as_chat_engine(streaming=True, similarity_top_k=5)
    while True:
        response = chat_engine.chat(query_str)
        return response


def run_query_engine(index,query_str):
    # Create query engine that can be used to query the index
    query_engine = index.as_query_engine(streaming=True, similarity_top_k=5)
    while True:
        response = query_engine.query(query_str)
        return response


def get_query(query_str):
    print("Loading config ...")
    config = Config()

    print("Loading data ...")
    data_loader = DataLoader(
        storage_dir=config.storage_dir,
        simple_data_dir=config.simple_data_dir,
        wiki_pages_file_path=config.wiki_pages_file_path
    )
    index = data_loader.load()

    if config.is_engine_chat():
        return run_chat_engine(index,query_str)
    elif config.is_engine_query():
        return run_query_engine(index,query_str)
    else:
        print(f"Invalid query engine specified in config file: {config.engine}")
        exit(-1)


if __name__ == "__main__":
    get_query()
