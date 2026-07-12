import os
import pickle

import faiss
import numpy as np

from app.core.config import settings
from app.core.logging import logger
from app.schemas.document_chunk import DocumentChunk
from app.schemas.vector_index import VectorIndex


class VectorStore:
    """
    Enterprise FAISS Vector Store.

    One instance manages one logical index
    (resume, career, jobs, interview, etc.)
    """

    def __init__(
        self,
        index_name: VectorIndex,
        dimension: int = 384
    ):

        self.dimension = dimension

        self.index_name = index_name

        self.index = faiss.IndexFlatL2(dimension)

        self.documents: list[DocumentChunk] = []

    # =====================================================
    # Internal Helpers
    # =====================================================

    def _get_paths(self):

        os.makedirs(
            settings.VECTOR_DB_DIR,
            exist_ok=True
        )

        index_path = os.path.join(
            settings.VECTOR_DB_DIR,
            f"{self.index_name.value}.index"
        )

        metadata_path = os.path.join(
            settings.VECTOR_DB_DIR,
            f"{self.index_name.value}_metadata.pkl"
        )

        return index_path, metadata_path

    # =====================================================
    # Check Existing Index
    # =====================================================

    def exists(self) -> bool:

        index_path, metadata_path = self._get_paths()

        return (
            os.path.exists(index_path)
            and os.path.exists(metadata_path)
        )

    # =====================================================
    # Add Embeddings
    # =====================================================

    def add(
        self,
        embeddings: np.ndarray,
        chunks: list[DocumentChunk]
    ):

        logger.info(
            f"Adding {len(chunks)} chunks to "
            f"{self.index_name.value} index."
        )

        self.index.add(
            embeddings.astype(np.float32)
        )

        self.documents.extend(chunks)

    # =====================================================
    # Search
    # =====================================================

    def search(
        self,
        query_embedding: np.ndarray,
        top_k: int = 3
    ) -> list[DocumentChunk]:

        logger.info(
            f"Searching {self.index_name.value} index."
        )

        distances, indices = self.index.search(
            query_embedding.astype(np.float32),
            top_k
        )

        results = []

        for idx in indices[0]:

            if idx == -1:
                continue

            results.append(
                self.documents[idx]
            )

        return results

    # =====================================================
    # Save
    # =====================================================

    # =====================================================
    # Save
    # =====================================================

    def save(self):

        index_path, metadata_path = self._get_paths()

        logger.info(
            f"Saving {self.index_name.value} vector database."
        )

        faiss.write_index(
            self.index,
            index_path
        )

        with open(
            metadata_path,
            "wb"
        ) as file:

            pickle.dump(
                self.documents,
                file
            )

        logger.info(
            f"{self.index_name.value} index saved successfully."
        )


        # =====================================================
    # Append
    # =====================================================

    def append(
        self,
        embeddings: np.ndarray,
        chunks: list[DocumentChunk]
    ):

        if self.exists():

            logger.info(
                f"Existing {self.index_name.value} index found."
            )

            self.load()

        else:

            logger.info(
                f"Creating new {self.index_name.value} index."
            )

        self.add(
            embeddings,
            chunks
        )

        self.save()

    # =====================================================
    # Load
    # =====================================================

    def load(self):

        index_path, metadata_path = self._get_paths()

        if not os.path.exists(index_path):

            raise FileNotFoundError(
                f"Index not found : {index_path}"
            )

        if not os.path.exists(metadata_path):

            raise FileNotFoundError(
                f"Metadata not found : {metadata_path}"
            )

        logger.info(
            f"Loading {self.index_name.value} vector database."
        )

        self.index = faiss.read_index(
            index_path
        )

        with open(
            metadata_path,
            "rb"
        ) as file:

            self.documents = pickle.load(file)

        logger.info(
            f"Loaded {len(self.documents)} chunks "
            f"from {self.index_name.value} index."
        )

    # =====================================================
    # Utility
    # =====================================================

    def total_vectors(self) -> int:

        return self.index.ntotal

    def clear(self):

        logger.info(
            f"Clearing {self.index_name.value} index."
        )

        self.index = faiss.IndexFlatL2(
            self.dimension
        )

        self.documents = []
