
def calculate_area(base,height,shape):

    if shape == "triangle" :
        triangle_area = (base * height)/2
        return triangle_area

    elif shape == "rectangle":
        rectangle_area = base * height
        return rectangle_area


sample1 = calculate_area(3,4,"rectangle")
sample2 = calculate_area(3,4,"triangle")
print(sample1)
print(sample2)

