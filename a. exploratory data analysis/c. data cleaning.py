import warnings

warnings.filterwarnings("ignore", category=UserWarning, message=".*Could not infer format.*")

class DataCleaning:
    def __init__(self, df):
        self.df = df

    def clean_and_convert_dtypes(self):
        if 'Order Date' in self.df.columns:
            try:
                self.df['Order Date'] = pd.to_datetime(self.df['Order Date'])
            except Exception as e:
                print(f"Error converting 'Order Date' to datetime: {e}")
                self.df['Order Date'] = pd.NaT 
        
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                try:
                    if col != 'Order Date':
                        self.df[col] = pd.to_datetime(self.df[col])
                except Exception as e:
                    pass  
            
            elif self.df[col].dtype in ['int64', 'float64']:
                self.df[col] = pd.to_numeric(self.df[col], errors='coerce')  

    def clean_column_names(self):
        self.df.columns = self.df.columns.str.strip().str.lower().str.replace(' ', '_')

    def clean_values(self):
        for col in self.df.select_dtypes(include=['object']).columns:
            self.df[col] = self.df[col].str.strip()

    def validate_column_names(self):
        spaces_in_columns = [col for col in self.df.columns if col != col.strip()]
        if spaces_in_columns:
            print(f" Warning: [ Some column names still have leading/trailing spaces: {spaces_in_columns} ]\n")
        else:
            print("Result: [ All column names are clean with no leading/trailing spaces.]\n")
        return spaces_in_columns

    def perform_data_cleaning(self):
        self.clean_column_names()
        self.clean_and_convert_dtypes()
        self.clean_values()

    def display_data_info(self):
        print("\n| 1. Data types after conversion: |")
        print(f"{self.df.dtypes}\n")
        print("\n| 2. Leading/trailing spaces validation: |")
        self.validate_column_names()
        print("\n| 3. Data columns after conversion: |")
        print(f"{self.df.columns}\n")
        print("\n| 4. Data after conversion: |")
        print(self.df.head())
