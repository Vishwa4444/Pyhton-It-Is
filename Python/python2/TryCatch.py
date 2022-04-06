def divide(divideby):
    try:
        return 40/divideby
    except Exception as e:
          print(e)
    finally:
        print("done")
print(divide(5))
# print(divide(0.0))
print(divide(5.6))