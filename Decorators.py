import time

def Timer(func):
    def Wrapper(*args, **kwargs):
        startTime = time.perf_counter()  # Highly accurate timer
        result = func(*args, **kwargs)   # Executes your function
        endTime = time.perf_counter()
        
        executionTime = endTime - startTime
        print(f"Time taken: {executionTime:.6f} seconds")
        return result
    return Wrapper

@Timer
def DoSomething():
    userInput = int(input("Enter a value: "))
    print("Doing some work...")
    for i in range(userInput):
        time.sleep(1)
        if (i % 5 == 0 and i != 0):
            print(f"work left: {userInput - i}")
    print("Finished doing work!")

DoSomething()