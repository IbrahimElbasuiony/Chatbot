"""Loading packages"""

from llama_index.core import StorageContext, load_index_from_storage
from links import indix_path

from llama_index.core.tools import QueryEngineTool, ToolMetadata
from create_indices import indexing


def create_vector_tool():
    """This function create pdf tool from indices file"""
    indexing()

    storagecontent = StorageContext.from_defaults(persist_dir=indix_path)  # the index path from links.py

    index = load_index_from_storage(storage_context=storagecontent)  # loading pdf indices

    # create tool
    pdf_tool = QueryEngineTool(
        index.as_query_engine(),
        metadata=ToolMetadata(
            name="Knowledge",
            description="Contain general information about the Founding of the Kingdom of Saudi Arabia and Al Al Saud "
                        "Descent"

        )
    )

    return pdf_tool
