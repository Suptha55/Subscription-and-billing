import pandas as pd
import logging

logger = logging.getLogger(__name__)


def load_subscriptions(file_path):
    """
    Load subscriptions.csv safely.
    - Strips column spaces
    - Handles file errors
    - Returns empty DataFrame if failure
    """
    try:
        df = pd.read_csv(file_path)

        # Clean column names
        df.columns = df.columns.str.strip()

        # Ensure required numeric fields are numeric
        if "monthly_fee" in df.columns:
            df["monthly_fee"] = pd.to_numeric(
                df["monthly_fee"], errors="coerce"
            ).fillna(0)

        if "usage_limit_gb" in df.columns:
            df["usage_limit_gb"] = pd.to_numeric(
                df["usage_limit_gb"], errors="coerce"
            ).fillna(0)

        logger.info("Subscriptions file loaded successfully.")
        return df

    except Exception as e:
        logger.error(f"Error loading subscriptions file: {e}")
        return pd.DataFrame()


def load_usage(file_path):
    """
    Load usage.csv safely.
    - Strips column spaces
    - Handles invalid numeric values
    - Returns empty DataFrame if failure
    """
    try:
        df = pd.read_csv(file_path)

        # Clean column names (IMPORTANT FIX)
        df.columns = df.columns.str.strip()

        # Convert data_used_gb safely
        if "data_used_gb" in df.columns:
            df["data_used_gb"] = pd.to_numeric(
                df["data_used_gb"], errors="coerce"
            ).fillna(0)

        logger.info("Usage file loaded successfully.")
        return df

    except Exception as e:
        logger.error(f"Error loading usage file: {e}")
        return pd.DataFrame()
