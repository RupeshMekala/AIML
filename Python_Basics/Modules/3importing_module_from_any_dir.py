import sys

sys.path.append("///module3.py")
import module3 as f

area = f.circle_area(3)
print(round(area, 2))
