# from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

# text = """
# class Car:
#     ""A simple class to represent a physical car.""

#     # The constructor method (runs automatically when a new car is created)
#     def __init__(self, make, model, year):
#         self.make = make      
#         self.model = model    
#         self.year = year      
#         self.odometer = 0     
        
#         print(f"My new vehicle is a {my_car.get_descriptive_name()}.")


# my_car.read_odometer()


# my_car.drive(150)"""

# splitter = RecursiveCharacterTextSplitter.from_language(
#     language=Language.PYTHON,
#     chunk_size=250,
#     chunk_overlap=0
# )

# result = splitter.split_text(text)

# print(len(result))
# print(result)



# Thsi is for markdown instead of python

from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
##class Car:
    ""A simple class to represent a physical car.""

    # The constructor method (runs automatically when a new car is created)
    def __init__(self, make, model, year):
        self.make = make      
        self.model = model    
       ## self.year = year      
        self.odometer = 0     
        
        print(f"My new vehicle is a {my_car.get_descriptive_name()}.")


my_car.read_odometer()


my_car.drive(150)"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=400,
    chunk_overlap=0
)

result = splitter.split_text(text)

print(len(result))
print(result)