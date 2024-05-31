from io import BytesIO
from faker import Faker
from fastapi.responses import FileResponse


fake = Faker()
from fastapi import Response
import pandas as pd
from pydantic import BaseModel

# def generate_social_media_handle(platform: str) -> str:
#     username = fake.user_name()
#     if platform == "facebook":
#         return f"https://www.facebook.com/{username}"
#     elif platform == "X-handle":
#         return f"https://www.X-handle.com/{username}"
#     # elif platform == "instagram":
#     #     return f"https://www.instagram.com/{username}"
#     elif platform == "linkedin":
#         return f"https://www.linkedin.com/in/{username}"
#     else:
#         return f"https://www.socialmedia.com/{username}"
    
# class DataRequest(BaseModel):
#     num_records: int
#     locale: str   = 'en_US'

# def test(data_request: DataRequest):
#     num_records = data_request.num_records
#     fake = Faker(data_request.locale)      
#     print("hello")
#     # Generating dummy data
#     data = []
#     for _ in range(num_records):
#         data.append({
#             'id': fake.uuid4(),
#             # 'org_id': fake.uuid4(),            
#             'first_name': fake.first_name(),
#             'last_name': fake.last_name(),
#             'address': fake.address(),
#             'email': fake.email(),
#             'birthdate': fake.date_of_birth(),
#             'phone_number': fake.phone_number(),
#             'state': fake.state(),
#             # 'country': fake.country(),
#             'company_name': fake.company(),            
#             'website': fake.domain_name(),   
#             'facebook_handle': generate_social_media_handle('facebook'),
#             'X_handle': generate_social_media_handle('X-handle'),
#             'linkedin_handle': generate_social_media_handle('linkedin'),                     
#         })
    
#     df = pd.DataFrame(data)
    
#     output = BytesIO()   
#     with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
#         x= df.to_excel(writer, index=False, sheet_name='Sheet1') 
#     with open("E:\KEDAR_Python\Mailer\c.xlsx","wb") as f:
#         f.write(x)
#     output.seek(0)
    
#     headers = {
#         'Content-Disposition': 'attachment; filename=dummy_data.xlsx',
#         'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#     }
#     return FileResponse(content=output.getvalue(), headers=headers)
# test(DataRequest(num_records=3))

####


def generate_social_media_handle(platform: str) -> str:
    username = fake.user_name()
    if platform == "facebook":
        return f"https://www.facebook.com/{username}"
    elif platform == "X-handle":
        return f"https://www.X-handle.com/{username}"
    # elif platform == "instagram":
    #     return f"https://www.instagram.com/{username}"
    elif platform == "linkedin":
        return f"https://www.linkedin.com/in/{username}"
    else:
        return f"https://www.socialmedia.com/{username}"
    
class DataRequest(BaseModel):
    num_records: int
    locale: str   = 'en_US'

def generate_excel(data_request: DataRequest):
    num_records = data_request.num_records
    fake = Faker(data_request.locale)      
    print("Generating data...")

    # Generating dummy data
    data = []
    for _ in range(num_records):
        data.append({
            'id': fake.uuid4(),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'address': fake.address(),
            'email': fake.email(),
            'birthdate': fake.date_of_birth(),
            'phone_number': fake.phone_number(),
            'state': fake.state(),
            'company_name': fake.company(),            
            'website': fake.domain_name(),   
            'facebook_handle': generate_social_media_handle('facebook'),
            'X_handle': generate_social_media_handle('X-handle'),
            'linkedin_handle': generate_social_media_handle('linkedin'),                     
        })

    df = pd.DataFrame(data)
    
    output = BytesIO()   
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')     
    output.seek(0)
    
    with open("dummy_data.xlsx", "wb") as f:
        f.write(output.getvalue())
    
    print("Excel file 'dummy_data.xlsx' has been generated.")

if __name__ == "__main__":
    # Example usage
    print("enter number of records")
    records = int(input())
    data_request = DataRequest(num_records=records)
    generate_excel(data_request)