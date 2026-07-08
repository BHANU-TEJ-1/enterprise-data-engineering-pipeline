from src.utils.database import test_connection

result = test_connection()

print(f"\nConnection Status: {result}")