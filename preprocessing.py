import pandas as pd

education_map = {
    'SSC': 1,
    '12TH': 2,
    'GRADUATE': 3,
    'UNDER GRADUATE': 3,
    'POST-GRADUATE': 4,
    'OTHERS': 1,
    'PROFESSIONAL': 3
}


def preprocess(df):
    """
    Performs all preprocessing required before prediction.
    """

    df = df.copy()

    # EDUCATION mapping
    df['EDUCATION'] = df['EDUCATION'].map(education_map).astype(int)

    # One Hot Encoding
    df = pd.get_dummies(
        df,
        columns=[
            'MARITALSTATUS',
            'GENDER',
            'last_prod_enq2',
            'first_prod_enq2'
        ],
        dtype=int
    )

    return df