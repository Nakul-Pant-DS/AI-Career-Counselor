import json
import re

from app.core.logging import logger


class ResponseParser:
    """
    Utility class for extracting valid JSON from LLM responses.
    """

    @staticmethod
    def parse(response: str) -> dict:
        """
        Extracts the first valid JSON object from an LLM response.

        Parameters
        ----------
        response : str
            Raw response returned by the LLM.

        Returns
        -------
        dict
            Parsed JSON dictionary.

        Raises
        ------
        ValueError
            If no valid JSON object is found.
        """

        logger.info("Parsing LLM response.")

        # Remove Markdown code fences if present
        cleaned = response.strip()

        cleaned = cleaned.replace("```json", "")
        cleaned = cleaned.replace("```", "")
        cleaned = cleaned.strip()

        # Try parsing directly
        try:
            data = json.loads(cleaned)

            logger.info("Valid JSON extracted successfully.")

            return data

        except Exception:
            pass

        # Otherwise search for first JSON object
        match = re.search(r"\{.*\}", cleaned, re.DOTALL)

        if match:

            try:

                data = json.loads(match.group())

                logger.info("Valid JSON extracted successfully.")

                return data

            except Exception as e:

                logger.error(f"JSON parsing failed: {e}")

        raise ValueError("No valid JSON object found in LLM response.")
