import qrcode
Name=input("Name:")
Age=int(input("Age:"))
Gender=input("Gender:")
Phone_no=int(input("Phone_Number:"))
Email=input("Email:")
Professionality=input("Professionality")
Employee_id=int(input("Employee_Id"))
data=f"Name:{Name}/n Age:{Age}/n Gender:{Gender} Phone_no:{Phone_no} Email:{Email} Professionality:{Professionality} Employee:{Employee_id}"
image=qrcode.make(data)
image.show()
print(image)