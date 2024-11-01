import pandas as pd

def import_data(filename: str)
   
    data = pd.read_excel(filename)
    return data

def filter_data(df: pd.DataFrame)

    df = df.dropna(subset=['CustomerID'])

    df = df[(df['Quantity'] >= 0) & (df['UnitPrice'] >= 0)]

    return df

def loyal_customers(df: pd.DataFrame, min_purchases: int)

    customer_counts = df['customer_id'].value_counts()
    
    loyal_customers = customer_counts[customer_counts >= min_purchases]
    
    result_df = loyal_customers.reset_index()
    result_df.columns = ['customer_id', 'purchase_count']
    
    return result_df

def quarterly_revenue(df: pd.DataFrame)

    df['date'] = pd.to_datetime(df['date'])
    
    df['quarter'] = df['date'].dt.to_period('Q')
    
    quarterly_summary = df.groupby('quarter')['revenue'].sum().reset_index(name='total_revenue')
    
    return quarterly_summary

def high_demand_products(df: pd.DataFrame, top_n: int)

    product_demand = df.groupby('product')['quantity'].sum().reset_index()
    
    top_products = product_demand.sort_values(by='quantity', ascending=False).head(top_n)
    
    return top_products

def purchase_patterns(df: pd.DataFrame)
   
    summary = df.groupby('product').agg(avg_quantity=('quantity', 'mean'),avg_unit_price=('unit_price', 'mean')).reset_index()
    return summary

def answer_conceptual_questions()
    answers = {
        "Q1": {"A"},
        "Q2": {"B"},  # Quarterly aggregation helps reveal seasonal trends.
        "Q3": {"C"},  # Loyal customers are easier to retain and less likely to churn.
        "Q4": {"A"},  # To optimize pricing strategies based on demand.
        "Q5": {"A"},  # Counting the total quantity sold of each product.
    }
    return answers

