import pandas as pd

def import_data(filename: str)
   
    data = pd.read_excel(filename)
    return data

def filter_data(df: pd.DataFrame) -> pd.DataFrame

    df = df.dropna(subset=['CustomerID'])

    df = df[(df['Quantity'] >= 0) & (df['UnitPrice'] >= 0)]

    return df

def loyal_customers(df: pd.DataFrame, min_purchases: int) -> pd.DataFrame

    customer_counts = df['customer_id'].value_counts()
    
    loyal_customers = customer_counts[customer_counts >= min_purchases]
    
    result_df = loyal_customers.reset_index()
    result_df.columns = ['customer_id', 'purchase_count']
    
    return result_df

def quarterly_revenue(df: pd.DataFrame) -> pd.DataFrame

    df['date'] = pd.to_datetime(df['date'])
    
    df['quarter'] = df['date'].dt.to_period('Q')
    
    quarterly_summary = df.groupby('quarter')['revenue'].sum().reset_index(name='total_revenue')
    
    return quarterly_summary

def high_demand_products(df: pd.DataFrame, top_n: int) -> pd.DataFrame

    product_demand = df.groupby('product')['quantity'].sum().reset_index()
    
    top_products = product_demand.sort_values(by='quantity', ascending=False).head(top_n)
    
    return top_products

def purchase_patterns(df: pd.DataFrame) -> pd.DataFrame
   
    summary = df.groupby('product').agg(avg_quantity=('quantity', 'mean'),avg_unit_price=('unit_price', 'mean')).reset_index()
    return summary

def answer_conceptual_questions() -> dict:
    answers = {
        "Q1": {"A", "C", "D"}, 
        "Q2": {"A", "B", "D"},
        "Q3": {"A", "B", "C"},
        "Q4": {"A", "B", "C"}, 
        "Q5": {"A", "B", "D"}, 
    }
    return answers

