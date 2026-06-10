import pandas as pd

# Data load 
df = pd.read_csv(r'C:\Users\H.T\Desktop\remote internships\DecodeLabs india\ecommerce_data.csv')

print(df.shape)



# Data cleaning

# Step 1: Duplicates dekho
print("\n=== DUPLICATES ===")
print("Duplicate rows:", df.duplicated().sum())


# Step 2: Missing values dekho
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())


# Step 3: Missing values handle karo
df['CouponCode'] = df['CouponCode'].fillna('NO_COUPON')
print("\nMissing values after cleaning:")
print(df.isnull().sum())


#check date issue
print("\nDate column sample:")
print(df['Date'].head(10))
print("\nDate type:", df['Date'].dtype)



# Step 4: Date format fix
df['Date'] = pd.to_datetime(df['Date'])
print("\nDate type after fix:", df['Date'].dtype)
print(df['Date'].head())


# Step 5: Clean data save karo
df.to_csv(r'C:\Users\H.T\Desktop\remote internships\DecodeLabs india\cleaned_ecommerce.csv', index=False)
print("\nClean data save ho gaya!")







# PDF Change Log banana
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate(
    r'C:\Users\H.T\Desktop\remote internships\DecodeLabs india\change_log.pdf',
    pagesize=A4
)

styles = getSampleStyleSheet()
elements = []

# Title
elements.append(Paragraph("Data Cleaning Change Log", styles['Title']))
elements.append(Paragraph("Project 1 - DecodeLabs Internship", styles['Normal']))
elements.append(Paragraph(" ", styles['Normal']))

# Table data
data = [
    ['Change ID', 'Description', 'Impact', 'Status'],
    ['CR001', 'CouponCode: 309 missing\nvalues filled with NO_COUPON', 'Preserved 309 records', 'Resolved'],
    ['CR002', 'Date column converted\nfrom string to datetime64', 'Proper date analysis\nnow possible', 'Resolved'],
    ['CR003', 'Duplicate rows checked\n0 duplicates found', 'Data integrity\nconfirmed', 'Resolved'],
]

table = Table(data, colWidths=[80, 180, 150, 80])
table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.darkblue),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('BACKGROUND', (0,1), (-1,-1), colors.lightblue),
]))

elements.append(table)
doc.build(elements)
print("\nPDF Change Log ready!")