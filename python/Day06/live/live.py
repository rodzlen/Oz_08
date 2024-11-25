## Day 06

# def busy_ping(x,y):
#     print(f"오늘도 {x}이 너무 바빠")
#     print(f'어떻게 하면 {y} 쉴 수 있을까?')

# busy_ping("발","매일")

def oz_len(x):
    count=0
    x = f"{x}"
    for i in x:
        count+=1
    return count

print(oz_len("asasdasdd"))